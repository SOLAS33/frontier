"""Frontier Chain: blockchain technology beyond money. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
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
    (2, "Ethereum Foundation. Ethereum white paper.", "https://ethereum.org/en/whitepaper/"),
    (3, "Haber, S. and Stornetta, W. (1991). How to time-stamp a digital document. Journal of Cryptology.", "https://link.springer.com/article/10.1007/BF00196791"),
    (4, "Securitize (2024). BlackRock launches first tokenized fund, BUIDL, on the Ethereum network.", "https://securitize.io/learn/press/blackrock-launches-first-tokenized-fund-buidl-on-the-ethereum-network"),
]
REFS = REFS + TB.CHAIN_REFS
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
     "profit": f"Charge fees on funds. Its tokenised money-market fund, BUIDL, launched in March 2024 on Ethereum and became the first from a Wall Street firm to pass $1 billion, in March 2025.{cite(15)}",
     "watch": "Tokenised fund size, rival launches, regulatory rulings on holding funds as tokens.",
     "rank": "The largest asset manager, with tokenisation as a small line.",
     "verdict": "A giant with a pilot"},
    {"t": "COIN", "name": "Coinbase", "kind": "Exchange, custody and the Base network",
     "rivals": "Kraken, Binance, Robinhood, banks offering custody",
     "profit": "Trading fees today. It runs Base, a rollup network, and hopes for steadier earnings from custody, stablecoin revenue and network fees.",
     "watch": "Share of volume, Base usage, stablecoin income, regulatory outcomes.",
     "rank": "The largest US-listed crypto firm, covered in more detail on Frontier Coin.",
     "verdict": "The most exposed to the whole theme"},
    {"t": "CRCL", "name": "Circle", "kind": "Stablecoin issuer (USDC)",
     "rivals": "Tether, PayPal, banks issuing their own tokens",
     "profit": "Earns interest on the reserves behind USDC. It profits as long as rates stay high and USDC use grows, and it shares reserve income with Coinbase under a collaboration agreement.",
     "watch": "USDC in circulation, interest rates, distribution costs, new rules such as the 2025 US stablecoin law.",
     "rank": "A young listed company with one main product.",
     "verdict": "A bet on the dollar token"},
    {"t": "HOOD", "name": "Robinhood", "kind": "Retail broker with tokenised shares",
     "rivals": "Interactive Brokers, Schwab, Coinbase, local brokers",
     "profit": f"Earns from trading, interest on balances and subscriptions. From 30 June 2025 it offered more than 200 tokenised US stocks and ETFs to customers in the EU and EEA, settled on Arbitrum One.{cite(27)}",
     "watch": "Tokenised product volumes, regulation in Europe and the US, trading activity.",
     "rank": "A fast-growing broker using tokenisation as a product line.",
     "verdict": "A broker trying a new rail"},
    {"t": "IBM", "name": "IBM", "kind": "Enterprise technology",
     "rivals": "Microsoft, Oracle, Accenture",
     "profit": f"Sells software, cloud and consulting. It and Maersk announced the end of TradeLens, their blockchain shipping platform, in November 2022. The platform was due to go offline by the end of the first quarter of 2023.{cite(18)}",
     "watch": "Software growth, any new ledger work with banks.",
     "rank": "A cautionary tale as much as a player.",
     "verdict": "Tried it, stepped back"},
]

LADDER = [("Whitepaper", "An idea and a|diagram"), ("Pilot", "Real money, a|small amount"), ("Regulated", "A legal route|exists"),
          ("Adopted", "Big firms use it|every day"), ("Cheaper", "Costs less than the|system it replaces"),
          ("Standard", "Rivals share|one ledger"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "mixed"), "IE": (3, 0, "friendly"), "GB": (4, 0, "friendly"), "CH": (5, 1, "friendly"),
         "DE": (6, 0, "friendly"), "FR": (4, 1, "friendly"), "SG": (9, 2, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "GB": "United Kingdom", "CH": "Switzerland", "DE": "Germany", "FR": "France", "SG": "Singapore"}
COUNTRY = {
    "US": {"co": "BlackRock, Coinbase, Circle, Robinhood", "gov": "A law on payment stablecoins was signed in 2025 (the GENIUS Act)", "ctl": "Rules for tokenised securities were still being worked out when we checked",
           "note": "The biggest asset managers, and unsettled rules for tokenised securities."},
    "GB": {"co": "HSBC, the Bank of England and the FCA", "gov": "A Digital Securities Sandbox, with HSBC approved to go live in July 2026. A digitally native gilt, DIGIT, is planned for a first transaction by Q1 2027", "ctl": "Bank of England and FCA",
           "note": "Testing the rules with real issuance."},
    "CH": {"co": "Swiss banks and exchanges", "gov": "A DLT Act approved by Parliament in 2020 creates DLT rights, so tokens can carry legal rights", "ctl": "Swiss law", "note": "A clear legal base for tokens."},
    "DE": {"co": "EU rules apply", "gov": "MiCA is in full application across the EU from December 2024", "ctl": "EU rules (MiCA)", "note": "Covered by EU rules."},
    "FR": {"co": "EU rules apply", "gov": "MiCA is in full application across the EU from December 2024. The EIB issued its 2021 digital bond with Banque de France taking part in the settlement", "ctl": "EU rules (MiCA)", "note": "Covered by EU rules."},
    "SG": {"co": "DBS, JPMorgan and MarketNode in early pilots", "gov": "Project Guardian, from 2022, tests tokenised assets with banks", "ctl": "Monetary Authority of Singapore", "note": "A government-led programme with banks."},
    "IE": {"co": "Fund administrators and banks", "gov": "Irish funds hold about 5.6 trillion euros in more than 9,000 funds, the third-largest fund domicile in the world, according to the Central Bank of Ireland", "ctl": "EU rules (MiCA)",
           "note": "The question is how tokenised funds are authorised and administered."},
}
HYPE = [
    ("5", "In daily use at scale", "Money moves and customers pay, every day, for years", "None clear for tokenised assets yet", "ok"),
    ("4", "Regulated product", "A legal route exists and an authorised firm sells it", "BUIDL, Robinhood's EU tokenised stocks, MiCA", "ok"),
    ("3", "Pilot with real money", "A bank or fund issues a small amount", "EIB digital bond, UK DIGIT planned", "dis"),
    ("2", "Consortium announcement", "Many firms say they will join", "TradeLens, which closed", "tgt"),
    ("1", "A whitepaper", "A diagram and a promise", "'Everything will be tokenised'", "tgt"),
]
SHOVELS = [
    ("Networks", "Ethereum, Arbitrum, Base", "Global", "Where tokens live and fees are earned"),
    ("Tokenised fund issuers", "BlackRock with Securitize", "United States", "BUIDL is issued on Ethereum"),
    ("Stablecoin issuers", "Circle", "United States", "The cash side of a trade on a ledger"),
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
                  [(256, "bits in the fingerprint that locks each record to the last", "", ""), (12, "seconds per slot on Ethereum", "", " s"),
                   (245, "to 255 million Australian dollars: what the ASX wrote off on a blockchain clearing project it scrapped", "A$", "m"),
                   (round(runs["COIN"]["multiple"]), "times Coinbase rose from low to high in under two years", "", "x")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "A ledger that many keep, rules that run on it, and proofs that save work.", f'''
<p>A blockchain is a list of records, grouped in batches. Each batch carries a fingerprint of the one before it, so changing an old record changes every fingerprint after it. Many computers keep a copy and follow a fixed rule to agree on each new batch. Bitcoin was the first, in 2008, as a way to move money without a bank.{cite(1)} Ethereum added programs that run on the ledger, called smart contracts, which opened the way to tokens that stand for other things.{cite(2)}</p>
{note("Why it is attractive", "<p>Two parties who do not trust each other can share one record. A trade can settle at the same moment as the payment, with no one in the middle holding the cash for days.</p>")}
<p>This site is about that second use. For the money side, including Bitcoin and its quantum risk, see <a href="../coin/">Frontier Coin</a>.</p>
{note("The catch", "<p>Most shared-record problems do not need a blockchain. A shared database run by one trusted party is cheaper and faster. The chain only helps where the parties will not accept one owner.</p>")}
<div class="fx-photos wide">
{photo("nyse-floor.jpg", caption="Brokers working on the floor of the New York Stock Exchange. A trade is agreed in an instant and settled later, which is the gap tokenisation aims to close.")}
{photo("vault-gold.jpg", caption="A vault stacked with gold bars, photographed for the US National Archives. Keeping valuable things has always meant trusting someone with the keys.")}
{photo("fed-board.jpg", caption="The US Federal Reserve Board in an open meeting, October 2023.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Uses" style="margin-top:36px">What it is used for</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Tokenised funds and bonds</h3><p>BlackRock's BUIDL fund launched in March 2024 and passed $1 billion in March 2025. The EIB issued a 100 million euro bond on Ethereum in 2021.{cite(15)}{cite(16)}</p></div>
<div class="card rv"><h3>Tokenised shares</h3><p>Robinhood has offered more than 200 tokenised US stocks and ETFs to EU customers since 30 June 2025.{cite(27)}</p></div>
<div class="card rv"><h3>Proofs</h3><p>A zero-knowledge proof shows something is true without showing the data. It also lets a network check many transactions cheaply.{cite(11)}</p></div>
<div class="card rv"><h3>Sandboxes and pilots</h3><p>The UK's Digital Securities Sandbox approved HSBC to go live in July 2026, and a digital gilt is planned.{cite(23)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Theft and bugs</h3><p>Chainalysis counted $2 billion taken in 13 attacks on cross-chain bridges by August 2022, and $3.8 billion stolen across crypto in 2022.{cite(20)}{cite(21)}</p></div>
<div class="card rv"><h3>Garbage in</h3><p>A ledger proves that a record has not changed. It cannot prove that the record was true when it was written.</p></div>
<div class="card rv"><h3>Consortium politics</h3><p>Maersk and IBM closed TradeLens after saying the need for full global industry collaboration had not been achieved.{cite(18)}</p></div>
<div class="card rv"><h3>Legacy systems</h3><p>The ASX scrapped a blockchain clearing replacement in 2022 and wrote off between A$245 million and A$255 million before tax.{cite(19)}</p></div>
</div>
{TB.chain_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1991</div><p>Haber and Stornetta describe a chain of time-stamped records that cannot be altered unnoticed.{cite(3)}</p></div>
<div class="ev"><div class="yr">2008</div><p>Bitcoin's design is published.{cite(1)}</p></div>
<div class="ev big"><div class="yr">April 2021</div><p>The European Investment Bank issues a 100 million euro, two-year digital bond on Ethereum.{cite(16)}</p></div>
<div class="ev"><div class="yr">2022</div><p>Project Guardian starts in Singapore.{cite(24)} Maersk and IBM announce the end of TradeLens. The ASX scraps its blockchain clearing project.{cite(18)}{cite(19)}</p></div>
<div class="ev big"><div class="yr">2024 to 2025</div><p>BlackRock launches BUIDL and it passes $1 billion.{cite(15)} MiCA applies in full across the EU from December 2024.{cite(13)} A US law on payment stablecoins is signed.{cite(28)} Robinhood offers tokenised stocks in the EU.{cite(27)}</p></div>
<div class="ev big"><div class="yr">2026</div><p>HSBC is approved to go live in the UK's Digital Securities Sandbox.{cite(23)}</p></div>
<div class="ev fut"><div class="yr">2027</div><p>The UK plans the first DIGIT transaction by Q1 2027.{cite(23)} ESMA recommends that the EU move to next-day settlement on 11 October 2027.{cite(26)}</p></div>
</div>''', K.key_idea("Useful where the parties distrust each other",
        "A shared ledger helps when rivals need one record and none will let another run it. In most other cases a database is simpler. "
        "The successes so far are funds, bonds and settlement pilots. The failures were platforms that tried to replace a whole industry at once."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>Regulators are giving tokens a legal footing: MiCA in the EU, a stablecoin law in the US, a UK sandbox. The biggest asset manager has a tokenised fund over $1 billion.{cite(13)}{cite(28)}{cite(15)}</p></div>
<div class="card rv"><h3>What has not</h3><p>Most trades still settle through the existing system. Totals for tokenised assets vary widely with the measure used, so check rwa.xyz and read its definitions.{cite(12)}</p></div>
<div class="card rv"><h3>What is new</h3><p>Governments and banks are issuing real instruments on ledgers: the EIB's bond, and the UK's planned digital gilt.{cite(16)}{cite(23)}</p></div>
</div>
<div class="wide">{photo("bank-run-1914.jpg", caption="Depositors queuing outside the German Savings Bank in New York during the run of August 1914.")}</div>''',
        K.key_idea("Plumbing, not a revolution",
                   "The real change is slow and technical: faster settlement and shared records between firms that already do business. "
                   "Its value is to cut cost and risk for big institutions, not to replace them."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Our judgement from the pilots so far. Not a forecast.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now: cash and treasuries</div><p>Tokenised money-market funds and Treasuries are among the largest tokenised assets, tracked by rwa.xyz.{cite(12)}</p></div>
<div class="ev fut"><div class="yr">2026 to 2027: government and bank pilots</div><p>The UK's DIGIT pilot, Singapore's Project Guardian and the UK sandbox test live issuance.{cite(23)}{cite(24)}</p></div>
<div class="ev fut"><div class="yr">2027: settlement speeds up anyway</div><p>ESMA recommends that the EU move to next-day settlement on 11 October 2027, which narrows the gap that tokenisation aims to close.{cite(26)}</p></div>
<div class="ev fut"><div class="yr">Later: shares and property</div><p>The law of ownership, not the software, is the slow part.</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The funds</h3><p>Irish funds hold about 5.6 trillion euros in more than 9,000 funds, the third-largest fund domicile in the world, according to the Central Bank of Ireland's Deputy Governor.{cite(22)}</p></div>
<div class="card rv"><h3>The rules</h3><p>MiCA, the EU crypto-asset regulation, applies in Ireland and has been in full application since December 2024.{cite(13)}</p></div>
<div class="card rv"><h3>The watch</h3><p>If funds are issued as tokens, Irish administrators and the Central Bank will be among the first to handle the rules.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a citizen</h3><p>Hold only what you can afford to lose in anything that calls itself a token. A token can be a claim on an asset held elsewhere, with no voting rights.{cite(27)}</p></div>
<div class="card rv"><h3>As a business</h3><p>Ask whether you need a shared ledger or only a shared database. If rivals will not agree on an owner, a ledger may help.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Listed firms earn from trading, interest and fees today. Tokenisation is a small line for most of them.</p></div>
</div>''', K.key_idea("Cash first, property last",
        "The things that are easiest to tokenise are the ones with clear law and a ready market. The harder the legal question, the later it comes."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "An asset manager, three platforms that live off crypto activity, and an old hand that stepped back.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The networks themselves<span>Ethereum and others</span></h3>
<dl><dt>What they are</dt><dd>Open ledgers. Their tokens, such as ether, trade on exchanges. They are not companies and have no earnings in the usual sense.</dd>
<dt>Use</dt><dd>Covered on Frontier Coin. Ether appears below for scale.</dd></dl><span class="verdict">The rails, without a balance sheet</span></article></div>
{K.prices_block("s-prices", "Share prices", "Five listed companies linked to tokenisation, with PayPal, ether and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. These rises followed crypto trading cycles more than tokenisation.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "A few tokenised funds are on the fourth rung. Most tokenised assets are on the second or third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Big custodians hold tokenised funds for clients as routine.</li><li>A bond issue larger than a pilot settles on chain.</li><li>A central bank or regulator accepts tokenised collateral.</li><li>Rivals agree on a shared ledger.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>A token that stands for an asset with no legal claim behind it.</li><li>A consortium announcement with no live trades.</li><li>Prices of listed firms jump on a tokenisation headline.</li><li>"On chain" used where a spreadsheet would do.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>clear rules or active pilots</span><span><i style="border-color:var(--violet)"></i>mixed or unsettled rules</span><span><i style="border-color:var(--red)"></i>closed to public chains</span>', "Pick a country. A summary from the cited public sources.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The platforms earn from crypto cycles. The incumbents have tokenisation as a pilot",
        "The firms that rose most are those that live off trading and the dollar token. BlackRock and IBM treat the chain as an experiment. "
        "Neither group yet earns much from tokenised assets."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Law, security, liquidity and trust.", f'''
<div class="cols wide">
<div class="card rv"><h3>Law</h3><p>A token is only as good as the legal claim behind it. Robinhood's EU tokens are claims on shares held by a US broker-dealer, with no voting rights.{cite(27)}</p></div>
<div class="card rv"><h3>Security</h3><p>Lost keys and contract bugs cannot be undone. Chainalysis counted $3.8 billion stolen in crypto in 2022.{cite(21)}</p></div>
<div class="card rv"><h3>Adoption</h3><p>Maersk and IBM said TradeLens built a viable platform, but it did not reach the commercial viability needed to continue.{cite(18)}</p></div>
<div class="card rv"><h3>Cash on the ledger</h3><p>Same-day swaps need cash in token form: a regulated stablecoin, a bank token or a central-bank token. The choice is still open.</p></div>
<div class="card rv"><h3>Cost of replacing the old system</h3><p>The ASX wrote off between A$245 million and A$255 million before tax when it scrapped its project.{cite(19)}</p></div>
<div class="card rv"><h3>Incumbents</h3><p>The old system is not standing still. ESMA recommends next-day settlement in the EU from 11 October 2027.{cite(26)}</p></div>
</div>
<div class="fx-photos wide">{photo("vault-gold.jpg", caption="Custody of valuable things has always depended on who holds the keys. On a chain, the keys are the asset.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>A ledger cannot fix a weak legal claim, a dishonest record or a security hole. It can only make a good process faster and its records harder to alter.</p></div></div>''',
        K.key_idea("A trust problem moved, not removed",
                   "A chain removes the need to trust a middle party with the record. It adds the need to trust the code, the keys, the data feeds and the law "
                   "behind the token. Those are the places failures have happened."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 80%</h3><p>Tokenised money-market funds and Treasuries keep growing. More large banks and governments issue pilot instruments on ledgers. Zero-knowledge proofs become routine inside rollups.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>A major exchange or clearing house settles part of its business on a shared ledger in live operation.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>Most trading in a major stock market settles on a blockchain by 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">The ledger will end up under much of finance. Most people will never notice it.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. The crypto-linked platforms are the most volatile and the most tied to the trading cycle.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Firms whose earnings rise and fall with crypto trading and interest rates. BlackRock and IBM have earnings that carry them whatever happens on chain.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>Settlement costs and delays fall across the market. The savings are largest for banks and funds and reach customers slowly, if at all.</p></div>
<div class="card rv"><h3>The test</h3><p>For any tokenisation claim, ask who holds the legal title, how it settles, what it costs against today's process and who will trade it.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A central bank token accepted for settlement in a large market. A clearing house moving real volume to a shared ledger. A large loss from a flaw in a regulated tokenised product.</div>''',
        K.key_idea("Slow plumbing, quick price swings",
                   "We expect tokenised assets to keep growing from a small base and the technology to settle into the background of finance. "
                   "The share prices of the platforms linked to it will keep following the crypto cycle."), short="Outlook")

    bands = [band("nyse-floor.jpg", "Where it began", "Trades agreed in seconds and settled later.", "Brokers on the floor of the New York Stock Exchange"),
             band("vault-gold.jpg", "Custody", "Whoever holds the keys holds the asset.", "A vault stacked with gold bars"),
             band("fed-board.jpg", "The rules", "Regulators decide which tokens count as what.", "The Federal Reserve Board in an open meeting"),
             band("bank-run-1914.jpg", "Why settlement matters", "Trust in the middle has failed before.", "Depositors queuing outside a New York bank in 1914"),
             band("nyse-floor.jpg", "Three years", "Time enough to see whether pilots become the plumbing.", "Brokers on the floor of the New York Stock Exchange")]
    foot = K.foot(REFS, AS_OF, "Frontier Chain", "chain",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain and credited under each picture. Tokenisation figures were checked against the sources listed and are rounded. Where sources disagreed the text says so. Crypto-asset and tokenised-asset rules differ by country and change often. Check the current rules before acting.")
    nf = K.notice("We explain how blockchains and tokenised assets work and show how the companies and their shares have behaved. We do not recommend any company, token or trade. Projections are scenarios, not forecasts.")
    facts = [("Ethereum slot time", "12 seconds"), ("Tokenised assets", "see rwa.xyz"), ("MiCA in full application", "Dec 2024"), ("Irish fund assets", "about 5.6tn euros")]
    body = K.assemble("chain", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
