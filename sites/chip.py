"""Frontier Chip: semiconductors and photonics. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_chip as TB

TITLE = "Frontier Chip"
AS_OF = "16 October 2026"

LIVE = {"cik": {"TSM": 1046179, "ASML": 937966, "INTC": 50863, "AMAT": 6951, "LITE": 1633978},
        "aliases": {"TSM": ["tsmc", "taiwan semiconductor"], "ASML": ["asml"], "INTC": ["intel"], "AMAT": ["applied materials"], "LITE": ["lumentum"]},
        "arxiv_terms": ["silicon photonics", "extreme ultraviolet lithography", "semiconductor"], "arxiv_cat": "physics.optics"}

REFS = [
    (1, "TSMC (2026). Fourth quarter 2025 earnings call transcript (2025 revenue of US$122 billion).", "https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf"),
    (2, "Convergedigest (2026). Intel closes 2025 flat as data centre and AI revenue grows.", "https://convergedigest.com/intel-closes-2025-flat-as-data-center-and-ai-revenue-grows/"),
]
REFS = REFS + TB.CHIP_REFS
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "TSM": [Scenario("bear", "Chip demand pauses and export rules tighten", 0.25, -0.30, 0.75),
            Scenario("base", "Advanced-node demand keeps growing", 0.50, 0.12, 0.75),
            Scenario("bull", "AI chip demand outruns supply for years", 0.25, 0.35, 0.75)],
    "ASML": [Scenario("bear", "Orders slip as chipmakers delay factories", 0.25, -0.30, 0.75),
             Scenario("base", "EUV sales grow with the backlog", 0.50, 0.12, 0.75),
             Scenario("bull", "High-NA and memory demand lift EUV sales", 0.25, 0.35, 0.75)],
    "INTC": [Scenario("bear", "18A yields disappoint and foundry losses continue", 0.40, -0.40, 0.75),
             Scenario("base", "Slow recovery, foundry still loss-making", 0.35, 0.05, 0.75),
             Scenario("bull", "Outside customers sign for its foundry", 0.25, 0.50, 0.75)],
    "AMAT": [Scenario("bear", "China sales fall further and orders slow", 0.30, -0.30, 0.75),
             Scenario("base", "Steady growth in equipment and services", 0.45, 0.10, 0.75),
             Scenario("bull", "A new factory-building cycle lifts orders", 0.25, 0.30, 0.75)],
    "LITE": [Scenario("bear", "AI optics demand cools after a very fast rise", 0.40, -0.45, 0.75),
             Scenario("base", "Growth continues at a slower pace", 0.35, 0.05, 0.75),
             Scenario("bull", "Co-packaged optics become standard in data centres", 0.25, 0.50, 0.75)],
}

COMPANIES = [
    {"t": "TSM", "name": "TSMC", "kind": "Chip foundry",
     "rivals": "Samsung Foundry, Intel Foundry",
     "profit": f"Makes chips to other firms' designs. Fourth-quarter 2025 revenue was US$33.73 billion with a 62.3% gross margin, and 77% of wafer revenue came from 7nm and smaller processes.{cite(11)} It guided a 2026 capital budget of US$52 billion to US$56 billion.",
     "watch": "Advanced-node demand, capital spending, export rules, Taiwan risk.",
     "rank": "It reached volume production at 2nm in late 2025.",
     "verdict": "A foundry at a 62.3% gross margin"},
    {"t": "ASML", "name": "ASML", "kind": "Chip-making equipment",
     "rivals": "None in EUV",
     "profit": f"Sells the lithography machines. 2025 net sales were 32.7 billion euros, with EUV system sales of 11.6 billion euros from 48 systems. Its backlog was 38.8 billion euros.{cite(12)} It guided 34 to 39 billion euros of sales for 2026.",
     "watch": "EUV orders, High-NA shipments, China sales.",
     "rank": f"The only company that makes EUV machines.{cite(19)}",
     "verdict": "The only EUV maker"},
    {"t": "INTC", "name": "Intel", "kind": "Chip designer and foundry",
     "rivals": "AMD, Nvidia, TSMC, Samsung",
     "profit": f"2025 revenue was $52.9 billion, flat. Intel Foundry's revenue was $17.8 billion and it lost $2.5 billion at the operating level in the fourth quarter alone.{cite(13)} The US government took about 9.9% of the company in August 2025.{cite(17)}",
     "watch": "18A yields, outside foundry customers, Irish and US fab output.",
     "rank": "A recovering incumbent. It runs Fab 34 in Leixlip, Ireland, a 17 billion euro investment.",
     "verdict": "A turnaround with a state shareholder"},
    {"t": "AMAT", "name": "Applied Materials", "kind": "Chip-making equipment",
     "rivals": "Lam Research, Tokyo Electron, KLA",
     "profit": f"Sells deposition, etch and other equipment. Fiscal 2025 revenue was about $28.4 billion, a record. China was about 29% of revenue, down from 45% at its peak.{cite(16)}",
     "watch": "China sales, export rules, memory and logic equipment orders.",
     "rank": "A leading equipment supplier.",
     "verdict": "Picks and shovels, with a China question"},
    {"t": "LITE", "name": "Lumentum", "kind": "Lasers and optical parts (photonics)",
     "rivals": "Coherent, and Chinese optical makers",
     "profit": f"Sells lasers and optical parts, with AI data centres driving demand. Fiscal 2026 revenue was $3.014 billion, up 83%, and cloud transceiver revenue rose more than 173%.{cite(15)}",
     "watch": "Data-centre optics orders, co-packaged optics, capacity.",
     "rank": "A photonics supplier whose revenue has risen very fast on AI spending.",
     "verdict": "The light side of the AI build-out"},
]

LADDER = [("Lab chip", "Works in a|laboratory"), ("Pilot line", "Made in small|numbers"), ("Volume", "High-volume|manufacturing"),
          ("Design wins", "Customers build|products on it"), ("Yield", "Most chips|work"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "mixed"), "IE": (3, 0, "friendly"), "NL": (5, 0, "friendly"), "CN": (9, 1, "restrictive"),
         "KR": (10, 0, "friendly"), "TW": (10, 2, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "NL": "Netherlands", "CN": "China", "KR": "South Korea", "TW": "Taiwan"}
COUNTRY = {
    "US": {"co": "Intel, Applied Materials, Nvidia", "gov": "The CHIPS and Science Act sets aside $52.7 billion for chips. The government took about 9.9% of Intel in August 2025", "ctl": "Export controls on advanced chips, including a licence rule for Nvidia's H20 in April 2025",
           "note": "Heavy subsidy and heavy export rules."},
    "IE": {"co": "Intel (Fab 34, Leixlip)", "gov": "Intel opened Fab 34 in September 2023, a 17 billion euro investment. It makes chips with EUV lithography", "ctl": "EU rules (Chips Act)", "note": "Home of Intel's main European chip factory."},
    "NL": {"co": "ASML", "gov": "Home of ASML, the only maker of EUV machines", "ctl": "Export licences for advanced machines", "note": "A single company at the centre of advanced chip making."},
    "TW": {"co": "TSMC", "gov": "Home of TSMC, with 2025 revenue of about US$122 billion", "ctl": "See the references", "note": "The centre of advanced manufacturing."},
    "KR": {"co": "Samsung, SK hynix", "gov": "Announced support of up to 26 trillion won, as reported in 2022", "ctl": "See the references", "note": "Strong in memory."},
    "CN": {"co": "Chinese chipmakers and equipment makers", "gov": "A state effort reported at more than $100 billion", "ctl": "Faces US export controls on advanced chips and equipment", "note": "A large market, restricted from the most advanced chips."},
}
HYPE = [
    ("5", "Audited revenue and margins", "A company reports profit from the product", "TSMC at a 62.3% gross margin", "ok"),
    ("4", "Backlog and capacity spending", "Customers have ordered and money is being spent", "ASML backlog of 38.8 billion euros", "ok"),
    ("3", "Volume production", "A process or product ramps in a factory", "TSMC 2nm and Intel 18A in 2025", "dis"),
    ("2", "A subsidy or equity stake", "A government commits money", "US stake in Intel", "dis"),
    ("1", "Roadmap", "A node or product due on a date", "Future process names", "tgt"),
]
SHOVELS = [
    ("EUV lithography", "ASML", "Netherlands", "The only maker of EUV machines"),
    ("Deposition and etch equipment", "Applied Materials", "United States", "Builds the layers of a chip. Record revenue in fiscal 2025"),
    ("Advanced manufacturing", "TSMC", "Taiwan", "77% of its wafer revenue is 7nm or smaller"),
    ("Lasers and optics", "Lumentum", "United States", "Fiscal 2026 revenue up 83% on AI data centres"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["TSM", "ASML", "INTC", "AMAT", "LITE", "NVDA"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["TSM", "ASML", "INTC", "AMAT", "LITE"],
                                     [["TSM", "TSMC"], ["ASML", "ASML"], ["INTC", "Intel"], ["AMAT", "Applied Materials"], ["LITE", "Lumentum"], ["NVDA", "Nvidia"]],
                                     {"TSM": "2016-01-04", "ASML": "2016-01-04", "INTC": "2016-01-04", "AMAT": "2016-01-04", "LITE": "2016-01-04", "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Controls", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("TSM", "ASML", "INTC", "AMAT", "LITE", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Intel", f"from {runs['INTC']['from']}", runs["INTC"]["multiple"], "lay"),
            ("Applied Materials", f"from {runs['AMAT']['from']}", runs["AMAT"]["multiple"], "lay"),
            ("ASML", f"from {runs['ASML']['from']}", runs["ASML"]["multiple"], "lay"),
            ("TSMC", f"from {runs['TSM']['from']}", runs["TSM"]["multiple"], "quantum"),
            ("Lumentum", f"from {runs['LITE']['from']}", runs["LITE"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Chip makers and equipment", ["TSM", "ASML", "AMAT", "INTC"], "var(--amber)"), ("Photonics", ["LITE"], "var(--teal)")])

    hero = K.hero("Frontier / Chip", "The finest chip patterns are printed by <em>one company's machines</em>",
                  "World chip sales reached $791.7 billion in 2025. The finest patterns on advanced chips are printed by machines that one company makes. Here is how the industry fits together, who is paid, and where Ireland sits.",
                  "sandia-chip.jpg", art_more.hero_network(),
                  [(792, "billion dollars of chips sold worldwide in 2025", "$", "bn"), (48, "EUV machines ASML recognised revenue on in 2025", "", ""),
                   (77, "per cent of TSMC's fourth-quarter wafer revenue came from 7nm and smaller processes", "", "%"),
                   (17, "billion euros: Intel's Fab 34 at Leixlip in Ireland", "", " bn euros")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Patterns on silicon, a handful of firms that can print them, and light that carries the data.", f'''
<p>A chip is made by printing patterns onto a silicon wafer, layer after layer, then cutting the wafer into chips. World sales of chips were $791.7 billion in 2025, up 25.6% on 2024. Logic chips made $301.9 billion of that and memory $223.1 billion.{cite(10)}</p>
{note("Why it is attractive", "<p>The industry association projects roughly $1 trillion of sales in 2026.</p>")}
<p>The finest patterns on advanced chips are printed with extreme ultraviolet light, by machines made by ASML, which is the only company that makes them.{cite(19)} TSMC makes chips to other firms' designs, and 77% of its fourth-quarter 2025 wafer revenue came from 7nm and smaller processes.{cite(11)}</p>
{note("The catch", "<p>The supply chain has a few single points: one company for EUV machines, a small number of firms for advanced manufacturing, and export rules that decide who can buy what.</p>")}
<div class="fx-photos wide">
{photo("sandia-chip.jpg", caption="A Sandia scientist in protective gear examining a microelectronics chip.")}
{photo("clean-room-fab.jpg", caption="The clean room of a semiconductor manufacturing plant.")}
{photo("laser-diode-chip.jpg", caption="A laser diode chip, the kind of device photonics firms sell.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Parts" style="margin-top:36px">The parts of the business</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Foundry</h3><p>TSMC reported revenue of US$33.73 billion in the fourth quarter of 2025 at a 62.3% gross margin.{cite(11)}</p></div>
<div class="card rv"><h3>Equipment</h3><p>ASML's 2025 sales were 32.7 billion euros and Applied Materials' fiscal 2025 revenue was about $28.4 billion.{cite(12)}{cite(16)}</p></div>
<div class="card rv"><h3>Chip design</h3><p>Intel's 2025 revenue was $52.9 billion, flat, with its foundry still loss-making.{cite(13)}</p></div>
<div class="card rv"><h3>Photonics</h3><p>Lumentum's fiscal 2026 revenue was $3.014 billion, up 83%, as AI data centres bought lasers and optics.{cite(15)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Export rules</h3><p>In April 2025 the US required a licence for Nvidia's H20 chip to go to China. It began issuing licences again in August.{cite(18)}</p></div>
<div class="card rv"><h3>China exposure</h3><p>China was about 29% of Applied Materials' fiscal 2025 revenue, down from a peak of 45%.{cite(16)}</p></div>
<div class="card rv"><h3>Turnarounds are slow</h3><p>Intel Foundry lost $2.5 billion at the operating level in the fourth quarter of 2025.{cite(13)}</p></div>
<div class="card rv"><h3>One supplier</h3><p>ASML is the only maker of EUV machines.{cite(19)}</p></div>
</div>
{TB.chip_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev big"><div class="yr">September 2023</div><p>Intel opens Fab 34 at Leixlip in Ireland, a 17 billion euro investment that makes chips with EUV lithography.{cite(14)}</p></div>
<div class="ev"><div class="yr">April 2025</div><p>The US requires a licence for Nvidia's H20 chips to go to China.{cite(18)}</p></div>
<div class="ev"><div class="yr">August 2025</div><p>The US government agrees to take about 9.9% of Intel for 433.3 million shares at $20.47.{cite(17)}</p></div>
<div class="ev big"><div class="yr">Late 2025</div><p>TSMC reaches volume production at 2nm.{cite(11)}</p></div>
<div class="ev"><div class="yr">2025</div><p>World chip sales reach $791.7 billion.{cite(10)}</p></div>
<div class="ev fut"><div class="yr">2026</div><p>The industry association projects about $1 trillion of sales. TSMC plans US$52 billion to US$56 billion of capital spending.{cite(10)}{cite(11)}</p></div>
</div>''', K.key_idea("Few firms, huge sums",
        "A few firms make the machines and the advanced chips, and they are earning very large revenues. "
        "The risks are concentrated too: export rules, China exposure and the cost of catching up."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>Chip sales rose 25.6% in 2025 to $791.7 billion, led by logic and memory.{cite(10)}</p></div>
<div class="card rv"><h3>What has not</h3><p>Advanced chip making still depends on one machine maker and a few factories.{cite(19)}</p></div>
<div class="card rv"><h3>What is new</h3><p>Governments hold or fund chipmakers. The US government owns about 9.9% of Intel.{cite(17)}</p></div>
</div>
<div class="wide">{photo("sierra-supercomputer.jpg", caption="The Sierra supercomputer at Lawrence Livermore National Laboratory, built from processors and accelerators.")}</div>''',
        K.key_idea("A trillion-dollar industry on a narrow base",
                   "The industry is growing very fast and rests on a few companies and a few machines. That is why governments and investors watch it so closely."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Our judgement from the figures. Not a forecast.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now: capacity</div><p>TSMC plans US$52 billion to US$56 billion of capital spending in 2026 and ASML holds a 38.8 billion euro backlog.{cite(11)}{cite(12)}</p></div>
<div class="ev fut"><div class="yr">Next: smaller processes</div><p>2nm is in volume production at TSMC and Intel's 18A is ramping.{cite(11)}{cite(13)}</p></div>
<div class="ev fut"><div class="yr">Alongside: light</div><p>Data centres are buying lasers and optics fast. Lumentum's revenue rose 83% in fiscal 2026.{cite(15)}</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>Intel at Leixlip</h3><p>Fab 34 opened in September 2023, a 17 billion euro investment that makes chips with EUV lithography.{cite(14)}</p></div>
<div class="card rv"><h3>The exposure</h3><p>Intel's results depend on its foundry turning profitable. It lost $2.5 billion at the operating level in the fourth quarter of 2025.{cite(13)}</p></div>
<div class="card rv"><h3>The rules</h3><p>The EU Chips Act aims to mobilise 43 billion euros of public and private money.{cite(20)}</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a worker</h3><p>Skills in process engineering, equipment maintenance and data-centre optics are in demand where factories are being built.</p></div>
<div class="card rv"><h3>As a business</h3><p>Chip supply can tighten. Ask suppliers about lead times for the parts you depend on.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Chip shares moved with AI demand and with export news. Equipment makers, foundries and photonics firms have different risks.</p></div>
</div>''', K.key_idea("Capacity first, then smaller chips, then light",
        "The order is clear: build capacity, move to smaller processes, move data with light. Intel's Irish factory is part of the first step."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "A foundry, a toll-gate machine maker, an incumbent in recovery, an equipment giant and a photonics firm.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The designers<span>Nvidia, AMD and others</span></h3>
<dl><dt>What they do</dt><dd>Design chips that foundries make. Nvidia is covered on Frontier Mind.</dd>
<dt>Why they matter</dt><dd>Their orders fill foundries and equipment makers' order books.</dd></dl><span class="verdict">The customers of the whole chain</span></article></div>
{K.prices_block("s-prices", "Share prices", "Five chip companies, with Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "TSMC and ASML are on the top rung. Intel Foundry is between volume and margin.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Backlogs grow faster than revenue.</li><li>Customers prepay for capacity.</li><li>Yields on a new process pass a target.</li><li>Equipment orders rise from several customers at once.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Orders from a few customers fund the whole expansion.</li><li>Capital spending runs far ahead of revenue.</li><li>Export rules change quickly.</li><li>Prices jump on any AI headline.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>makes chips or machines</span><span><i style="border-color:var(--violet)"></i>subsidises and restricts</span><span><i style="border-color:var(--red)"></i>restricted from advanced chips</span>', "Pick a country. A summary from the cited public sources.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The money is in the toll gates",
        "The firms that sit at the narrowest points of the chain, the machines and the advanced factories, report the best margins. "
        "Their risk is concentration in customers, in countries and in one technology."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Export rules, concentration, turnarounds and cycles.", f'''
<div class="cols wide">
<div class="card rv"><h3>Export rules</h3><p>A licence rule on Nvidia's H20 in April 2025 led Nvidia to expect about $5.5 billion in charges.{cite(18)}</p></div>
<div class="card rv"><h3>China exposure</h3><p>China was about 29% of Applied Materials' fiscal 2025 revenue.{cite(16)}</p></div>
<div class="card rv"><h3>Turnaround risk</h3><p>Intel Foundry still lost money in 2025 even as 18A began to ramp.{cite(13)}</p></div>
<div class="card rv"><h3>One machine</h3><p>ASML is the only maker of EUV machines. Any problem there stops the whole chain.{cite(19)}</p></div>
<div class="card rv"><h3>Capital cost</h3><p>TSMC alone plans US$52 billion to US$56 billion of capital spending in 2026.{cite(11)}</p></div>
<div class="card rv"><h3>Boom and bust</h3><p>Lumentum's revenue rose 83% in a year. Fast rises like that can reverse when orders pause.{cite(15)}</p></div>
</div>
<div class="fx-photos wide">{photo("sandia-mems.jpg", caption="The world's smallest micro-chain drive, fabricated at Sandia National Laboratories.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>A very small number of companies and machines sit under a trillion-dollar industry, and governments are now deciding who may buy what.</p></div></div>''',
        K.key_idea("Concentration is the risk and the moat",
                   "The same narrowness that gives these firms their margins makes the industry fragile to one rule, one factory or one customer."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 80%</h3><p>More volume production at 2nm and beyond. More chip factory announcements. More tokens of state support or ownership.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>An outside customer commits a large order to Intel Foundry's most advanced process.</p></div>
<div class="card rv"><h3>Unlikely, under 20%</h3><p>A second company ships EUV machines in volume.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">The chip industry will keep growing. It will also keep depending on a very small number of firms and machines.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Firms that depend on a few customers or on China sales, and firms that must turn a foundry profitable.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>AI demand keeps filling factories and order books, and the new processes reach good yields.</p></div>
<div class="card rv"><h3>The test</h3><p>For any chip claim, ask who makes it, on what process, at what yield and for which customers.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A change to export rules that closes a large market. A failure of a new process to reach good yields. A second source of EUV machines.</div>''',
        K.key_idea("Strong growth on a narrow base",
                   "We expect more factories, smaller processes and more optics. We also expect export rules and customer concentration to stay the main risks."), short="Outlook")

    bands = [band("sandia-chip.jpg", "The chip", "Examined in protective gear.", "A Sandia scientist examining a microelectronics chip"),
             band("clean-room-fab.jpg", "The factory", "The clean room of a chip plant.", "The clean room of a semiconductor manufacturing plant"),
             band("laser-diode-chip.jpg", "The light", "A laser diode chip.", "A laser diode chip"),
             band("sierra-supercomputer.jpg", "The machine", "Built from processors.", "The Sierra supercomputer"),
             band("sandia-mems.jpg", "The small", "A chain drive made at microscopic scale.", "A micro-chain drive made at Sandia")]
    foot = K.foot(REFS, AS_OF, "Frontier Chip", "chip",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Company and industry figures were checked against the sources listed and are rounded. Where sources disagreed the text says so.")
    nf = K.notice("We explain how the semiconductor industry works and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("World chip sales 2025", "$791.7bn"), ("EUV machine makers", "one"), ("TSMC 7nm and smaller", "77% of wafers"), ("Intel Fab 34, Ireland", "17bn euros")]
    body = K.assemble("chip", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
