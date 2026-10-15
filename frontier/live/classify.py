"""Turns raw filings and headlines into typed events.

Rules, not a language model: transparent, free and repeatable. Each type has a `prior` that says which way it
usually tilts the odds of a company meeting its milestones (+ toward the bull story, - toward the bear story),
in probability points before decay. Priors are the author's judgement and are replaced by measured reactions
(live/impact.py) when there are enough past cases.
"""
from __future__ import annotations

import re

# type -> (label, prior tilt in probability points)
TYPES = {
    "share_sale": ("Share sale or shelf registration", -2.0),
    "contract": ("Contract, partnership or material agreement", +1.5),
    "technical": ("Technical result or milestone", +2.0),
    "acquisition": ("Acquisition or merger", 0.0),
    "earnings": ("Results of operations", 0.0),
    "leadership": ("Leadership change", -0.5),
    "legal_risk": ("Legal, short-seller or regulatory risk", -2.0),
    "policy": ("Government policy or export control", 0.0),
    "periodic": ("Annual or quarterly report", 0.0),
    "other_filing": ("Other filing", 0.0),
}

ITEM_MAP = {"1.01": "contract", "1.02": "contract", "2.01": "acquisition", "2.02": "earnings", "2.03": "share_sale",
            "3.02": "share_sale", "5.02": "leadership", "8.01": "other_filing", "7.01": "other_filing"}
FORM_MAP = {"424B5": "share_sale", "424B3": "share_sale", "424B4": "share_sale", "S-3": "share_sale", "S-3ASR": "share_sale",
            "S-1": "share_sale", "10-K": "periodic", "10-Q": "periodic"}
NOISE_FORMS = {"4", "3", "5", "SC 13G", "SC 13G/A", "144", "S-8", "DEF 14A", "ARS", "CORRESP", "UPLOAD", "EFFECT"}

KEYWORDS = [
    ("share_sale", r"\b(offering|private placement|priced|raises? \$|at-the-market|atm program|share sale|registered direct)\b"),
    ("acquisition", r"\b(acquir\w+|acquisition|merger|takeover)\b"),
    ("legal_risk", r"\b(short[- ]seller|short report|lawsuit|class action|investigation|subpoena|sec charges)\b"),
    ("policy", r"\b(export control|export ban|sanction|tariff|restriction|entity list|national quantum)\b"),
    ("technical", r"\b(logical qubit|error[- ]correct\w*|fidelity|record|breakthrough|milestone|quantum advantage|qubits?)\b"),
    ("contract", r"\b(contract|award\w*|order|agreement|partnership|partners? with|collaborat\w+|selected)\b"),
    ("earnings", r"\b(earnings|quarter|revenue|results|guidance)\b"),
    ("leadership", r"\b(appoints?|names? new|ceo|cfo|steps down|resigns?)\b"),
]


def classify_filing(f: dict) -> str | None:
    """None means noise that should not be shown (insider forms, proxy material and so on)."""
    form = f["form"].upper()
    if form in NOISE_FORMS or form.startswith("SC 13"):
        return None
    if form in FORM_MAP:
        return FORM_MAP[form]
    if form.startswith("8-K"):
        types = [ITEM_MAP[i] for i in re.split(r"[,\s]+", f.get("items", "")) if i in ITEM_MAP]
        for pref in ("share_sale", "acquisition", "contract", "leadership", "earnings", "other_filing"):
            if pref in types:
                return pref
        return "other_filing"
    return "other_filing"


ALIASES = {"IONQ": ["ionq"], "RGTI": ["rigetti"], "QBTS": ["d-wave", "dwave", "qbts"], "QUBT": ["quantum computing inc", "qubt"]}
IGNORE = r"\b(vs\.?|versus|upgraded|downgraded|price target|better (buy|stock)|should you|here is|here's what)\b"


def mentions(title: str, ticker: str, aliases: dict | None = None) -> bool:
    t = title.lower()
    names = (aliases or ALIASES).get(ticker, [])
    return ticker.lower() in t or any(a in t for a in names)


def classify_headline(title: str) -> str | None:
    t = title.lower()
    if re.search(IGNORE, t):
        return None
    for kind, pat in KEYWORDS:
        if re.search(pat, t):
            return kind
    return None


def prior(kind: str) -> float:
    return TYPES.get(kind, ("", 0.0))[1]
