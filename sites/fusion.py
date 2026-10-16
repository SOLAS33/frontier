"""Frontier Fusion: fusion power and the milestones that matter. Voice rules: docs/VOICE.md."""
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
    (1, "Fusion Industry Association. The global fusion industry report (annual).", "https://www.fusionindustryassociation.org/"),
    (2, "International Atomic Energy Agency. World Fusion Outlook (annual).", "https://www.iaea.org/publications/search/type/world-fusion-outlook"),
    (3, "ITER Organization. What is ITER?", "https://www.iter.org/"),
    (4, "UK Atomic Energy Authority. STEP Fusion.", "https://www.ukaea.org/"),
    (5, "US Department of Energy. Fusion energy sciences.", "https://www.energy.gov/science/fes/fusion-energy-sciences"),
    (6, "Wendelstein 7-X. Max Planck Institute for Plasma Physics.", "https://www.ipp.mpg.de/w7x"),
    (7, "Helion. Company site and plans.", "https://www.helionenergy.com/"),
    (8, "Lazard. Levelized cost of energy+ (annual).", "https://www.lazard.com/research-insights/levelized-cost-of-energyplus/"),
    (9, "Euratom and Fusion for Energy. Europe's contribution to ITER.", "https://fusionforenergy.europa.eu/"),
]
REFS = REFS + TB.FUSION_REFS + [(14, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/")]
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "BRKR": [Scenario("bear", "Research funding and instrument orders stay weak", 0.30, -0.25, 0.75),
             Scenario("base", "Steady growth in instruments, small gain from fusion magnets", 0.50, 0.10, 0.75),
             Scenario("bull", "Instrument demand recovers and superconductor sales grow", 0.20, 0.35, 0.75)],
    "AMSC": [Scenario("bear", "Grid orders slow and the 2025 rally unwinds", 0.40, -0.40, 0.75),
             Scenario("base", "Grid and Navy sales grow, fusion adds nothing", 0.40, 0.05, 0.75),
             Scenario("bull", "Power-grid demand lifts earnings for years", 0.20, 0.45, 0.75)],
    "LASR": [Scenario("bear", "Defence orders slip and the rally unwinds", 0.40, -0.40, 0.75),
             Scenario("base", "Laser sales grow with defence demand", 0.40, 0.05, 0.75),
             Scenario("bull", "Large defence contracts convert to revenue", 0.20, 0.45, 0.75)],
}

COMPANIES = [
    {"t": "BRKR", "name": "Bruker", "kind": "Scientific instruments and superconducting wire",
     "rivals": "Thermo Fisher, Agilent, Waters, JEOL",
     "profit": "Sell instruments to universities, drug firms and industry. Its superconducting wire unit supplies magnets for MRI, research and fusion machines such as ITER.",
     "watch": "Research budgets, instrument orders, and any large fusion magnet contract.",
     "rank": "A diversified instrument maker. Fusion is a small part of its business.",
     "verdict": "A fusion supplier in name only"},
    {"t": "AMSC", "name": "American Superconductor", "kind": "Grid equipment and ship protection",
     "rivals": "Hitachi Energy, Siemens Energy, GE Vernova and others",
     "profit": "Sell power-grid equipment and Navy products. It was founded on superconducting wire, but those sales are no longer the main earner.",
     "watch": "Grid orders, Navy contracts, and any return to superconducting wire for fusion.",
     "rank": "Its price rose sharply in 2025 on grid demand, not on fusion.",
     "verdict": "A superconductor name without a fusion business"},
    {"t": "LASR", "name": "nLight", "kind": "High-power lasers",
     "rivals": "IPG Photonics, Coherent, Lumentum",
     "profit": "Sell industrial and defence lasers. Fusion designs that use lasers rely on very different, much larger machines.",
     "watch": "Defence contracts, order backlog, margins.",
     "rank": "A laser maker with no disclosed fusion revenue.",
     "verdict": "A laser company, not a fusion one"},
]

LADDER = [("Plasma", "A hot plasma|is held"), ("Gain above 1", "More fusion energy|than heating in"), ("Net power", "A plant sends|power to a grid"),
          ("First plant", "Built, run and|financed"), ("Fleet", "Many alike at|a falling price"),
          ("Cheap power", "Beats gas and wind|with storage"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "IE": (3, 0, "restrictive"), "GB": (4, 0, "friendly"), "FR": (4, 1, "friendly"),
         "DE": (6, 0, "friendly"), "RU": (8, 0, "mixed"), "IN": (8, 2, "mixed"), "CN": (9, 1, "friendly"), "KR": (10, 0, "friendly"),
         "JP": (11, 1, "friendly")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "DE": "Germany", "RU": "Russia",
         "IN": "India", "CN": "China", "KR": "South Korea", "JP": "Japan"}
COUNTRY = {
    "US": {"co": "Commonwealth Fusion Systems, Helion, TAE, Zap, Pacific Fusion; Livermore (NIF) and Princeton labs", "gov": "A federal fusion programme and a milestone-based scheme that pays private firms as they hit targets",
           "ctl": "Fuel, magnets and materials are mostly home or allied supply", "note": "The most private money and the only facility to show gain above 1 at the target."},
    "GB": {"co": "Tokamak Energy, UKAEA, First Light", "gov": "Backs a prototype plant, STEP, at West Burton in Nottinghamshire, with a 2040 target",
           "ctl": "Left the EU's ITER and Euratom arrangements after Brexit", "note": "Ran JET, the machine with the longest-lasting energy record, until it closed in 2023."},
    "FR": {"co": "CEA, ITER Organization, Renaissance Fusion", "gov": "Hosts ITER at Cadarache", "ctl": "EU and ITER rules", "note": "Host of the world's largest fusion project."},
    "DE": {"co": "Proxima Fusion, Marvel Fusion, Focused Energy, Max Planck Institute", "gov": "Committed over two billion euros to fusion to 2029 under a national plan", "ctl": "EU rules",
           "note": "Home of the Wendelstein 7-X stellarator and a growing group of start-ups."},
    "CN": {"co": "China National Nuclear Corporation, ENN, Energy Singularity, Startorus", "gov": "State programme with several experimental tokamaks and a larger burning-plasma device under construction in Hefei", "ctl": "Closed market",
           "note": "Building fast and with a strong state backing. EAST holds long-pulse records."},
    "JP": {"co": "Kyoto Fusioneering, Helical Fusion, QST", "gov": "National strategy to demonstrate power in the 2030s", "ctl": "Follows allied rules", "note": "Runs JT-60SA, the largest tokamak operating today."},
    "KR": {"co": "KFE, Doosan, Samsung C&T", "gov": "Public programme with a plan for a demonstration", "ctl": "Follows allied rules", "note": "Runs KSTAR, which has held 100 million degrees for tens of seconds."},
    "CA": {"co": "General Fusion, Ontario Power Generation, Canadian Nuclear Laboratories", "gov": "Public funds for tritium handling and research", "ctl": "Large tritium holder from its CANDU fleet",
           "note": "One of the few holders of tritium at scale."},
    "RU": {"co": "Rosatom, Kurchatov Institute", "gov": "Member of ITER and runs the T-15MD tokamak", "ctl": "Western sanctions limit cooperation", "note": "A founding partner in ITER with limited contact now."},
    "IN": {"co": "Institute for Plasma Research", "gov": "Member of ITER and runs a small tokamak programme", "ctl": "Trade rules limit some materials", "note": "A partner, not a leader."},
    "IE": {"co": "None building a plant", "gov": "Takes part in European fusion research through the EU's Euratom programme", "ctl": "EU rules",
           "note": "No Irish fusion project. Interest is in future power supply and in suppliers."},
}
HYPE = [
    ("5", "Net power to a grid", "A plant that has sent power out for a year", "None yet", "ok"),
    ("4", "Gain above 1 in the plasma", "More fusion power than heating power", "NIF target gain, laser route", "ok"),
    ("3", "Signed offtake with money behind it", "A buyer commits to pay for power from a plant not yet built", "Google with Commonwealth Fusion Systems, Microsoft with Helion", "dis"),
    ("2", "Funding round or government grant", "Money to build a machine", "Rounds of hundreds of millions", "dis"),
    ("1", "Roadmap or press release", "A target date and a rendering", "'Power on the grid by 2030'", "tgt"),
]
SHOVELS = [
    ("High-temperature superconducting tape", "Faraday Factory Japan, Fujikura, SuperOx, Shanghai Superconductor", "Japan, Russia, China", "Compact tokamaks need hundreds of kilometres of it. Output is small"),
    ("Large magnets and vacuum vessels", "Toshiba, Mitsubishi Heavy Industries, ASG Superconductors", "Japan, Italy", "A handful of firms can build them"),
    ("Tritium", "Ontario Power Generation, Canadian Nuclear Laboratories", "Canada", "A few tens of kilograms exist worldwide. Heavy-water reactors make nearly all of it"),
    ("Lithium-6 for breeding", "State laboratories and a few suppliers", "United States, Russia, China", "Enriching it is an old process that few countries still run"),
    ("Tungsten and special steels", "Mining and metals firms", "China, Austria", "Wall materials have to survive neutrons and heat"),
    ("Pulsed power and lasers", "Specialist suppliers", "US, Europe", "Laser fusion needs lasers far larger than any industrial machine"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["BRKR", "AMSC", "LASR", "NVDA"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["BRKR", "AMSC", "LASR"],
                                     [["BRKR", "Bruker"], ["AMSC", "American Superconductor"], ["LASR", "nLight"], ["NVDA", "Nvidia"]],
                                     {"BRKR": px_first("BRKR"), "AMSC": px_first("AMSC"), "LASR": px_first("LASR"), "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Supply and trade", "note": "Read"}, "IE")
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
                  "Fusion has made energy in the lab for decades and has never run a power station. Here is how close it is, who is paying for it, and why almost none of it can be bought on a stock exchange.",
                  "nif-laser-bay.jpg", art_more.hero_tokamak(),
                  [(150, "million degrees Celsius needed in the plasma, roughly", "about ", ""), (10, "billion dollars raised by private fusion companies, roughly", "about $", "bn"),
                   (4, "times: the most energy a laser shot has returned compared with the energy that reached the target", "about ", "x"),
                   (0, "fusion plants sending power to any grid today", "", "")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Squeezing hydrogen until it fuses, and the reasons it has taken seventy years.", f'''
<p>Fusion joins two light atomic nuclei into a heavier one and releases energy. It is what powers the Sun. On Earth the easiest reaction joins two forms of hydrogen, deuterium and tritium. They make helium and a fast neutron, and about ten million times as much energy per kilogram as burning coal.</p>
{note("Why it is attractive", "<p>The fuel is plentiful. Deuterium comes from seawater and tritium can be made from lithium. A plant gives off no carbon while running and cannot melt down, because the fuel in the chamber at any moment would run for only seconds.</p>")}
<p>The difficulty is that nuclei repel each other. To make them fuse, the fuel has to be heated to over 100 million degrees, which turns it into a plasma, and held away from every wall long enough to burn. Two ways to do it work in the lab: hold it with magnets, or squeeze a small pellet with lasers so fast it fuses before it flies apart.{cite(2)}</p>
{note("The catch", "<p>Getting more energy out of the fuel than went into the heating is only the first step. The plant has to turn that heat into more electricity than the machine uses, survive years of neutron damage and make its own tritium.</p>")}
<div class="fx-photos wide">
{photo("tftr.jpg", caption="The Tokamak Fusion Test Reactor at Princeton, which ran from 1982 to 1997 and was the first to use a half-and-half mixture of deuterium and tritium.")}
{photo("tftr-vessel.jpg", caption="A view inside the vessel of the Tokamak Fusion Test Reactor.")}
{photo("nif-hohlraum.jpg", caption="A hohlraum, the gold cylinder that holds the fuel capsule at the National Ignition Facility. Laser light turns into X-rays inside it and squeezes the capsule.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Approaches" style="margin-top:36px">The two big ideas</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Magnets</h3><p>Hold the plasma in a doughnut-shaped field and heat it for as long as you like. This is the tokamak and the stellarator. ITER is the largest one.{cite(3)}</p></div>
<div class="card rv"><h3>Lasers</h3><p>Fire many laser beams at a pellet. The pellet burns for a billionth of a second. The National Ignition Facility did this and got more fusion energy out than laser energy in.{cite(10)}</p></div>
<div class="card rv"><h3>Pulsed machines</h3><p>Smaller devices that squeeze or collide plasma with an electric pulse. Helion and others are betting that cheap, fast-built machines can win.{cite(7)}</p></div>
<div class="card rv"><h3>New magnets</h3><p>High-temperature superconducting magnets are much stronger than the old kind. Fusion power rises steeply with field strength, so the same output fits in a much smaller machine.{cite(13)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Net energy</h3><p>The laser shot gave 1.5 times the laser energy that reached the target. The lasers drew about a hundred times that from the wall. A power plant needs the whole chain to come out ahead.</p></div>
<div class="card rv"><h3>Tritium</h3><p>A few tens of kilograms exist in the world. A plant has to breed more than it burns. No one has tested that at scale.</p></div>
<div class="card rv"><h3>Materials</h3><p>Fast neutrons damage the walls and turn them radioactive. The waste is much shorter-lived than fission waste, but it is real.</p></div>
<div class="card rv"><h3>Cost</h3><p>ITER's cost has risen several times, and its schedule has slipped by about a decade since it was agreed.{cite(3)}</p></div>
</div>
{TB.fusion_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1950s</div><p>The tokamak is invented in the Soviet Union. Britain and the US start their own fusion programmes.</p></div>
<div class="ev"><div class="yr">1985</div><p>Reagan and Gorbachev agree to build a joint international fusion machine. It becomes ITER.</p></div>
<div class="ev"><div class="yr">1997</div><p>The JET tokamak in Britain makes 16 megawatts of fusion power, about two thirds of the heating power put in.</p></div>
<div class="ev"><div class="yr">2006</div><p>ITER's members sign the agreement to build it in France.</p></div>
<div class="ev big"><div class="yr">2021</div><p>Commonwealth Fusion Systems and MIT test a 20 tesla high-temperature superconducting magnet, the key to smaller machines.</p></div>
<div class="ev big"><div class="yr">December 2022</div><p>The National Ignition Facility gets 3.15 megajoules of fusion energy from 2.05 megajoules of laser energy on the target. Later shots reach higher.</p></div>
<div class="ev"><div class="yr">2023 to 2025</div><p>JET sets a final record and shuts down. EAST and WEST hold plasmas for over 1,000 seconds. Private companies raise large rounds.</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>SPARC aims for the first magnetic machine with gain above 1. See chapter 6.</p></div>
</div>''', K.key_idea("Real physics, unfinished engineering",
        "Fusion works. Machines have made it happen for decades. What has not been shown is a device that returns more energy than it uses "
        "as a whole, for long enough to be a power station. That is an engineering problem, and a hard one."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>A laser experiment showed more energy out than in at the target, and magnets got much stronger. Private money followed.</p></div>
<div class="card rv"><h3>What has not</h3><p>No machine has produced net electricity. The fuel cycle, the wall materials and the cost are all unproven.</p></div>
<div class="card rv"><h3>What is new</h3><p>Companies are promising power from 2028 to the early 2030s, and some buyers have signed up. Most of the dates are targets, not results.</p></div>
</div>
<div class="wide">{photo("nif-laser-bay.jpg", caption="Laser Bay 2 at the National Ignition Facility in California, one of two bays holding the beamlines that fire at a fuel pellet the size of a peppercorn.")}</div>''',
        K.key_idea("Closer than before, and still not there",
                   "Fusion has crossed a scientific line in the lab and has not crossed the engineering line to a power plant. "
                   "Private companies say they will cross it within a decade. Treat the dates as targets."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Test machines first, then pilot plants, then a fleet.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">2026 to 2028: test machines</div><p>SPARC aims for gain above 1 in a magnetic device. Helion aims to show electricity from a pulsed machine. Several others run smaller tests.</p></div>
<div class="ev fut"><div class="yr">2028 to 2032: pilot plants</div><p>The first plants intended to send power to a grid, in the US and the UK, with buyers already named. Few will finish on the first date given.</p></div>
<div class="ev fut"><div class="yr">2030s: ITER and the state programmes</div><p>ITER's deuterium-tritium burn is planned for the late 2030s.{cite(3)} China, Japan, Korea and the UK aim at demonstration plants in the 2030s.{cite(4)}</p></div>
<div class="ev fut"><div class="yr">2040s: a fleet, or not</div><p>The test is whether fusion can be built in numbers at a price near that of other firm power. If it cannot, it stays a research tool.</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The law</h3><p>Fusion is not the same as fission in physics or in risk. Whether Irish rules would treat it differently has not been tested, because no one has proposed a plant.</p></div>
<div class="card rv"><h3>The money</h3><p>Ireland pays into Euratom through the EU budget, which funds Europe's share of ITER.{cite(9)}</p></div>
<div class="card rv"><h3>The demand</h3><p>Data centres used 21% of metered electricity in 2023,{cite(14)} and large buyers are the ones signing the first fusion power contracts elsewhere. See GridWatch for the live Irish grid.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a citizen</h3><p>Do not expect fusion power in Ireland before the 2040s. Expect announcements long before that.</p></div>
<div class="card rv"><h3>As a business</h3><p>Plan electricity supply on gas, wind, solar, storage and possibly fission. Treat a fusion offer as an option to track, not a plan.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Almost all of the money in fusion is in private companies that cannot be bought on an exchange. The listed names here are suppliers with little fusion revenue.</p></div>
</div>''', K.key_idea("Test machines now, power plants later",
        "The next three years are about test machines. Pilot plants come after, and a fleet after that. "
        "Each step is a chance for a date to slip."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Almost no pure plays are listed. The big bets are private, and the listed names are suppliers.", f'''
<p>The Fusion Industry Association counted over fifty fusion companies and close to ten billion dollars of private funding by mid 2025.{cite(1)} Almost none of it can be bought on an exchange. The three listed companies below are suppliers or neighbours. We include them because people ask, and we say plainly how small the link is.</p>
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The private companies<span>Not listed</span></h3>
<dl><dt>Who</dt><dd>Commonwealth Fusion Systems (compact tokamak, with Google and Eni as named buyers), Helion (pulsed machine, with a Microsoft power agreement for 2028), TAE Technologies, Tokamak Energy, Pacific Fusion, Zap Energy, General Fusion, Proxima Fusion and others.{cite(13)}{cite(7)}</dd>
<dt>Money</dt><dd>The largest have each raised hundreds of millions to over a billion dollars from venture funds, energy companies and technology firms.</dd>
<dt>How to follow them</dt><dd>Funding announcements, test results and permits. This site's live layer watches filings and headlines for the listed names only.</dd></dl><span class="verdict">Where the money is, and where you cannot follow it</span></article></div>
{K.prices_block("s-prices", "Share prices since listing", "The three listed names with a loose link to fusion, and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. None of these rises came from fusion revenue.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Laser fusion has reached the second rung at the target. No magnetic machine has. No plant has reached the third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>A magnetic machine shows gain above 1.</li><li>A buyer signs for power with a price and a date.</li><li>Banks lend against a plant without a government guarantee.</li><li>Breeding blankets are tested at scale.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Share prices of unrelated companies jump on fusion headlines.</li><li>Dates that are always about a decade away.</li><li>Gain quoted for the target without the wall-plug cost.</li><li>Agreements to buy power from plants that do not yet exist.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>public programme and private firms</span><span><i style="border-color:var(--violet)"></i>partner in public programmes</span><span><i style="border-color:var(--red)"></i>little activity</span>', "Pick a country. A summary from public sources, so treat the detail as approximate.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Many are private or part of larger groups. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The money is private. The listed names are neighbours",
        "Fusion is funded by venture capital, governments and technology buyers. The three listed names that people link to it earn very little from it. "
        "Their prices have moved on other news."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Gain, fuel, materials, cost and time.", f'''
<div class="cols wide">
<div class="card rv"><h3>Gain across the whole plant</h3><p>A plant must turn heat into electricity, run its magnets or lasers and its pumps, and still have power left. That needs plasma gain far above 1, and most machines are far from it.</p></div>
<div class="card rv"><h3>Tritium supply</h3><p>The fuel cycle only closes if the blanket breeds more tritium than the plasma burns. It has been calculated and not demonstrated.</p></div>
<div class="card rv"><h3>Materials</h3><p>The first wall faces fast neutrons and heat. No material has yet been tested for years under both.</p></div>
<div class="card rv"><h3>Cost</h3><p>Early fusion power is expected to cost more than gas, wind plus storage, or large fission.{cite(8)} It wins only if the machine gets cheap by repetition.</p></div>
<div class="card rv"><h3>Magnets</h3><p>High-temperature superconducting tape is made by a few firms in small amounts. A fleet needs thousands of kilometres of it.</p></div>
<div class="card rv"><h3>Time and money</h3><p>ITER was agreed in 2006 and its start has moved to the 2030s. Private firms are faster, but they spend money fast too.</p></div>
</div>
<div class="fx-photos wide">{photo("tftr-vessel.jpg", caption="Inside the vessel of the Tokamak Fusion Test Reactor. A power plant version has to survive for years of operation, not weeks.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>Fusion has to prove it can be built cheaply, repeatedly and for years. Physics results do not show that. Operating plants do, and none exists. Until one does, claims about price and date are forecasts, and forecasts in this field have been wrong in one direction for fifty years.</p></div></div>''',
        K.key_idea("A materials and plumbing problem as much as physics",
                   "The plasma is the part that has been studied for longest. The walls, the fuel cycle, the magnets and the cost of building many of them "
                   "have barely been tested. Those are where plans usually fail."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 75%</h3><p>More private funding rounds. Additional power-purchase agreements for plants not yet built. New records for plasma duration and temperature in state machines.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>A compact magnetic machine reports plasma gain above 1.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>Any device sends net electricity to a grid before 2029.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "three listed")}
<div class="pull wide">Fusion will probably work. Whether it will be a business in your working life is a different question.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each of the three listed names ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. We do not expect fusion news to drive any of them.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Shareholders who buy these names for fusion. The link is thin, and the prices follow grid, defence and instrument orders.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A working pilot plant would draw in a supply chain of magnets, tape, tritium handling and materials. Some firms in it are not yet listed anywhere.</p></div>
<div class="card rv"><h3>The test</h3><p>For any fusion claim, ask three things: what gain, measured how, and at what energy cost from the wall. Answers to all three are rare.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A magnetic machine reaching gain above 1 on schedule. A breeding blanket tested with real tritium output. A plant financed by banks without a state guarantee.</div>''',
        K.key_idea("Physics is ahead of engineering, and money is ahead of both",
                   "We expect more test results, more funding and more power agreements over the next three years, and no electricity from a fusion plant. "
                   "The listed companies people associate with fusion are only loosely tied to it."), short="Outlook")

    bands = [band("nif-laser-bay.jpg", "Lasers", "192 beams aimed at a pellet the size of a peppercorn.", "A laser bay at the National Ignition Facility"),
             band("tftr.jpg", "Magnets", "A doughnut of magnetic field holds a plasma hotter than the Sun's core.", "A tokamak fusion reactor"),
             band("nif-hohlraum.jpg", "Gold", "The cylinder that turns laser light into X-rays around the fuel.", "A gold hohlraum"),
             band("tftr-vessel.jpg", "The inside", "The wall has to face fast neutrons for years.", "Inside the vessel of a tokamak"),
             band("nif-laser-bay.jpg", "Three years", "Time enough to see if a second machine matches the first.", "A laser bay at the National Ignition Facility")]
    foot = K.foot(REFS, AS_OF, "Frontier Fusion", "fusion",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Fusion results and funding figures are from public sources and are rounded.")
    nf = K.notice("We explain how fusion works and show how the few related listed companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Plasma temperature", "about 150m C"), ("Net-power plants", "none yet"), ("Private funding", "about $10bn"), ("Listed pure plays", "almost none")]
    body = K.assemble("fusion", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
