"""Frontier Atom: fission power and small modular reactors. Voice rules: docs/VOICE.md."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_blocks as TB

TITLE = "Frontier Atom"
AS_OF = "16 October 2026"

LIVE = {"cik": {"OKLO": 1849056, "SMR": 1822966, "LEU": 1065059, "NNE": 1923891, "BWXT": 1486957},
        "aliases": {"OKLO": ["oklo"], "SMR": ["nuscale"], "LEU": ["centrus"], "NNE": ["nano nuclear"], "BWXT": ["bwx technologies", "bwxt"]},
        "arxiv_terms": ["nuclear reactor", "small modular reactor", "uranium enrichment"], "arxiv_cat": "physics.ins-det"}

REFS = [
    (1, "International Atomic Energy Agency. Power Reactor Information System (PRIS).", "https://pris.iaea.org"),
    (2, "International Energy Agency (2025). The path to a new era for nuclear energy.", "https://www.iea.org/reports/the-path-to-a-new-era-for-nuclear-energy"),
    (3, "World Nuclear Association. Information library: small nuclear power reactors.", "https://world-nuclear.org/information-library/nuclear-fuel-cycle/nuclear-power-reactors/small-nuclear-power-reactors"),
    (4, "US Nuclear Regulatory Commission. Advanced reactors and small modular reactors.", "https://www.nrc.gov/reactors/new-reactors/advanced.html"),
    (5, "US Department of Energy. High-assay low-enriched uranium (HALEU) explained.", "https://www.energy.gov/ne/articles/what-high-assay-low-enriched-uranium-haleu"),
    (6, "Lazard. Levelized cost of energy+ (annual).", "https://www.lazard.com/research-insights/levelized-cost-of-energyplus/"),
    (7, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/"),
    (8, "International Energy Agency (2025). Energy and AI.", "https://www.iea.org/reports/energy-and-ai"),
    (9, "Posiva. Final disposal facility at Onkalo, Finland.", "https://www.posiva.fi/en/index.html"),
]
REFS = REFS + TB.ATOM_REFS + [(13, "World Nuclear News / IAEA (2026). Operating reactors and nuclear share of global electricity, 2025.", "https://pris.iaea.org/PRIS/WorldStatistics/OperationalReactorsByCountry.aspx"),
    (14, "Central Statistics Office (2026). Data centres metered electricity consumption 2025 (data centres used 23% of metered electricity, 7,663 GWh).", "https://www.irishtimes.com/business/2026/07/07/data-centres-account-for-almost-one-quarter-of-irish-electricity-usage-in-2025/"),
    (15, "US Nuclear Regulatory Commission (2026). NRC approves construction permit for TVA Clinch River small modular reactor.", "https://www.nrc.gov/about-nrc/news-releases/2026/26-079"),
    (16, "Slugger O'Toole (2026). Dail to consider ending Ireland's ban on nuclear power.", "https://sluggerotoole.com/2026/05/25/dail-to-consider-ending-irelands-ban-on-nuclear-power/"),
    (17, "Electricity Regulation Act 1999, section 18 (Irish statute book).", "https://revisedacts.lawreform.ie/eli/1999/act/23/section/18/revised/en/html")]
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "OKLO": [Scenario("bear", "Licensing slips and it has to raise more money", 0.45, -0.50, 0.75),
             Scenario("base", "Progress on licensing, no revenue yet", 0.35, 0.00, 0.75),
             Scenario("bull", "A licence arrives and a first plant is financed", 0.20, 0.60, 0.75)],
    "SMR": [Scenario("bear", "No firm orders and cash runs down", 0.40, -0.45, 0.75),
            Scenario("base", "Slow orders from partners", 0.35, 0.00, 0.75),
            Scenario("bull", "A firm order for a first plant lands", 0.25, 0.55, 0.75)],
    "LEU": [Scenario("bear", "Fuel prices fall and subsidies slip", 0.35, -0.40, 0.75),
            Scenario("base", "Enrichment expands on schedule", 0.40, 0.05, 0.75),
            Scenario("bull", "Fuel shortages and long contracts lift earnings", 0.25, 0.40, 0.75)],
    "NNE": [Scenario("bear", "Stays pre-revenue and dilutes holders", 0.45, -0.50, 0.75),
            Scenario("base", "Test units advance", 0.35, 0.00, 0.75),
            Scenario("bull", "A first customer commits", 0.20, 0.55, 0.75)],
    "BWXT": [Scenario("bear", "Naval work slows and civil orders stall", 0.25, -0.20, 0.75),
             Scenario("base", "Steady defence and civil growth", 0.50, 0.10, 0.75),
             Scenario("bull", "Reactor component orders accelerate", 0.25, 0.30, 0.75)],
}

COMPANIES = [
    {"t": "OKLO", "name": "Oklo", "kind": "Advanced reactor developer",
     "rivals": "NuScale, X-energy, TerraPower, Kairos, GE Vernova, Rolls-Royce SMR",
     "profit": "Get a licence from the US regulator, build a first plant on budget and sell power under long contracts. It has no revenue today.",
     "watch": "Licensing milestones, fuel supply, site and customer agreements, share sales.",
     "rank": "A development-stage company with large ambitions and a price that already assumes success.",
     "verdict": "A licence application with a share price"},
    {"t": "SMR", "name": "NuScale", "kind": "Small modular reactor designer",
     "rivals": "GE Vernova Hitachi, Westinghouse, Rolls-Royce SMR, X-energy",
     "profit": "Convert its approved design into a first firm order and build it for a price customers accept. Its largest planned project was cancelled in 2023 when costs rose.",
     "watch": "Firm orders, cost estimates, cash runway, partners such as Fluor funding the work.",
     "rank": "Its 77 MWe design has US regulator approval. No plant has been ordered and built yet.",
     "verdict": "Approved, not yet ordered"},
    {"t": "LEU", "name": "Centrus Energy", "kind": "Uranium enrichment and fuel",
     "rivals": "Urenco, Orano, Rosatom (Russian state firm), and a few new entrants",
     "profit": "It earns on fuel it sells and enrichment it builds. It profits when fuel is short and long contracts are priced high.",
     "watch": "Long-term contract prices, government funding for new fuel types, progress at its Ohio plant.",
     "rank": "The only US-owned maker of the high-assay fuel several new designs need, in small volumes.",
     "verdict": "A bottleneck owner with a small base"},
    {"t": "NNE", "name": "Nano Nuclear Energy", "kind": "Micro reactor developer",
     "rivals": "Oklo, Westinghouse eVinci, BWXT, Radiant",
     "profit": "Build a first micro reactor that regulators accept and find buyers for it. It has no revenue today.",
     "watch": "Test results, regulatory steps, fuel supply, share sales.",
     "rank": "A young company listed in 2024 with a concept stage product.",
     "verdict": "The most speculative of the five"},
    {"t": "BWXT", "name": "BWX Technologies", "kind": "Reactor components and fuel",
     "rivals": "Huntington Ingalls, Westinghouse, a few specialist suppliers",
     "profit": "Already profitable. It builds the reactors that power US submarines and aircraft carriers and wins civil orders as well.",
     "watch": "Backlog, naval programme funding, civil reactor component orders.",
     "rank": "The established industrial supplier, with a defence anchor.",
     "verdict": "The steady one"},
]

LADDER = [("Concept", "A design on|paper"), ("Licence", "A regulator|approves it"), ("Financing", "Banks and buyers|commit money"),
          ("First plant", "Built on time|and budget"), ("Fleet", "Factory builds|many alike"),
          ("Cheap power", "Beats gas and|wind plus storage"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "IE": (3, 0, "restrictive"), "GB": (4, 0, "friendly"), "FR": (4, 1, "friendly"),
         "DE": (6, 0, "restrictive"), "FI": (7, 0, "friendly"), "CH": (5, 1, "mixed"), "RU": (8, 0, "mixed"), "CN": (9, 1, "friendly"),
         "KR": (10, 0, "friendly"), "JP": (11, 1, "mixed"), "IN": (8, 2, "friendly"), "AE": (7, 2, "friendly")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "DE": "Germany", "FI": "Finland",
         "CH": "Switzerland", "RU": "Russia", "CN": "China", "KR": "South Korea", "JP": "Japan", "IN": "India", "AE": "United Arab Emirates"}
COUNTRY = {
    "US": {"co": "Westinghouse, GE Vernova, NuScale, Oklo, TerraPower, X-energy, Constellation", "gov": "Executive orders in 2025 set a goal of quadrupling nuclear capacity by 2050; faster licensing and fuel funding",
           "ctl": "Ban on Russian uranium imports with waivers to 2027", "note": "The largest fleet, and the biggest push to build new designs, helped by data-centre demand."},
    "CA": {"co": "OPG, Cameco, GE Vernova Hitachi", "gov": "Approved a BWRX-300 small reactor at Darlington, Ontario", "ctl": "Large uranium exporter", "note": "First G7 country to approve a grid-scale SMR build in the West."},
    "GB": {"co": "Rolls-Royce SMR, EDF, Urenco", "gov": "Selected Rolls-Royce SMR for its programme and backs Sizewell C", "ctl": "Follows allied fuel policy", "note": "Wants a home-grown design."},
    "FR": {"co": "EDF, Orano, Framatome", "gov": "Plans to build six new large reactors; 70% of its power is nuclear", "ctl": "Enrichment and recycling at home", "note": "The model for a nuclear-led grid."},
    "FI": {"co": "Fortum, TVO, Posiva", "gov": "Olkiluoto 3 online in 2023; deep repository for waste under test", "ctl": "EU rules", "note": "The first country close to a working waste repository."},
    "DE": {"co": "Large utilities, now out of nuclear", "gov": "Closed its last reactors in April 2023", "ctl": "EU rules", "note": "Decided against, at a cost to its power prices. The debate continues."},
    "IE": {"co": "None", "gov": "Irish law prohibits nuclear generation, and a bill to repeal the prohibition was introduced in May 2026", "ctl": "Interconnected to the UK and France", "note": "Buys nuclear power indirectly through its interconnectors."},
    "RU": {"co": "Rosatom", "gov": "The largest exporter of reactors and the largest supplier of enrichment", "ctl": "Western sanctions and import bans", "note": "The supplier the West is trying to replace."},
    "CN": {"co": "CNNC, CGN", "gov": "The largest build programme in the world, many new reactors a year", "ctl": "Closed market", "note": "Builds on schedule, at lower cost."},
    "KR": {"co": "KEPCO, Doosan Enerbility, KHNP", "gov": "Reversed a phase-out and exports reactors", "ctl": "Follows allied rules", "note": "A strong builder and supplier of heavy components."},
    "JP": {"co": "Utilities restarting reactors, Mitsubishi, Hitachi", "gov": "Restarting reactors after the 2011 shutdowns", "ctl": "Follows allied rules", "note": "Slow, steady restart after Fukushima."},
    "IN": {"co": "NPCIL, Tata", "gov": "Target of a large expansion and new private participation", "ctl": "Special trade rules for fuel", "note": "A big future market."},
    "AE": {"co": "ENEC, Barakah plant", "gov": "Four large reactors running at Barakah", "ctl": "Strict non-proliferation terms", "note": "Proved a newcomer can build quickly."},
    "CH": {"co": "Utilities with ageing reactors", "gov": "The Federal Council proposed lifting the ban on new plants in August 2025", "ctl": "EU-aligned", "note": "Rethinking."},
}
HYPE = [
    ("5", "Operating record", "A plant that has run and produced power for years", "Fleet capacity factors, IAEA statistics", "ok"),
    ("4", "Regulator approval", "A formal licence or design certification", "NuScale's design approval", "ok"),
    ("3", "Signed contract", "A binding agreement with money attached", "Long-term fuel contracts", "dis"),
    ("2", "Agreement in principle", "A memorandum or letter of intent", "Many data-centre power announcements", "tgt"),
    ("1", "Roadmap or press release", "A target date and a rendering", "'Online by 2030'", "tgt"),
]
SHOVELS = [
    ("Uranium mining", "Cameco, Kazatomprom, Orano", "Canada, Kazakhstan, France", "Kazakhstan produces the largest share"),
    ("Enrichment", "Urenco, Orano, Rosatom, Centrus", "Europe, Russia, US", "A few sites in the world do all of it"),
    ("Large forgings", "Doosan, Japan Steel Works, Framatome", "Korea, Japan, France", "Few firms can make reactor vessels"),
    ("Construction", "Bechtel, Fluor, KEPCO E&C", "US, Korea", "Cost overruns usually live here"),
    ("Operators", "Constellation, EDF, Vistra", "US, France", "Run the plants that exist now"),
    ("Waste", "Posiva, Orano, national bodies", "Finland, France", "Final storage is still an unsolved or slow problem in most countries"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["OKLO", "SMR", "LEU", "NNE", "BWXT", "CEG", "VST", "CCJ"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["OKLO", "SMR", "LEU", "NNE", "BWXT"],
                                     [["OKLO", "Oklo"], ["SMR", "NuScale"], ["LEU", "Centrus"], ["NNE", "Nano Nuclear"], ["BWXT", "BWX Technologies"],
                                      ["CEG", "Constellation"], ["VST", "Vistra"], ["CCJ", "Cameco"], ["NVDA", "Nvidia"]],
                                     {"OKLO": px_first("OKLO"), "SMR": px_first("SMR"), "LEU": "2020-01-06", "NNE": px_first("NNE"), "BWXT": "2016-07-04",
                                      "CEG": px_first("CEG"), "VST": "2016-10-03", "CCJ": "2020-03-16", "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Fuel and trade", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("OKLO", "SMR", "LEU", "NNE", "BWXT", "CEG", "CCJ", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Uranium miner Cameco", f"from {runs['CCJ']['from']}", runs["CCJ"]["multiple"], "lay"),
            ("Centrus Energy", f"from {runs['LEU']['from']}", runs["LEU"]["multiple"], "quantum"),
            ("NuScale", f"from {runs['SMR']['from']}", runs["SMR"]["multiple"], "quantum"),
            ("Oklo", f"from {runs['OKLO']['from']}", runs["OKLO"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Reactor developers", ["OKLO", "SMR", "NNE"], "var(--amber)"), ("Operators and suppliers", ["CEG", "VST", "BWXT", "CCJ"], "var(--teal)")])

    hero = K.hero("Frontier / Atom", "The oldest <em>new</em> power source",
                  "Fission has run reliably for seventy years and has been late and over budget for fifty. Here is what small reactors change, who is paid if they work, and why artificial intelligence put nuclear back on the table.",
                  "atr-core.jpg", art_more.hero_reactor(),
                  [(413, "power reactors in operation at the end of 2025, according to the IAEA", "", ""), (8, "per cent of the world's electricity came from fission in 2025 (8.4%)", "about ", "%"),
                   (round(runs["OKLO"]["multiple"]), "times Oklo rose from low to high in a year", "", "x"),
                   (0, "reactors in Ireland, where nuclear power is prohibited by law", "", "")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Splitting atoms, boiling water, and the reasons it costs so much to build.", f'''
<p>A fission reactor splits the nuclei of uranium atoms. Each split releases heat and neutrons, and the neutrons split more atoms, which keeps the reaction going. The heat boils water, the steam turns a turbine, and the turbine drives a generator. Fuel for an ordinary reactor is uranium enriched to a few per cent of the fissile isotope. A pellet the size of a fingertip holds about as much energy as a tonne of coal.</p>
{note("Why it is attractive", "<p>It runs day and night, in any weather, from a very small amount of fuel, and emits almost no carbon while running.</p>")}
<p>The IAEA counted 413 power reactors in operation at the end of 2025. Fission supplied 8.4% of the world's electricity in 2025, down from 8.7% in 2024 even though generation rose slightly.{cite(13)}</p>
{note("The catch", "<p>The plants are expensive, slow and bespoke. The cost of the money tied up during construction is often the largest cost.</p>")}
<div class="fx-photos wide">
{photo("x10-reactor.jpg", caption="Workers loading uranium slugs into the face of the X-10 Graphite Reactor at Oak Ridge in 1943. It was the second reactor ever built.")}
{photo("atr-core.jpg", caption="The four-lobed core of the Advanced Test Reactor in Idaho under 20 feet of water.")}
{photo("cherenkov.jpg", caption="Cherenkov glow around the core of a research reactor. The blue light is particles moving faster than light does in water.")}
</div>
<h3 class="wide" id="s-smr" data-nav="Small reactors" style="margin-top:36px">What a small modular reactor is</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Smaller</h3><p>Under 300 megawatts per unit, against 1,000 or more for a traditional plant. Easier to site, to finance and to place next to a factory or data centre.{cite(3)}</p></div>
<div class="card rv"><h3>Built in a factory</h3><p>The idea is to build many alike on a production line and ship them, so that costs fall with each one, as with aircraft.</p></div>
<div class="card rv"><h3>New designs</h3><p>Some use water, as today. Others use molten salt, sodium or gas as the coolant. Each brings new safety features and new licensing questions.{cite(4)}</p></div>
<div class="card rv"><h3>New fuel</h3><p>Many advanced designs need fuel enriched to between 5% and 20%, called HALEU. Very little is made outside Russia.{cite(5)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Cost and time</h3><p>Vogtle in Georgia, the last big US build, cost roughly twice its first estimate and came years late.</p></div>
<div class="card rv"><h3>Safety record, public view</h3><p>Three accidents, at Three Mile Island, Chernobyl and Fukushima, shaped policy for decades. Deaths per unit of energy are low, but trust is hard to rebuild.</p></div>
<div class="card rv"><h3>Waste</h3><p>It is small in volume and well contained, but there is no operating final repository yet. Finland's is the closest.{cite(9)}</p></div>
<div class="card rv"><h3>Fuel supply</h3><p>Enrichment is concentrated in a handful of sites, and the largest is Russian.</p></div>
</div>
{TB.atom_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev big"><div class="yr">1942</div><p>Chicago Pile-1 achieves the first controlled chain reaction.</p></div>
<div class="ev"><div class="yr">1951</div><p>An experimental reactor in Idaho lights four bulbs, the first electricity from fission.</p></div>
<div class="ev"><div class="yr">1954</div><p>Obninsk in the Soviet Union becomes the first reactor to feed a grid.</p></div>
<div class="ev"><div class="yr">1979 to 1986</div><p>Three Mile Island partly melts down. Chernobyl explodes. New orders in the West all but stop.</p></div>
<div class="ev"><div class="yr">2011</div><p>Fukushima. Germany begins a phase-out. Japan shuts its fleet.</p></div>
<div class="ev big"><div class="yr">2023</div><p>Vogtle 3 enters service, the first new US reactor in years. NuScale's largest planned project is cancelled as costs climb.</p></div>
<div class="ev big"><div class="yr">2024 to 2025</div><p>Technology companies sign deals for nuclear power for their data centres, including a restart of a Three Mile Island unit. The US sets a goal to quadruple nuclear capacity by 2050.</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The first small reactors get construction approval in the West: TerraPower's Natrium in March 2026, and TVA's BWRX-300 at Clinch River on 29 September 2026, with commercial operation targeted for 2033.{cite(15)} See chapter 6.</p></div>
</div>''', K.key_idea("Reliable power, built slowly",
        "A reactor splits uranium to make heat. It runs around the clock in any weather and gives off almost no carbon. It is also the most expensive and "
        "slowest kind of power station to build, which is why new ones have been rare. Small factory-built reactors are an attempt to fix the cost "
        "and the schedule."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>Electricity demand started growing again, mostly because of data centres, and grids cannot build wind and solar fast enough without something steady beside them.</p></div>
<div class="card rv"><h3>What has not</h3><p>Nuclear plants still cost a great deal to build, and the only new ones in the West were years late and well over budget.</p></div>
<div class="card rv"><h3>What is new</h3><p>A bet that smaller, factory-built reactors will be cheaper and faster, and that buyers with deep pockets will pay for the first ones.</p></div>
</div>
<div class="wide">{photo("centrifuges.jpg", caption="A cascade of gas centrifuges used to enrich uranium. Fuel for almost every reactor passes through machines like these, and very few sites in the world have them.")}</div>''',
        K.key_idea("Simple, steady, expensive",
                   "Nuclear power is a reliable way to make electricity and a hard thing to build cheaply. The new idea is to build small ones the way aircraft are "
                   "built, in volume, to bring the price down. It has not been proven yet."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Restarts and extensions first, then small reactors, then fuel.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2028: keep what exists</div><p>Life extensions and restarts of shut plants. This is the cheapest new power available and where most of the near-term gain is.</p></div>
<div class="ev fut"><div class="yr">2027 to 2031: first small units</div><p>Several designs aim for first plants in Canada, the US and the UK. Dates have slipped before and probably will again.</p></div>
<div class="ev fut"><div class="yr">2028 to 2035: fuel</div><p>New enrichment capacity in the West. Prices for enriched fuel stay high until it arrives.</p></div>
<div class="ev fut"><div class="yr">2030s: a fleet, or not</div><p>The test of whether small reactors can be built in numbers at a lower price. If they can, they take a real share of new power. If they cannot, they stay a niche.</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The law</h3><p>Section 18(6) of the Electricity Regulation Act 1999 says an order under that section shall not provide for the use of nuclear fission to generate electricity.{cite(17)} In May 2026 a Fianna Fail TD, James O'Connor, brought a bill to remove the prohibition, and the Taoiseach said Ireland is open to nuclear. The government has said it has no plans to authorise a plant.{cite(16)}</p></div>
<div class="card rv"><h3>The demand</h3><p>Data centres used 23% of metered electricity in 2025, up from 21% in 2023.{cite(14)}{cite(7)} The IEA expects data-centre demand worldwide to roughly double by 2030.{cite(8)}</p></div>
<div class="card rv"><h3>The indirect link</h3><p>Ireland already imports power through links to Britain and France, which both have nuclear fleets. See GridWatch for the live picture of the Irish grid.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a citizen</h3><p>Expect a public debate about nuclear in Ireland within this decade. The facts on cost, safety and waste in this chapter are the starting set.</p></div>
<div class="card rv"><h3>As a business</h3><p>If you run a power-hungry site, ask your supplier about its long-term mix and price risk. Contracts will start to name nuclear and gas by source.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Listed nuclear shares are in two groups: operators and suppliers with real earnings, and developers with a plan. They behave very differently.</p></div>
</div>''', K.key_idea("Keep, restart, then maybe build",
        "The nearest gains are in keeping existing plants running and restarting a few shut ones. New small reactors are later and less certain. "
        "Fuel supply is the quiet constraint underneath both."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Developers with a plan, suppliers with an order book, and the operators of the plants that already exist.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The operators and miners<span>Constellation, Vistra, Cameco</span></h3>
<dl><dt>Position</dt><dd>Constellation runs the largest nuclear fleet in the US. Vistra owns plants and gas. Cameco mines uranium in Canada and owns a stake in Westinghouse.</dd>
<dt>Why they matter</dt><dd>They earn from plants that already work, and benefit when power prices rise.</dd>
<dt>Use</dt><dd>The lower-risk way to hold the theme.</dd></dl><span class="verdict">The revenue is already there</span></article></div>
{K.prices_block("s-prices", "Share prices since listing", "The new reactor names listed in 2022 and 2024.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. All of the developer names have fallen steeply since their peaks.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Several designs have approvals. None has yet built a first plant in the West on time and on budget.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>A firm order with a price and a delivery date.</li><li>Banks lend against it without a government guarantee.</li><li>A first plant is built to its original budget.</li><li>Fuel supply contracts are signed for ten years.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Agreements in principle that name no price.</li><li>Developers with no revenue sell shares into each rally.</li><li>Completion dates move back a year at a time.</li><li>A licence is described as an order.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>building or backing it</span><span><i style="border-color:var(--violet)"></i>mixed</span><span><i style="border-color:var(--red)"></i>restricted or phasing out</span>', "Pick a country. A summary from public sources, so treat the detail as approximate.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("Operators earn now. Developers earn later, if at all",
        "The companies running existing plants make money today and gain as power prices rise. The companies designing new reactors have mostly not built one "
        "yet and are valued on a plan. The two groups have behaved very differently, and will."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Cost, licensing, fuel, people and trust.", f'''
<div class="cols wide">
<div class="card rv"><h3>Cost of money</h3><p>Years of construction mean years of interest. A project with a 10-year build and a high interest rate can double in cost before it earns anything.{cite(6)}</p></div>
<div class="card rv"><h3>Licensing</h3><p>New designs need years of review. Regulators in the US, Canada and the UK have promised faster paths and are being tested on them.{cite(4)}</p></div>
<div class="card rv"><h3>Fuel</h3><p>New designs need fuel that barely exists outside Russia. Building supply takes years and large contracts.{cite(5)}</p></div>
<div class="card rv"><h3>People</h3><p>Welders, engineers and operators are scarce after decades of few new builds.</p></div>
<div class="card rv"><h3>Trust</h3><p>One serious accident anywhere harms every project. Public support depends on the record being clean.</p></div>
<div class="card rv"><h3>Competition</h3><p>Gas turbines, solar with batteries and wind with storage keep getting cheaper. Nuclear has to beat them at the price of a firm supply.</p></div>
</div>
<div class="fx-photos wide">{photo("control-room.jpg", caption="A training replica of the Advanced Test Reactor control room at Idaho National Laboratory.")}
<div class="card" style="align-self:start"><h3>The cost problem in one line</h3><p>The first of anything is expensive. Factory-built reactors only get cheaper if the factory has a stream of orders to keep it busy. Orders only come if the first ones are cheap. Breaking that circle is the whole business plan. Governments, large technology buyers and the defence budget are the likely first customers, because they can pay more than a utility.</p></div></div>''',
        K.key_idea("It is a construction problem, not a physics problem",
                   "The physics is well known. The things that go wrong are the schedule, the cost of money, the fuel supply and public trust. "
                   "A project that gets all four right is rare, which is why the first few matter so much."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 75%</h3><p>More restarts and life extensions. More power contracts between technology firms and existing plants. More small reactors get US construction permits, after Natrium and Clinch River.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>The first fuel for advanced reactors from a Western enricher reaches commercial volumes by 2028.</p></div>
<div class="card rv"><h3>Unlikely, under 20%</h3><p>A small modular reactor in the West delivers power to a grid before 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">Nuclear will probably be part of the answer. Most of the developers will not be around to see it.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. The reactor developers fell steeply from their 2025 peaks, and their cash needs are large.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Pre-revenue developers must keep raising money, and each raise weakens existing holders. BWXT and the operators have earnings that carry them.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A first licence and a financed plant would re-rate the sector. The winners are likely to be those with fuel and manufacturing, not only a design.</p></div>
<div class="card rv"><h3>The test</h3><p>For each developer, check three things: a licence, a customer with a binding contract, and the fuel. Having all three is rare.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A binding firm order at a published price. A first plant finished at its original budget. A large government choosing to guarantee construction cost overruns.</div>''',
        K.key_idea("Real demand, slow supply, and a rough ride for the developers",
                   "We expect demand for firm power to keep rising and nuclear to get more attention and more contracts. We expect most new reactors to arrive later "
                   "than announced. The share prices of the developers reflect the first and ignore the second."), short="Outlook")

    bands = [band("x10-reactor.jpg", "Where it started", "The second reactor ever built, in 1943, was loaded by hand.", "Workers loading uranium slugs into a reactor face"),
             band("centrifuges.jpg", "Fuel", "A handful of sites in the world enrich nearly all of the fuel.", "A cascade of gas centrifuges"),
             band("control-room.jpg", "Operations", "A nuclear plant is a very large machine run by a very small team.", "A reactor control room"),
             band("cherenkov.jpg", "Why it glows", "Blue light from particles moving faster than light does in water.", "Cherenkov glow around a reactor core"),
             band("atr-core.jpg", "Three years", "Time enough to see if the first small reactors are ordered, or only announced.", "A reactor core under water")]
    foot = K.foot(REFS, AS_OF, "Frontier Atom", "atom",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Reactor and project facts are from public sources and are rounded.")
    nf = K.notice("We explain how fission and small reactors work and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Reactors operating, end 2025", "413"), ("Share of world power, 2025", "8.4%"), ("Irish law", "prohibits"), ("HALEU supply", "mostly Russia")]
    body = K.assemble("atom", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
