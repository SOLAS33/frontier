"""Frontier Fusion: fusion power and the milestones that matter. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_fusion as TB

TITLE = "Frontier Fusion"
AS_OF = "16 October 2026"

LIVE = {"cik": {"BRKR": 1109354, "AMSC": 880807, "LASR": 1124796},
        "aliases": {"BRKR": ["bruker"], "AMSC": ["american superconductor", "amsc"], "LASR": ["nlight"]},
        "arxiv_terms": ["tokamak", "stellarator", "inertial confinement fusion"], "arxiv_cat": "physics.plasm-ph"}

REFS = [
    (1, "World Nuclear News (2025). Access to funding remains a major issue for fusion, says industry report (Fusion Industry Association survey).", "https://world-nuclear-news.org/articles/access-to-funding-remains-a-major-issue-for-fusion-says-fia"),
    (2, "ITER Organization. ITER history.", "https://www.iter.org/proj/iterhistory"),
    (3, "Physics World (2024). ITER fusion reactor hit by massive decade-long delay and 5 billion euro price hike.", "https://physicsworld.com/a/iter-fusion-reactor-hit-by-massive-decade-long-delay-and-e5bn-price-hike/"),
    (4, "UK Government (2025). 2.5 billion pounds for world-first prototype fusion energy plant.", "https://www.gov.uk/government/news/25-billion-for-world-first-prototype-fusion-energy-plant"),
    (5, "Clean Energy Wire (2025). German government pledges more than 2 billion euros for nuclear fusion.", "https://www.cleanenergywire.org/news/german-government-pledges-more-eu2-bln-nuclear-fusion"),
    (6, "Commonwealth Fusion Systems (2025). Google and Commonwealth Fusion Systems sign strategic partnership.", "https://cfs.energy/news-and-media/google-and-commonwealth-fusion-systems-sign-strategic-partnership/"),
    (7, "Commonwealth Fusion Systems (2025). Eni and Commonwealth Fusion Systems sign a $1 billion+ power purchase agreement.", "https://cfs.energy/news-and-media/eni-and-commonwealth-fusion-systems-sign-1-billion/"),
    (8, "Helion (2025). Helion secures land and begins building on the site of the world's first fusion power plant.", "https://www.businesswire.com/news/home/20250730326704/en/Helion-Secures-Land-and-Begins-Building-on-the-Site-of-Worlds-First-Fusion-Power-Plant"),
    (9, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/"),
]
REFS = REFS + TB.FUSION_REFS + [
    (26, "ANS Nuclear Newswire (2025). China launches fusion-focused company.", "https://www.ans.org/news/2025-07-30/article-7244/china-launches-fusionfocused-company/"),
    (27, "World Nuclear News. Japan and EU mark first plasma from JT-60SA fusion device.", "https://world-nuclear-news.org/Articles/Japan-and-EU-mark-first-plasma-from-JT-60SA-fusion"),
    (28, "Bruker (2009). BEST receives contract for superconductors from the ITER fusion energy project.", "https://ir.bruker.com/press-releases/press-release-details/2009/Bruker-Energy--Supercon-Technologies-BEST-Receives-36-Million-Contract-for-High-Performance-Superconductors-from-ITER-Fusion-Energy-Project/default.aspx"),
    (29, "AMSC. Fourth quarter and fiscal year 2025 financial results.", "https://ir.amsc.com/news-releases/news-release-details/amsc-reports-fourth-quarter-and-fiscal-year-2025-financial"),
    (30, "nLight. Annual report on Form 10-K for 2025.", "https://www.sec.gov/Archives/edgar/data/1124796/000112479626000012/lasr-20251231.htm"),
    (31, "Physics World (2025). General Fusion lays off staff due to unexpected and urgent financing constraints.", "https://physicsworld.com/a/general-fusion-lays-off-staff-due-to-unexpected-and-urgent-financing-constraints/"),
    (32, "TechCrunch (2025). Nvidia, Google and Bill Gates help Commonwealth Fusion Systems raise $863m.", "https://techcrunch.com/2025/08/28/nvidia-google-and-bill-gates-help-commonwealth-fusion-systems-raise-863m"),
    (34, "Vladimir, M. (2023). REBCO tape industry roundtable: producers and capacity. Fermilab Indico.", "https://indico.fnal.gov/event/61772/attachments/172362/233118/matias%20vladimir.pdf"),
    (35, "ITER Organization. Europe completes niobium-tin strand production.", "https://www.iter.org/node/16817"),
    (33, "Lawrence Livermore National Laboratory. LLNL's breakthrough ignition experiment highlighted in Physical Review Letters.", "https://lasers.llnl.gov/news/llnls-breakthrough-ignition-experiment-highlighted-in-physical-review-letters"),
]

cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "BRKR": [Scenario("bear", "Research funding and instrument orders stay weak", 0.30, -0.25, 0.75),
             Scenario("base", "Steady growth in instruments, small gain from fusion magnets", 0.50, 0.10, 0.75),
             Scenario("bull", "Instrument demand recovers and superconductor sales grow", 0.20, 0.35, 0.75)],
    "AMSC": [Scenario("bear", "Grid orders slow and the 2025 rally unwinds", 0.40, -0.40, 0.75),
             Scenario("base", "Grid and wind sales keep growing, fusion adds nothing", 0.40, 0.05, 0.75),
             Scenario("bull", "Power-grid demand lifts earnings for years", 0.20, 0.45, 0.75)],
    "LASR": [Scenario("bear", "Defence orders slip and the rally unwinds", 0.40, -0.40, 0.75),
             Scenario("base", "Laser sales grow with defence demand", 0.40, 0.05, 0.75),
             Scenario("bull", "Large defence contracts convert to revenue", 0.20, 0.45, 0.75)],
}

COMPANIES = [
    {"t": "BRKR", "name": "Bruker", "kind": "Scientific instruments and superconducting wire",
     "rivals": "Thermo Fisher, Agilent, Waters, JEOL",
     "profit": f"Sell instruments to universities, drug firms and industry. Its superconductor subsidiary, BEST, won a 24.5 million euro contract in 2009 to supply niobium-tin wire for ITER's magnets.{cite(28)} We found no figure for how much of its revenue comes from fusion.",
     "watch": "Research budgets, instrument orders, and any large fusion magnet contract.",
     "rank": "A diversified instrument maker. Fusion is a small part of what it sells.",
     "verdict": "A fusion supplier, with a small fusion share"},
    {"t": "AMSC", "name": "American Superconductor", "kind": "Grid and wind equipment",
     "rivals": "Hitachi Energy, Siemens Energy, GE Vernova and others",
     "profit": f"In its fiscal 2025, ended 31 March 2026, revenue was $299.2 million, about 84% from grid products and 16% from wind.{cite(29)} Its early business was superconducting wire. We found no fusion revenue line.",
     "watch": "Grid orders, Navy ship-protection contracts, and any return to superconducting wire for fusion.",
     "rank": "A grid and wind equipment maker. Its price peaked in September 2025.",
     "verdict": "A superconductor name without a fusion business"},
    {"t": "LASR", "name": "nLight", "kind": "High-power lasers",
     "rivals": "IPG Photonics, Coherent, Lumentum",
     "profit": f"Sell lasers for defence, industry and microfabrication. In 2025, 67% of its $261.3 million revenue came from aerospace and defence.{cite(30)} Its filings describe no fusion customers.",
     "watch": "Defence contracts, order backlog, margins.",
     "rank": "A laser maker with no disclosed fusion revenue.",
     "verdict": "A laser company, not a fusion one"},
]

LADDER = [("Plasma", "A hot plasma|is held"), ("Gain above 1", "More fusion energy|than heating in"), ("Net power", "A plant sends|power to a grid"),
          ("First plant", "Built, run and|financed"), ("Fleet", "Many alike at|a falling price"),
          ("Cheap power", "Beats gas and wind|with storage"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "IE": (3, 0, "restrictive"), "GB": (4, 0, "friendly"), "FR": (4, 1, "friendly"),
         "DE": (6, 0, "friendly"), "RU": (8, 0, "mixed"), "IN": (8, 2, "mixed"), "CN": (9, 1, "friendly"), "KR": (10, 0, "mixed"),
         "JP": (11, 1, "friendly")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "DE": "Germany", "RU": "Russia",
         "IN": "India", "CN": "China", "KR": "South Korea", "JP": "Japan"}
COUNTRY = {
    "US": {"co": "Commonwealth Fusion Systems, Helion, Pacific Fusion, Zap Energy; Lawrence Livermore (NIF)", "gov": "NIF at Livermore achieved ignition in December 2022 and a target gain above 4 in April 2025",
           "ctl": "See the references", "note": "The most private money and the only facility to show gain above 1 at the target."},
    "GB": {"co": "Tokamak Energy, UKAEA", "gov": "A 2.5 billion pound fusion commitment, with the STEP prototype planned at West Burton in Nottinghamshire and first operations targeted for 2040", "ctl": "See the references",
           "note": "Ran JET, which set the 69 MJ energy record, until it entered decommissioning in December 2023."},
    "FR": {"co": "CEA, ITER Organization", "gov": "Hosts ITER at Cadarache. WEST held a plasma for over 1,300 seconds in 2025", "ctl": "See the references", "note": "Host of the largest fusion project being built."},
    "DE": {"co": "Proxima Fusion, Marvel Fusion, Max Planck Institute", "gov": "An October 2025 action plan commits more than 2 billion euros to 2029", "ctl": "See the references",
           "note": "Home of the Wendelstein 7-X stellarator."},
    "CN": {"co": "China National Nuclear Corporation, China Fusion Energy Co.", "gov": "EAST held a 1,066 second plasma in 2025. BEST, in Hefei, is due for completion by end of 2027. A state fusion company was set up in 2025 with 15 billion yuan of registered capital", "ctl": "See the references",
           "note": "Building fast with state backing."},
    "JP": {"co": "QST, Kyoto Fusioneering", "gov": "JT-60SA, built with Europe, was inaugurated in December 2023 and is described as the world's largest operating superconducting tokamak", "ctl": "See the references", "note": "A partner of Europe in the JT-60SA project."},
    "KR": {"co": "Korean research institutes", "gov": "A member of ITER", "ctl": "See the references", "note": "ITER member since 2003."},
    "CA": {"co": "General Fusion (British Columbia)", "gov": "General Fusion cut about a quarter of its staff in May 2025 and raised 22 million dollars in August 2025", "ctl": "CANDU reactors are a main source of tritium",
           "note": "A fusion start-up that has struggled to fund itself, and a tritium source."},
    "RU": {"co": "Russian research institutes", "gov": "A member of ITER", "ctl": "See the references", "note": "ITER member."},
    "IN": {"co": "Indian research institutes", "gov": "A member of ITER since 2005", "ctl": "See the references", "note": "ITER member."},
    "IE": {"co": "None found building a fusion plant", "gov": "Data centres used 21% of metered electricity in 2023", "ctl": "See the references",
           "note": "The interest is in future power supply."},
}
HYPE = [
    ("5", "Net power to a grid", "A plant that has sent power out for a year", "None yet", "ok"),
    ("4", "Gain above 1 in the plasma", "More fusion power than heating power", "NIF target gain, laser route", "ok"),
    ("3", "Signed offtake with money behind it", "A buyer commits to pay for power from a plant not yet built", "Google and Eni with Commonwealth Fusion Systems", "dis"),
    ("2", "Funding round or government grant", "Money to build a machine", "Helion 425 million dollars, Pacific Fusion 900 million", "dis"),
    ("1", "Roadmap or press release", "A target date and a rendering", "A plant by a given year", "tgt"),
]
SHOVELS = [
    ("High-temperature superconducting tape", "SuperOx, Fujikura, Shanghai Superconductor", "Russia and Japan, Japan, China", "A 2023 industry roundtable listed fusion as the biggest current demand" + cite(34)),
    ("Niobium-tin wire for large magnets", "Bruker EAS, Oxford Superconducting Technology", "Germany, UK", "Together they made Europe's share of ITER's toroidal field strand" + cite(35)),
    ("Tritium", "Canadian Nuclear Laboratories, Ontario Power Generation", "Canada, South Korea", "CANDU heavy-water reactors in Canada and South Korea are the main commercial source" + cite(22)),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["BRKR", "AMSC", "LASR", "NVDA"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["BRKR", "AMSC", "LASR"],
                                     [["BRKR", "Bruker"], ["AMSC", "American Superconductor"], ["LASR", "nLight"], ["NVDA", "Nvidia"]],
                                     {"BRKR": px_first("BRKR"), "AMSC": px_first("AMSC"), "LASR": px_first("LASR"), "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Source", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("BRKR", "AMSC", "LASR", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Bruker", f"from {runs['BRKR']['from']}", runs["BRKR"]["multiple"], "lay"),
            ("nLight", f"from {runs['LASR']['from']}", runs["LASR"]["multiple"], "quantum"),
            ("American Superconductor", f"from {runs['AMSC']['from']}", runs["AMSC"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Superconductor and instrument names", ["BRKR", "AMSC"], "var(--amber)"), ("Laser maker", ["LASR"], "var(--teal)")])

    hero = K.hero("Frontier / Fusion", "The power source that is always <em>thirty years away</em>",
                  "Fusion has made energy in the lab and has never run a power station. Here is how close it is, who is paying for it, and why almost none of it can be bought on a stock exchange.",
                  "nif-laser-bay.jpg", art_more.hero_tokamak(),
                  [(150, "million degrees Celsius needed in the plasma", "about ", ""), (53, "private fusion companies had raised about $9.8 billion between them by mid 2025", "", ""),
                   (4, "the most energy a NIF shot has returned, as a multiple of the laser energy on the target (April 2025)", "over ", "x"),
                   (0, "fusion plants sending power to any grid today", "", "")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Squeezing hydrogen until it fuses, and the reasons it is taking so long.", f'''
<p>Fusion joins two light atomic nuclei into a heavier one and releases energy. It is what powers the Sun. On Earth the easiest reaction joins two forms of hydrogen, deuterium and tritium. They make helium and a fast neutron, and 17.6 MeV of energy per reaction.{cite(21)}</p>
{note("Why it is attractive", f"<p>ITER lists the advantages: no greenhouse gases while running, deuterium from water and tritium bred from lithium, no possible meltdown because the fuel in the vessel at any moment lasts only seconds, and no long-lived high-activity waste.{cite(19)}</p>")}
<p>The difficulty is that nuclei repel each other. To make them fuse, the fuel has to be heated to about 150 million degrees, which turns it into a plasma, and held away from every wall long enough to burn.{cite(19)} Two ways to do it work in the lab: hold the plasma with magnets, or compress a small fuel capsule so fast that it fuses before it flies apart.</p>
{note("The catch", f"<p>Getting more energy out of the fuel than went into the target is only the first step. NIF's lasers use about 100 times more energy than the laser light they deliver.{cite(33)} A plant has to turn heat into more electricity than the machine uses, survive neutron damage and make its own tritium.</p>")}
<div class="fx-photos wide">
{photo("tftr.jpg", caption="The Tokamak Fusion Test Reactor at Princeton. It made its first deuterium-tritium shots in December 1993 and passed 10 megawatts of fusion power in 1994.")}
{photo("tftr-vessel.jpg", caption="A view inside the vessel of the Tokamak Fusion Test Reactor.")}
{photo("nif-hohlraum.jpg", caption="A hohlraum, the gold cylinder that holds the fuel capsule at the National Ignition Facility. Laser light turns into X-rays inside it and squeezes the capsule.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Approaches" style="margin-top:36px">The big ideas</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Magnets</h3><p>Hold the plasma in a doughnut-shaped field and heat it for as long as you like. This is the tokamak and the stellarator. ITER is a seven-member international project building a large tokamak in southern France.{cite(2)}</p></div>
<div class="card rv"><h3>Lasers</h3><p>NIF fires 192 laser beams at a target about the size of a pencil eraser. In December 2022 it got 3.15 MJ of fusion energy from 2.05 MJ of laser energy on the target.{cite(10)}{cite(11)}</p></div>
<div class="card rv"><h3>Pulsed machines</h3><p>Helion collides and compresses plasma rings with magnets and says it recovers the energy as electric current directly. Pacific Fusion compresses a target with an electric pulse.{cite(23)}{cite(24)}</p></div>
<div class="card rv"><h3>New magnets</h3><p>In September 2021 Commonwealth Fusion Systems and MIT took a large high-temperature superconducting magnet to a field of 20 tesla.{cite(16)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Net energy</h3><p>A target gain above 1 does not mean net energy for a power plant, because the laser facility uses about 100 times more energy than the light it delivers.{cite(33)}</p></div>
<div class="card rv"><h3>Tritium</h3><p>Estimates of the world's stock run from about 20 to 30 kg, mostly from CANDU reactors. A plant has to breed more than it burns, and that has not been shown at scale.{cite(22)}</p></div>
<div class="card rv"><h3>Materials</h3><p>The neutrons activate the wall. ITER expects the parts to be reusable or recyclable within about 100 years.{cite(19)}</p></div>
<div class="card rv"><h3>Cost and time</h3><p>In 2024 ITER moved the start of research operation to 2034 and the start of deuterium-tritium operation to 2039, with about 5 billion euros of extra cost.{cite(3)}</p></div>
</div>
{TB.fusion_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1985</div><p>At the Geneva summit, Soviet leader Gorbachev proposes a joint international fusion project to US President Reagan. It becomes ITER.{cite(2)}</p></div>
<div class="ev"><div class="yr">1993 to 1994</div><p>TFTR at Princeton makes its first deuterium-tritium shots and passes 10 MW of fusion power.{cite(14)}</p></div>
<div class="ev"><div class="yr">1997</div><p>JET in Britain makes 16 MW of fusion power, a peak that still stands.{cite(14)}</p></div>
<div class="ev"><div class="yr">2006</div><p>ITER's members sign the agreement to build it in France.{cite(2)}</p></div>
<div class="ev big"><div class="yr">2021</div><p>Commonwealth Fusion Systems and MIT test a 20 tesla high-temperature superconducting magnet.{cite(16)}</p></div>
<div class="ev big"><div class="yr">5 December 2022</div><p>The National Ignition Facility gets 3.15 megajoules of fusion energy from 2.05 megajoules of laser energy on the target.{cite(10)}</p></div>
<div class="ev"><div class="yr">2023 to 2025</div><p>JET makes a 69 megajoule record and goes into decommissioning.{cite(13)} EAST and WEST hold plasmas for over 1,000 seconds.{cite(18)} NIF reaches a gain above 4.{cite(12)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>Commonwealth Fusion Systems targets gain above 1 in SPARC in 2027.{cite(15)} See chapter 6.</p></div>
</div>''', K.key_idea("Real physics, unfinished engineering",
        "Fusion works in the lab. A laser shot has returned more energy than reached its target. No device has produced net electricity "
        "from the whole plant. Showing that is an engineering problem, and a hard one."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>A laser experiment returned more energy than reached its target, and high-temperature magnets reached 20 tesla. Private money followed.{cite(1)}</p></div>
<div class="card rv"><h3>What has not</h3><p>No machine has produced net electricity. The fuel cycle, the wall materials and the cost are all unproven.</p></div>
<div class="card rv"><h3>What is new</h3><p>Companies have signed power agreements for plants that do not exist yet. Google and Eni with Commonwealth Fusion Systems, and Microsoft with Helion.{cite(6)}{cite(7)}{cite(8)}</p></div>
</div>
<div class="wide">{photo("nif-laser-bay.jpg", caption="Laser Bay 2 at the National Ignition Facility in California, one of two bays holding the beamlines that fire at a target the size of a pencil eraser.")}</div>''',
        K.key_idea("Closer than before, and still not there",
                   "Fusion has crossed a scientific line in the lab and has not crossed the engineering line to a power plant. "
                   "Private companies give dates in the 2020s and 2030s. Treat the dates as targets."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Test machines first, then pilot plants, then a fleet.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">2026 to 2028: test machines</div><p>SPARC is aimed at gain above 1 in 2027.{cite(15)} China's BEST, in Hefei, is due for completion by the end of 2027.{cite(26)} Helion says Polaris is already demonstrating electricity from fusion, which is a company claim.{cite(23)}</p></div>
<div class="ev fut"><div class="yr">About 2028 to the early 2030s: pilot plants</div><p>Helion's Orion plant is planned to start operations in 2028 for Microsoft. It began building in July 2025.{cite(8)} Commonwealth Fusion Systems plans ARC, a 400 MW plant in Virginia, for the early 2030s, with Google and Eni as buyers.{cite(6)}{cite(7)}</p></div>
<div class="ev fut"><div class="yr">2030s: ITER and state programmes</div><p>ITER plans deuterium-tritium operation from 2039.{cite(3)} The UK's STEP prototype in Nottinghamshire targets first operations in 2040.{cite(4)} Germany has committed over 2 billion euros to 2029 with the aim of the first fusion power plant in Germany.{cite(5)}</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The demand</h3><p>Data centres used 21% of Ireland's metered electricity in 2023, up from 5% in 2015.{cite(9)}</p></div>
<div class="card rv"><h3>The timing</h3><p>On the builders' own dates the first fusion plants send power out in 2028 at the earliest, in the United States. Irish supply decisions this decade cannot rely on them.</p></div>
<div class="card rv"><h3>The live picture</h3><p>See GridWatch for the live state of the Irish grid.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a citizen</h3><p>Expect announcements long before electricity. A power agreement is a promise to buy, not a plant.</p></div>
<div class="card rv"><h3>As a business</h3><p>Plan electricity supply on sources that exist now. Treat a fusion offer as an option to track.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Almost all of the money in fusion is in private companies that cannot be bought on an exchange. The listed names here sell to other markets.</p></div>
</div>''', K.key_idea("Test machines now, power plants later",
        "The next three years are about test machines. Pilot plants come after. Each step is a chance for a date to slip."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Almost no pure plays are listed. The big bets are private, and the listed names are suppliers.", f'''
<p>The Fusion Industry Association's 2025 survey counted 53 companies that had raised $9.766 billion in total, with $2.64 billion raised in the 12 months to July 2025.{cite(1)} Almost none of that can be bought on an exchange. The three listed companies below are suppliers or neighbours. We include them because people ask, and we say plainly how small the link is.</p>
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The private companies<span>Not listed</span></h3>
<dl><dt>Commonwealth Fusion Systems</dt><dd>A compact tokamak, SPARC, under construction in Massachusetts.{cite(15)} It raised $863 million in 2025.{cite(32)} Google agreed to buy 200 MW from its ARC plant and Eni signed an agreement worth more than $1 billion.{cite(6)}{cite(7)}</dd>
<dt>Helion</dt><dd>A pulsed machine. It raised $425 million in January 2025 and began building its Orion plant in Washington state in July 2025.{cite(8)}{cite(1)}</dd>
<dt>Pacific Fusion</dt><dd>Raised a $900 million Series A.{cite(1)}</dd>
<dt>General Fusion</dt><dd>Cut about a quarter of its staff in May 2025 and raised $22 million in August 2025.{cite(31)}</dd>
<dt>How to follow them</dt><dd>Funding announcements, test results and permits. This site's live layer watches filings and headlines for the listed names only.</dd></dl><span class="verdict">Where the money is, and where you cannot follow it</span></article></div>
{K.prices_block("s-prices", "Share prices since listing", "The three listed names with a loose link to fusion, and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. None of these rises came from fusion revenue.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Laser fusion has reached the second rung at the target. No magnetic machine has. No plant has reached the third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>A magnetic machine shows gain above 1.</li><li>A buyer signs for power with a price and a date.</li><li>Banks lend against a plant without a government guarantee.</li><li>Breeding blankets are tested at scale.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Share prices of unrelated companies jump on fusion headlines.</li><li>Gain quoted for the target without the cost of running the laser.</li><li>Agreements to buy power from plants that do not yet exist.</li><li>Dates that move back a year at a time.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>public programme and private firms</span><span><i style="border-color:var(--violet)"></i>partner in public programmes</span><span><i style="border-color:var(--red)"></i>no fusion plant found</span>', "Pick a country. A summary from the cited public sources.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Many are private or part of larger groups. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The money is private. The listed names are neighbours",
        "Fusion is funded by venture capital, governments and technology buyers. The three listed names that people link to it earn little or nothing from it. "
        "Their prices have moved on other news."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Gain, fuel, materials, cost and time.", f'''
<div class="cols wide">
<div class="card rv"><h3>Gain across the whole plant</h3><p>A plant must turn heat into electricity, run its magnets or lasers and still have power left. NIF's laser facility uses about 100 times more energy than the light it delivers.{cite(33)}</p></div>
<div class="card rv"><h3>Tritium supply</h3><p>The fuel cycle only closes if the blanket breeds more tritium than the plasma burns. Estimates of today's stock run from 20 to 30 kg.{cite(22)}</p></div>
<div class="card rv"><h3>Materials</h3><p>The first wall faces fast neutrons and heat. ITER and the pilot plants are the first tests of how long parts last.{cite(19)}</p></div>
<div class="card rv"><h3>Funding</h3><p>General Fusion cut about a quarter of its staff in May 2025 after what it called an urgent financing constraint.{cite(31)}</p></div>
<div class="card rv"><h3>Magnets</h3><p>High-temperature superconducting tape is made by a few firms, and fusion is the main driver of new demand.</p></div>
<div class="card rv"><h3>Time</h3><p>ITER's 2024 baseline moved the start of research operation to 2034 and deuterium-tritium operation to 2039.{cite(3)}</p></div>
</div>
<div class="fx-photos wide">{photo("tftr-vessel.jpg", caption="Inside the vessel of the Tokamak Fusion Test Reactor. A power plant version has to survive years of operation, not weeks.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>Fusion has to prove it can be built repeatedly and run for years. Physics results do not show that. Operating plants do, and none exists. Until one does, claims about price and date are forecasts.</p></div></div>''',
        K.key_idea("A materials and plumbing problem as much as physics",
                   "The plasma is the part that has been studied for longest. The walls, the fuel cycle, the magnets and the cost of building many of them "
                   "have barely been tested. Those are where plans usually fail."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 75%</h3><p>More private funding rounds. More power-purchase agreements for plants not yet built. New duration records in state machines.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>A compact magnetic machine reports plasma gain above 1.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>Any device sends net electricity to a grid before 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "three listed")}
<div class="pull wide">Fusion will probably work. Whether it will be a business in your working life is a different question.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each of the three listed names ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. We do not expect fusion news to drive any of them.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Shareholders who buy these names for fusion. The link is thin, and the prices follow grid, defence and instrument orders.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A working pilot plant would draw in a supply chain of magnets, tape, tritium handling and materials. Some firms in it are not listed anywhere.</p></div>
<div class="card rv"><h3>The test</h3><p>For any fusion claim, ask three things: what gain, measured how, and at what energy cost from the wall.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A magnetic machine reaching gain above 1 on schedule. A breeding blanket tested with real tritium output. A plant financed by banks without a state guarantee.</div>''',
        K.key_idea("Physics is ahead of engineering, and money is ahead of both",
                   "We expect more test results, more funding and more power agreements over the next three years, and no electricity from a fusion plant. "
                   "The listed companies people associate with fusion are only loosely tied to it."), short="Outlook")

    bands = [band("nif-laser-bay.jpg", "Lasers", "192 beams aimed at a target the size of a pencil eraser.", "A laser bay at the National Ignition Facility"),
             band("tftr.jpg", "Magnets", "A doughnut of magnetic field holds a plasma hotter than the Sun's core.", "A tokamak fusion reactor"),
             band("nif-hohlraum.jpg", "Gold", "The cylinder that turns laser light into X-rays around the fuel.", "A gold hohlraum"),
             band("tftr-vessel.jpg", "The inside", "The wall has to face fast neutrons for years.", "Inside the vessel of a tokamak"),
             band("nif-laser-bay.jpg", "Three years", "Time enough to see if a second machine matches the first.", "A laser bay at the National Ignition Facility")]
    foot = K.foot(REFS, AS_OF, "Frontier Fusion", "fusion",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Fusion results and funding figures were checked against the sources listed and are rounded. Where sources disagreed the text says so.")
    nf = K.notice("We explain how fusion works and show how the few related listed companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Plasma temperature", "about 150m C"), ("Net-power plants", "none yet"), ("Private funding to mid 2025", "about $9.8bn"), ("Listed pure plays", "almost none")]
    body = K.assemble("fusion", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
