"""How did these stocks actually react to filings of each type? A small event study on daily prices.

Abnormal return = stock return minus the benchmark's over the same window (benchmark: QQQ, a plain market proxy).
Filings accepted after 4pm New York time are dated to the next trading day, because that is when the market
could first react. Statistics are pooled over the four pure-plays and reported with case counts; small samples are
flagged, never hidden.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from frontier.live.classify import classify_filing


def daily_prices(symbols: list[str]) -> dict[str, pd.Series]:
    import yfinance as yf
    out = {}
    for s in symbols:
        h = yf.Ticker(s).history(period="max", interval="1d", auto_adjust=True)["Close"].dropna()
        h.index = pd.to_datetime(h.index).tz_localize(None).normalize()
        out[s] = h
    return out


def effective_date(f: dict) -> pd.Timestamp:
    d = pd.Timestamp(f["date"])
    acc = f.get("accepted")
    if acc:
        try:
            et = pd.Timestamp(acc).tz_convert("America/New_York")
            if et.hour >= 16:
                return d + pd.offsets.BDay(1)
        except (ValueError, TypeError):
            pass
    return d


def reactions(filings: list[dict], px: dict[str, pd.Series], bench: str = "QQQ") -> pd.DataFrame:
    rows, seen = [], set()
    b = px.get(bench)
    for f in filings:
        kind = classify_filing(f)
        s = px.get(f["ticker"])
        if kind is None or s is None or b is None:
            continue
        eff = effective_date(f)
        key = (f["ticker"], eff, kind)
        if key in seen:
            continue
        seen.add(key)
        i = s.index.searchsorted(eff, side="left")
        if i < 1 or i + 4 >= len(s):
            continue
        d0 = s.index[i - 1]
        j = b.index.searchsorted(s.index[i], side="left")
        if j < 1 or j + 4 >= len(b) or b.index[j] != s.index[i]:
            continue
        r1 = s.iloc[i] / s.iloc[i - 1] - 1 - (b.iloc[j] / b.iloc[j - 1] - 1)
        r5 = s.iloc[i + 4] / s.iloc[i - 1] - 1 - (b.iloc[j + 4] / b.iloc[j - 1] - 1)
        rows.append({"ticker": f["ticker"], "type": kind, "date": s.index[i], "r1": r1, "r5": r5})
    return pd.DataFrame(rows, columns=["ticker", "type", "date", "r1", "r5"])


def table(df: pd.DataFrame, min_n: int = 8) -> list[dict]:
    """Per event type: n, median and mean abnormal move over 1 and 5 days, share positive, t-statistic of the 5-day mean."""
    out = []
    for kind, g in df.groupby("type"):
        n = len(g)
        r5 = g["r5"].to_numpy()
        se = r5.std(ddof=1) / np.sqrt(n) if n > 2 else float("nan")
        out.append({"type": kind, "n": int(n), "median_1d": float(g["r1"].median()), "median_5d": float(np.median(r5)),
                    "mean_5d": float(r5.mean()), "share_up_5d": float((r5 > 0).mean()),
                    "t_5d": float(r5.mean() / se) if se and se == se and se > 0 else None, "enough": bool(n >= min_n)})
    return sorted(out, key=lambda r: -r["n"])
