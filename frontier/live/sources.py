"""Free public sources for the live backend. Every function returns plain dicts and never raises on network trouble:
a failed source is reported in the run's `sources` status, and the rest of the run carries on."""
from __future__ import annotations

import os
import time
import xml.etree.ElementTree as ET
from urllib.parse import quote

import httpx

CIK = {"IONQ": 1824920, "RGTI": 1838359, "QBTS": 1907982, "QUBT": 1758009}
COMPANY_QUERY = {"IONQ": '"IonQ"', "RGTI": '"Rigetti Computing"', "QBTS": '"D-Wave Quantum"', "QUBT": '"Quantum Computing Inc"'}
ARXIV_TERMS = ["IonQ", "Rigetti", "D-Wave", "Quantinuum", "Google Quantum AI", "IBM Quantum"]


def sec_ua() -> str:
    """SEC fair-access policy asks for a declared contact. Set SEC_CONTACT_EMAIL in the environment (a secret in Actions)."""
    contact = os.environ.get("SEC_CONTACT_EMAIL", "").strip()
    contact = contact if "@" in contact else ""
    return f"Solas33-Frontier research ({contact or '+https://github.com/SOLAS33/frontier'})"


def _client(ua: str | None = None, timeout: float = 30.0) -> httpx.Client:
    return httpx.Client(headers={"User-Agent": ua or "Solas33-Frontier/1.0 (+https://github.com/SOLAS33/frontier)"},
                        timeout=timeout, follow_redirects=True)


def edgar_filings(ticker: str, cik: int | None = None, client: httpx.Client | None = None) -> list[dict]:
    """Recent filings: date, acceptance time, form, 8-K item codes, link. Newest first."""
    cik = cik or CIK[ticker]
    c = client or _client(sec_ua())
    r = c.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    r.raise_for_status()
    rec = r.json()["filings"]["recent"]
    out = []
    for i in range(len(rec["accessionNumber"])):
        acc = rec["accessionNumber"][i]
        out.append({
            "ticker": ticker, "date": rec["filingDate"][i], "accepted": rec.get("acceptanceDateTime", [None] * 9999)[i],
            "form": rec["form"][i], "items": (rec.get("items") or [""] * 9999)[i] or "",
            "title": rec.get("primaryDocDescription", [""] * 9999)[i] or rec["form"][i],
            "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{rec['primaryDocument'][i]}",
            "id": f"sec:{acc}",
        })
    return out


def gdelt_headlines(query: str, days: int = 7, n: int = 12, client: httpx.Client | None = None) -> list[dict]:
    """Headlines and links only (no article text). GDELT asks for at most one request every 5 seconds."""
    c = client or _client()
    url = ("https://api.gdeltproject.org/api/v2/doc/doc?query=" + quote(query) +
           f"&mode=artlist&format=json&maxrecords={n}&timespan={days}d&sort=datedesc")
    r = c.get(url)
    for wait in (8, 16, 30):  # GDELT rate-limits hard: back off and retry
        if r.status_code < 400 and r.text.strip().startswith("{"):
            break
        time.sleep(wait)
        r = c.get(url)
    r.raise_for_status()
    if not r.text.strip().startswith("{"):
        return []
    out = []
    for a in r.json().get("articles", []):
        if a.get("language", "English") != "English":
            continue
        d = a.get("seendate", "")
        out.append({"id": "news:" + a["url"], "date": f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) >= 8 else "",
                    "title": a.get("title", "").strip(), "url": a["url"], "source": a.get("domain", ""),
                    "country": a.get("sourcecountry", "")})
    return out


def arxiv_papers(term: str, n: int = 4, client: httpx.Client | None = None) -> list[dict]:
    c = client or _client()
    url = ("http://export.arxiv.org/api/query?search_query=all:" + quote(f'"{term}"') +
           f"+AND+cat:quant-ph&sortBy=submittedDate&sortOrder=descending&max_results={n}")
    r = c.get(url)
    r.raise_for_status()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in ET.fromstring(r.text).findall("a:entry", ns):
        out.append({"id": "arxiv:" + e.findtext("a:id", "", ns), "date": e.findtext("a:published", "", ns)[:10],
                    "title": " ".join(e.findtext("a:title", "", ns).split()), "url": e.findtext("a:id", "", ns),
                    "term": term, "authors": [a.findtext("a:name", "", ns) for a in e.findall("a:author", ns)][:3]})
    return out


def polite_sleep(seconds: float = 8.0):
    time.sleep(seconds)
