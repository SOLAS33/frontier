"""Frontier Cell: batteries and energy storage. Voice rules: docs/VOICE.md."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_blocks as TB

TITLE = "Frontier Cell"
AS_OF = "16 October 2026"

LIVE = {"cik": {"QS": 1811414, "ENVX": 1828318, "EOSE": 1805077, "FLNC": 1868941, "ALB": 915913},
        "aliases": {"QS": ["quantumscape"], "ENVX": ["enovix"], "EOSE": ["eos energy"], "FLNC": ["fluence"], "ALB": ["albemarle"]},
        "arxiv_terms": ["lithium-ion battery", "solid-state electrolyte", "sodium-ion"], "arxiv_cat": "cond-mat.mtrl-sci"}

REFS = [
    (1, "International Energy Agency (2025). Global EV outlook 2025.", "https://www.iea.org/reports/global-ev-outlook-2025"),
    (2, "International Energy Agency (2025). Batteries and secure energy transitions.", "https://www.iea.org/reports/batteries-and-secure-energy-transitions"),
    (3, "BloombergNEF. Electric vehicle outlook and battery price survey.", "https://about.bnef.com/electric-vehicle-outlook/"),
    (4, "The Nobel Prize in Chemistry 2019: Goodenough, Whittingham, Yoshino, for the development of lithium-ion batteries.", "https://www.nobelprize.org/prizes/chemistry/2019/summary/"),
    (5, "US Energy Information Administration. Battery storage in the United States: an update on market trends.", "https://www.eia.gov/analysis/studies/electricity/batterystorage/"),
    (6, "EirGrid. Industry information: system services and the grid.", "https://www.eirgrid.ie/industry"),
    (7, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/"),
    (8, "International Energy Agency (2025). Energy and AI.", "https://www.iea.org/reports/energy-and-ai"),
    (9, "European Union. Regulation (EU) 2023/1542 concerning batteries and waste batteries.", "https://eur-lex.europa.eu/eli/reg/2023/1542/oj"),
]
REFS = REFS + TB.CELL_REFS + [(12, "Central Statistics Office (2026). Data centres metered electricity consumption 2025 (data centres used 23% of metered electricity, 7,663 GWh).", "https://www.irishtimes.com/business/2026/07/07/data-centres-account-for-almost-one-quarter-of-irish-electricity-usage-in-2025/"),
    (13, "QuantumScape (2026). Second quarter 2026 results (Form 8-K).", "https://www.sec.gov/Archives/edgar/data/0001811414/000119312526312423/qs-ex99_1.htm"),
    (14, "Eos Energy Enterprises (2026). Second quarter 2026 financial results.", "https://investors.eose.com/news-releases/news-release-details/eos-energy-enterprises-reports-second-quarter-2026-financial/"),
    (15, "Fluence Energy (2026). Third fiscal quarter 2026 results.", "https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-inc-reports-third-fiscal-quarter-2026-results"),
    (16, "Benchmark Mineral Intelligence (2026). Lithium price watch.", "https://source.benchmarkminerals.com/article/lithium-price-watch-what-the-forward-curve-is-telling-buyers-right-now"),
    (17, "BloombergNEF (2025). Lithium-ion battery pack prices fall to $108 per kilowatt-hour.", "https://about.bnef.com/insights/commodities/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices/")]
cite = K.cite_factory(REFS)

SCEN = {
    "QS": [Scenario("bear", "Cells miss automotive tests and it keeps raising money", 0.45, -0.50, 0.75),
           Scenario("base", "Samples progress, no volume yet", 0.35, 0.00, 0.75),
           Scenario("bull", "A carmaker commits to volume production", 0.20, 0.60, 0.75)],
    "ENVX": [Scenario("bear", "Revenue stays small and cash runs down", 0.40, -0.45, 0.75),
             Scenario("base", "Phone cells ramp slowly", 0.40, 0.00, 0.75),
             Scenario("bull", "A large device maker commits", 0.20, 0.50, 0.75)],
    "EOSE": [Scenario("bear", "Costs outrun revenue and funding is tight", 0.45, -0.50, 0.75),
             Scenario("base", "Orders arrive, margins stay negative", 0.35, 0.00, 0.75),
             Scenario("bull", "Long-duration storage becomes a market", 0.20, 0.55, 0.75)],
    "FLNC": [Scenario("bear", "Margins stay thin and orders slip", 0.35, -0.35, 0.75),
             Scenario("base", "Revenue grows with the market", 0.40, 0.05, 0.75),
             Scenario("bull", "Grid storage keeps growing very fast", 0.25, 0.45, 0.75)],
    "ALB": [Scenario("bear", "Lithium stays oversupplied", 0.35, -0.30, 0.75),
            Scenario("base", "Prices recover slowly", 0.40, 0.05, 0.75),
            Scenario("bull", "Demand from storage and cars tightens supply", 0.25, 0.45, 0.75)],
}

COMPANIES = [
    {"t": "QS", "name": "QuantumScape", "kind": "Solid-state battery developer",
     "rivals": "Toyota, Samsung SDI, Solid Power, CATL and every large cell maker",
     "profit": "Make a solid-state cell that passes automotive tests, then make it at volume and at a price. In 2026 it amended its PowerCo agreement, cutting maximum development payments from about $131 million to $75.4 million, kept a 2029 production target, and announced a Honda partnership. Quarterly net loss was about $98 million.{cite(13)}",
     "watch": "Third-party test data, carmaker commitments, factory partners, share sales.",
     "rank": "The best known solid-state developer, with a carmaker partner. Not yet in a production vehicle.",
     "verdict": "A real technical problem and a long runway"},
    {"t": "ENVX", "name": "Enovix", "kind": "Silicon anode cells",
     "rivals": "Sila, Amprius, large cell makers adding silicon to graphite",
     "profit": "Win phone and wearable makers who pay for energy density, then scale its factory yield.",
     "watch": "Factory yield, named customers, quarterly revenue against cash burn.",
     "rank": "Second-quarter 2026 revenue was about $9.0 million. The test is manufacturing yield.",
     "verdict": "Small cells, small revenue, high hopes"},
    {"t": "EOSE", "name": "Eos Energy", "kind": "Zinc long-duration storage",
     "rivals": "Form Energy (iron-air), flow batteries, lithium with more hours",
     "profit": "Make batteries that last 8 to 12 hours at a price that beats lithium on long storage, and fix its manufacturing costs.",
     "watch": "Gross margin, orders, factory output, funding.",
     "rank": "Second-quarter 2026 revenue was $68.8 million with a backlog of $807 million, and it still lost money on each unit sold.{cite(14)}",
     "verdict": "A useful idea that has not yet shown a margin"},
    {"t": "FLNC", "name": "Fluence", "kind": "Grid storage systems",
     "rivals": "Tesla Megapack, Sungrow, CATL, BYD",
     "profit": "Sell and run grid storage with a better margin than the Chinese cell makers, using software and services.",
     "watch": "Order backlog, gross margin, tariffs and cell supply, service revenue.",
     "rank": "In the quarter to June 2026 it had revenue of about $650 million, a 5.1% gross margin and a record backlog of about $6.4 billion.{cite(15)}",
     "verdict": "The picks-and-shovels role, with thin margins"},
    {"t": "ALB", "name": "Albemarle", "kind": "Lithium producer",
     "rivals": "SQM, Ganfeng, Tianqi, new mines in Australia and Africa",
     "profit": "Earns when lithium is expensive and loses when it is cheap. Lithium carbonate was about $19,750 a tonne in September 2026 on Benchmark's assessment, more than double the 2025 US average of about $9,000. Its 2026 outlook is given for $10, $20 and $30 a kilogram.",
     "watch": "Lithium price, mine costs, expansion plans, demand from storage and cars.",
     "rank": "One of the largest producers outside China, in a market with large swings.",
     "verdict": "A commodity cycle"},
]

LADDER = [("Lab result", "A better cell|in a paper"), ("Pilot line", "Hundreds of cells|made by machine"), ("Qualification", "A carmaker tests|and accepts it"),
          ("First product", "In a car or a|grid unit"), ("Volume", "Gigawatt-hours|a year"), ("Cost parity", "Beats the incumbent|on price"),
          ("Profit", "Makers earn|their capital back")]

TILES = {"CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "CL": (1, 3, "mixed"), "IE": (3, 0, "friendly"), "GB": (4, 0, "friendly"),
         "DE": (6, 0, "friendly"), "SE": (7, 0, "friendly"), "FR": (4, 1, "friendly"), "KR": (10, 0, "leader"), "CN": (9, 1, "leader"),
         "JP": (11, 1, "leader"), "IN": (8, 2, "friendly"), "AU": (10, 3, "mixed"), "CD": (6, 3, "mixed")}
NAMES = {"CA": "Canada", "US": "United States", "CL": "Chile", "IE": "Ireland", "GB": "United Kingdom", "DE": "Germany", "SE": "Sweden",
         "FR": "France", "KR": "South Korea", "CN": "China", "JP": "Japan", "IN": "India", "AU": "Australia", "CD": "DR Congo"}
COUNTRY = {
    "CN": {"co": "CATL, BYD, EVE, Gotion", "gov": "Industrial policy since the 2010s; heavy state support from mine to cell",
           "ctl": "Controls on some graphite and battery technology exports", "note": "Made more than 80% of the world's battery cells in 2025, according to the IEA's 2026 outlook."},
    "KR": {"co": "LG Energy Solution, Samsung SDI, SK On", "gov": "Large support for cells and materials", "ctl": "Follows allied rules", "note": "The main non-Chinese cell makers."},
    "JP": {"co": "Panasonic, Toyota, AESC", "gov": "Subsidies and a solid-state push", "ctl": "Follows allied rules", "note": "Pioneered lithium-ion. Strong in solid-state patents."},
    "US": {"co": "Tesla, QuantumScape, Fluence, Albemarle, GM, Ford", "gov": "Inflation Reduction Act credits and a tariff wall on Chinese cells",
           "ctl": "Tariffs on Chinese batteries and rules on sourcing", "note": "Subsidy swings with each administration."},
    "DE": {"co": "Volkswagen's PowerCo, BMW, Mercedes, Northvolt's remains", "gov": "EU Battery Regulation applies; subsidy for local factories", "ctl": "EU rules",
           "note": "Europe's cell factories have struggled to compete on cost."},
    "SE": {"co": "Northvolt, which failed in 2025; Stegra", "gov": "EU-backed", "ctl": "EU rules", "note": "A cautionary example of scaling cell making in Europe."},
    "FR": {"co": "Verkor, ACC, Saft", "gov": "State-backed gigafactories", "ctl": "EU rules", "note": "Trying to build a cell industry from scratch."},
    "GB": {"co": "AESC Sunderland, Britishvolt (failed), Faraday Institution research", "gov": "Automotive transformation fund", "ctl": "Rules of origin in the EU trade deal", "note": "Strong research, small manufacturing."},
    "CA": {"co": "Lithium and nickel miners, Northvolt Quebec plan", "gov": "Subsidies for processing and cell plants", "ctl": "Follows US rules", "note": "A source of battery minerals and clean power."},
    "AU": {"co": "Pilbara, IGO, Liontown (lithium miners)", "gov": "Critical minerals strategy and funding", "ctl": "Exports raw spodumene, mostly refined in China", "note": "The largest lithium miner, and it ships the ore."},
    "CL": {"co": "SQM, Albemarle", "gov": "A national lithium strategy with the state taking part-ownership", "ctl": "State involvement in new projects", "note": "Brines in the Atacama give some of the cheapest lithium."},
    "CD": {"co": "Large cobalt mines, many Chinese-owned", "gov": "Mining code revisions", "ctl": "Cobalt export limits introduced in 2025", "note": "Supplies most of the world's cobalt. Works to cut cobalt out of cells."},
    "IN": {"co": "Tata Agratas, Reliance", "gov": "Production-linked incentive scheme for cells", "ctl": "Import duties", "note": "A late and large entrant."},
    "IE": {"co": "Grid batteries, wind and solar developers, EirGrid", "gov": "Capacity and system-services auctions pay batteries to stabilise the grid",
           "ctl": "EU battery rules apply", "note": "Batteries help the grid absorb wind that would otherwise be switched off. See GridWatch for the live picture."},
}
HYPE = [
    ("5", "Independent test data", "Cells tested by a third party and published", "Test-lab cycle life results", "ok"),
    ("4", "Fleet performance", "Real packs in real use, with failure data", "Years of grid storage operation", "ok"),
    ("3", "Company data sheet", "Numbers from the maker, on its own terms", "Energy density figures in a launch", "dis"),
    ("2", "Pilot line claim", "Results from a small line, not a factory", "Samples shipped to partners", "tgt"),
    ("1", "Roadmap or press release", "A target year and a number", "'Production by 2028'", "tgt"),
]
SHOVELS = [
    ("Lithium", "Albemarle, SQM, Ganfeng, Pilbara", "Chile, Australia, China", "Prices have swung five-fold in three years"),
    ("Cathode and anode materials", "Umicore, BASF, Chinese specialists", "Belgium, Germany, China", "Most graphite is refined in China"),
    ("Cells", "CATL, BYD, LG, Panasonic, Samsung SDI", "China, Korea, Japan", "The step where most of the value sits"),
    ("Grid integrators", "Fluence, Tesla Energy, Sungrow", "US, China", "Put cells into containers and run them"),
    ("Recycling", "Redwood, Li-Cycle (restructured), Umicore", "US, Canada, Belgium", "Recovers metal and lowers the need for mining"),
    ("Chargers and grid gear", "ABB, Siemens, Schneider", "Europe", "Connects the cells to the grid"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["QS", "ENVX", "EOSE", "FLNC", "ALB", "TSLA", "GM", "F"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["QS", "ENVX", "EOSE", "FLNC", "ALB"],
                                     [["QS", "QuantumScape"], ["ENVX", "Enovix"], ["EOSE", "Eos Energy"], ["FLNC", "Fluence"], ["ALB", "Albemarle"],
                                      ["TSLA", "Tesla"], ["GM", "General Motors"], ["F", "Ford"], ["NVDA", "Nvidia"]],
                                     {"QS": px_first("QS"), "ENVX": px_first("ENVX"), "EOSE": px_first("EOSE"), "FLNC": px_first("FLNC"), "ALB": "2020-03-16",
                                      "TSLA": "2020-03-16", "GM": "2020-03-16", "F": "2020-03-16", "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Trade and rules", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("QS", "ENVX", "EOSE", "FLNC", "ALB", "TSLA", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Tesla", f"from {runs['TSLA']['from']}", runs["TSLA"]["multiple"], "lay"),
            ("Eos Energy", f"from {runs['EOSE']['from']}", runs["EOSE"]["multiple"], "quantum"),
            ("Fluence", f"from {runs['FLNC']['from']}", runs["FLNC"]["multiple"], "quantum"),
            ("Albemarle", f"from {runs['ALB']['from']}", runs["ALB"]["multiple"], "quantum"),
            ("QuantumScape", f"from {runs['QS']['from']}", runs["QS"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Battery pure-plays", ["QS", "ENVX", "EOSE", "FLNC"], "var(--amber)"), ("Carmakers and lithium", ["TSLA", "GM", "F", "ALB"], "var(--teal)")])

    hero = K.hero("Frontier / Cell", "The part of the grid you can <em>carry</em>",
                  "A battery is a way to move electricity through time. Prices fell by about nine-tenths in fifteen years, and that is why cars, grids and phones are changing. Here is who makes money from it and who only promises to.",
                  "edison-factory.jpg", art_more.hero_cells(),
                  [(90, "per cent fall in battery pack prices since 2010, roughly", "about ", "%"), (80, "per cent of the world's battery cells were made in China in 2025", "over ", "%"),
                   (19750, "dollars a tonne: battery-grade lithium carbonate in September 2026, more than double the 2025 US average", "about $", ""),
                   (round(runs["EOSE"]["multiple"]), "times Eos Energy rose from low to high in one run", "", "x")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Two electrodes, a salt bath and a century of chemistry.", f'''
<p>A rechargeable battery stores energy by pushing charged atoms from one electrode to another, and releases it when they flow back. In a lithium-ion cell the atoms are lithium. The negative electrode is usually graphite and the positive electrode a metal oxide or iron phosphate. A thin plastic separator keeps them from touching, and a liquid or solid electrolyte carries the lithium between them.</p>
{note("Why lithium", "<p>It is the lightest metal and gives a high voltage. That means a lot of energy for the weight, which is what phones and cars need.</p>")}
<p>The 2019 Nobel Prize in Chemistry went to the people who made the lithium-ion cell practical.{cite(4)} Packs have fallen in price from well over a thousand dollars per kilowatt-hour in 2010 to roughly a tenth of that now.{cite(3)}</p>
{note("The price shift", "<p>Cheap cells made electric cars competitive, and then made grid storage pay. Both effects are only a few years old.</p>")}
<div class="fx-photos wide">
{photo("edison-trolley.jpg", caption="Thomas Edison riding a trolley powered by one of his storage batteries, in the early 1900s.")}
{photo("detroit-electric.jpg", caption="A Detroit Electric car on a promotional tour near Mount Rainier. Electric cars sold well in 1910. Cheap petrol ended that.")}
{photo("edison-factory.jpg", caption="Inside Edison's storage battery factory in West Orange, New Jersey, in the 1910s.")}
</div>
<h3 class="wide" id="s-chem" data-nav="Chemistries" style="margin-top:36px">Which chemistry for which job</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Lithium iron phosphate</h3><p>Cheaper and safer, a bit heavier. Now most of the world's storage and a large share of cars.{cite(1)}</p></div>
<div class="card rv"><h3>Nickel-rich lithium</h3><p>More energy per kilogram. Used where range matters. Costlier and more fire-sensitive.</p></div>
<div class="card rv"><h3>Sodium-ion</h3><p>No lithium, no cobalt, cheaper materials, less energy per kilogram. Entering production, mainly in China.</p></div>
<div class="card rv"><h3>Solid-state and long-duration</h3><p>Solid electrolytes promise more energy and safer cells. Iron-air, zinc and flow batteries aim to store power for eight hours to days, at a low cost per kilowatt-hour.</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Fire</h3><p>A damaged cell can overheat and set neighbours alight. Grid sites have burned, and insurers price it.</p></div>
<div class="card rv"><h3>Wear</h3><p>Cells lose capacity each cycle. Warranties promise 70 to 80% after ten years.</p></div>
<div class="card rv"><h3>Materials</h3><p>Lithium, nickel, cobalt and graphite come from a few places, and most of the refining is in one country.{cite(2)}</p></div>
<div class="card rv"><h3>Cost of scaling</h3><p>Building cell factories in new places has failed more often than it has worked. Northvolt, once Europe's hope, collapsed in 2025.</p></div>
</div>
{TB.cell_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1800</div><p>Volta's pile, the first battery.</p></div>
<div class="ev"><div class="yr">1859</div><p>The lead-acid battery, still in every petrol car.</p></div>
<div class="ev big"><div class="yr">1900s</div><p>Edison's nickel-iron battery and early electric cars. Cheap petrol and the electric starter motor ended their lead.</p></div>
<div class="ev big"><div class="yr">1991</div><p>Sony sells the first commercial lithium-ion cell.</p></div>
<div class="ev"><div class="yr">2008 to 2012</div><p>Tesla Roadster and the first mass-market electric cars. Packs still cost over $600 per kilowatt-hour.</p></div>
<div class="ev big"><div class="yr">2015 to 2020</div><p>China builds out cell factories and pack prices fall below $150.</p></div>
<div class="ev"><div class="yr">2022</div><p>Lithium prices spike, then fall far over two years. In 2026 they roughly double from the 2025 average.</p></div>
<div class="ev big"><div class="yr">2023 to 2025</div><p>Grid battery installations grow very fast. Sodium-ion cells enter production. Northvolt files for bankruptcy in March 2025, and Lyten agrees to buy its assets.</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The test of whether solid-state and long-duration designs reach volume. See chapter 6.</p></div>
</div>''', K.key_idea("Cheap cells changed two industries",
        "A battery pack cost more than a thousand dollars per kilowatt-hour in 2010 and a tenth of that today. That one change made electric cars "
        "competitive and made storing wind and solar power on the grid pay. The next gains are in cost and durability, and most of the world's "
        "cell making is in China."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines.", f'''
<div class="cols wide">
<div class="card rv"><h3>In a car</h3><p>The battery is a third to a half of the price of the car. Cheaper cells mean cheaper electric cars.</p></div>
<div class="card rv"><h3>On the grid</h3><p>Batteries soak up midday solar and wind, and release it in the evening. That lets grids use more of both without switching them off.</p></div>
<div class="card rv"><h3>In the supply chain</h3><p>Most of the work, from refining to cell making, is done in China, and the rest of the world is trying to catch up behind trade barriers.</p></div>
</div>''', K.key_idea("A cheap way to move energy through time",
                      "Electricity is hard to store. A battery stores it for a few hours at a price that has come down enough to matter. The value is in "
                      "smoothing the grid and making vehicles that need no fuel."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Grids first, then cars, then the materials chain.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2028: grid storage</div><p>The fastest-growing use. Batteries are paid to absorb surplus wind and solar and to stabilise frequency.{cite(5)}</p></div>
<div class="ev fut"><div class="yr">2026 to 2030: cars</div><p>Cheaper cells push electric cars to price parity with petrol in more markets. Tariffs and subsidies decide where, and when.{cite(1)}</p></div>
<div class="ev fut"><div class="yr">2027 to 2032: new chemistries</div><p>Sodium-ion at volume, solid-state in small luxury runs, long-duration storage in pilots.</p></div>
<div class="ev fut"><div class="yr">2030s: the chain moves</div><p>Recycling, new mines and regional cell plants. How much of the chain leaves China depends on subsidy and trade rules.{cite(9)}</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The wind problem</h3><p>On windy nights Irish wind farms are often asked to turn down because the grid cannot take their output. Batteries are the cheapest fix.</p></div>
<div class="card rv"><h3>How they are paid</h3><p>Grid-scale batteries earn from system-services contracts and capacity auctions run by EirGrid.{cite(6)} Hundreds of megawatts are connected and more are contracted.</p></div>
<div class="card rv"><h3>The data-centre link</h3><p>Data centres drew 23% of Irish metered electricity in 2025, up from 21% in 2023.{cite(12)}{cite(7)} Batteries on site are one of the ways to ease the pressure on the grid.{cite(8)}</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>At home</h3><p>A home battery pays only if you have solar or a time-of-use tariff. Ask for the payback in years, under your own usage.</p></div>
<div class="card rv"><h3>In business</h3><p>A site with a high peak demand charge can often cut the bill with a battery. Get a quote with real load data.</p></div>
<div class="card rv"><h3>With a car</h3><p>The battery is the part that ages. Look at the warranty on capacity, not only the distance on a full charge.</p></div>
<div class="card rv"><h3>With savings</h3><p>The listed names are a mix of tiny developers and commodity businesses. Their share prices swing with lithium and with subsidy.</p></div>
</div>''', K.key_idea("Storage on the grid first, cars next",
        "The quickest effect is on the grid, where batteries make more wind and solar usable. Cars follow as cells get cheaper. New chemistries and the "
        "supply chain take longer, and politics decides much of where the factories end up."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Developers with a lab result, integrators with an order book, and a commodity producer.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The carmakers<span>Tesla, GM, Ford</span></h3>
<dl><dt>Position</dt><dd>They buy most of the world's cells and run the largest battery programmes outside China. Tesla also sells grid storage.</dd>
<dt>Why they matter</dt><dd>Their orders decide whether a cell maker scales. Their share prices depend on much more than batteries.</dd>
<dt>Use</dt><dd>The lower-risk way to hold the theme, with a much smaller upside from any one cell breakthrough.</dd></dl><span class="verdict">The customers</span></article></div>
{K.prices_block("s-prices", "Share prices since listing", "Several of these came to market through mergers with blank-cheque companies in 2020 and 2021.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. Most of the battery names are far below their peaks.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 1), "The developers are on the lower rungs. The integrators and producers are higher but squeezed by price.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>A carmaker names a model with a new cell inside.</li><li>Third-party test data on cycle life is published.</li><li>Orders in gigawatt-hours with a price.</li><li>Lithium prices recover for a year.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>A 'breakthrough' with no independent test.</li><li>Capacity announced with no customers.</li><li>Cash needs that exceed revenue for years.</li><li>Dependence on a subsidy that must be renewed.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>leaders</span><span><i style="border-color:var(--violet)"></i>building</span><span><i style="border-color:var(--red)"></i>raw materials</span>', "Pick a country. A summary from public sources, so treat the detail as approximate.")}
<div class="callout t wide"><b>Why politics moves these shares.</b> Most cells and most refining are in one country. Tariffs, export controls on graphite and subsidy changes can reshape a company's outlook in a week.</div>
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("Selling shovels is not the same as owning the gold",
        "The profit in batteries so far sits with the big cell makers in Asia. The listed developers are mostly small and spend more than they earn. "
        "The integrators have real revenue and thin margins. The producers swing with the price of lithium."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Materials, safety, cost and competition.", f'''
<div class="cols wide">
<div class="card rv"><h3>Materials and refining</h3><p>Lithium, cobalt, nickel and graphite come from a few countries, and most of the refining is done in China.{cite(2)}</p></div>
<div class="card rv"><h3>Safety</h3><p>Thermal runaway is rare and serious. Regulators and insurers are tightening rules on sites near homes.</p></div>
<div class="card rv"><h3>Energy density</h3><p>Cells improve a few per cent a year, not by leaps. A claimed leap needs independent proof.</p></div>
<div class="card rv"><h3>Cost versus gas</h3><p>For long storage, a battery has to beat a gas turbine and a hydro dam. Eight hours is the line most chemistries struggle with.</p></div>
<div class="card rv"><h3>Recycling</h3><p>EU rules require recovery targets and a battery passport.{cite(9)} The first big waves of end-of-life packs arrive in the 2030s.</p></div>
<div class="card rv"><h3>Trade</h3><p>Tariffs and export controls reshape who can buy what. Plans made for one regime fail under another.</p></div>
</div>
<div class="fx-photos wide">{photo("wind-farm.jpg", caption="A wind farm in Idaho. Wind and solar are cheap. The hard part is when they produce, which is where batteries come in.")}
{photo("solar-install.jpg", caption="Workers installing solar panels. Solar at midday creates a surplus the grid must absorb or waste.")}</div>''',
        K.key_idea("The chemistry is not the hard part",
                   "The chemistry works. The limits are materials, factories, safety and price against gas. A battery that is twice as good in a lab can still lose "
                   "if it is a third harder to make."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology and the market</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 75%</h3><p>Grid battery installations keep growing at double digit rates. LFP and sodium-ion take more share. Prices keep falling.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>One western cell maker with a new chemistry reaches meaningful volume. Two or more fail or are bought cheaply.</p></div>
<div class="card rv"><h3>Unlikely, under 20%</h3><p>A solid-state cell is in a mass-market car by 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">Batteries will keep getting cheaper and more common. The listed companies are not the same thing as the technology.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. Most are far below their listing prices and need more money to reach profit.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Pre-revenue developers rely on share sales. The integrators face price pressure from Chinese suppliers. The lithium producer follows a price it does not control.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A qualified cell with a carmaker contract or a profitable long-duration order book would re-rate its owner quickly. Both are binary events.</p></div>
<div class="card rv"><h3>The test</h3><p>For each, find out who has bought it, at what price, and with whose money. A subsidy is a customer, and it can change.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> Independent test data showing a solid-state cell at automotive life. A long-duration storage maker reporting a positive gross margin. A durable recovery in lithium prices.</div>''',
        K.key_idea("A great industry with a hard market for small companies",
                   "We expect storage to be one of the fastest-growing parts of the energy system, and cheaper chemistries to take share. We do not expect the "
                   "small listed developers to share equally in it, and some will not get through."), short="Outlook")

    bands = [band("edison-trolley.jpg", "Where it started", "Edison built storage batteries for trolleys and cars a century ago.", "Thomas Edison riding a battery-powered trolley"),
             band("detroit-electric.jpg", "A false start", "Electric cars sold well in 1910. Then petrol got cheap.", "A Detroit Electric car on a mountain road"),
             band("edison-factory.jpg", "Where it is made", "Making cells is a manufacturing problem, as it was a century ago.", "A battery factory interior"),
             band("wind-farm.jpg", "Why the grid wants them", "Wind and solar are cheap and they come at the wrong time.", "A wind farm"),
             band("solar-install.jpg", "Three years", "Long enough to see which chemistries reach volume.", "Workers installing solar panels")]
    foot = K.foot(REFS, AS_OF, "Frontier Cell", "cell",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain and credited under each picture. Market figures are rounded and from public sources.")
    nf = K.notice("We explain how batteries work and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Pack price since 2010", "about -90%"), ("Cells made in China, 2025", "over 80%"), ("Lithium carbonate, Sept 2026", "$19,750/t"), ("Irish data-centre share, 2025", "23%")]
    body = K.assemble("cell", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
