"""Share-price data: weekly closes from Yahoo Finance, cached as JSON so builds are repeatable and offline-safe.

The cache holds, per ticker: name, dates (ISO), closes (split and dividend adjusted). `refresh` rewrites it;
every other function works on the cache only.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "data" / "prices.json"

# Everything the quantum site draws. Order is the legend order.
UNIVERSE = {
    "IONQ": "IonQ", "RGTI": "Rigetti", "QBTS": "D-Wave", "QUBT": "Quantum Computing Inc",
    "IBM": "IBM", "GOOGL": "Alphabet (Google)", "MSFT": "Microsoft", "NVDA": "Nvidia", "HON": "Honeywell",
    "AAPL": "Apple", "BTC-USD": "Bitcoin",
}
# Histories begin at the date each series is meaningful for this site.
START = {"QUBT": "2018-07-30", "IBM": "2010-01-04", "GOOGL": "2010-01-04", "MSFT": "2010-01-04",
         "NVDA": "2010-01-04", "HON": "2010-01-04", "AAPL": "1990-01-01", "BTC-USD": "2014-09-15"}


def refresh(tickers=None) -> dict:
    import yfinance as yf
    data = load() if CACHE.exists() else {}
    for sym in tickers or UNIVERSE:
        h = yf.Ticker(sym).history(period="max", interval="1wk", auto_adjust=True)["Close"].dropna()
        if h.empty:
            print(f"  {sym}: no data")
            continue
        start = START.get(sym, "0000")
        pairs = [(str(i.date()), round(float(v), 5)) for i, v in h.items() if str(i.date()) >= start]
        data[sym] = {"name": UNIVERSE.get(sym, sym), "d": [p[0] for p in pairs], "c": [p[1] for p in pairs]}
        print(f"  {sym}: {len(pairs)} weeks, {pairs[0][0]} to {pairs[-1][0]}")
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(data), encoding="utf-8")
    return data


def load() -> dict:
    return json.loads(CACHE.read_text(encoding="utf-8"))


def stats(s: dict) -> dict:
    """First, peak and latest close with dates, and the changes between them."""
    c, d = s["c"], s["d"]
    ip = max(range(len(c)), key=c.__getitem__)
    return {"first_date": d[0], "first": c[0], "peak_date": d[ip], "peak": c[ip], "last_date": d[-1], "last": c[-1],
            "x_from_start": c[-1] / c[0], "pct_from_peak": (c[-1] / c[ip] - 1) * 100}


def since(s: dict, start: str) -> dict:
    i = next((k for k, x in enumerate(s["d"]) if x >= start), len(s["d"]) - 1)
    return {"d": s["d"][i:], "c": s["c"][i:]}


def annual_vol(s: dict, weeks: int = 104) -> float:
    """Annualised volatility of weekly log returns over the last `weeks` weeks."""
    c = s["c"][-(weeks + 1):]
    r = [math.log(b / a) for a, b in zip(c, c[1:])]
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / (len(r) - 1)) * math.sqrt(52)


def best_run(s: dict, years: float = 2.0) -> dict:
    """Largest rise from a low to a later high within `years`, the shape an 'explosion' leaves behind."""
    c, d, w = s["c"], s["d"], int(years * 52)
    best = (1.0, 0, 0)
    for i in range(len(c)):
        j = max(range(i, min(len(c), i + w)), key=c.__getitem__)
        if c[j] / c[i] > best[0]:
            best = (c[j] / c[i], i, j)
    return {"multiple": best[0], "from": d[best[1]], "to": d[best[2]], "low": c[best[1]], "high": c[best[2]]}
