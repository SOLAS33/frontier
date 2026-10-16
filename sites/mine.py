"""Frontier Mine: critical minerals, rare earths, lithium and copper. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more
from frontier import sitekit as K
from frontier.components import note
from frontier.scenarios import Scenario
from sites import tech_mine as TB
from sites import _gen

TITLE = "Frontier Mine"
AS_OF = "16 October 2026"

LIVE = {"cik": {"MP": 1801368, "LAC": 1966983, "FCX": 831259, "UUUU": 1385849, "ALB": 915913},
        "aliases": {"MP": ["mp materials"], "LAC": ["lithium americas", "thacker pass"], "FCX": ["freeport", "grasberg"], "UUUU": ["energy fuels"], "ALB": ["albemarle"]},
        "arxiv_terms": ["rare earth", "lithium extraction", "critical minerals"], "arxiv_cat": "cond-mat.mtrl-sci"}

REFS = TB.MINE_REFS
cite = K.cite_factory(REFS)

SCEN = {
    "MP": [Scenario("bear", "The magnet plant slips and NdPr prices fall", 0.30, -0.40, 0.75),
           Scenario("base", "Output grows with the price floor", 0.45, 0.10, 0.75),
           Scenario("bull", "Magnets scale for several large customers", 0.25, 0.45, 0.75)],
    "LAC": [Scenario("bear", "Costs rise and lithium prices stay low", 0.40, -0.45, 0.75),
            Scenario("base", "Construction continues on a slow timeline", 0.35, 0.05, 0.75),
            Scenario("bull", "Thacker Pass starts on time and prices recover", 0.25, 0.55, 0.75)],
    "FCX": [Scenario("bear", "Grasberg takes longer to restart", 0.30, -0.30, 0.75),
            Scenario("base", "Output recovers in stages", 0.45, 0.10, 0.75),
            Scenario("bull", "Copper prices rise with the restart on schedule", 0.25, 0.35, 0.75)],
    "UUUU": [Scenario("bear", "Rare earth output stays small and uranium prices stay low", 0.40, -0.40, 0.75),
             Scenario("base", "Heavy rare earths scale slowly", 0.35, 0.05, 0.75),
             Scenario("bull", "Heavy rare earths scale and trade rules help", 0.25, 0.55, 0.75)],
    "ALB": [Scenario("bear", "Lithium prices stay low", 0.35, -0.35, 0.75),
            Scenario("base", "A slow recovery in lithium prices", 0.40, 0.08, 0.75),
            Scenario("bull", "Lithium prices recover with demand", 0.25, 0.45, 0.75)],
}

COMPANIES = [
    {"t": "MP", "name": "MP Materials", "kind": "Rare earth mining and magnets",
     "rivals": "Chinese rare earth producers",
     "profit": f"Mines and refines rare earths at Mountain Pass, California. In 2025 it made a record 2,599 tonnes of NdPr oxide, up 101%, and made its first magnets on commercial equipment in the fourth quarter. The Department of Defense bought $400 million of preferred stock and agreed a 10-year price floor of $110 per kilogram for NdPr.{cite(12)}{cite(11)}",
     "watch": "NdPr output, the Texas magnet plant, magnet customers, price floor payments.", "rank": "The main US rare earth producer, with the US government as its largest shareholder on an as-converted basis.",
     "verdict": "A state-backed bet on a second supply chain"},
    {"t": "LAC", "name": "Lithium Americas", "kind": "Lithium mine under construction",
     "rivals": "Albemarle and other lithium producers",
     "profit": f"Building Thacker Pass in Nevada, owned 62% by Lithium Americas and 38% by General Motors. It has a US Department of Energy loan of about $2.26 billion and guides $1.3 billion to $1.6 billion of capital spending for 2026. Mechanical completion is targeted for late 2027.{cite(13)}{cite(14)}",
     "watch": "Construction progress, cost, lithium price.", "rank": "A development-stage project with no revenue yet.",
     "verdict": "A large mine still to be built"},
    {"t": "FCX", "name": "Freeport-McMoRan", "kind": "Copper, gold and molybdenum",
     "rivals": "Other large copper miners",
     "profit": f"One of the largest copper miners. On 8 September 2025 about 800,000 tonnes of wet material entered the Grasberg block cave in Indonesia and seven workers died. It cut its 2026 copper sales estimate from 3.4 billion to about 3.1 billion pounds, and the shares fell more than 13% on its first-quarter report.{cite(15)}{cite(16)}",
     "watch": "Grasberg restart, copper price, cost.", "rank": "A large, established producer with a big operational problem.",
     "verdict": "Copper, with Grasberg in recovery"},
    {"t": "UUUU", "name": "Energy Fuels", "kind": "Uranium and rare earths",
     "rivals": "Other uranium and rare earth producers",
     "profit": f"Mines uranium and separates rare earths at its White Mesa Mill in Utah. In March 2026 it made its first kilogram of terbium oxide at 99.9% purity, after about 29 kilograms of dysprosium oxide. Both are heavy rare earths under Chinese export controls.{cite(17)}",
     "watch": "Heavy rare earth output, uranium sales, the planned Australian acquisition.", "rank": "A small producer of heavy rare earths outside China.",
     "verdict": "Small amounts of the scarce ones"},
    {"t": "ALB", "name": "Albemarle", "kind": "Lithium and specialty chemicals",
     "rivals": "Chinese and Chilean lithium producers",
     "profit": f"Sells lithium for batteries. 2025 net sales were about $5.1 billion on one summary, and lower lithium prices cut energy storage profit. Its 2026 outlook is given for lithium prices of $10, $20 and $30 per kilogram.{cite(18)}",
     "watch": "Lithium price, cost cuts, plant closures such as Kemerton Train 1.", "rank": "The established lithium producer.",
     "verdict": "Lithium at a low price"},
]

LADDER = [("Resource", "Minerals are|in the ground"), ("Permit", "Approved to|mine"), ("Funding", "Money is|committed"),
          ("Construction", "The mine or|plant is built"), ("Production", "Output reaches|design rate"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "friendly"), "IE": (3, 0, "friendly"), "CN": (9, 1, "restrictive"), "ID": (9, 2, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "CN": "China", "ID": "Indonesia"}
COUNTRY = {
    "CN": {"co": "Chinese rare earth and magnet makers", "gov": "Mined 60% of magnet rare earths in 2024, refined 91% and made 94% of sintered permanent magnets", "ctl": "April 2025 licensing, with an October 2025 expansion suspended until 10 November 2026",
           "note": "The centre of the supply chain."},
    "US": {"co": "MP Materials, Lithium Americas, Energy Fuels, Freeport-McMoRan", "gov": "The Department of Defense took a stake in MP Materials and set a $110 per kilogram NdPr price floor. The Department of Energy lent about $2.26 billion for Thacker Pass", "ctl": "See the references",
           "note": "Using public money to build a second supply chain."},
    "ID": {"co": "Freeport-McMoRan's Grasberg mine", "gov": "Grasberg's block cave had a mud rush in September 2025 that killed seven workers", "ctl": "See the references", "note": "Home of a very large copper and gold mine now in recovery."},
    "IE": {"co": "Boliden Tara Mines, near Navan", "gov": "Tara is one of Europe's largest zinc mines. Boliden halted it in 2023 and it reopened around the end of 2024. The EU's Critical Raw Materials Act sets 2030 benchmarks for extraction, processing and recycling", "ctl": "EU rules",
           "note": "Home of a large zinc mine under EU benchmarks."},
}
HYPE = [
    ("5", "Production at design rate", "A mine or plant that has run for years", "Freeport's mines before 2025", "ok"),
    ("4", "Output records and contracts", "A company reports growing output and signed buyers", "MP Materials' 2,599 tonnes and its Apple and GM deals", "ok"),
    ("3", "A government stake or loan", "State money commits to a project", "US stake in MP, DOE loan for Thacker Pass", "dis"),
    ("2", "A first small batch", "A kilogram or a pilot of a scarce product", "Energy Fuels' first terbium oxide", "dis"),
    ("1", "A plan for a plant", "A plant on a slide", "A magnet plant planned for Texas", "tgt"),
]
SHOVELS = [
    ("Rare earth mining and separation", "MP Materials, Energy Fuels", "United States", "China is dominant in the refining stage"),
    ("Magnet making", "MP Materials (planned 10X plant)", "United States", "China made 94% of sintered magnets in 2024"),
    ("Lithium", "Albemarle, Lithium Americas", "United States", "Prices have been low, and a mine is under construction"),
    ("Zinc, in Europe", "Boliden", "Ireland, Sweden", "Tara Mines reopened around the end of 2024"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    C = dict(
        slug="mine", name="Mine", as_of=AS_OF, live=LIVE, refs=REFS, scen=SCEN, companies=COMPANIES, ladder=LADDER, hype=HYPE, shovels=SHOVELS,
        tiles=TILES, names=NAMES, country=COUNTRY, map_default="IE",
        order=["MP", "LAC", "FCX", "UUUU", "ALB", "NVDA"], default=["MP", "LAC", "FCX", "UUUU", "ALB"],
        tm_assets=[["MP", "MP Materials"], ["LAC", "Lithium Americas"], ["FCX", "Freeport-McMoRan"], ["UUUU", "Energy Fuels"], ["ALB", "Albemarle"], ["NVDA", "Nvidia"]],
        tm_default={"MP": px_first("MP"), "LAC": px_first("LAC"), "FCX": "2016-01-04", "UUUU": "2016-01-04", "ALB": "2016-01-04", "NVDA": "2022-10-10"},
        runs_for=("MP", "LAC", "FCX", "UUUU", "ALB", "NVDA"),
        mult=[("Nvidia, 2022 to 2024", "NVDA", "ref"), ("Freeport-McMoRan", "FCX", "lay"), ("Albemarle", "ALB", "lay"), ("Lithium Americas", "LAC", "quantum"),
              ("Energy Fuels", "UUUU", "quantum"), ("MP Materials", "MP", "quantum")],
        index_groups=[("Rare earths and uranium", ["MP", "UUUU"], "var(--amber)"), ("Lithium and copper", ["LAC", "FCX", "ALB"], "var(--teal)")],
        tech=TB.mine_html(cite),
        data_note="Production, deal and trade-rule figures were checked against the sources listed. Some company figures come from summaries and are marked as such.",
        notice="We explain critical minerals and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.",
        facts=[("China refined magnet rare earths", "91%"), ("US NdPr price floor", "$110/kg"), ("MP NdPr oxide 2025", "2,599 t"), ("China pause expires", "10 Nov 2026")],
        bands=[("mountain-pass.jpg", "Rare earths", "The Mountain Pass rare earth mine in California, seen from space.", "The Mountain Pass rare earth mine"),
               ("salar-atacama.jpg", "Lithium brine", "The Salar de Atacama in Chile.", "The Salar de Atacama"),
               ("chuqui.jpg", "Copper", "Loading rock at the Chuquicamata copper mine in Chile.", "Loading rock at a copper mine"),
               ("bingham-1942.jpg", "A century of digging", "The Bingham Canyon open-pit mine in 1942.", "The Bingham Canyon open-pit mine in 1942"),
               ("uranium-mill.jpg", "Three years", "Time enough to see which plants are built.", "A uranium mill outside Moab")],
        hero=dict(h1="China refines most of what the West <em>digs up</em>",
                  lead="China mined 60% of the world's magnet rare earths in 2024, refined 91% and made 94% of the strong magnets. Western governments are now paying to build a second chain. Here is who is building it, what it costs, and what could go wrong.",
                  img="chuqui.jpg", art=art_more.hero_reactor(),
                  stats=[(91, "per cent of magnet rare earths refined in China in 2024", "", "%"), (110, "dollars per kilogram: the US price floor for NdPr oxide from MP Materials", "$", ""),
                         (2599, "tonnes of NdPr oxide made by MP Materials in 2025, a record", "", ""),
                         (7, "workers died in the Grasberg mud rush of September 2025", "", "")]),
        ch1=dict(sub="Digging is the first step. Refining and magnets are where the squeeze is.",
                 intro=f'''<p>Critical minerals are the metals that batteries, magnets and wires need: rare earths, lithium and copper. China mined 60% of the world's magnet rare earths in 2024, refined 91% of them and made 94% of the world's sintered permanent magnets.{cite(10)}</p>
{note("Why it is attractive", "<p>Electric motors, wind turbines and many defence systems use these metals. Governments now treat their supply as a security issue, and are paying for new supply.</p>")}
<p>In July 2025 the US Department of Defense bought $400 million of preferred stock in MP Materials and agreed a 10-year price floor of $110 per kilogram for NdPr oxide.{cite(11)} The EU's Critical Raw Materials Act sets 2030 benchmarks: 10% of annual consumption from EU extraction, 40% from processing and 25% from recycling, with no more than 65% from one non-EU country.{cite(20)}</p>
{note("The catch", "<p>New mines and plants take years, and accidents, prices and permits can all stop them. The chain is also concentrated in one country.</p>")}''',
                 photos=[("mountain-pass.jpg", "The Mountain Pass rare earth mine in California seen from space by ASTER."), ("chuqui.jpg", "Loading rock from the Chuquicamata copper mine in Chile."),
                         ("salar-atacama.jpg", "The Salar de Atacama in Chile, seen from space by ASTER.")],
                 paths_nav="Parts", paths_title="The parts of the business",
                 paths=[("Rare earths", f"MP Materials made a record 2,599 tonnes of NdPr oxide in 2025 and its first magnets on commercial equipment.{cite(12)}"),
                        ("Lithium", f"Albemarle's energy storage profit fell in 2025 on lower lithium prices. Thacker Pass is under construction.{cite(18)}{cite(13)}"),
                        ("Copper", f"Freeport's Grasberg mine had a mud rush in September 2025 that killed seven workers.{cite(15)}"),
                        ("Heavy rare earths", f"Energy Fuels made its first kilogram of terbium oxide in March 2026.{cite(17)}")],
                 limits=[("Accidents", f"Seven workers died at Grasberg in September 2025, and Freeport cut its 2026 copper estimate to about 3.1 billion pounds.{cite(15)}{cite(16)}"),
                         ("Low prices", f"Lower lithium prices cut Albemarle's energy storage profit in 2025.{cite(18)}"),
                         ("Export controls", f"China's October 2025 expansion of export controls is suspended until 10 November 2026.{cite(19)}"),
                         ("Time", f"Thacker Pass mechanical completion is targeted for late 2027.{cite(14)}")],
                 history=[("April 2025", f"China introduces licensing controls on seven heavy rare earth elements and magnets.{cite(10)}", ""),
                          ("July 2025", f"The Pentagon takes a stake in MP Materials and sets a price floor.{cite(11)}", "big"),
                          ("September 2025", f"The Grasberg mud rush kills seven workers.{cite(15)}", "big"),
                          ("November 2025", f"China suspends its October expansion of rare earth export controls until 10 November 2026.{cite(19)}", ""),
                          ("March 2026", f"Energy Fuels makes its first kilogram of terbium oxide.{cite(17)}", ""),
                          ("10 November 2026", f"China's pause on the October 2025 controls expires.{cite(19)}", "fut")],
                 key=("A second supply chain costs money and time", "Western governments are paying for rare earths, lithium and copper supply. The plants are being built, and accidents, prices and Chinese controls can all change the outcome.")),
        ch2=dict(cards=[("What changed", f"The US government now owns a stake in a rare earth miner and guarantees its price.{cite(11)}"),
                        ("What has not", f"China still refines 91% of magnet rare earths.{cite(10)}"),
                        ("What is new", f"The EU has set 2030 benchmarks for extraction, processing and recycling.{cite(20)}")],
                 photo=("bingham-1942.jpg", "The Utah Copper Company's open-pit mine at Bingham Canyon in 1942."),
                 key=("Governments are the new investors", "Public money and price floors are changing what gets built. The plants still have to run.")),
        ch3=dict(sub="Our judgement from the filings. Not a forecast.",
                 timeline=[("Now to November 2026: the pause", f"China's pause on its October 2025 export-control expansion runs until 10 November 2026.{cite(19)}", "fut"),
                           ("2026 to 2027: Grasberg and Thacker Pass", f"Grasberg restarts in stages, with Block 1 targeted for 2027. Thacker Pass targets mechanical completion in late 2027.{cite(15)}{cite(14)}", "fut"),
                           ("2028: US magnets at scale", f"The 10X magnet plant in Texas is planned, with commissioning expected in 2028 according to the Pentagon deal terms.{cite(11)}", "fut")],
                 ireland=[("The mine", f"Boliden's Tara Mines near Navan is one of Europe's largest zinc mines. It was halted in 2023 and reopened around the end of 2024, with about 380 employees.{cite(21)}{cite(22)}"),
                          ("The rules", f"The EU's Critical Raw Materials Act sets benchmarks for extraction, processing and recycling by 2030.{cite(20)}"),
                          ("The watch", "Zinc is not one of the rare earths, and Tara shows how fragile mining economics are: it was halted when prices were low.")],
                 prepare=[("As a citizen", "Prices of electric cars and wind turbines depend partly on these metals and on trade rules."),
                          ("As a business", "Ask suppliers where magnets and battery materials come from."),
                          ("As an investor", "These shares move on government news, metal prices and accidents.")],
                 key=("Pause, restart, build", "The next year is about China's pause, Grasberg's restart and the first Western magnets.")),
        ch4=dict(sub="A rare earth leader, a lithium builder, a copper giant in recovery, a heavy rare earth pioneer and an incumbent lithium producer.",
                 extra="", prices_title="Share prices", prices_blurb="Five listed critical-mineral companies, with Nvidia for scale.",
                 booms_caption="Log scale, from weekly closes, adjusted for splits.",
                 ladder_caption="MP Materials is furthest up. Lithium Americas is under construction. Energy Fuels is at the first small batch.",
                 good=["A plant runs at design rate.", "A government commits money with a price floor.", "Customers sign multi-year contracts.", "Costs per tonne fall."],
                 bad=["A price floor is the only buyer.", "An accident cuts output.", "A plant date slips again.", "Export controls change overnight."],
                 map_key='<span><i style="border-color:var(--teal)"></i>mines or plants</span><span><i style="border-color:var(--violet)"></i>policy only</span><span><i style="border-color:var(--red)"></i>dominant refiner under export rules</span>',
                 key=("The state is the customer and the shareholder", "The best-supported name has the US government as its largest holder and price guarantor. The others depend on metal prices and execution.")),
        ch5=dict(sub="Accidents, prices, time and trade rules.",
                 cards=[("Safety", f"The Grasberg mud rush killed seven workers.{cite(15)}"),
                        ("Production", f"Freeport cut its 2026 copper sales estimate from 3.4 to about 3.1 billion pounds.{cite(16)}"),
                        ("Price", f"Lower lithium prices cut Albemarle's energy storage profit.{cite(18)}"),
                        ("Time", f"Thacker Pass is targeted for mechanical completion in late 2027.{cite(14)}"),
                        ("Concentration", f"China refined 91% of magnet rare earths in 2024.{cite(10)}"),
                        ("Policy", f"China's export-control pause expires on 10 November 2026.{cite(19)}")],
                 photo=("clayton-valley.jpg", "Clayton Valley, Nevada, where lithium has been produced, seen from space by ASTER."),
                 line="A mine needs a permit, money, a safe operation and a price that pays. A refinery needs the same plus a customer. Governments can help with some of these and not all.",
                 key=("Safety, price and time", "Every project here can fail on one of three things: an accident, a price, or a delay.")),
        ch6=dict(n_word="five", expect=[("Likely, about 75%", "More government price supports and stakes. More Western rare earth separation announcements. Thacker Pass construction continues."),
                                        ("Even odds, about 50%", "MP Materials delivers magnets in volume to at least one large customer."),
                                        ("Unlikely, under 15%", "The West makes a majority of its own magnet rare earths by 2029.")],
                 pull="The West can build a second supply chain. It will take longer and cost more than the announcements say.",
                 why=[("Why we lean that way", "Our scenarios put the chance of each company ending the three years below today's price at {lo} to {hi}. These are volatile shares that move on policy."),
                      ("Who is exposed", "Companies whose output depends on a price floor, a plant not yet built or one big mine."),
                      ("If it goes right", "Western magnets and refined metals reach large buyers at prices that cover costs."),
                      ("The test", "For each company, check output, costs and whether customers have signed binding contracts.")],
                 mind="China ending its export-control pause on 10 November 2026. A plant start earlier than planned. Another serious mine accident.",
                 key=("Slow building, fast policy", "We expect policy to move faster than plants.")),
    )
    return _gen.build(C, cite)
