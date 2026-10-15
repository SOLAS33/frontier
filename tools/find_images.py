"""Finds photos that carry no copyright restriction, using Wikimedia Commons licence metadata.

  python tools/find_images.py "dilution refrigerator" "ion trap" ...      list candidates
  python tools/find_images.py --download IDS.json                           fetch chosen files into assets/img

Accepted: public domain (including US government works) and CC0. Everything else is rejected, including CC BY,
because the attribution and share-alike terms are exactly what this site wants to avoid carrying. Trademark and
non-free flags on the file page also reject it. A credits file is written next to the images.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import httpx

API = "https://commons.wikimedia.org/w/api.php"
UA = "SolasFrontier/1.0 (hello@solas33.com) research image finder"
OK_LICENCE = re.compile(r"^(public domain|pd[- ]|cc0|cc[- ]?zero|no restrictions)", re.I)
BAD_FLAGS = ("nonfree", "non-free", "trademark", "fairuse", "fair use")
ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "frontier" / "assets" / "img"


def _meta(v: dict, k: str) -> str:
    return re.sub(r"<[^>]+>", "", (v.get(k) or {}).get("value", "")).strip()


def search(query: str, limit: int = 25, width: int = 1600) -> list[dict]:
    p = {"action": "query", "format": "json", "generator": "search", "gsrsearch": f"{query} filetype:bitmap",
         "gsrnamespace": 6, "gsrlimit": limit, "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata",
         "iiurlwidth": width, "iiextmetadatafilter": "LicenseShortName|Copyrighted|Artist|Credit|ImageDescription|Restrictions|UsageTerms|AttributionRequired"}
    with httpx.Client(headers={"User-Agent": UA}, timeout=30) as c:
        r = c.get(API, params=p)
        r.raise_for_status()
    out = []
    for page in (r.json().get("query", {}).get("pages") or {}).values():
        ii = (page.get("imageinfo") or [{}])[0]
        m = ii.get("extmetadata") or {}
        lic = _meta(m, "LicenseShortName")
        flags = (_meta(m, "Restrictions") + " " + _meta(m, "UsageTerms")).lower()
        if not OK_LICENCE.search(lic) or _meta(m, "Copyrighted").lower() == "true" or any(b in flags for b in BAD_FLAGS):
            continue
        if ii.get("mime") != "image/jpeg" or ii.get("width", 0) < 1400:
            continue
        out.append({"title": page["title"], "licence": lic, "w": ii["width"], "h": ii["height"], "thumb": ii.get("thumburl"),
                    "page": ii.get("descriptionurl"), "credit": _meta(m, "Credit")[:120], "artist": _meta(m, "Artist")[:80],
                    "desc": _meta(m, "ImageDescription")[:140]})
    return out


def download(items: list[dict]) -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    credits = []
    with httpx.Client(headers={"User-Agent": UA}, timeout=60, follow_redirects=True) as c:
        for it in items:
            r = c.get(it["thumb"])
            r.raise_for_status()
            (IMG / it["file"]).write_bytes(r.content)
            credits.append({k: it.get(k) for k in ("file", "title", "licence", "artist", "credit", "page", "alt")})
            print("saved", it["file"], len(r.content) // 1024, "KB")
    path = IMG / "credits.json"
    have = {c["file"]: c for c in json.loads(path.read_text(encoding="utf-8"))} if path.exists() else {}
    have.update({c["file"]: c for c in credits})
    path.write_text(json.dumps(list(have.values()), indent=1), encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1] == "--download":
        download(json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")))
    else:
        for q in sys.argv[1:]:
            print(f"\n## {q}")
            for c in search(q):
                print(f"- {c['title']} | {c['licence']} | {c['w']}x{c['h']} | {c['artist'][:40]} | {c['desc'][:90]}")
