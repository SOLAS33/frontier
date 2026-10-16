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
    # Frontier Coin
    "COIN": "Coinbase", "MSTR": "Strategy", "MARA": "Marathon Digital", "RIOT": "Riot Platforms", "CRCL": "Circle",
    "HOOD": "Robinhood", "PYPL": "PayPal", "BLK": "BlackRock", "ETH-USD": "Ethereum", "SOL-USD": "Solana",
    # Frontier Mind
    "AMD": "AMD", "MU": "Micron", "CRWV": "CoreWeave", "SMCI": "Super Micro", "AMZN": "Amazon", "META": "Meta", "AVGO": "Broadcom",
    # Frontier Atom
    "OKLO": "Oklo", "SMR": "NuScale", "LEU": "Centrus Energy", "NNE": "Nano Nuclear", "BWXT": "BWX Technologies", "CEG": "Constellation Energy",
    "VST": "Vistra", "CCJ": "Cameco",
    # Frontier Cell
    # Frontier Bot, Drone, Fusion
    "SYM": "Symbotic", "SERV": "Serve Robotics", "TER": "Teradyne", "ISRG": "Intuitive Surgical", "ROK": "Rockwell Automation",
    "AVAV": "AeroVironment", "KTOS": "Kratos", "RCAT": "Red Cat", "ONDS": "Ondas", "UMAC": "Unusual Machines", "LMT": "Lockheed Martin",
    "NOC": "Northrop Grumman", "RTX": "RTX", "AMSC": "American Superconductor", "BRKR": "Bruker", "LASR": "nLight", "GEV": "GE Vernova",
    "QS": "QuantumScape", "ENVX": "Enovix", "EOSE": "Eos Energy", "FLNC": "Fluence", "ALB": "Albemarle", "TSLA": "Tesla", "GM": "General Motors", "F": "Ford",
    # Frontier Chip, Orbit, Gene, Carbon, Tide, Mine
    "TSM": "TSMC", "ASML": "ASML", "INTC": "Intel", "AMAT": "Applied Materials", "LITE": "Lumentum",
    "RKLB": "Rocket Lab", "ASTS": "AST SpaceMobile", "PL": "Planet Labs", "LUNR": "Intuitive Machines", "RDW": "Redwire",
    "CRSP": "CRISPR Therapeutics", "NTLA": "Intellia", "BEAM": "Beam Therapeutics", "LLY": "Eli Lilly", "NVO": "Novo Nordisk",
    "NVX": "Novonix", "WWR": "Westwater Resources", "NMG": "Nouveau Monde Graphite",
    "OPTT": "Ocean Power Technologies", "WAVE": "Eco Wave Power", "ORA": "Ormat Technologies", "FRVO": "Fervo Energy",
    "MP": "MP Materials", "UUUU": "Energy Fuels", "LAC": "Lithium Americas", "FCX": "Freeport-McMoRan",
}
# Histories begin at the date each series is meaningful for this site.
START = {"QUBT": "2018-07-30", "IBM": "2010-01-04", "GOOGL": "2010-01-04", "MSFT": "2010-01-04",
         "NVDA": "2010-01-04", "HON": "2010-01-04", "AAPL": "1990-01-01", "BTC-USD": "2014-09-15",
         "ETH-USD": "2017-11-09", "SOL-USD": "2020-04-10", "COIN": "2021-04-14", "HOOD": "2021-07-29", "PYPL": "2015-07-20", "BLK": "2010-01-04",
         "MSTR": "2020-08-01", "MARA": "2018-06-01", "RIOT": "2018-01-01", "CRCL": "2025-06-05",
         "NVDA": "2010-01-04", "AMD": "2010-01-04", "MU": "2010-01-04", "CRWV": "2025-03-28", "SMCI": "2010-01-04", "AMZN": "2010-01-04",
         "META": "2012-05-18", "AVGO": "2010-01-04", "OKLO": "2024-05-09", "SMR": "2022-03-02", "LEU": "2020-01-01", "NNE": "2024-05-20",
         "BWXT": "2016-07-01", "CEG": "2022-02-02", "VST": "2016-05-01", "CCJ": "2010-01-04", "QS": "2020-11-30", "ENVX": "2021-07-14",
         "EOSE": "2020-11-01", "FLNC": "2021-10-28", "ALB": "2010-01-04", "TSLA": "2010-06-29", "GM": "2010-11-18", "F": "2010-01-04",
         "SYM": "2022-06-27", "SERV": "2021-01-01", "TER": "2010-01-04", "ISRG": "2010-01-04", "ROK": "2010-01-04", "AVAV": "2010-01-04",
         "KTOS": "2010-01-04", "RCAT": "2019-01-01", "ONDS": "2020-01-01", "UMAC": "2024-02-09", "LMT": "2010-01-04", "NOC": "2010-01-04",
         "RTX": "2010-01-04", "TSM": "2016-01-04", "ASML": "2016-01-04", "INTC": "2016-01-04", "AMAT": "2016-01-04", "LITE": "2016-01-04", "LLY": "2016-01-04", "NVO": "2016-01-04", "WWR": "2016-01-04", "OPTT": "2016-01-04", "ORA": "2016-01-04", "UUUU": "2016-01-04", "FCX": "2016-01-04", "AMSC": "2018-01-01", "BRKR": "2010-01-04", "LASR": "2018-01-01", "GEV": "2024-04-02"}


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
