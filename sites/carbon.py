"""Frontier Carbon: graphene, carbon nanotubes and battery graphite. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more
from frontier import sitekit as K
from frontier.components import note
from frontier.scenarios import Scenario
from sites import tech_carbon as TB
from sites import _gen

TITLE = "Frontier Carbon"
AS_OF = "16 October 2026"

LIVE = {"cik": {"NVX": 1859795, "WWR": 839470, "NMG": 1649752},
        "aliases": {"NVX": ["novonix"], "WWR": ["westwater"], "NMG": ["nouveau monde", "nmg"]},
        "arxiv_terms": ["graphene", "carbon nanotube", "graphite anode"], "arxiv_cat": "cond-mat.mtrl-sci"}

REFS = TB.CARBON_REFS
cite = K.cite_factory(REFS)

SCEN = {
    "NVX": [Scenario("bear", "Funding runs short and production is delayed", 0.45, -0.50, 0.75),
            Scenario("base", "Panasonic and PowerCo volumes start slowly", 0.35, 0.00, 0.75),
            Scenario("bull", "Production ramps and new customers sign", 0.20, 0.55, 0.75)],
    "WWR": [Scenario("bear", "Financing is not secured and the plant stalls", 0.50, -0.55, 0.75),
            Scenario("base", "Financing arrives late and output starts slowly", 0.30, 0.00, 0.75),
            Scenario("bull", "Funding closes and a new offtaker signs", 0.20, 0.60, 0.75)],
    "NMG": [Scenario("bear", "The plant decision slips and financing tightens", 0.40, -0.45, 0.75),
            Scenario("base", "The mine ramps and the plant decision comes late", 0.35, 0.05, 0.75),
            Scenario("bull", "The plant is financed and built on time", 0.25, 0.55, 0.75)],
}

COMPANIES = [
    {"t": "NVX", "name": "Novonix", "kind": "Synthetic graphite anode material",
     "rivals": "Chinese anode makers, which supplied almost 96% of synthetic graphite anode material",
     "profit": f"Makes synthetic graphite in Chattanooga, Tennessee. At the end of 2025 it had $79.9 million of cash and had claimed $42.3 million of a $100 million US Department of Energy grant. It said more funding would be needed.{cite(18)} A supply agreement with a Stellantis subsidiary was ended in November 2025.",
     "watch": "Production for Panasonic and PowerCo, funding, new customers.", "rank": "A US maker of synthetic graphite, still ramping.",
     "verdict": "A real plant with a funding question"},
    {"t": "WWR", "name": "Westwater Resources", "kind": "Natural graphite processing",
     "rivals": "Chinese anode makers",
     "profit": f"Building the Kellyton graphite plant in Alabama. SK On ended its procurement agreement on 31 March 2026. The company says it can start production about 12 months after the remaining financing is secured.{cite(19)}",
     "watch": "Financing, a replacement offtaker, qualification samples.", "rank": "A plant under construction without full funding.",
     "verdict": "Built in part, not yet funded"},
    {"t": "NMG", "name": "Nouveau Monde Graphite", "kind": "Graphite mine and anode plant",
     "rivals": "Chinese graphite producers",
     "profit": f"Plans a mine at Matawinie in Quebec and an anode plant at Becancour. In April 2026 it announced C$213 million of equity from the Canada Growth Fund, Investissement Quebec and Eni. Panasonic Energy has a binding offtake for 13,000 tonnes a year of anode material. It targets a final investment decision on the plant in the second half of 2026.{cite(20)}{cite(21)}",
     "watch": "The plant decision, remaining financing, offtake terms.", "rank": "A mine funded in April 2026 and a plant still awaiting a decision.",
     "verdict": "Funded for the mine, not yet for the plant"},
]

LADDER = [("Lab sample", "Made in a|laboratory"), ("Pilot plant", "Small plant|runs"), ("Qualified", "A customer|approves it"),
          ("Offtake", "A binding order|with a price"), ("Full plant", "Built and|running"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "friendly"), "US": (1, 1, "friendly"), "IE": (3, 0, "friendly"), "GB": (4, 0, "friendly"), "CN": (9, 1, "restrictive"),
         "KR": (10, 0, "friendly"), "AU": (10, 2, "friendly")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "CN": "China", "KR": "South Korea", "AU": "Australia"}
COUNTRY = {
    "CN": {"co": "Chinese anode makers", "gov": "Produced about 70% of the world's natural flake graphite in 2022 and almost 96% of synthetic graphite anode material", "ctl": "Export licences required for certain graphite from 1 December 2023", "note": "The centre of the supply chain."},
    "US": {"co": "Novonix, Westwater Resources", "gov": "Commerce set a 93.5% preliminary anti-dumping rate on Chinese anode graphite in July 2025", "ctl": "Duties on Chinese graphite", "note": "Using trade rules to open a market for local graphite."},
    "CA": {"co": "Nouveau Monde Graphite", "gov": "The Canada Growth Fund and Investissement Quebec are investing in the Matawinie mine", "ctl": "See the references", "note": "A mine and a plant planned in Quebec."},
    "KR": {"co": "LG Chem", "gov": "LG Chem planned to reach 6,100 tonnes a year of carbon nanotube capacity by early 2025", "ctl": "See the references", "note": "A large nanotube maker."},
    "GB": {"co": "University of Manchester", "gov": "Graphene was first isolated at Manchester, with a Nobel Prize in 2010", "ctl": "See the references", "note": "Where graphene began."},
    "IE": {"co": "AMBER at Trinity College Dublin", "gov": "AMBER researchers developed a mixing method to make defect-free graphene in bulk, reported in 2014", "ctl": "See the references", "note": "A leading Irish graphene research centre."},
    "AU": {"co": "Novonix", "gov": "Novonix is an Australian-listed company that builds its plant in the US", "ctl": "See the references", "note": "Where Novonix started."},
}
HYPE = [
    ("5", "Full-scale production with customers", "A plant runs at design capacity and sells", "Chinese graphite supply", "ok"),
    ("4", "Binding offtake and funding", "A customer signs and money is committed", "Nouveau Monde's Panasonic offtake and C$213 million", "ok"),
    ("3", "Plant under construction", "A plant is built in part", "Westwater's Kellyton plant, Novonix's Chattanooga plant", "dis"),
    ("2", "Grant or conditional loan", "A government offers money", "US Department of Energy grant to Novonix", "dis"),
    ("1", "A material that will change everything", "A lab property with no product", "Early graphene claims", "tgt"),
]
SHOVELS = [
    ("Natural flake graphite", "Chinese producers, Nouveau Monde (planned)", "China, Canada", "China produced about 70% of the world's natural flake graphite in 2022"),
    ("Synthetic graphite anode material", "Chinese anode makers, Novonix", "China, United States", "China supplied almost 96% of it"),
    ("Carbon nanotubes", "LG Chem", "South Korea", "A conductive additive in lithium-ion batteries"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    C = dict(
        slug="carbon", name="Carbon", as_of=AS_OF, live=LIVE, refs=REFS, scen=SCEN, companies=COMPANIES, ladder=LADDER, hype=HYPE, shovels=SHOVELS,
        tiles=TILES, names=NAMES, country=COUNTRY, map_default="IE",
        order=["NVX", "WWR", "NMG", "ALB", "NVDA"], default=["NVX", "WWR", "NMG"],
        tm_assets=[["NVX", "Novonix"], ["WWR", "Westwater Resources"], ["NMG", "Nouveau Monde Graphite"], ["ALB", "Albemarle"], ["NVDA", "Nvidia"]],
        tm_default={"NVX": px_first("NVX"), "WWR": "2016-01-04", "NMG": px_first("NMG"), "ALB": "2016-01-04", "NVDA": "2022-10-10"},
        runs_for=("NVX", "WWR", "NMG", "ALB", "NVDA"),
        mult=[("Nvidia, 2022 to 2024", "NVDA", "ref"), ("Albemarle", "ALB", "lay"), ("Westwater Resources", "WWR", "quantum"), ("Nouveau Monde", "NMG", "quantum"), ("Novonix", "NVX", "quantum")],
        index_groups=[("Graphite names", ["NVX", "WWR", "NMG"], "var(--amber)"), ("Lithium reference", ["ALB"], "var(--teal)")],
        tech=TB.carbon_html(cite),
        data_note="Company figures, trade rules and research history were checked against the sources listed.",
        notice="We explain graphene, nanotubes and battery graphite and show how the few listed companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.",
        facts=[("Graphene Flagship", "1bn euros, 2013 to 2023"), ("China synthetic anode share", "almost 96%"), ("US duty on Chinese anode graphite", "93.5%"), ("Graphene Nobel Prize", "2010")],
        bands=[("graphene-stm.jpg", "The sheet", "A section of graphene seen with a scanning tunnelling microscope.", "A graphene sheet under a microscope"),
               ("graphite-pebble.jpg", "The black stuff", "A graphite pebble from a pebble-bed reactor.", "A graphite pebble"),
               ("nist-nanotube-chips.jpg", "Nanotubes", "Custom chips coated with carbon nanotubes.", "Chips coated with carbon nanotubes"),
               ("acs3-sail.jpg", "Composites", "NASA's Advanced Composite Solar Sail System.", "NASA's Advanced Composite Solar Sail System spacecraft"),
               ("sandia-electrode.jpg", "The electrode", "A researcher holds an electrode.", "A Sandia researcher holding a battery electrode")],
        hero=dict(h1="The wonder material, and the <em>plain black powder</em> that matters more",
                  lead="Graphene won a Nobel Prize in 2010 and has taken longer to reach products than its backers hoped. Graphite, the ordinary carbon in battery anodes, is where supply is tight and governments are acting. Here is what is real, who is paid, and what is still a lab result.",
                  img="nist-nanotube-chips.jpg", art=art_more.hero_cells(),
                  stats=[(1, "billion euros: the Graphene Flagship's ten-year budget, 2013 to 2023", "", " bn euros"), (96, "per cent of synthetic graphite anode material came from China, according to one account", "almost ", "%"),
                         (100, "million dollars: the US Department of Energy grant to Novonix, of which $42.3 million had been claimed by the end of 2025", "$", "m"),
                         (2010, "the year graphene's discoverers won the Nobel Prize in Physics", "", "")]),
        ch1=dict(sub="A single layer of atoms, and the powder in every battery.",
                 intro=f'''<p>Carbon comes in many forms. Graphene is a single layer of carbon atoms in a honeycomb, first isolated at the University of Manchester, a feat that won a Nobel Prize in 2010.{cite(13)} Carbon nanotubes are rolled-up sheets of it. Graphite is stacked layers, and is used for battery anodes.</p>
{note("Why it is attractive", "<p>Graphene is thin, strong and conducts well. Graphite anodes are in the batteries that power cars and grids, and governments now treat their supply as strategic.</p>")}
<p>Europe set up the Graphene Flagship in 2013 with a budget of 1 billion euros over ten years. At the halfway point it reported over 25 commercial products, and IEEE Spectrum counted nine companies and 46 products, with critics saying graphene had not lived up to expectations.{cite(11)}</p>
{note("The catch", "<p>The money is in graphite supply and nanotube additives, not graphene itself. And the graphite supply chain is concentrated in China.</p>")}''',
                 photos=[("graphene-stm.jpg", "A scanning tunnelling microscope image of a section of graphene sheet."), ("nist-nanotube-chips.jpg", "Custom chips coated with carbon nanotubes, made at NIST."),
                         ("graphite-pebble.jpg", "A graphite pebble fuel assembly for a pebble-bed reactor.")],
                 paths_nav="Forms", paths_title="The forms of carbon",
                 paths=[("Graphene", f"First isolated at Manchester. The Graphene Flagship reported over 25 commercial products by its halfway point.{cite(13)}{cite(11)}"),
                        ("Nanotubes", f"LG Chem says nanotubes cut the conductive additive needed in a battery by about 30% and raise conductivity by about 10%.{cite(15)}"),
                        ("Graphite", f"China produced about 70% of the world's natural flake graphite in 2022 and almost 96% of synthetic graphite anode material.{cite(16)}"),
                        ("Carbon fibre", "The US Department of Energy runs a carbon fibre technology facility at Oak Ridge, Tennessee.")],
                 limits=[("Slow products", f"The Graphene Flagship named the lack of standardisation as an obstacle.{cite(11)}"),
                         ("Supply concentration", f"China's export licences on certain graphite took effect on 1 December 2023.{cite(16)}"),
                         ("Trade duties", f"The US set a 93.5% preliminary anti-dumping rate on Chinese anode graphite in July 2025.{cite(17)}"),
                         ("Funding", f"Novonix said at the end of 2025 that it would need more funding.{cite(18)}")],
                 history=[("2010", f"Graphene, first isolated at Manchester, wins its discoverers the Nobel Prize.{cite(13)}", "big"),
                          ("2013", f"The EU launches the Graphene Flagship with a 1 billion euro, ten-year budget.{cite(11)}", ""),
                          ("2014", f"AMBER at Trinity College Dublin reports a mixing method to make graphene in bulk.{cite(14)}", ""),
                          ("December 2023", f"China starts requiring licences to export certain graphite.{cite(16)}", "big"),
                          ("July 2025", f"The US sets a 93.5% preliminary anti-dumping rate on Chinese anode graphite.{cite(17)}", ""),
                          ("2026", f"Westwater loses its SK On agreement. Nouveau Monde announces C$213 million of equity for its mine.{cite(19)}{cite(20)}", "fut")],
                 key=("The plain material matters more than the famous one", "Graphene has produced products slowly. Graphite for batteries is where supply is tight and governments are acting.")),
        ch2=dict(cards=[("What changed", f"Governments treat battery graphite as strategic: China's licences, US anti-dumping duties.{cite(16)}{cite(17)}"),
                        ("What has not", f"Graphene has not produced a mass-market product on the scale its backers hoped.{cite(11)}"),
                        ("What is new", f"Western graphite projects are getting funding and losing offtakers at the same time.{cite(19)}{cite(20)}")],
                 photo=("sandia-electrode.jpg", "A Sandia researcher holding an electrode made by coating copper foil."),
                 key=("Famous material, plain market", "The investment story is in graphite supply, with a few small listed companies that are not yet fully funded.")),
        ch3=dict(sub="Our judgement from the filings. Not a forecast.",
                 timeline=[("Now: funding and trade rules", f"Plants wait for funding. Duties and licences shape who can sell.{cite(17)}{cite(16)}", "fut"),
                           ("Second half of 2026: decisions", f"Nouveau Monde targets a final investment decision on its anode plant.{cite(21)}", "fut"),
                           ("Next: production for Panasonic and others", f"Novonix is ramping production at Chattanooga for Panasonic and PowerCo.{cite(18)}", "fut")],
                 ireland=[("The research", f"AMBER at Trinity College Dublin developed a bulk graphene method, reported in 2014.{cite(14)}"),
                          ("The firms", "We found no listed Irish graphite or graphene company."),
                          ("The watch", "Irish graphene research is the Irish link to this sector. Its commercial route is through licensing and spin-outs.")],
                 prepare=[("As a citizen", "Battery prices depend partly on graphite supply and trade rules."),
                          ("As a business", "Ask battery suppliers where their anode material comes from."),
                          ("As an investor", "The listed graphite companies are small and still funding their plants. Their prices move on funding news.")],
                 key=("Funding, then production, then margins", "The next steps are plant decisions and first production. Margins come later.")),
        ch4=dict(sub="Three small listed companies, building graphite supply outside China.",
                 extra="", prices_title="Share prices since listing", prices_blurb="Three graphite companies, with Albemarle and Nvidia for scale.",
                 booms_caption="Log scale, from weekly closes, adjusted for splits.",
                 ladder_caption="None of the three has reached full-scale production. Nouveau Monde has the strongest funding of the three.",
                 good=["A plant reaches full funding.", "A binding offtake is signed with a price.", "First commercial shipments go to a battery maker.", "Duties keep Chinese material out."],
                 bad=["An offtake is ended.", "Funding is conditional and not closed.", "A company sells shares to keep going.", "A plant decision slips."],
                 map_key='<span><i style="border-color:var(--teal)"></i>active in the sector</span><span><i style="border-color:var(--violet)"></i>partner</span><span><i style="border-color:var(--red)"></i>dominant supplier under export rules</span>',
                 key=("Small companies, big hurdles", "The three listed names are building plants, losing offtakers and raising money. Their prices reflect hope more than output.")),
        ch5=dict(sub="Funding, offtakers, trade rules and standardisation.",
                 cards=[("Offtake risk", f"A Stellantis subsidiary ended its Novonix agreement in November 2025 and SK On ended its Westwater agreement in March 2026.{cite(19)}"),
                        ("Funding", f"Novonix had $79.9 million of cash at the end of 2025 and said more funding would be needed.{cite(18)}"),
                        ("Concentration", f"China supplied almost 96% of synthetic graphite anode material.{cite(16)}"),
                        ("Trade rules", f"US duties on Chinese anode graphite: 93.5% anti-dumping, and 66.68% countervailing on natural graphite anode material in February 2026.{cite(17)}"),
                        ("Standardisation", f"The Graphene Flagship named the lack of standards as an obstacle.{cite(11)}"),
                        ("Timing", f"Westwater says production starts about 12 months after financing closes.{cite(19)}")],
                 photo=("cftf-line.jpg", "The Carbon Fiber Technology Facility at Oak Ridge, Tennessee."),
                 line="A graphite plant needs money, a customer and a trade rule that keeps cheap imports out. The three listed companies have some of each and none has all three.",
                 key=("Money, customers and rules", "A plant needs all three. Each of the listed companies is missing at least one.")),
        ch6=dict(n_word="three", expect=[("Likely, about 75%", "More graphite trade rules. More funding announcements. At least one Western anode plant starts commercial production."),
                                         ("Even odds, about 50%", "Nouveau Monde reaches a final investment decision on its anode plant."),
                                         ("Unlikely, under 15%", "Western producers supply a large share of the world's anode graphite by 2029.")],
                 pull="Graphite will matter more than graphene. The listed companies still have to prove they can build.",
                 why=[("Why we lean that way", "Our scenarios put the chance of each company ending the three years below today's price at {lo} to {hi}. All three are small and still funding their plants."),
                      ("Who is exposed", "Companies that need new financing and have lost an offtaker."),
                      ("If it goes right", "A funded plant with a binding offtake and a trade rule behind it would re-rate the company."),
                      ("The test", "For each company, check three things: whether it is funded, whether a customer is bound by contract, and whether the plant is running.")],
                 mind="A company signing a new binding offtake at a stated price. Full financing for a plant. A change in trade duties.",
                 key=("Plants before profits", "We expect more funding news and slow production. The trade rules help, and the plants still have to run.")),
    )
    return _gen.build(C, cite)
