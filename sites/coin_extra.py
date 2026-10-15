"""Frontier Coin: reference data for the country map, evidence ladder and supply chain. Approximate, from public sources."""
from __future__ import annotations

TILES = {
    "CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "SV": (0, 2, "mixed"), "IE": (3, 0, "friendly"), "GB": (4, 0, "mixed"),
    "NL": (5, 0, "friendly"), "DE": (6, 0, "friendly"), "FR": (4, 1, "friendly"), "CH": (5, 1, "friendly"), "AE": (7, 2, "friendly"),
    "KR": (10, 0, "mixed"), "CN": (9, 1, "restrictive"), "JP": (11, 1, "mixed"), "IN": (8, 2, "mixed"), "SG": (9, 2, "mixed"), "AU": (10, 3, "mixed"),
}
NAMES = {"CA": "Canada", "US": "United States", "SV": "El Salvador", "IE": "Ireland", "GB": "United Kingdom", "NL": "Netherlands",
         "DE": "Germany", "FR": "France", "CH": "Switzerland", "AE": "United Arab Emirates", "KR": "South Korea", "CN": "China",
         "JP": "Japan", "IN": "India", "SG": "Singapore", "AU": "Australia"}
MAP_LABELS = {"co": "Firms", "gov": "Rules", "ctl": "Tax and limits", "note": "Read"}
COUNTRY = {
    "US": {"co": "Coinbase, Strategy, Circle, Marathon, Riot, BlackRock, Robinhood", "gov": "Spot Bitcoin funds approved in January 2024. The GENIUS Act (2025) set a federal framework for payment stablecoins",
           "ctl": "Gains taxed as property. Exchanges register with state and federal regulators", "note": "The deepest market and most of the listed companies. Policy has swung from enforcement to acceptance."},
    "CA": {"co": "Several exchanges and miners, first spot Bitcoin funds in 2021", "gov": "Securities regulators register trading platforms",
           "ctl": "Capital gains tax", "note": "Early to regulated funds. Cheap hydro power helped mining."},
    "SV": {"co": "State holdings of Bitcoin", "gov": "Made Bitcoin legal tender in 2021 and made acceptance voluntary in 2025 under an IMF programme",
           "ctl": "IMF conditions on public-sector use", "note": "The first country to try it as money. Few people use it."},
    "IE": {"co": "Several large exchanges keep staff or an EU base in Dublin; Kraken's European arm is authorised here", "gov": "The Central Bank of Ireland authorises firms under the EU MiCA rules",
           "ctl": "CGT on gains; MiCA consumer rules", "note": "A regulatory and employment hub for the sector. Check current authorisations before relying on this."},
    "GB": {"co": "Exchanges and funds, a large London trading desk base", "gov": "FCA registers firms for money-laundering checks and applies strict promotion rules since October 2023",
           "ctl": "Capital gains tax", "note": "A full regime is still being legislated."},
    "NL": {"co": "Exchanges and custody firms", "gov": "MiCA applies in full from 30 December 2024", "ctl": "Wealth-based taxation of holdings", "note": "Regulated, with a strong payments sector."},
    "DE": {"co": "Banks offering crypto custody, exchanges", "gov": "MiCA, plus an earlier national custody licence", "ctl": "Gains tax-free after a one-year hold for individuals", "note": "A bank-led market."},
    "FR": {"co": "Exchanges, Circle's EU base, hardware wallet makers", "gov": "MiCA, plus an earlier national licence", "ctl": "Flat tax on gains", "note": "A cautious regulator that wrote much of the template."},
    "CH": {"co": "Zug 'Crypto Valley' foundations, banks with custody", "gov": "FINMA licensing and a distributed-ledger law", "ctl": "No capital gains tax for private investors", "note": "A neutral home for token foundations."},
    "AE": {"co": "Large exchanges with regional headquarters", "gov": "Dubai's VARA and Abu Dhabi's regulator licence virtual-asset firms", "ctl": "No personal income tax", "note": "Competes hard to host the industry."},
    "KR": {"co": "Large domestic exchanges", "gov": "Trading through real-name bank accounts", "ctl": "A gains tax has been repeatedly delayed", "note": "Very high retail participation."},
    "CN": {"co": "Equipment makers, notably mining machines", "gov": "Banned trading and mining in 2021 and pushes its own digital yuan", "ctl": "Capital controls", "note": "Mining left China in 2021, mostly to the US and Kazakhstan."},
    "JP": {"co": "Registered domestic exchanges", "gov": "Licensing by the FSA after Mt. Gox and Coincheck", "ctl": "Gains taxed as income, up to 55%", "note": "Strict custody rules came from large hacks."},
    "IN": {"co": "Domestic exchanges, large retail user base", "gov": "No ban and no comprehensive law", "ctl": "30% tax on gains and 1% withheld on each trade", "note": "The tax pushed much trading offshore."},
    "SG": {"co": "Exchanges and funds, a finance hub", "gov": "MAS licenses providers and limits retail marketing", "ctl": "No capital gains tax", "note": "Tightened after the 2022 collapses."},
    "AU": {"co": "Exchanges, spot funds listed in 2024", "gov": "Exchanges register with AUSTRAC", "ctl": "Capital gains tax", "note": "Steadily building a licensing regime."},
}

HYPE = [
    ("5", "On-chain and audited", "Data anyone can check on the public ledger, or audited accounts", "Bitcoin supply, wallet balances, stablecoin reserves with an attestation", "ok"),
    ("4", "Regulated filing", "A prospectus, SEC filing or a licence application", "Company 10-Ks, spot fund prospectuses", "ok"),
    ("3", "Exchange data", "Prices and volumes from trading venues, often self-reported", "Reported trading volumes, listing dates", "dis"),
    ("2", "Company claim", "A statement by the project or firm", "Roadmaps, 'partnership' announcements, treasury plans", "tgt"),
    ("1", "Influencer or social post", "An opinion with no checkable fact behind it", "Price targets, 'next 100x' lists", "tgt"),
]

SHOVELS = [
    ("Exchanges", "Coinbase, Kraken, Binance, Bitstamp", "US, Ireland, global", "Where most people buy. Revenue follows trading volume"),
    ("Custody", "Coinbase Custody, Anchorage, bank custodians", "US, Switzerland", "Holds the keys for funds and institutions"),
    ("Stablecoin issuers", "Circle (USDC), Tether (USDT)", "US, global", "Earn the interest on the reserves"),
    ("Mining machines", "Bitmain, MicroBT, Canaan", "China, Singapore", "A handful of makers supply almost every miner"),
    ("Fund wrappers", "BlackRock, Fidelity, Grayscale", "US", "The route most institutions use"),
    ("Analytics and compliance", "Chainalysis, Elliptic", "US, UK", "Traces coins for banks and police"),
]

STUDY_ROWS = [
    ("Fantom (FTM)", "1,439x", "Mar 2020", "Jan 2022", "-79%"), ("Axie Infinity (AXS)", "1,192x", "Nov 2020", "Nov 2021", "-99%"),
    ("BNB", "877x", "Nov 2017", "Oct 2025", "-44%"), ("Ethereum (ETH)", "716x", "Dec 2016", "Aug 2025", "-50%"),
    ("Bitcoin (BTC)", "591x", "Aug 2015", "Oct 2025", "-34%"), ("Dogecoin (DOGE)", "436x", "Mar 2020", "May 2021", "-88%"),
    ("The Sandbox (SAND)", "243x", "Nov 2020", "Nov 2021", "-99%"), ("Solana (SOL)", "219x", "Dec 2020", "Jan 2025", "-60%"),
    ("Chainlink (LINK)", "136x", "Jan 2019", "May 2021", "-76%"), ("Cardano (ADA)", "127x", "Mar 2020", "Sep 2021", "-92%"),
]
