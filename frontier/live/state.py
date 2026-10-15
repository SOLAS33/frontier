"""Projection state: base scenario probabilities, news-driven tilts that fade, a change log and a prediction ledger.

Rules that keep this honest:
  * a tilt moves probability between the bear and bull stories only, never the price itself;
  * every event's effect halves every HALF_LIFE_DAYS and the total tilt is capped at +/- CAP points;
  * no story drops below FLOOR; probabilities always sum to 1;
  * every change of at least one whole point is written to the change log with its cause;
  * ledger rows are append-only and hash-chained, so an edit would be visible.
"""
from __future__ import annotations

import hashlib
import json
import math
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

HALF_LIFE_DAYS = 30.0
CAP = 12.0
FLOOR = 0.05


def _age_days(ev_date: str, today: date) -> float:
    return max(0.0, (today - date.fromisoformat(ev_date[:10])).days)


def active_tilt(events: list[dict], today: date) -> tuple[float, list[dict]]:
    """Net tilt in probability points toward the bull story (negative = toward bear), and the top contributing events."""
    parts = []
    for e in events:
        w = 0.5 ** (_age_days(e["date"], today) / HALF_LIFE_DAYS)
        parts.append({**e, "weight": w, "contribution": e["nudge"] * w})
    net = float(np.clip(sum(p["contribution"] for p in parts), -CAP, CAP))
    parts.sort(key=lambda p: -abs(p["contribution"]))
    return net, [p for p in parts if abs(p["contribution"]) >= 0.05][:5]


def apply_tilt(base: dict[str, float], tilt_pts: float) -> dict[str, float]:
    """base: {'bear':p,'base':p,'bull':p}. Moves tilt_pts/100 from bear to bull (or back), respecting FLOOR."""
    t = tilt_pts / 100.0
    bear, mid, bull = base["bear"], base["base"], base["bull"]
    if t >= 0:
        t = min(t, bear - FLOOR)
    else:
        t = -min(-t, bull - FLOOR)
    return {"bear": bear - t, "base": mid, "bull": bull + t}


def mixture_quantiles(price: float, scen: list[dict], months: int, qs=(0.1, 0.5, 0.9)) -> list[float]:
    """Analytic quantiles of a lognormal mixture at `months` ahead. scen items: p, drift (median yearly change), sigma."""
    from math import erf, log, sqrt

    def cdf(x: float) -> float:
        tot = 0.0
        for s in scen:
            mu = log(price) + log1p(s["drift"]) * months / 12
            sd = s["sigma"] * sqrt(months / 12)
            tot += s["p"] * 0.5 * (1 + erf((log(x) - mu) / (sd * sqrt(2)))) if sd > 0 else s["p"] * (1.0 if x >= math.exp(mu) else 0.0)
        return tot

    out = []
    for q in qs:
        lo, hi = price * 1e-4, price * 1e4
        for _ in range(80):
            mid = math.sqrt(lo * hi)
            lo, hi = (mid, hi) if cdf(mid) < q else (lo, mid)
        out.append(round(math.sqrt(lo * hi), 4))
    return out


def log1p(x: float) -> float:
    return math.log1p(x)


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def append_jsonl(path: Path, row: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, separators=(",", ":")) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def ledger_append(path: Path, row: dict) -> dict:
    """Hash-chained, append-only prediction log."""
    prev = read_jsonl(path)
    row = {**row, "prev": prev[-1]["hash"] if prev else "genesis"}
    body = json.dumps({k: v for k, v in row.items() if k != "hash"}, sort_keys=True, separators=(",", ":"))
    row["hash"] = hashlib.sha256(body.encode()).hexdigest()[:20]
    append_jsonl(path, row)
    return row


def ledger_verify(path: Path) -> bool:
    prev = "genesis"
    for r in read_jsonl(path):
        body = json.dumps({k: v for k, v in r.items() if k != "hash"}, sort_keys=True, separators=(",", ":"))
        if r["prev"] != prev or hashlib.sha256(body.encode()).hexdigest()[:20] != r["hash"]:
            return False
        prev = r["hash"]
    return True


def score_ledger(rows: list[dict], latest: dict[str, float], today: date) -> dict:
    """Score predictions whose horizon has passed against the latest known price. Returns counts and per-row results."""
    scored, total = [], 0
    for r in rows:
        total += 1
        due = date.fromisoformat(r["date"]).toordinal() + int(r["months"] * 30.4)
        if due > today.toordinal() or r["ticker"] not in latest:
            continue
        a = latest[r["ticker"]]
        side = "below" if a < r["p10"] else "above" if a > r["p90"] else "inside"
        scored.append({"date": r["date"], "ticker": r["ticker"], "months": r["months"], "p10": r["p10"], "p50": r["p50"],
                       "p90": r["p90"], "actual": a, "result": side})
    inside = sum(1 for s in scored if s["result"] == "inside")
    return {"logged": total, "scored": len(scored), "inside_band": inside,
            "coverage": (inside / len(scored)) if scored else None, "expected_coverage": 0.8, "rows": scored[-40:]}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
