"""Frontier Orbit: launch, satellites and the space industry. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more
from frontier import sitekit as K
from frontier.components import note
from frontier.scenarios import Scenario
from sites import tech_orbit as TB
from sites import _gen

TITLE = "Frontier Orbit"
AS_OF = "16 October 2026"

LIVE = {"cik": {"RKLB": 1819994, "ASTS": 1780312, "PL": 1836833, "LUNR": 1844452, "RDW": 1819810},
        "aliases": {"RKLB": ["rocket lab"], "ASTS": ["ast spacemobile", "bluebird"], "PL": ["planet labs"], "LUNR": ["intuitive machines"], "RDW": ["redwire"]},
        "arxiv_terms": ["satellite constellation", "lunar lander", "reusable launch vehicle"], "arxiv_cat": "astro-ph.IM"}

REFS = TB.ORBIT_REFS
cite = K.cite_factory(REFS)

SCEN = {
    "RKLB": [Scenario("bear", "Neutron slips again and cash needs grow", 0.35, -0.45, 0.75),
             Scenario("base", "Electron grows and Neutron flies late", 0.40, 0.08, 0.75),
             Scenario("bull", "Neutron flies and wins large launch contracts", 0.25, 0.55, 0.75)],
    "ASTS": [Scenario("bear", "Deployment slips and it must raise more money", 0.45, -0.55, 0.75),
             Scenario("base", "The network grows and service starts slowly", 0.30, 0.00, 0.75),
             Scenario("bull", "Service launches with large carriers and revenue scales", 0.25, 0.60, 0.75)],
    "PL": [Scenario("bear", "Government demand slows", 0.30, -0.35, 0.75),
           Scenario("base", "Revenue grows with the backlog", 0.45, 0.12, 0.75),
           Scenario("bull", "Large defence and commercial contracts convert faster", 0.25, 0.45, 0.75)],
    "LUNR": [Scenario("bear", "A lander fails again and government awards slip", 0.40, -0.45, 0.75),
             Scenario("base", "Revenue grows with the acquisition", 0.35, 0.05, 0.75),
             Scenario("bull", "Lander and network contracts convert to profit", 0.25, 0.50, 0.75)],
    "RDW": [Scenario("bear", "Losses continue and funding tightens", 0.40, -0.45, 0.75),
            Scenario("base", "Revenue grows toward its guidance", 0.35, 0.05, 0.75),
            Scenario("bull", "Contract wins turn into profit", 0.25, 0.45, 0.75)],
}

COMPANIES = [
    {"t": "RKLB", "name": "Rocket Lab", "kind": "Launch and spacecraft",
     "rivals": "SpaceX and other small and medium launch firms",
     "profit": f"Sells launches on Electron and builds spacecraft. 2025 revenue was $601.8 million, with a net loss of $198.2 million and a backlog of $1.85 billion. It flew 21 Electron launches, all successful. Neutron, its larger rocket, slipped to late 2026.{cite(12)}",
     "watch": "Neutron's first flight, backlog conversion, cash.", "rank": "It flew 21 Electron launches in 2025, against SpaceX's 165.",
     "verdict": "A real business with a big bet pending"},
    {"t": "ASTS", "name": "AST SpaceMobile", "kind": "Direct-to-phone satellites",
     "rivals": "Starlink's direct-to-cell service and others",
     "profit": f"Builds BlueBird satellites that connect to ordinary phones. BlueBird 7 reached the wrong orbit on a New Glenn rocket in April 2026 and was to be deorbited.{cite(22)} In May 2026 it was still targeting about 45 satellites in orbit during 2026.{cite(13)}",
     "watch": "Launch cadence, service start, carrier contracts, share sales.", "rank": "Pre-commercial, with agreements with mobile operators.",
     "verdict": "A network still being built"},
    {"t": "PL", "name": "Planet Labs", "kind": "Earth-observation data",
     "rivals": "Other imagery providers",
     "profit": f"Sells imagery and data from its satellites. Fiscal 2026 revenue was $307.7 million, up 26%, with a backlog over $900 million and its first full year of positive adjusted EBITDA and free cash flow. It guides fiscal 2027 revenue of $415 to $440 million.{cite(14)}",
     "watch": "Backlog conversion, government contracts, free cash flow.", "rank": "A company that has reached cash flow break-even.",
     "verdict": "The steadier of the young names"},
    {"t": "LUNR", "name": "Intuitive Machines", "kind": "Lunar landers and space services",
     "rivals": "Other lunar lander companies",
     "profit": f"Builds landers and sells space services to NASA. IM-2 tipped over after landing on 6 March 2025. It completed an $800 million acquisition of Lanteris Space Systems in the first quarter of 2026 and guides 2026 revenue of $900 million to $1 billion.{cite(15)}{cite(16)}",
     "watch": "Next landing, contract awards, integration of the acquisition.", "rank": "A lunar-lander pioneer turning into a larger contractor.",
     "verdict": "Landers with a bigger business behind them"},
    {"t": "RDW", "name": "Redwire", "kind": "Space infrastructure and components",
     "rivals": "Larger aerospace primes",
     "profit": f"Builds spacecraft parts, docking systems and platforms. 2025 revenue was $335.4 million, up 10.3%, with a net loss of $226.6 million and a record backlog of $411.2 million. It guides 2026 revenue of $450 to $500 million.{cite(17)}",
     "watch": "Backlog conversion, losses, liquidity.", "rank": "A growing supplier with large losses.",
     "verdict": "Growing, and still losing money"},
]

LADDER = [("Prototype", "Flown once|or tested"), ("Reliable", "Flies again|and again"), ("Contracts", "Customers sign|and pay"),
          ("Cadence", "Many flights|a year"), ("Positive cash", "Pays for itself"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "friendly"), "CA": (1, 0, "friendly"), "IE": (3, 0, "friendly"), "CN": (9, 1, "friendly")}
NAMES = {"US": "United States", "CA": "Canada", "IE": "Ireland", "CN": "China"}
COUNTRY = {
    "US": {"co": "SpaceX, Rocket Lab, AST SpaceMobile, Planet Labs, Intuitive Machines, Redwire", "gov": "NASA flew Artemis II in April 2026. US government space spending was about $77 billion in 2024", "ctl": "See the references",
           "note": "The home of most listed space companies."},
    "CA": {"co": "Canadian Space Agency", "gov": "Canadian astronaut Jeremy Hansen flew on Artemis II", "ctl": "See the references", "note": "A partner in Artemis."},
    "IE": {"co": "116 Irish companies engaged with ESA in 2024", "gov": "Ireland committed more than 170 million euros to ESA programmes at the November 2025 ministerial", "ctl": "See the references",
           "note": "A small nation expanding its space activity."},
    "CN": {"co": "Chinese launch companies", "gov": "Estimates of China's 2025 orbital launches range from 68 to 92", "ctl": "See the references", "note": "Counts of its launches differ by source."},
}
HYPE = [
    ("5", "Many successful flights", "A rocket or satellite service that has flown or run for years", "SpaceX's 165 launches in 2025", "ok"),
    ("4", "Revenue and a growing backlog", "Customers pay and orders accumulate", "Rocket Lab 1.85 billion dollars, Planet over 900 million", "ok"),
    ("3", "Cash-flow positive", "A space company that pays for itself", "Planet Labs in fiscal 2026", "dis"),
    ("2", "Agreements in principle", "Contracts with mobile operators or agencies", "AST SpaceMobile's operator agreements", "dis"),
    ("1", "A first flight date", "A vehicle on a schedule", "Neutron, now late 2026", "tgt"),
]
SHOVELS = [
    ("Launch", "SpaceX, Rocket Lab", "United States", "SpaceX flew about half of all orbital launches in 2025"),
    ("Earth-observation data", "Planet Labs", "United States", "First full year of positive free cash flow in fiscal 2026"),
    ("Spacecraft parts and docking", "Redwire", "United States", "Record backlog of $411.2 million"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    C = dict(
        slug="orbit", name="Orbit", as_of=AS_OF, live=LIVE, refs=REFS, scen=SCEN, companies=COMPANIES, ladder=LADDER, hype=HYPE, shovels=SHOVELS,
        tiles=TILES, names=NAMES, country=COUNTRY, map_default="IE",
        order=["RKLB", "ASTS", "PL", "LUNR", "RDW", "NVDA"], default=["RKLB", "ASTS", "PL", "LUNR", "RDW"],
        tm_assets=[["RKLB", "Rocket Lab"], ["ASTS", "AST SpaceMobile"], ["PL", "Planet Labs"], ["LUNR", "Intuitive Machines"], ["RDW", "Redwire"], ["NVDA", "Nvidia"]],
        tm_default={"RKLB": px_first("RKLB"), "ASTS": px_first("ASTS"), "PL": px_first("PL"), "LUNR": px_first("LUNR"), "RDW": px_first("RDW"), "NVDA": "2022-10-10"},
        runs_for=("RKLB", "ASTS", "PL", "LUNR", "RDW", "NVDA"),
        mult=[("Nvidia, 2022 to 2024", "NVDA", "ref"), ("Redwire", "RDW", "lay"), ("Planet Labs", "PL", "lay"), ("Intuitive Machines", "LUNR", "quantum"),
              ("Rocket Lab", "RKLB", "quantum"), ("AST SpaceMobile", "ASTS", "quantum")],
        index_groups=[("Launch and satellites", ["RKLB", "ASTS", "PL"], "var(--amber)"), ("Landers and infrastructure", ["LUNR", "RDW"], "var(--teal)")],
        tech=TB.orbit_html(cite),
        data_note="Space economy, launch counts and company results were checked against the sources listed.",
        notice="We explain how the space industry works and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.",
        facts=[("Global space economy 2024", "$613bn"), ("Orbital launches 2025", "about 325"), ("SpaceX launches 2025", "165"), ("Artemis II", "April 2026")],
        bands=[("falcon9-starlink.jpg", "Launch", "A Falcon 9 carrying Starlink satellites leaves Cape Canaveral.", "A Falcon 9 rocket launching from Cape Canaveral"),
               ("artemis2-moon.jpg", "The Moon", "Earth sets over the Moon, photographed by the Artemis II crew.", "Earth setting over the Moon"),
               ("cubesats-iss.jpg", "Small satellites", "A trio of CubeSats leaves the space station.", "CubeSats ejected from the space station"),
               ("iss-array.jpg", "In orbit", "The space station's solar array above Earth's horizon.", "The International Space Station solar array"),
               ("artemis1-launch.jpg", "Three years", "Time enough to see a Moon landing attempt and a new rocket or two.", "NASA's Space Launch System launching on Artemis I")],
        hero=dict(h1="A launch almost <em>every day</em>, and the Moon is back",
                  lead="There were about 325 orbital launches in 2025, a record, and SpaceX flew nearly half. Artemis II flew people around the Moon in April 2026. Here is what is being built in orbit, who is paid, and what is still a target.",
                  img="falcon9-starlink.jpg", art=art_more.hero_reactor(),
                  stats=[(613, "billion dollars: the global space economy in 2024", "$", "bn"), (165, "launches by SpaceX in 2025, nearly half of all orbital launches", "", ""),
                         (lambda r: round(r["RKLB"]["multiple"]), "times Rocket Lab rose from low to high in two years", "", "x"),
                         (252756, "miles from Earth: the distance Artemis II reached, a record", "about ", "")]),
        ch1=dict(sub="Rockets are a delivery service. The money is in what they deliver.",
                 intro=f'''<p>A rocket puts a payload into orbit. The payloads are satellites that sell connectivity, images and data, and spacecraft that go to the Moon. The global space economy was $613 billion in 2024, up 7.8%, with government budgets of about $132 billion of it.{cite(10)} In 2025 there were about 325 orbital launches, a record, and SpaceX flew 165 of them.{cite(11)}</p>
{note("Why it is attractive", "<p>Companies sell connectivity, images and launches to paying customers and governments, in an economy of $613 billion.</p>")}
<p>In April 2026 NASA's Artemis II flew four astronauts around the Moon and back, the first crewed lunar voyage since Apollo 17. It reached about 252,756 miles from Earth.{cite(18)}</p>''',
                 photos=[("falcon9-starlink.jpg", "A Falcon 9 rocket carrying Starlink satellites launching from Cape Canaveral."), ("electron-prefire.jpg", "Technicians integrating NASA's PREFIRE spacecraft with a Rocket Lab Electron rocket."),
                         ("cubesats-iss.jpg", "A trio of CubeSats ejected into Earth orbit from the International Space Station.")],
                 paths_nav="Parts", paths_title="The parts of the business",
                 paths=[("Launch", f"SpaceX flew 165 of about 325 orbital launches in 2025. Rocket Lab flew 21 Electron launches.{cite(11)}{cite(12)}"),
                        ("Satellite services", f"Planet Labs had $307.7 million of revenue in fiscal 2026. AST SpaceMobile targets about 45 BlueBird satellites in orbit in 2026.{cite(14)}{cite(13)}"),
                        ("Lunar landers", f"Intuitive Machines' IM-2 lander tipped over in March 2025.{cite(16)}"),
                        ("Crewed exploration", f"Artemis II flew in April 2026. It did not land on the Moon.{cite(18)}")],
                 limits=[("Launch delays", f"Rocket Lab's Neutron slipped to late 2026 after a tank failed in a test.{cite(12)}"),
                         ("Off-nominal orbits", f"AST SpaceMobile's BlueBird 7 reached the wrong orbit on a New Glenn rocket in April 2026 and was to be deorbited.{cite(22)}"),
                         ("Landing is hard", f"IM-2 tipped over on 6 March 2025, which the company blamed on altimeter signal problems and long shadows.{cite(16)}"),
                         ("Losses", f"Redwire's 2025 net loss was $226.6 million on $335.4 million of revenue.{cite(17)}")],
                 history=[("March 2025", f"Intuitive Machines' IM-2 lander tips over after landing near the Moon's south pole.{cite(16)}", "big"),
                          ("2025", f"About 325 orbital launches, a record. SpaceX flies 165.{cite(11)}", ""),
                          ("November 2025", f"Ireland commits more than 170 million euros to European space programmes.{cite(19)}", ""),
                          ("1 to 10 April 2026", f"Artemis II flies around the Moon and returns.{cite(18)}", "big"),
                          ("April 2026", f"AST SpaceMobile's BlueBird 7 reaches the wrong orbit on a New Glenn rocket.{cite(22)}", ""),
                          ("Late 2026", f"Rocket Lab's Neutron is now planned to fly.{cite(12)}", "fut")],
                 key=("Strong demand, uneven execution", "The space economy is large and growing and reusable rockets work. Many young firms are still losing money and missing dates. The firms with backlogs and cash flow are separating from those without.")),
        ch2=dict(cards=[("What changed", f"Launch cadence hit a record in 2025 and a crewed Moon flyby flew in 2026.{cite(11)}{cite(18)}"),
                        ("What has not", f"Many companies in the sector still report net losses. Neutron, BlueBird deployment and lunar landing all missed or changed targets.{cite(12)}{cite(13)}{cite(16)}"),
                        ("What is new", f"Planet Labs reported its first full year of positive free cash flow, and Intuitive Machines bought a satellite maker for $800 million.{cite(14)}{cite(15)}")],
                 photo=("artemis2-eclipse.jpg", "A solar eclipse photographed by the Artemis II crew on 6 April 2026."),
                 key=("Space is a business, and a rough one", "A few firms have revenue, backlog and cash flow. Most have a plan. The first group is growing. The second group keeps asking for money.")),
        ch3=dict(sub="Our judgement from the figures. Not a forecast.",
                 timeline=[("Now: launch and data", f"Launch cadence is at a record and Earth-observation firms are reaching cash flow.{cite(11)}{cite(14)}", "fut"),
                           ("2026: new rockets and networks", f"Neutron is planned for late 2026 and AST SpaceMobile targets about 45 satellites in orbit.{cite(12)}{cite(13)}", "fut"),
                           ("From 2028: a Moon landing", "NASA's stated goal is to land astronauts on the Moon from 2028.", "fut")],
                 ireland=[("The funding", f"Ireland committed more than 170 million euros to ESA programmes through 2030 at the November 2025 ministerial.{cite(19)}"),
                          ("The firms", f"Irish firms won a record 24 million euros of ESA contracts in 2024, with 116 companies engaged.{cite(20)}"),
                          ("The watch", "Irish suppliers sell into the European space programme. The listed names on this page are mostly American.")],
                 prepare=[("As a citizen", "Expect more space news, and treat a launch date as a target."),
                          ("As a business", "Satellite data and connectivity are the parts of the sector that sell to ordinary firms."),
                          ("As an investor", "Space shares have moved far more than their results. The firms with backlog and cash flow behave differently from those without.")],
                 key=("Cadence first, then the Moon", "Launch and data are working now. New rockets and networks are due next. A Moon landing is later.")),
        ch4=dict(sub="A launch firm, a network builder, a data company, a lander firm and a parts maker.",
                 extra=f'''<article class="card co rv"><h3>The private giant<span>SpaceX, not listed</span></h3>
<dl><dt>Launches</dt><dd>165 orbital launches in 2025, nearly half of the world's.{cite(11)}</dd>
<dt>Starlink</dt><dd>Secondary reports put its subscribers at about 12 million at the end of June 2026.{cite(21)}</dd>
<dt>Use</dt><dd>It cannot be bought directly. Every company below competes with it or buys from it.</dd></dl><span class="verdict">The firm everyone else is measured against</span></article>''',
                 prices_title="Share prices since listing", prices_blurb="Five listed space companies, with Nvidia for scale.",
                 booms_caption="Log scale, from weekly closes, adjusted for splits. Several of these names rose and fell by very large amounts.",
                 ladder_caption="Launch is on the upper rungs. Landers and direct-to-phone networks are lower down.",
                 good=["Launches repeat on schedule.", "Backlog converts to revenue.", "Free cash flow turns positive.", "Customers sign for the next generation."],
                 bad=["A first-flight date that moves again.", "A network that needs more money every year.", "Prices jump on a rival's launch.", "Agreements in principle with no revenue."],
                 map_key='<span><i style="border-color:var(--teal)"></i>space programme or companies</span><span><i style="border-color:var(--violet)"></i>partner</span><span><i style="border-color:var(--red)"></i>none</span>',
                 key=("The firms with backlogs are separating", "Planet Labs and Rocket Lab report revenue and backlog. Others are valued on a network or a rocket still to fly.")),
        ch5=dict(sub="Delays, landings, losses and dependence on one launcher.",
                 cards=[("Delays", f"Neutron slipped to late 2026.{cite(12)}"), ("Landings", f"IM-2 tipped over in March 2025.{cite(16)}"),
                        ("Wrong orbit", f"BlueBird 7 reached an off-nominal orbit in April 2026 and was to be deorbited.{cite(22)}"),
                        ("Losses", f"Rocket Lab lost $198.2 million in 2025. Redwire lost $226.6 million.{cite(12)}{cite(17)}"),
                        ("One launcher", f"SpaceX flew 165 of about 325 orbital launches in 2025.{cite(11)}"),
                        ("Government dependence", f"Government budgets were about $132 billion of the $613 billion space economy in 2024.{cite(10)}")],
                 photo=("iss-array.jpg", "The International Space Station's solar panel array and Earth's horizon."),
                 line="Space is hard and the schedules are optimistic. The firms that win will be those that can fly reliably and keep paying their bills.",
                 key=("A reliability and cash problem", "The physics works. What fails is the schedule and the balance sheet. Look at backlog, cash flow and flights completed, not at renderings.")),
        ch6=dict(n_word="five", expect=[("Likely, about 80%", "More than 300 orbital launches a year. More satellite launches by SpaceX and others. More lunar missions announced."),
                                        ("Even odds, about 50%", "Neutron reaches orbit and Intuitive Machines or a rival lands upright on the Moon."),
                                        ("Unlikely, under 20%", "A crewed landing on the Moon before 2029.")],
                 pull="Space will keep growing as a business. Most of the listed names are still waiting for the part that pays.",
                 why=[("Why we lean that way", "Our scenarios put the chance of each company ending the three years below today's price at {lo} to {hi}. Several of these shares are very volatile."),
                      ("Who is exposed", "Firms that depend on a first flight, a network that is not yet complete or large government awards."),
                      ("If it goes right", "A reusable medium-lift rocket and a working direct-to-phone network would change the economics of the sector."),
                      ("The test", "For any space claim, ask how many flights, how much backlog and how much cash.")],
                 mind="Neutron flying and landing its stage. A lander surviving a landing. A network starting paid service at scale.",
                 key=("More flights, uneven results", "We expect launch to keep growing and the weaker firms to keep struggling. The firms that report backlog and cash flow are better placed than those valued on a plan.")),
    )
    return _gen.build(C, cite)
