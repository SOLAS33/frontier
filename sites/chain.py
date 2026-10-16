"""Frontier Chain: blockchain technology beyond money. Voice rules: docs/VOICE.md."""
from __future__ import annotations

from frontier import art, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_chain as TB

TITLE = "Frontier Chain"
AS_OF = "16 October 2026"

LIVE = {"cik": {"BLK": 2012383, "COIN": 1679788, "CRCL": 1876042, "HOOD": 1783879, "IBM": 51143},
        "aliases": {"BLK": ["blackrock", "buidl"], "COIN": ["coinbase"], "CRCL": ["circle internet", "usdc"], "HOOD": ["robinhood"], "IBM": ["ibm"]},
        "arxiv_terms": ["zero-knowledge proof", "smart contract", "blockchain rollup"], "arxiv_cat": "cs.CR"}

REFS = [
    (1, "Nakamoto, S. (2008). Bitcoin: a peer-to-peer electronic cash system.", "https://bitcoin.org/bitcoin.pdf"),
    (2, "Buterin, V. (2014). Ethereum white paper.", "https://ethereum.org/en/whitepaper/"),
    (3, "BlackRock. BUIDL: the USD Institutional Digital Liquidity Fund.", "https://securitize.io/learn/press/blackrock-launches-first-tokenized-fund-buidl-on-the-ethereum-network"),
    (4, "European Investment Bank. Digital bond issuance.", "https://www.eib.org/en/press/all/2021-141-european-investment-bank-eib-issues-its-first-ever-digital-bond-on-a-public-blockchain"),
    (5, "Maersk (2022). TradeLens to discontinue operations.", "https://www.maersk.com/news/articles/2022/11/29/maersk-and-ibm-to-discontinue-tradelens"),
    (6, "ASX (2022). CHESS replacement project: update.", "https://www.asx.com.au/markets/clearing-and-settlement-services/chess-replacement"),
    (7, "Chainalysis. Crypto crime report (annual): hacks and bridge losses.", "https://www.chainalysis.com/blog/2022-biggest-year-ever-for-crypto-hacking/"),
    (8, "Central Bank of Ireland. Investment funds statistics.", "https://www.centralbank.ie/statistics"),
    (9, "European Union. Regulation on markets in crypto-assets (MiCA).", "https://eur-lex.europa.eu/eli/reg/2023/1114/oj"),
]
REFS = REFS + TB.CHAIN_REFS + [(14, "Haber, S. and Stornetta, W. (1991). How to time-stamp a digital document. Journal of Cryptology.", "https://link.springer.com/article/10.1007/BF00196791")]
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "BLK": [Scenario("bear", "Markets fall and tokenised funds stay small", 0.20, -0.20, 0.75),
            Scenario("base", "Steady growth, tokenisation a small line", 0.55, 0.10, 0.75),
            Scenario("bull", "Tokenised funds become a real product line", 0.25, 0.30, 0.75)],
    "COIN": [Scenario("bear", "Trading volumes fall and rivals cut fees", 0.40, -0.45, 0.75),
             Scenario("base", "Earnings follow the crypto cycle", 0.35, 0.05, 0.75),
             Scenario("bull", "Stablecoin and network fees grow beside trading", 0.25, 0.50, 0.75)],
    "CRCL": [Scenario("bear", "Interest rates fall and rivals share the market", 0.45, -0.50, 0.75),
             Scenario("base", "The stablecoin grows with usage, margins narrow", 0.35, 0.00, 0.75),
             Scenario("bull", "Dollar tokens become routine in payments", 0.20, 0.60, 0.75)],
    "HOOD": [Scenario("bear", "Retail trading cools and fees are cut", 0.35, -0.40, 0.75),
             Scenario("base", "Steady growth in accounts and products", 0.40, 0.08, 0.75),
             Scenario("bull", "Tokenised shares add a large new line", 0.25, 0.45, 0.75)],
    "IBM": [Scenario("bear", "Software and consulting growth stalls", 0.25, -0.20, 0.75),
            Scenario("base", "Steady growth, chain work stays small", 0.50, 0.08, 0.75),
            Scenario("bull", "Hybrid cloud and AI lift earnings", 0.25, 0.25, 0.75)],
}

COMPANIES = [
    {"t": "BLK", "name": "BlackRock", "kind": "Asset manager",
     "rivals": "Vanguard, State Street, Fidelity, Franklin Templeton",
     "profit": "Charge fees on funds. Its tokenised money-market fund, BUIDL, is a way to hold the same assets in a token, with the same fee.",
     "watch": "Tokenised fund size, rival launches, regulatory rulings on holding funds as tokens.",
     "rank": "The largest asset manager, with tokenisation as a small experiment.",
     "verdict": "A giant with a pilot"},
    {"t": "COIN", "name": "Coinbase", "kind": "Exchange, custody and the Base network",
     "rivals": "Kraken, Binance, Robinhood, banks offering custody",
     "profit": "Trading fees today. It hopes for steadier earnings from custody, stablecoin revenue and fees on Base, its rollup network.",
     "watch": "Share of volume, Base usage, stablecoin income, regulatory outcomes.",
     "rank": "The largest US-listed crypto firm, covered in more detail on Frontier Coin.",
     "verdict": "The most exposed to the whole theme"},
    {"t": "CRCL", "name": "Circle", "kind": "Stablecoin issuer (USDC)",
     "rivals": "Tether, PayPal, banks issuing their own tokens",
     "profit": "Earns interest on the reserves behind USDC. It profits as long as rates stay high and USDC use grows, and it shares revenue with distributors such as Coinbase.",
     "watch": "USDC in circulation, interest rates, distribution costs, new rules.",
     "rank": "A young listed company since 2025 with one product.",
     "verdict": "A bet on the dollar token"},
    {"t": "HOOD", "name": "Robinhood", "kind": "Retail broker with tokenised shares",
     "rivals": "Interactive Brokers, Schwab, Coinbase, local brokers",
     "profit": "Earns from trading, interest on balances and subscriptions. It has begun offering tokenised stocks to customers in Europe.",
     "watch": "Tokenised product volumes, regulation in Europe and the US, trading activity.",
     "rank": "A fast-growing broker using tokenisation as a product line.",
     "verdict": "A broker trying a new rail"},
    {"t": "IBM", "name": "IBM", "kind": "Enterprise technology",
     "rivals": "Microsoft, Oracle, Accenture, specialised chain firms",
     "profit": "Sells software, cloud and consulting. It built enterprise blockchain products, and closed the shipping platform TradeLens in 2023.",
     "watch": "Software growth, any new ledger work with banks.",
     "rank": "A cautionary tale as much as a player.",
     "verdict": "Tried it, stepped back"},
]

LADDER = [("Whitepaper", "An idea and a|diagram"), ("Pilot", "Real money, a|small amount"), ("Regulated", "A legal route|exists"),
          ("Adopted", "Big firms use it|every day"), ("Cheaper", "Costs less than the|system it replaces"),
          ("Standard", "Rivals share|one ledger"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "mixed"), "US": (1, 1, "mixed"), "IE": (3, 0, "mixed"), "GB": (4, 0, "friendly"), "FR": (4, 1, "friendly"),
         "DE": (6, 0, "friendly"), "CH": (5, 1, "friendly"), "SG": (9, 2, "friendly"), "AE": (7, 2, "friendly"), "HK": (10, 1, "friendly"),
         "CN": (9, 0, "restrictive"), "JP": (11, 1, "mixed"), "KR": (10, 0, "mixed")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "DE": "Germany", "CH": "Switzerland",
         "SG": "Singapore", "AE": "United Arab Emirates", "HK": "Hong Kong", "CN": "China", "JP": "Japan", "KR": "South Korea"}
COUNTRY = {
    "US": {"co": "BlackRock, Franklin Templeton, JPMorgan, Coinbase, Circle, DTCC", "gov": "A 2025 law set rules for payment stablecoins, and regulators are working on tokenised securities",
           "ctl": "Rules still being written, with agencies sometimes in conflict", "note": "The biggest asset managers and the biggest uncertainty about rules."},
    "GB": {"co": "Banks and the London Stock Exchange group, Archax", "gov": "A digital securities sandbox lets firms test tokenised trading, and a digital gilt pilot is planned",
           "ctl": "Financial Conduct Authority approval", "note": "Testing the rules before committing."},
    "FR": {"co": "Societe Generale (SG Forge), Banque de France pilots", "gov": "Early national rules for tokenised funds", "ctl": "EU rules", "note": "One of the earliest euro-denominated tokenised bond issuers."},
    "DE": {"co": "Deutsche Boerse, Siemens, Boerse Stuttgart", "gov": "A law lets electronic securities be issued on a ledger", "ctl": "EU rules", "note": "Siemens has issued digital bonds."},
    "CH": {"co": "SIX Digital Exchange, UBS, Sygnum", "gov": "A DLT law since 2021 gives tokens legal standing", "ctl": "Financial markets regulator FINMA", "note": "A clear legal base and an operating digital exchange."},
    "SG": {"co": "DBS, Monetary Authority of Singapore pilots", "gov": "Project Guardian: government-backed tests of tokenised assets with banks", "ctl": "Licensing by the central bank", "note": "A government-led programme with banks."},
    "HK": {"co": "HSBC, Hong Kong Monetary Authority pilots", "gov": "Issued tokenised government green bonds", "ctl": "Licensing for crypto platforms", "note": "Positioning as a hub for tokenised assets for China-linked flows."},
    "AE": {"co": "Dubai and Abu Dhabi regulators and crypto firms", "gov": "Dedicated crypto regulators and friendly licensing", "ctl": "Free zone rules", "note": "Open for business, small base."},
    "CN": {"co": "State banks, the e-CNY project", "gov": "Bans public crypto trading and runs its own state digital currency", "ctl": "Tight", "note": "A state ledger, not a public one."},
    "JP": {"co": "SBI, Nomura, MUFG", "gov": "Rules for security tokens and stablecoins", "ctl": "Financial Services Agency licensing", "note": "Orderly and slow."},
    "KR": {"co": "Large exchanges, banks", "gov": "Developing stablecoin and tokenised securities rules", "ctl": "Strict exchange rules", "note": "Heavy retail use, rules catching up."},
    "CA": {"co": "Exchange-traded crypto funds, banks", "gov": "Regulators allow crypto funds and guide issuers", "ctl": "Provincial regulators", "note": "Early with spot crypto funds."},
    "IE": {"co": "Fund administrators and banks, with Dublin as a leading fund domicile", "gov": "The Central Bank authorises funds and crypto firms under EU rules (MiCA)",
           "ctl": "EU rules", "note": "Very large funds industry. The key question is how tokenised funds are authorised and administered."},
}
HYPE = [
    ("5", "In daily use at scale", "Money moves and customers pay, every day, for years", "Stablecoin transfers, a few tokenised funds", "ok"),
    ("4", "Regulated product", "A legal route exists and an authorised firm sells it", "EU DLT Pilot Regime, Swiss DLT law", "ok"),
    ("3", "Pilot with real money", "A bank or fund issues a small amount", "Digital bonds, tokenised repo", "dis"),
    ("2", "Consortium announcement", "Many firms say they will join", "Shipping and trade consortia, several closed", "tgt"),
    ("1", "A whitepaper", "A diagram and a promise", "'Everything will be tokenised'", "tgt"),
]
SHOVELS = [
    ("Networks", "Ethereum, Solana, Base, Arbitrum", "Global", "Where tokens live and fees are earned"),
    ("Custody and keys", "BNY, State Street, Coinbase, Anchorage, Fireblocks", "US, Europe", "Banks and specialists hold keys for big investors"),
    ("Stablecoins and deposits", "Circle, Tether, banks' own tokens", "US, Europe", "The cash side of a trade on a ledger"),
    ("Issuance and transfer agents", "Securitize, Broadridge, Franklin Templeton", "US", "The legal record of who owns a token"),
    ("Oracles and data", "Chainlink, Pyth", "Global", "Contracts need prices and facts from outside"),
    ("Proofs and security audits", "Specialist firms and research groups", "Global", "Bugs in contracts have cost billions" ),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["BLK", "COIN", "CRCL", "HOOD", "IBM", "PYPL", "ETH-USD", "NVDA"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["BLK", "COIN", "CRCL", "HOOD", "IBM"],
                                     [["BLK", "BlackRock"], ["COIN", "Coinbase"], ["CRCL", "Circle"], ["HOOD", "Robinhood"], ["IBM", "IBM"],
                                      ["PYPL", "PayPal"], ["ETH-USD", "Ether"], ["NVDA", "Nvidia"]],
                                     {"BLK": "2016-01-04", "COIN": px_first("COIN"), "CRCL": px_first("CRCL"), "HOOD": px_first("HOOD"),
                                      "IBM": "2016-01-04", "PYPL": px_first("PYPL"), "ETH-USD": px_first("ETH-USD"), "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Rules", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("COIN", "CRCL", "HOOD", "ETH-USD", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Ether", f"from {runs['ETH-USD']['from']}", runs["ETH-USD"]["multiple"], "lay"),
            ("Robinhood", f"from {runs['HOOD']['from']}", runs["HOOD"]["multiple"], "quantum"),
            ("Coinbase", f"from {runs['COIN']['from']}", runs["COIN"]["multiple"], "quantum"),
            ("Circle", f"from {runs['CRCL']['from']}", runs["CRCL"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Crypto-linked platforms", ["COIN", "CRCL", "HOOD"], "var(--amber)"), ("Incumbents", ["BLK", "IBM"], "var(--teal)")])

    hero = K.hero("Frontier / Chain", "A shared record nobody <em>can quietly change</em>",
                  "A blockchain is a ledger that many parties keep together. Its first use was money. Its likelier use is the plumbing under funds, bonds and contracts. Here is what works, what has been tried and dropped, and who is paid.",
                  "nyse-floor.jpg", art.hero_chain(),
                  [(256, "bits in the fingerprint that locks each record to the last", "", ""), (12, "seconds between new batches of records on Ethereum", "", " s"),
                   (250, "million Australian dollars the ASX wrote off on a blockchain project it scrapped", "about A$", "m"),
                   (round(runs["COIN"]["multiple"]), "times Coinbase rose from low to high in under two years", "", "x")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "A ledger that many keep, rules that run on it, and proofs that save work.", f'''
<p>A blockchain is a list of records, grouped in batches. Each batch carries a fingerprint of the one before it, so changing an old record changes every fingerprint after it. Many computers keep a copy and follow a fixed rule to agree on each new batch. Bitcoin was the first, in 2008, as a way to move money without a bank.{cite(1)} Ethereum added programs that run on the ledger, called smart contracts, which opened the way to tokens that stand for other things.{cite(2)}</p>
{note("Why it is attractive", "<p>Two parties who do not trust each other can share one record. A trade can settle at the same moment as the payment, with no one in the middle holding the cash for two days.</p>")}
<p>This site is about that second use. For the money side, including Bitcoin and its quantum risk, see <a href="../coin/">Frontier Coin</a>.</p>
{note("The catch", "<p>Most shared-record problems do not need a blockchain. A shared database run by one trusted party is cheaper and faster. The chain only helps where the parties will not accept one owner.</p>")}
<div class="fx-photos wide">
{photo("nyse-floor.jpg", caption="Brokers working on the floor of the New York Stock Exchange. Trades are agreed in an instant and settled days later, which is the delay tokenisation aims to remove.")}
{photo("vault-gold.jpg", caption="A vault stacked with gold bars, photographed for the US National Archives. Custody of valuable things has always meant trusting someone with the keys.")}
{photo("fed-board.jpg", caption="The US Federal Reserve Board in an open meeting, October 2023. Central banks and regulators decide the rules tokens live under.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Uses" style="margin-top:36px">What it is used for</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Tokenised funds and bonds</h3><p>A fund share or bond recorded as a token that can be sent and settled in minutes. BlackRock's BUIDL fund passed two billion dollars in 2025.{cite(3)}{cite(12)}</p></div>
<div class="card rv"><h3>Programmable settlement</h3><p>A contract swaps the asset and the payment at once, or not at all. That removes the days of risk between trade and settlement.</p></div>
<div class="card rv"><h3>Proofs</h3><p>A zero-knowledge proof shows something is true, such as a balance or an age, without showing the data. It also lets a network check thousands of transactions cheaply.{cite(11)}</p></div>
<div class="card rv"><h3>Provenance and records</h3><p>Tracing a battery, a diamond or a land title. It works only if what is put in the record is honest in the first place.</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Bugs in contracts</h3><p>A program that holds money and cannot be recalled turns every mistake into a theft. Bridges between networks alone lost billions of dollars.{cite(7)}</p></div>
<div class="card rv"><h3>Garbage in</h3><p>A ledger proves that a record has not changed. It cannot prove that the record was true when it was written.</p></div>
<div class="card rv"><h3>Consortium politics</h3><p>Rivals will not join a platform run by one of them. TradeLens, from Maersk and IBM, closed in 2023 for that reason.{cite(5)}</p></div>
<div class="card rv"><h3>Legacy systems</h3><p>Replacing a stock exchange's clearing system with a blockchain cost the ASX about 250 million Australian dollars before it stopped.{cite(6)}</p></div>
</div>
{TB.chain_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1991</div><p>Haber and Stornetta describe a chain of time-stamped records that cannot be altered unnoticed.{cite(14)}</p></div>
<div class="ev"><div class="yr">2008</div><p>Bitcoin's design is published.{cite(1)}</p></div>
<div class="ev big"><div class="yr">2015</div><p>Ethereum launches with smart contracts.{cite(2)}</p></div>
<div class="ev"><div class="yr">2016 to 2018</div><p>Banks and shipping firms form blockchain consortia. Most fade.</p></div>
<div class="ev big"><div class="yr">2021</div><p>The European Investment Bank issues a 100 million euro digital bond on Ethereum.{cite(4)}</p></div>
<div class="ev"><div class="yr">2022 to 2023</div><p>The ASX scraps its blockchain clearing replacement. TradeLens closes. The EU DLT Pilot Regime starts.{cite(13)}</p></div>
<div class="ev big"><div class="yr">2024 to 2025</div><p>BlackRock launches BUIDL. Rollups cut fees to cents. The US sets rules for payment stablecoins. The EU's crypto rules take full effect.{cite(9)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>Big institutions test tokenised funds and bonds in volume. See chapter 6.</p></div>
</div>''', K.key_idea("Useful where the parties distrust each other",
        "A shared ledger helps when rivals need one record and none will let another run it. In most other cases a database is simpler. "
        "The successes so far are funds, bonds and settlement. The failures were platforms that tried to replace a whole industry at once."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>Fees on rollups fell to cents, laws in the EU, Switzerland and the US gave tokens a legal footing, and the biggest fund manager launched a tokenised fund.</p></div>
<div class="card rv"><h3>What has not</h3><p>Most trades still settle in a day or two through the old system. The amounts on chain are small beside the markets they copy.</p></div>
<div class="card rv"><h3>What is new</h3><p>Large firms are testing the same-day swap of an asset for cash, with the regulator's agreement.</p></div>
</div>
<div class="wide">{photo("bank-run-1914.jpg", caption="Depositors queuing outside the German Savings Bank in New York during the run of August 1914. Settlement risk and trust in intermediaries are old problems.")}</div>''',
        K.key_idea("Plumbing, not a revolution",
                   "The real change is slow and technical: faster settlement and shared records between firms that already do business. "
                   "Its value is to cut cost and risk for big institutions, not to replace them."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Cash and treasuries first, then funds, then shares and property.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2027: cash and treasuries</div><p>Dollar tokens and tokenised money-market funds spread as collateral and settlement cash, because their rules are clearest.</p></div>
<div class="ev fut"><div class="yr">2027 to 2029: funds and bonds</div><p>Fund shares and bonds issued on a ledger by banks and managers. Europe's move to next-day settlement in 2027 sets the pace there.</p></div>
<div class="ev fut"><div class="yr">2028 to 2031: shares and trading</div><p>Tokenised stocks and same-day trading where regulators allow. Exchanges and clearing houses decide how fast.</p></div>
<div class="ev fut"><div class="yr">2030s: property and private assets</div><p>Land, private credit and unlisted shares. The law of ownership is the slow part, not the software.</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The funds</h3><p>Ireland administers several trillion euros of investment funds.{cite(8)} If funds are issued as tokens, Irish administrators and the Central Bank will be among the first to handle the rules.</p></div>
<div class="card rv"><h3>The rules</h3><p>The EU's crypto rules apply in Ireland, and the DLT Pilot Regime allows tokenised securities trading under supervision.{cite(9)}{cite(13)}</p></div>
<div class="card rv"><h3>The people</h3><p>Dublin has many fund administration and banking jobs that tokenisation could change. Some tasks shrink. Others, such as checking and oversight, grow.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a citizen</h3><p>Hold only what you can afford to lose in anything that calls itself a token. Rules for consumers vary by product.</p></div>
<div class="card rv"><h3>As a business</h3><p>Ask whether you need a shared ledger or only a shared database. If rivals will not agree on an owner, a ledger may help.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Listed firms earn from trading, interest and fees today. Tokenisation is a small line for most of them.</p></div>
</div>''', K.key_idea("Cash first, property last",
        "The things that are easiest to tokenise are the ones with clear law and a ready market. The harder the legal question, the later it comes."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "An asset manager, three platforms that live off crypto activity, and an old hand that stepped back.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The networks themselves<span>Ethereum, Solana and others</span></h3>
<dl><dt>What they are</dt><dd>Open ledgers. Their tokens, such as ether, trade on exchanges. They are not companies and have no owners or earnings in the usual sense.</dd>
<dt>Why they matter</dt><dd>They earn fees paid in their own tokens. The price of those tokens has moved far more than any firm's earnings.</dd>
<dt>Use</dt><dd>Covered on Frontier Coin. Ether appears below for scale.</dd></dl><span class="verdict">The rails, without a balance sheet</span></article></div>
{K.prices_block("s-prices", "Share prices", "Five listed companies linked to tokenisation, with PayPal, ether and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. These rises came from crypto trading volumes more than from tokenisation.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Stablecoins and a few funds are on the fourth rung. Most tokenised assets are on the second or third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Big custodians hold tokenised funds for clients as routine.</li><li>Collateral posted on a ledger is accepted by clearing houses.</li><li>A bond issue larger than a pilot settles on chain.</li><li>Rivals agree on a shared ledger.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>A token that stands for an asset with no legal claim behind it.</li><li>A consortium announcement with no live trades.</li><li>Prices of listed firms jump on a tokenisation headline.</li><li>"On chain" used where a spreadsheet would do.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>clear rules and active pilots</span><span><i style="border-color:var(--violet)"></i>mixed or unsettled rules</span><span><i style="border-color:var(--red)"></i>closed to public chains</span>', "Pick a country. A summary from public sources, so treat the detail as approximate.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The platforms earn from crypto cycles. The incumbents have tokenisation as a pilot",
        "The firms that rose most are those that live off trading and the dollar token. The giants, BlackRock and IBM, treat the chain as an experiment. "
        "Neither group yet earns much from tokenised assets."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Law, security, liquidity, trust and cost.", f'''
<div class="cols wide">
<div class="card rv"><h3>Law</h3><p>A token is only as good as the legal claim behind it. Who owns the asset if the issuer fails is the question regulators spend most time on.</p></div>
<div class="card rv"><h3>Security</h3><p>Lost keys and contract bugs cannot be undone. Billions have been stolen from bridges and exchanges.{cite(7)}</p></div>
<div class="card rv"><h3>Liquidity</h3><p>A tokenised bond is only useful if someone will trade it. Many sit unsold.</p></div>
<div class="card rv"><h3>Cash on the ledger</h3><p>Same-day swaps need cash in token form: a regulated stablecoin, a bank token or a central-bank token. The choice is still open.</p></div>
<div class="card rv"><h3>Privacy</h3><p>Public ledgers show every transaction. Banks need to keep positions private, which is why zero-knowledge proofs matter.</p></div>
<div class="card rv"><h3>Incumbents</h3><p>The old system is not standing still. Next-day settlement in the US since 2024 and in Europe from 2027 narrows the gap.</p></div>
</div>
<div class="fx-photos wide">{photo("vault-gold.jpg", caption="Custody of valuable things has always depended on who holds the keys. On a chain, the keys are the asset.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>A ledger cannot fix a weak legal claim, a dishonest record or a security hole. It can only make a good process faster and its records harder to alter. The firms that win will be those that deal with law and security first and the technology second.</p></div></div>''',
        K.key_idea("A trust problem moved, not removed",
                   "A chain removes the need to trust a middle party with the record. It adds the need to trust the code, the keys, the oracle and the law "
                   "behind the token. Those are the places failures have happened."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 80%</h3><p>Tokenised money-market funds and treasuries grow several times over. More large banks issue tokenised deposits or bonds. Zero-knowledge proofs become routine inside rollups.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>A major exchange or clearing house settles part of its business on a shared ledger in live operation.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>Most trading in a major stock market settles on a blockchain by 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">The ledger will end up under much of finance. Most people will never notice it.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. The crypto-linked platforms are the most volatile and the most tied to the trading cycle.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Firms whose earnings rise and fall with crypto trading and interest rates. BlackRock and IBM have earnings that carry them whatever happens on chain.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>Settlement costs and delays fall across the market. The savings are largest for banks and funds and flow to customers slowly, if at all.</p></div>
<div class="card rv"><h3>The test</h3><p>For any tokenisation claim, ask who holds the legal title, how it settles, what it costs against today's process and who will trade it.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A central bank token accepted for settlement in a large market. A clearing house moving real volume to a shared ledger. A large loss from a flaw in a regulated tokenised product.</div>''',
        K.key_idea("Slow plumbing, quick price swings",
                   "We expect tokenised assets to keep growing from a small base and the technology to settle into the background of finance. "
                   "The share prices of the platforms linked to it will keep following the crypto cycle."), short="Outlook")

    bands = [band("nyse-floor.jpg", "Where it began", "Trades agreed in seconds and settled days later.", "Brokers on the floor of the New York Stock Exchange"),
             band("vault-gold.jpg", "Custody", "Whoever holds the keys holds the asset.", "A vault stacked with gold bars"),
             band("fed-board.jpg", "The rules", "Regulators decide which tokens count as what.", "The Federal Reserve Board in an open meeting"),
             band("bank-run-1914.jpg", "Why settlement matters", "Trust in the middle has failed before.", "Depositors queuing outside a New York bank in 1914"),
             band("nyse-floor.jpg", "Three years", "Time enough to see whether pilots become the plumbing.", "Brokers on the floor of the New York Stock Exchange")]
    foot = K.foot(REFS, AS_OF, "Frontier Chain", "chain",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain and credited under each picture. Tokenisation figures are from public sources and are rounded. Crypto-asset and tokenised-asset rules differ by country and change often. Check the current rules before acting.")
    nf = K.notice("We explain how blockchains and tokenised assets work and show how the companies and their shares have behaved. We do not recommend any company, token or trade. Projections are scenarios, not forecasts.")
    facts = [("Ethereum block time", "12 seconds"), ("Tokenised treasuries", "several $bn"), ("Same-day settlement", "pilots only"), ("Ireland fund assets", "trillions of euros")]
    body = K.assemble("chain", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
