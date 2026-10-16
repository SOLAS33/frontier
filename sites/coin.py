"""Frontier Coin: copy, data and assembly. Voice rules are in docs/VOICE.md and are checked by tools/voice_lint.py."""
from __future__ import annotations

import json

from frontier import art, art_coin, charts, prices
from frontier.components import band, chapter, fig, key_idea, note, photo, series_list, watch_promo
from frontier.scenarios import Scenario, simulate
from sites import coin_extra as X
from sites.quantum_extra import tile_map
from sites import tech_blocks as TB

TITLE = "Frontier Coin"
AS_OF = "16 October 2026"

LIVE = {"cik": {"COIN": 1679788, "MSTR": 1050446, "MARA": 1507605, "RIOT": 1167419, "CRCL": 1876042},
        "aliases": {"COIN": ["coinbase"], "MSTR": ["microstrategy", "strategy inc", "saylor"], "MARA": ["marathon digital", "mara holdings", "marathon"],
                    "RIOT": ["riot platforms", "riot blockchain"], "CRCL": ["circle internet", "usdc", "circle ("]},
        "arxiv_terms": ["Bitcoin", "Ethereum", "stablecoin"], "arxiv_cat": "cs.CR"}

REFS = [
    (1, "Nakamoto, S. (2008). Bitcoin: a peer-to-peer electronic cash system.", "https://bitcoin.org/bitcoin.pdf"),
    (2, "Cambridge Centre for Alternative Finance. Cambridge Bitcoin Electricity Consumption Index.", "https://ccaf.io/cbnsi/cbeci"),
    (3, "Webber et al. (2022). The impact of hardware specifications on reaching quantum advantage in the fault tolerant regime (Bitcoin signature estimate).", "https://arxiv.org/abs/2108.12371"),
    (4, "Roetteler et al. (2017). Quantum resource estimates for computing elliptic curve discrete logarithms.", "https://arxiv.org/abs/1706.06752"),
    (5, "Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits.", "https://arxiv.org/abs/2505.15917"),
    (6, "NIST. Post-quantum cryptography standards (FIPS 203, 204, 205).", "https://csrc.nist.gov/projects/post-quantum-cryptography"),
    (7, "BIP 360: pay to quantum resistant hash (draft proposal).", "https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki"),
    (8, "European Union. Regulation (EU) 2023/1114 on markets in crypto-assets (MiCA).", "https://eur-lex.europa.eu/eli/reg/2023/1114/oj"),
    (9, "Bank for International Settlements (2023). Crypto shocks and retail losses. BIS Bulletin 69.", "https://www.bis.org/publ/bisbull69.htm"),
    (10, "International Energy Agency (2024). Electricity 2024: data centres, AI and cryptocurrencies.", "https://www.iea.org/reports/electricity-2024"),
    (11, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/"),
    (12, "Solas33 (2026). World-State Engine crypto focus study: take-offs, 100x tokens and listings, 652 tokens.", "https://frontier.solas33.com/coin/#study"),
]
REFS = REFS + TB.COIN_REFS + [(18, "Silicon Republic (2023). Coinbase chooses Dublin as its EU regulatory hub.", "https://siliconrepublic.com/?p=1052620"),
    (19, "Business Wire (2025). Kraken secures MiCA licence from the Central Bank of Ireland.", "https://www.businesswire.com/news/home/20250625529871/en"),
    (20, "The Block (2025). Kraken secures MiCA license in Ireland; Coinbase obtained its MiCA license in Luxembourg.", "https://www.theblock.co/post/359751/kraken-secures-mica-license-in-ireland-to-scale-european-operations")]
RTITLE = {n: t for n, t, _ in REFS}


def cite(*ids):
    return "".join(f'<sup><a href="#r{i}" title="{RTITLE[i]}">[{i}]</a></sup>' for i in ids)


def fmt_p(v):
    return f"${v:,.2f}" if v < 100 else f"${v:,.0f}"


SCEN = {
    "COIN": [Scenario("bear", "Trading volumes dry up in a long crypto winter", 0.35, -0.40, 0.75),
             Scenario("base", "Volumes recover, new revenue lines grow slowly", 0.40, 0.10, 0.75),
             Scenario("bull", "A new boom and stablecoin and payments revenue scale", 0.25, 0.50, 0.75)],
    "MSTR": [Scenario("bear", "Bitcoin falls and the premium to its holdings disappears", 0.40, -0.50, 0.75),
             Scenario("base", "Bitcoin drifts, the company keeps funding purchases", 0.35, 0.00, 0.75),
             Scenario("bull", "Bitcoin rises and the premium returns", 0.25, 0.55, 0.75)],
    "MARA": [Scenario("bear", "Hashprice stays low and costs outrun revenue", 0.45, -0.50, 0.75),
             Scenario("base", "Mining breaks even and hosting grows a little", 0.35, 0.00, 0.75),
             Scenario("bull", "Bitcoin rises or data-centre hosting lands big contracts", 0.20, 0.55, 0.75)],
    "RIOT": [Scenario("bear", "Hashprice stays low and expansion stalls", 0.40, -0.45, 0.75),
             Scenario("base", "Mining holds, hosting contracts arrive slowly", 0.35, 0.00, 0.75),
             Scenario("bull", "Its power sites win large data-centre tenants", 0.25, 0.50, 0.75)],
    "CRCL": [Scenario("bear", "Interest rates fall and rivals take share", 0.35, -0.35, 0.75),
             Scenario("base", "USDC grows steadily", 0.40, 0.05, 0.75),
             Scenario("bull", "Stablecoin payments go mainstream", 0.25, 0.40, 0.75)],
}

COMPANIES = [
    {"t": "COIN", "name": "Coinbase", "kind": "Exchange and custody",
     "rivals": "Kraken, Binance, Robinhood, Crypto.com, and the banks",
     "profit": "Already profitable in good years. It has to earn more from things that do not depend on trading volume: custody, stablecoin revenue and its Base network.",
     "watch": "Trading volume, share of revenue from USDC and subscriptions, regulatory outcomes, hacks.",
     "rank": "The largest regulated exchange in the US. Revenue still swings with the price of Bitcoin.",
     "verdict": "The industry's utility, and priced like it"},
    {"t": "MSTR", "name": "Strategy", "kind": "Bitcoin holding company",
     "rivals": "Spot Bitcoin funds such as BlackRock's IBIT",
     "profit": "It makes no money from software that matters to the share price. It works only if Bitcoin rises and investors pay more than the value of the coins it holds.",
     "watch": "Its premium to Bitcoin held, debt and preferred share payments, how it funds each purchase.",
     "rank": "The biggest corporate holder of Bitcoin. A bet on one asset, financed partly with debt.",
     "verdict": "Not a software company. A Bitcoin proxy with debt"},
    {"t": "MARA", "name": "Marathon Digital", "kind": "Bitcoin mining",
     "rivals": "Riot, CleanSpark, Core Scientific, and the newer data-centre landlords",
     "profit": "Mine Bitcoin for less than it sells for, after each halving cuts the reward, or find a better use for its power sites.",
     "watch": "Cost to mine one coin, hashprice (what a unit of mining power earns in a day), power contracts, hosting deals, share sales.",
     "rank": "Among the largest miners by hash rate. A price-taker in a business with falling rewards.",
     "verdict": "Gains in a rally, pain in every winter"},
    {"t": "RIOT", "name": "Riot Platforms", "kind": "Bitcoin mining",
     "rivals": "Marathon, CleanSpark, Core Scientific, data-centre landlords",
     "profit": "Same sum as Marathon, but with large power sites in Texas that could be sold to data-centre tenants instead.",
     "watch": "Hosting or lease contracts for its power, cost per coin, power credits, share sales.",
     "rank": "A top-tier miner with cheap, flexible power.",
     "verdict": "A miner with an option on being a landlord"},
    {"t": "CRCL", "name": "Circle", "kind": "Stablecoin issuer (USDC)",
     "rivals": "Tether, PayPal's stablecoin, bank-issued tokens",
     "profit": "It earns interest on the dollars behind every USDC. Profit grows with USDC in circulation and falls when interest rates fall.",
     "watch": "USDC in circulation, interest rates, the share of income paid to distributors such as Coinbase.",
     "rank": "The leading regulated dollar stablecoin. Listed in June 2025, so the price history is short.",
     "verdict": "A rate-sensitive bank with a new label"},
]

LADDER = [("Idea", "A paper and|a few believers"), ("Early users", "Hobbyists and|traders"), ("Big exchanges", "Coinbase and|Binance list it"),
          ("Regulated funds", "Spot funds launch|in 2024"), ("Banks and payments", "Stablecoins and|tokenised assets"),
          ("Everyday money", "Used to pay,|not to speculate"), ("Profit for the builders", "Infrastructure|earns a margin")]

KEY = {
    "learn": key_idea("A shared notebook that nobody owns",
                      "Crypto is a ledger kept by thousands of computers that agree on the same list of who owns what, without a bank in the middle. "
                      "Your coins are an entry in that list, and a secret key is the only thing that lets you move them. Lose the key and the "
                      "coins are gone. That is the whole invention, and it is also why it is so easy to get wrong."),
    "simple": key_idea("Money, plumbing and a casino",
                       "Some of crypto is a new way to move money, some is plumbing for banks and funds, and a large part is people trading "
                       "something with no cash flow. Knowing which part you are looking at matters more than any price chart."),
    "change": key_idea("Regulators arrived before the mass market did",
                       "In the last two years the biggest markets wrote rules for exchanges and stablecoins, and the big asset managers launched "
                       "regulated Bitcoin funds. That made crypto easier for institutions to hold and harder for scammers to hide in. The next "
                       "question is whether people use it to pay, and whether quantum computers eventually threaten it."),
    "companies": key_idea("The companies live and die by the price of one asset",
                          "Exchanges earn when people trade, miners earn when Bitcoin is worth more than it costs to make, treasury companies earn "
                          "when investors pay a premium for their coins, and issuers earn interest. All four tie back to the same price chart."),
    "hurdles": key_idea("Security, rules and energy are the limits",
                        "Hacks and lost keys have cost holders billions. Rules differ by country and change by election. A proof-of-work network "
                        "uses as much electricity as a mid-sized country. And a future quantum computer could forge the signatures that "
                        "protect Bitcoin, unless the network changes first."),
    "outlook": key_idea("Bitcoin has a rhythm. The stocks magnify it",
                        "Bitcoin has risen for about a year after each halving, then fallen hard. The companies in this chapter move more than "
                        "Bitcoin does, in both directions. If the rhythm holds the next few years are a winter followed by a thaw, and several "
                        "listed firms will not make it through unchanged."),
}


def build():
    px = prices.load()
    stat = {t: prices.stats(px[t]) for t in px}
    run_syms = ["COIN", "MSTR", "MARA", "RIOT", "BTC-USD", "ETH-USD", "SOL-USD", "AAPL", "NVDA"]
    runs = {t: prices.best_run(px[t]) for t in run_syms}
    sims = {t: simulate(px[t]["c"][-1], prices.annual_vol(px[t]), sc, years=3) for t, sc in SCEN.items()}
    btc = stat["BTC-USD"]

    order = ["COIN", "MSTR", "MARA", "RIOT", "CRCL", "HOOD", "PYPL", "BLK", "BTC-USD", "ETH-USD"]
    names = {t: px[t]["name"] for t in order}
    all_t = order + ["SOL-USD", "AAPL", "NVDA"]
    series_js = {t: {"d": px[t]["d"], "c": [round(v, 3) for v in px[t]["c"]]} for t in all_t}
    scen_js = {}
    for t in SCEN:
        vol = prices.annual_vol(px[t])
        scen_js[t] = {"name": px[t]["name"], "price": px[t]["c"][-1], "tilt_pts": 0,
                      "hist": {"d": px[t]["d"][-104:], "c": [round(v, 3) for v in px[t]["c"][-104:]]},
                      "scen": [{"k": s.key, "label": s.label, "p": s.probability, "drift": s.drift, "sigma": round(vol * s.vol_mult, 4)} for s in SCEN[t]]}
    tm_assets = [["BTC-USD", "Bitcoin"], ["ETH-USD", "Ethereum"], ["SOL-USD", "Solana"], ["COIN", "Coinbase"], ["MSTR", "Strategy"],
                 ["MARA", "Marathon Digital"], ["AAPL", "Apple"], ["NVDA", "Nvidia"]]
    tm_default = {"BTC-USD": "2016-01-25", "ETH-USD": px["ETH-USD"]["d"][0], "SOL-USD": px["SOL-USD"]["d"][0], "COIN": px["COIN"]["d"][0],
                  "MSTR": "2020-08-03", "MARA": "2020-04-13", "AAPL": "1997-12-22", "NVDA": "2022-10-10"}
    data_js = (f"window.PRICES={json.dumps(series_js, separators=(',', ':'))};"
               f"window.PRICE_ORDER={json.dumps(order)};window.PRICE_NAMES={json.dumps(names)};window.PRICE_DEFAULT={json.dumps(['COIN', 'MSTR', 'MARA', 'RIOT', 'BTC-USD'])};"
               f"window.SCEN={json.dumps(scen_js, separators=(',', ':'))};"
               f"window.TM_ASSETS={json.dumps(tm_assets)};window.TM_DEFAULT={json.dumps(tm_default)};"
               f"window.COUNTRY={json.dumps(X.COUNTRY)};window.COUNTRY_NAMES={json.dumps(X.NAMES)};"
               f"window.MAP_LABELS={json.dumps(X.MAP_LABELS)};window.MAP_DEFAULT=\"IE\";")

    def basket(members):
        idx = {t: dict(zip(px[t]["d"], px[t]["c"])) for t in members}
        start = max(px[t]["d"][0] for t in members)
        dates = [d for d in px[members[0]]["d"] if d >= start and all(d in idx[t] for t in members)]
        lvl, out = 100.0, []
        for i, d in enumerate(dates):
            if i:
                lvl *= 1 + sum(idx[t][d] / idx[t][dates[i - 1]] - 1 for t in members) / len(members)
            out.append(lvl)
        return dates, out
    pd_d, pd_v = basket(["COIN", "MSTR", "MARA", "RIOT"])
    bg_d, bg_v = basket(["HOOD", "PYPL", "BLK"])
    bg = [(d, v) for d, v in zip(bg_d, bg_v) if d >= pd_d[0]]
    btc_d = [d for d in px["BTC-USD"]["d"] if d >= pd_d[0]]
    btc_c = [c for d, c in zip(px["BTC-USD"]["d"], px["BTC-USD"]["c"]) if d >= pd_d[0]]
    idx_svg = charts.index_chart([("Crypto pure-plays", pd_d, pd_v, "var(--amber)"),
                                  ("Large groups", [d for d, _ in bg], [v / bg[0][1] * 100 for _, v in bg], "var(--teal)"),
                                  ("Bitcoin", btc_d, [c / btc_c[0] * 100 for c in btc_c], "var(--violet)")])
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult_items = [
        ("Apple, 1997 to 1999", f"from {runs['AAPL']['from']}", runs["AAPL"]["multiple"], "ref"),
        ("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
        ("Bitcoin", f"from {runs['BTC-USD']['from']}", runs["BTC-USD"]["multiple"], "lay"),
        ("Ethereum", f"from {runs['ETH-USD']['from']}", runs["ETH-USD"]["multiple"], "lay"),
        ("Solana", f"from {runs['SOL-USD']['from']}", runs["SOL-USD"]["multiple"], "lay"),
        ("Marathon Digital", f"from {runs['MARA']['from']}", runs["MARA"]["multiple"], "quantum"),
        ("Riot Platforms", f"from {runs['RIOT']['from']}", runs["RIOT"]["multiple"], "quantum"),
        ("Strategy", f"from {runs['MSTR']['from']}", runs["MSTR"]["multiple"], "quantum"),
        ("Coinbase", f"from {runs['COIN']['from']}", runs["COIN"]["multiple"], "quantum"),
    ]

    def stat_cell(val, label, pre="", suf=""):
        return f'<div class="stat"><b data-count="{val}" data-pre="{pre}" data-suf="{suf}">{pre}{val:,.0f}{suf}</b><span>{label}</span></div>'

    hero = f'''<header class="fx-hero" id="top">
<div class="fx-hero-img"><img src="img/gold-doppie.jpg" alt="" decoding="async"></div>{art.hero_chain()}
<div class="fx-hero-in"><div class="fx-kicker">Frontier / Coin</div>
<h1>Money with <em>no bank</em> behind it</h1>
<p class="lead">Crypto is part invention, part plumbing and part casino. Here is which part is which, who earns a living from it, and what a quantum computer would do to it.</p>
<div class="fx-stats">
{stat_cell(round(btc["last"] / 1000), "US dollars per Bitcoin today, in thousands", "$", "k")}
{stat_cell(round(abs(btc["pct_from_peak"])), "below its 2025 peak (weekly close)", "", "%")}
{stat_cell(25, "of 652 tokens ever rose 100-fold, and most are down 90% or more", "", "")}
{stat_cell(150, "terawatt-hours a year, roughly, for the Bitcoin network", "", " TWh")}
</div></div></header>
<div class="fx-ticker" aria-label="Live prices and announcements"><div class="fx-ticker-track" id="fx-ticker-track"><span>Prices and announcements load here.</span></div></div>'''

    notice = ('<div class="callout r wide" style="margin-top:70px"><b>Information only.</b> We explain how crypto works and show how its '
              'companies and their shares have behaved. We do not recommend any coin, company or trade. Projections are scenarios, not '
              'forecasts. Crypto-assets are volatile and can fall to zero. The disclosures are at the foot of the page.</div>')

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "The ledger, the keys, the miners, the exchanges, and the ways people lose money.", f'''
<p>Bitcoin began in 2008 as a nine-page paper by a person or group using the name Satoshi Nakamoto.{cite(1)} The idea was a list of who owns what, kept by thousands of computers that all check each other, so that no bank has to keep it. The first list entry was written in January 2009.</p>
{note("In one line", "<p>A ledger nobody owns, a key only you hold, and a rule for who gets to write the next page.</p>")}
<p>Three parts do the work. A <b>ledger</b> is split into pages called blocks, each carrying a fingerprint of the page before, so changing history breaks every later fingerprint. A <b>private key</b> signs each payment, and anyone can check the signature with the matching public key. A <b>rule for the next page</b> decides who writes it: Bitcoin makes computers race with electricity (mining), while Ethereum and most newer coins pick writers by who has locked up coins (staking).</p>
{note("The catch", "<p>If you lose the key, nobody can recover the coins. If someone steals it, nobody can reverse the payment. There is no helpline.</p>")}
<div class="cols wide">
<figure class="fig rv" style="margin:0">{art_coin.ledger()}<figcaption><b>The ledger.</b> Pages chained together by fingerprints.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art_coin.signature()}<figcaption><b>The key.</b> A signature that only the owner can make.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art_coin.peg()}<figcaption><b>The stablecoin.</b> A token that tries to hold one dollar.</figcaption></figure>
</div>
<h3 class="wide" id="s-where" data-nav="Where" style="margin-top:36px">Where people actually hold it</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>On an exchange</h3><p>You hold an IOU from a company that holds the keys. Easy, regulated in the big markets, and exposed to the exchange's failure. FTX was one.</p></div>
<div class="card rv"><h3>In your own wallet</h3><p>You hold the key. Nobody can freeze it and nobody can rescue it.</p></div>
<div class="card rv"><h3>In a fund</h3><p>A regulated fund holds the coins and you hold a share, in an ordinary brokerage account. Since 2024 this is how most institutions get exposure.</p></div>
<div class="card rv"><h3>As a stablecoin</h3><p>A token backed by dollars in a bank, which pays the issuer the interest. The part of crypto that is nearest to ordinary payments.</p></div>
</div>
{TB.coin_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev big"><div class="yr">2008 to 2009</div><p>The Bitcoin paper is published and the first block is written.{cite(1)}</p></div>
<div class="ev"><div class="yr">2010</div><p>Someone pays 10,000 coins for two pizzas, the first known purchase.</p></div>
<div class="ev"><div class="yr">2014</div><p>The Mt. Gox exchange collapses after losing about 850,000 coins.</p></div>
<div class="ev big"><div class="yr">2015</div><p>Ethereum launches with programmable contracts.</p></div>
<div class="ev"><div class="yr">2017</div><p>The initial coin offering boom. Most of the tokens sold are worth little by 2019.</p></div>
<div class="ev"><div class="yr">2020</div><p>The March crash, then a stimulus-fuelled run that takes many coins up by 100 times.</p></div>
<div class="ev"><div class="yr">2022</div><p>Terra's coin collapses in May and FTX fails in November. Retail losses are large.{cite(9)}</p></div>
<div class="ev big"><div class="yr">Jan 2024</div><p>US regulators approve spot Bitcoin funds. Within a year the funds held hundreds of thousands of coins.</p></div>
<div class="ev"><div class="yr">Dec 2024</div><p>The EU's MiCA rules apply in full.{cite(8)} Bitcoin passes $100,000 for the first time.</p></div>
<div class="ev big"><div class="yr">2025</div><p>The US passes the GENIUS Act, a federal framework for dollar stablecoins. Bitcoin peaks in the autumn near ${btc["peak"] / 1000:.0f}k.</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>A year of falling prices. Bitcoin is now ${btc["last"] / 1000:.0f}k, {abs(btc["pct_from_peak"]):.0f}% below that peak.</p></div>
</div>''', KEY["learn"], short="Basics")

    ch2 = chapter("simple", 2, "The short version", "What you need to follow the rest.", f'''
<div class="cols wide">
<div class="card rv"><h3>Money</h3><p>Bitcoin is mostly used as a store of value that people hope will rise, not as something to buy a coffee with. In a few countries with weak currencies, people do use stablecoins to hold dollars.</p></div>
<div class="card rv"><h3>Plumbing</h3><p>Banks, funds and payment firms are testing the same technology to settle trades faster. Tokenised money market funds and bonds are the examples to watch.</p></div>
<div class="card rv"><h3>Casino</h3><p>Most of the thousands of tokens have no cash flow and no use. Their price is what the next buyer will pay. Of 652 tokens we studied, 25 ever rose 100-fold, and 21 of those are now down 75% or more.{cite(12)}</p></div>
</div>
<div class="wide">{photo("hyperinflation-note.jpg", caption="A one million mark note issued in Bonn in 1923, during German hyperinflation. Every currency story in crypto starts from a failure like this one.")}</div>''', KEY["simple"], short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Rules first, funds second, payments third, and a quantum question underneath.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2027: rules</div><p>MiCA licences in the EU, a US stablecoin law, and licensing in Singapore, Dubai and the UK. Exchanges that cannot get a licence leave the market.{cite(8)}</p></div>
<div class="ev fut"><div class="yr">2026 to 2028: wrappers</div><p>Spot funds, then funds for other coins, then tokenised funds that settle on a blockchain. The route most big investors take is through a fund, not a wallet. <a href="../chain/">Frontier Chain</a> follows the tokenisation side.</p></div>
<div class="ev fut"><div class="yr">2027 to 2030: payments</div><p>Stablecoins used by firms to move money across borders and by apps as a default dollar. Banks that issue their own tokens.</p></div>
<div class="ev fut"><div class="yr">Whenever it comes: quantum</div><p>A large enough quantum computer could forge the signatures that protect most coins. Everything below depends on whether the networks change first.</p></div>
</div>
<h3 class="wide" id="s-quantum" data-nav="Quantum" style="margin-top:36px">The quantum risk to Bitcoin</h3>
<div class="cols wide">
<div class="card rv"><h3>What is at risk</h3><p>Bitcoin signs payments with elliptic-curve cryptography. A large quantum computer running Shor's algorithm could work out a private key from a public key.{cite(4)} Coins in addresses whose public key is already visible on the chain are exposed. Older address types and any address that has spent before are the main cases.</p></div>
<div class="card rv"><h3>How big a machine</h3><p>One estimate says breaking a Bitcoin signature within an hour would need about 317 million physical qubits, and within a day about 13 million.{cite(3)} The best machines today have a few hundred usable qubits. RSA-2048 now needs under a million on the newest estimate.{cite(5)}</p></div>
<div class="card rv"><h3>What the network can do</h3><p>Move coins to quantum-safe addresses and add a new signature type. Proposals exist.{cite(7)} NIST has standardised replacement algorithms.{cite(6)} The hard part is agreement, and what to do about coins whose owners never move them.</p></div>
</div>
<div class="callout wide"><b>Our read.</b> This is a slow-moving problem with a known fix, not a near-term threat. The risk to watch for is a sudden jump in the best qubit estimates, which the Frontier Quantum site tracks.</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:44px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>A regulator in Dublin</h3><p>The Central Bank of Ireland authorises crypto firms under MiCA, and a firm authorised here can serve the whole EU.{cite(8)} Kraken received its MiCA licence from the Central Bank of Ireland on 25 June 2025.{cite(19)} Coinbase chose Dublin as its EU hub in 2023 but obtained its MiCA licence in Luxembourg.{cite(18)}{cite(20)}</p></div>
<div class="card rv"><h3>Tax</h3><p>Gains are subject to capital gains tax, and Revenue expects them to be declared. Mining and staking income can be taxed as income.</p></div>
<div class="card rv"><h3>The warning label</h3><p>The Central Bank requires warnings on crypto adverts and has repeated that investors can lose all their money. This site follows that spirit.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>Before you buy anything</h3><p>Decide the amount you could lose in full without changing your life. Use a regulated platform in your own country. Keep a record of every trade for tax.</p></div>
<div class="card rv"><h3>Before you trust a platform</h3><p>Check that it holds a licence, publishes proof of reserves and separates customer assets from its own. Assume anything promising fixed high returns is a scam.</p></div>
<div class="card rv"><h3>Before you hold your own keys</h3><p>Write down the recovery phrase on paper. Store it away from the device. Never type it into a website or give it to anyone, including support staff.</p></div>
</div>
<h3 class="wide" id="s-defence" data-nav="States" style="margin-top:44px">States, sanctions and secrecy</h3>
<div class="cols wide">
<div class="card rv"><h3>States hold it</h3><p>Governments seized coins in criminal cases and a few have bought them. Sanctions evasion and ransomware payments have also run through crypto, which is why exchanges now trace coins.</p></div>
<div class="card rv"><h3>What you cannot see</h3><p>Some state holdings and some mining activity are not disclosed. Any ranking of "who holds how much" is an estimate.</p></div>
</div>''', KEY["change"], short="Change")

    cos = []
    for c in COMPANIES:
        s = stat[c["t"]]
        cos.append(f'''<article class="card co rv"><h3>{c["name"]}<span>{c["t"]} &middot; {c["kind"]}</span></h3>
<dl><dt>Started at</dt><dd>{fmt_p(s["first"])} in {s["first_date"][:7]}. Now {fmt_p(s["last"])}. Peak {fmt_p(s["peak"])} in {s["peak_date"][:7]}, so {abs(s["pct_from_peak"]):.0f}% below it.</dd>
<dt>Rivals</dt><dd>{c["rivals"]}</dd><dt>Needs for profit</dt><dd>{c["profit"]}</dd><dt>Watch</dt><dd>{c["watch"]}</dd>
<dt>How it stands</dt><dd>{c["rank"]}</dd></dl><span class="verdict">{c["verdict"]}</span></article>''')
    hype = "".join(f'<tr><td class="n">{lvl}</td><td><b>{name}</b><br><span class="muted">{desc}</span></td><td>{ex}</td>'
                   f'<td><span class="tag {cls}">{"strong" if cls == "ok" else "caution" if cls == "dis" else "weak"}</span></td></tr>'
                   for lvl, name, desc, ex, cls in X.HYPE)
    shovels = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in X.SHOVELS)
    study = "".join(f"<tr><td>{a}</td><td class='n'>{b}</td><td class='n'>{c}</td><td class='n'>{d}</td><td class='n'>{e}</td></tr>" for a, b, c, d, e in X.STUDY_ROWS)
    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Who earns a living from crypto, what has to happen for them to make money, and what past booms did to their shares.", f'''
<div class="cols wide">{"".join(cos)}
<article class="card co rv"><h3>The big groups<span>BlackRock, Robinhood, PayPal</span></h3>
<dl><dt>Position</dt><dd>BlackRock runs the largest spot Bitcoin fund. Robinhood earns on crypto trading for retail customers. PayPal runs a stablecoin and lets users buy and sell.</dd>
<dt>Why they matter</dt><dd>Crypto is a small part of each business, so Bitcoin moves their shares by a few per cent.</dd>
<dt>Use</dt><dd>A lower-risk way to hold the theme, with a much smaller upside if it works.</dd></dl>
<span class="verdict">Where the money goes when it wants a wrapper</span></article></div>
<h3 class="wide" id="s-prices" data-nav="Prices" style="margin-top:44px">Share prices and coins</h3>
<p class="wide">Weekly closes to <span id="lastdate"></span>, adjusted for splits. Coin prices are in US dollars.</p>
<div class="ctrl wide" id="tickers" role="group" aria-label="Companies"></div>
<div class="ctrl wide" role="group" aria-label="Chart options">
<button data-mode="growth" aria-pressed="true">Growth, 100 = start</button><button data-mode="price" aria-pressed="false">Price (US$)</button>
<button data-range="all" aria-pressed="false">Full history</button><button data-range="2021" aria-pressed="false">Since 2021</button>
<button data-range="2024" aria-pressed="true">Since 2024</button><button data-range="1y" aria-pressed="false">Last year</button></div>
<figure class="fig wide"><svg id="chart" viewBox="0 0 900 440" role="img" aria-label="Weekly prices"></svg><div id="tip">Move across the chart to read values.</div></figure>
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years. The famous booms are in violet and teal. Crypto coins and miners did far more than any ordinary company has, and gave most of it back.</p>
{note("Reading it", "<p>Marathon rose 177 times from the March 2020 low to the November 2021 high. At the date of this page it is {pct:.0f}% below its 2021 peak.</p>".replace("{pct:.0f}", f"{abs(stat['MARA']['pct_from_peak']):.0f}"))}
{fig(charts.multiples(mult_items), "Log scale, from weekly closes. Past rises do not repeat on a schedule.", 1)}
<h3 class="wide" id="study" data-nav="Study" style="margin-top:44px">What 652 tokens did</h3>
<p>This is our own study of every token with at least four months of trading history on the major exchanges, to 14 October 2026.{cite(12)} Tokens that never reached those exchanges are missing, so the real odds are worse.</p>
<div class="cols wide">
<div class="card rv"><h3>The odds</h3><p>25 of 652 tokens (3.8%) ever rose 100-fold from a low. 180 (28%) rose 10-fold. 21 of the 25 are now down 75% or more from their peak.</p></div>
<div class="card rv"><h3>The timing</h3><p>92% of take-offs happened while Bitcoin was above its 200-day average, which describes 58% of all days. 13 of the 25 started from the March 2020 crash.</p></div>
<div class="card rv"><h3>The listing effect</h3><p>Crypto.com listed 17 of the 21 hundred-fold tokens it carries only after they had taken off, a median 231 days later. After a Coinbase listing, tokens fell a median 8% in the next week and 16% over months two and three.</p></div>
<div class="card rv"><h3>The rule that failed</h3><p>Buying at a new 90-day high while Bitcoin was in an uptrend, then holding 90 days, made a median -11.5% across 2,291 trades. Bitcoin made +15.5% over the same days.</p></div>
</div>
<div class="scroll wide"><table><thead><tr><th>Token</th><th class="n">Rose</th><th class="n">From</th><th class="n">To</th><th class="n">Now vs peak</th></tr></thead><tbody>{study}</tbody></table></div>
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 3), "Crypto has reached the funds and regulation rungs. Ordinary payments and profit for the builders are still ahead.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Bitcoin climbs back above its 200-day average after a long fall.</li><li>Fund inflows rise for weeks, not days.</li><li>Stablecoin supply grows.</li><li>Exchange revenue rises without a new coin craze.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Coins with no use double in a week.</li><li>Companies announce a Bitcoin purchase plan and the share price jumps more than the coins are worth.</li><li>Borrowing in futures markets hits records.</li><li>Your taxi driver has a coin.</li></ul></div>
</div>
<h3 class="wide" id="s-live" data-nav="Live" style="margin-top:44px">Live updates</h3>
<p class="wide">The page checks filings and headlines and shows how they move the odds used in chapter 6. <span id="live-stamp">Loading the live layer.</span></p>
<div class="cols wide">
<div class="card"><h3>Announcements that moved the odds</h3><ul class="feed" id="live-events"><li>Loading.</li></ul></div>
<div class="card"><h3>Change log</h3><ul class="feed" id="live-log"><li>Loading.</li></ul></div>
<div class="card"><h3>Headlines (links to the publisher)</h3><ul class="feed" id="live-news"><li>Loading.</li></ul></div>
<div class="card"><h3>New research papers that mention these coins</h3><ul class="feed" id="live-papers"><li>Loading.</li></ul></div>
</div>
<p class="cap wide" id="live-status"></p>
<div class="scroll wide"><table id="live-react"></table></div>
<p class="cap wide">How these stocks moved after past filings of each type, against QQQ. The live layer uses it to size its nudges, with case counts shown.</p>
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{hype}</tbody></table></div>
<h3 class="wide" id="s-map" data-nav="Map" style="margin-top:44px">Where it is welcome</h3>
<p class="wide">Pick a country. Teal marks friendly regimes, violet mixed ones, red restrictive ones. A summary from public sources, so treat the detail as approximate.</p>
<div class="map-wrap wide"><figure class="fig" style="margin:0">{tile_map(X.TILES, X.NAMES)}
<div class="map-key"><span><i style="border-color:var(--teal)"></i>friendly</span><span><i style="border-color:var(--violet)"></i>mixed</span><span><i style="border-color:var(--red)"></i>restrictive</span></div></figure><div class="card" id="map-panel"></div></div>
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{shovels}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
<p>Weekly rebalanced equal-weight baskets set to 100 at the start, with Bitcoin for comparison.</p>
{fig(idx_svg, "Crypto pure-plays: Coinbase, Strategy, Marathon, Riot. Large groups: Robinhood, PayPal, BlackRock.", 3)}
<h3 class="wide" id="s-time" data-nav="Time" style="margin-top:44px">Time machine</h3>
<p>Pick an asset and a date. See what the money would be worth now, how high it went, and how far it fell on the way.</p>
<div class="ctrl wide"><label>Asset <select id="tm-asset"></select></label><label>From <input type="date" id="tm-date"></label><label>Amount (US$) <input type="number" id="tm-amt" value="1000" min="1" step="100"></label></div>
<figure class="fig wide"><svg id="tm-svg" viewBox="0 0 900 260" role="img" aria-label="Value of the investment over time"></svg><div id="tm-out" class="tmout"></div></figure>''', KEY["companies"], short="Money")

    power_items = [("Ethereum network, after 2022", 0.01), ("Irish data centres, 2023", 6.3), ("All Irish electricity use", 30), ("Bitcoin network, estimate", 150),
                   ("Data centres, AI and crypto worldwide, 2022", 460)]
    ch5 = chapter("hurdles", 5, "The limits, and the power bill", "What can go wrong, and how much electricity it uses.", f'''
<div class="cols wide">
<div class="card rv"><h3>Theft and loss</h3><p>Exchange hacks, stolen keys and lost recovery phrases are routine. Billions of dollars of coins have been taken, and almost none is recovered.</p></div>
<div class="card rv"><h3>Failure of intermediaries</h3><p>Terra and FTX collapsed in 2022 and customers lost what they held there.{cite(9)} A licence reduces the risk. It does not remove it.</p></div>
<div class="card rv"><h3>Rules that change</h3><p>The same activity can be legal in one country and banned in the next. Taxes differ and change each budget.</p></div>
<div class="card rv"><h3>Concentration</h3><p>A small number of wallets hold a large share of most coins. Prices of small tokens can be moved by one seller.</p></div>
<div class="card rv"><h3>Scale and speed</h3><p>Bitcoin handles a handful of transactions per second on its main chain. Payment-grade volume has to move to second layers or other networks.</p></div>
<div class="card rv"><h3>Quantum</h3><p>Covered in chapter 3. Slow, solvable, and worth watching.</p></div>
</div>
<h3 class="wide" id="s-power" data-nav="Power" style="margin-top:44px">Power</h3>
<p>The Bitcoin network uses roughly 140 to 175 terawatt-hours a year on the Cambridge estimates (a 2025 survey gave 138, its running index about 175), about as much as a mid-sized European country.{cite(2)} Proof-of-work is the cause. Ethereum cut its use by more than 99% in 2022 by switching to staking.</p>
{note("Why it is built this way", "<p>The electricity is the security. An attacker would need to match it. That makes the cost a feature to Bitcoin's supporters and a flaw to its critics.</p>")}
{fig(charts.bars_h(power_items, lambda v: (f"{v:g} TWh" if v >= 1 else f"{v * 1000:g} GWh"), lo_exp=-2, hi_exp=3, highlight="Bitcoin network, estimate", label="Electricity use, terawatt-hours a year, log scale", left=270), "Log scale, approximate, per year. Sources: Cambridge index" + cite(2) + ", Central Statistics Office" + cite(11) + ", IEA" + cite(10) + ".", 4)}
<div class="fx-photos wide">{photo("power-lines.jpg", caption="High-voltage lines at dusk. Miners go where power is cheapest, which is why they follow stranded hydro, wind and gas.")}
<div class="card" style="align-self:start"><h3>The power question has a second half</h3><p>Miners are now among the largest buyers of flexible power. Some sell back to the grid during demand peaks. A few are converting sites to host AI data centres, which pay more per megawatt than mining. Whether that is good news for the miners depends on whether they keep the power contracts.</p></div></div>''', KEY["hurdles"], short="Limits")

    rows = "".join(f'<tr><td>{c["name"]} ({c["t"]})</td><td class="n">{fmt_p(sims[c["t"]]["end_p10"])}</td><td class="n">{fmt_p(sims[c["t"]]["end_p50"])}</td>'
                   f'<td class="n">{fmt_p(sims[c["t"]]["end_p90"])}</td><td class="n">{sims[c["t"]]["prob_below_start"]:.0%}</td></tr>' for c in COMPANIES)
    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the market</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 65%</h3><p>Bitcoin survives and stays the largest coin. Regulated funds and stablecoins keep growing. A few more large banks and payment firms offer crypto services.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>The four-year rhythm repeats: a weak 2026 and 2027 before the April 2028 halving, then a rally into 2029. It has held three times, which proves little.</p></div>
<div class="card rv"><h3>Unlikely, under 25%</h3><p>Crypto becomes a normal way to pay for everyday goods in a rich country, or a quantum computer breaks Bitcoin signatures.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into assets like these. Solas33 holds no position in any company or coin named and takes no payment from any of them.</div>
<h3 class="wide" id="s-scenarios" data-nav="Scenarios" style="margin-top:40px">What it could mean for the five companies</h3>
<p>Pick a company and move the sliders to set your own odds. Dashed lines are the typical path in each story. The bands hold the middle 50% and 80% of outcomes once the stories are mixed.</p>
<figure class="fig wide" id="fan">
<div class="ctrl" id="fan-tabs" role="group" aria-label="Company"></div>
<svg id="fansvg" viewBox="0 0 900 440" role="img" aria-label="Recent price and three-year scenario range for the chosen company"></svg>
<div class="sliders">
<label>Chance of the bear story <input type="range" id="sl-bear" min="0" max="90" step="1"></label>
<label>Chance of the bull story <input type="range" id="sl-bull" min="0" max="90" step="1"></label>
<label>Volatility (100 = last two years, scaled) <input type="range" id="sl-vol" min="40" max="160" step="5"></label>
<button type="button" id="fan-reset" class="plain">Back to our odds</button></div>
<p id="fan-probs" class="cap"></p><p id="fan-read"></p><p id="fan-tilt" class="cap"></p>
<figcaption><b>Fig 5.</b> The live layer may tilt our odds by a few points because of dated announcements, never by more than 12.</figcaption></figure>
<div class="scroll wide"><table><thead><tr><th>Stock</th><th class="n">Low end (10th)</th><th class="n">Middle</th><th class="n">High end (90th)</th><th class="n">Below today</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cap wide">Three years from the build date, at our starting odds.</p>
<h3 class="wide" id="s-record" data-nav="Record" style="margin-top:36px">Our record</h3>
<div class="card wide"><p id="live-score">Loading the scorecard.</p>
<p class="cap">Every week the site writes down its 3, 6 and 12-month ranges in a hash-chained log before the outcome is known, then scores them.</p></div>
<div class="pull wide">Crypto will probably still be here in 2029. A lot of the companies around it will have been through a winter first.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Bitcoin is {abs(btc["pct_from_peak"]):.0f}% below its peak and the stocks are further down. The scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}, which is lower than for quantum because these shares have already been through a fall.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Miners and Strategy are the most exposed. Coinbase and Circle have other income and are less tied to the coin price. Strategy's debt and preferred payments mean it can be forced to act in a bad year.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>The winners are the firms with licences, customers and non-trading income. A few-fold gain is a normal good outcome. The 30x to 177x rises behind us were one-time events from a very low base.</p></div>
<div class="card rv"><h3>The test</h3><p>Ask of each company how much of its revenue survives a coin price that is half of today's. That number, more than any forecast, is the one to know.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> Bitcoin holding above its 200-day average for six months with rising fund inflows. A large bank issuing a stablecoin that customers actually use. A credible, funded plan to move Bitcoin to quantum-safe signatures.</div>''', KEY["outlook"], short="Outlook")

    bands = {
        "ch2": band("vault-gold.jpg", "Store of value", "People have wanted somewhere to put wealth that nobody can print.", "A vault stacked with gold bars"),
        "ch3": band("bank-run-1914.jpg", "Why trust matters", "Bank runs are why people wanted money no bank can freeze. They are also why regulators exist.", "Depositors queuing outside a bank in 1914"),
        "ch4": band("nyse-floor.jpg", "Where the money is", "Every coin on this page is also a ticker symbol, and a share price.", "Brokers on the floor of the New York Stock Exchange"),
        "ch5": band("power-lines.jpg", "Electricity", "The security of Bitcoin is paid for in power.", "Transmission lines at dusk"),
        "ch6": band("gold-doppie.jpg", "Three years", "Gold has had five thousand years to prove itself. Crypto has had seventeen.", "A gold coin from 1626"),
    }
    foot = f'''<footer class="fx-foot" id="disclosures"><div class="fx-foot-in">
<h2 style="font-size:1.6rem">Sources, method and disclosures</h2>
<ol>{"".join(f'<li id="r{n}">[{n}] <a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for n, t, u in REFS)}</ol>
<div class="cols">
<div class="card"><h3>Information only</h3><p>This site is general information and education. It is not investment advice, a recommendation, an offer or a solicitation, and it takes no account of your circumstances. Crypto-assets are not regulated like bank deposits and are not protected by deposit guarantee schemes. Speak to a licensed adviser before acting.</p></div>
<div class="card"><h3>Scenarios, not forecasts</h3><p>Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%. Prices can fall to zero.</p></div>
<div class="card"><h3>Conflicts</h3><p>Solas33 holds no position in any company, coin or token named and takes no payment from any of them. The only benefit to Solas33 is traffic to its own sites as a provider of information. There is no advertising. If any of that changes it will be stated here with the date.</p></div>
<div class="card"><h3>Data</h3><p>Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain and credited under each picture. Our token study covers tokens listed on major exchanges and has survivorship bias.</p></div>
<div class="card"><h3>Corrections</h3><p>Errors are fixed and logged. Write to <a href="mailto:hello@solas33.com">hello@solas33.com</a>. Editorial responsibility: Solas33. Content last reviewed {AS_OF}.</p></div>
<div class="card"><h3>For researchers and teachers</h3><p>Cite as Solas33, Frontier Coin, with the page date. The live layer is public: <a href="live.json">live.json</a> and an <a href="feed.xml">RSS feed</a>.</p></div>
</div>
<p style="margin-top:28px">Part of <a href="../">Frontier</a>. Code is public at <a href="https://github.com/SOLAS33/frontier">github.com/SOLAS33/frontier</a>.</p>
</div></footer>'''

    flow = (f'<div class="fx-flow">{notice}{ch1}</div>{bands["ch2"]}<div class="fx-flow">{ch2}</div>{bands["ch3"]}<div class="fx-flow">{ch3}</div>'
            f'{bands["ch4"]}<div class="fx-flow">{ch4}</div>{bands["ch5"]}<div class="fx-flow">{ch5}</div>{bands["ch6"]}<div class="fx-flow">{ch6}</div>')
    facts = [("Bitcoin now", f"${btc['last'] / 1000:.0f}k"), ("From 2025 peak", f"-{abs(btc['pct_from_peak']):.0f}%"), ("Tokens to 100x", "25 of 652"),
             ("Network power", "~150 TWh")]
    frows = "".join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a, b in facts)
    rail = ('<aside class="fx-rail" id="fx-rail" aria-label="Live and series panels"><div id="fx-live" aria-live="polite"></div>'
            f'<section class="rp"><h4>Numbers to hold on to</h4>{frows}</section>'
            f'<section class="rp"><h4>In this series</h4><div class="rp-list">{series_list("coin")}</div></section></aside>')
    body = (f'{hero}<nav class="fx-spine" id="fx-spine" aria-label="Chapters"></nav>{rail}{flow}'
            f'<div class="fx-flow">{watch_promo()}</div>{foot}')
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
