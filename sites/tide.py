"""Frontier Tide: wave, tidal and other new ways to harvest energy. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more
from frontier import sitekit as K
from frontier.components import note
from frontier.scenarios import Scenario
from sites import tech_tide as TB
from sites import _gen

TITLE = "Frontier Tide"
AS_OF = "16 October 2026"

LIVE = {"cik": {"OPTT": 1378140, "WAVE": 1846715, "ORA": 1296445, "FRVO": 1853868},
        "aliases": {"OPTT": ["ocean power technologies", "powerbuoy"], "WAVE": ["eco wave power"], "ORA": ["ormat"], "FRVO": ["fervo"]},
        "arxiv_terms": ["wave energy converter", "tidal turbine", "enhanced geothermal"], "arxiv_cat": "physics.flu-dyn"}

REFS = TB.TIDE_REFS
cite = K.cite_factory(REFS)

SCEN = {
    "OPTT": [Scenario("bear", "Losses continue and it must raise money again", 0.45, -0.50, 0.75),
             Scenario("base", "Defence orders keep the lights on", 0.35, 0.00, 0.75),
             Scenario("bull", "Backlog converts and revenue scales", 0.20, 0.55, 0.75)],
    "WAVE": [Scenario("bear", "Pilots do not become orders and cash runs down", 0.50, -0.55, 0.75),
             Scenario("base", "Pilots continue with small revenue", 0.30, 0.00, 0.75),
             Scenario("bull", "A first large project is financed", 0.20, 0.60, 0.75)],
    "ORA": [Scenario("bear", "Power prices and curtailment squeeze margins", 0.25, -0.25, 0.75),
            Scenario("base", "Steady growth in geothermal and storage", 0.50, 0.10, 0.75),
            Scenario("bull", "Data-centre contracts multiply", 0.25, 0.35, 0.75)],
    "FRVO": [Scenario("bear", "Delays and financing needs weigh on the shares", 0.40, -0.45, 0.75),
             Scenario("base", "Construction proceeds with the usual delays", 0.35, 0.05, 0.75),
             Scenario("bull", "Cape Station delivers power and more contracts follow", 0.25, 0.55, 0.75)],
}

COMPANIES = [
    {"t": "OPTT", "name": "Ocean Power Technologies", "kind": "Wave-powered buoys and ocean data",
     "rivals": "Other marine technology and defence-sensor makers",
     "profit": f"Sells PowerBuoy systems. Fiscal 2026 revenue was about $4.1 million, down from $5.9 million, with a net loss of $43.7 million and a backlog of $19.8 million, on secondary summaries of its results. Its work is mostly for defence and maritime awareness.{cite(15)}",
     "watch": "Backlog conversion, defence contracts, funding, its listing.", "rank": "A long-established wave-energy name whose business has moved to ocean data.",
     "verdict": "A buoy company, not a power company"},
    {"t": "WAVE", "name": "Eco Wave Power", "kind": "Wave energy converters",
     "rivals": "Other wave-energy developers",
     "profit": f"Builds wave-energy floaters that attach to existing structures. Its 2025 revenue was $38,000, its net loss about $3.7 million and its year-end cash $6.3 million. Its Port of Los Angeles pilot lowered its floaters into the water in 2025.{cite(16)}",
     "watch": "Pilot results, a first large project, cash.", "rank": "A pilot-stage company.",
     "verdict": "Pilots, not yet a business"},
    {"t": "ORA", "name": "Ormat Technologies", "kind": "Geothermal power",
     "rivals": "Other geothermal developers and utilities",
     "profit": f"Operates geothermal and solar plants totalling 1,340 MW. 2025 revenue was $989.6 million, up 12.5%. It signed a 15-year agreement of up to 150 MW with Google through NV Energy and a 20-year agreement with Switch.{cite(17)}",
     "watch": "New data-centre contracts, curtailment, product backlog.", "rank": "The established, profitable name in this group.",
     "verdict": "The only one with real revenue"},
    {"t": "FRVO", "name": "Fervo Energy", "kind": "Next-generation geothermal",
     "rivals": "Ormat and other geothermal developers",
     "profit": f"Builds Cape Station in Utah, with a 500 MW first phase. It priced its IPO on 12 May 2026 at $27 a share and raised about $2.2 billion including extra shares. Its 2025 revenue was $140,000 and its net loss about $57.8 million.{cite(18)}{cite(21)}",
     "watch": "Cape Station first power, drilling costs, contracts, share price.", "rank": "Newly listed, pre-revenue, with a large cash pile.",
     "verdict": "A big bet on drilling for heat"},
]

LADDER = [("Prototype", "Tested at|sea or in rock"), ("Pilot", "Delivers power to|a grid"), ("Contracts", "A buyer commits|with a price"),
          ("First plant", "A plant runs|for a year"), ("Fleet", "Many plants|at a falling cost"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "friendly"), "IE": (3, 0, "friendly"), "GB": (4, 0, "friendly"), "FR": (4, 1, "friendly"), "KR": (10, 0, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "KR": "South Korea"}
COUNTRY = {
    "FR": {"co": "EDF", "gov": "Home of La Rance, a 240 MW tidal barrage and one of the two plants that make up IRENA's global total", "ctl": "See the references", "note": "The oldest large tidal plant."},
    "KR": {"co": "Korean utilities", "gov": "Home of Sihwa, a 254 MW tidal barrage", "ctl": "See the references", "note": "The largest tidal plant by capacity."},
    "GB": {"co": "MeyGen (Ampeak Energy), Orbital Marine Power, HydroWing", "gov": "The UK's sixth allocation round awarded 28 MW of tidal stream at £172 per MWh, the third round in a row with a tidal ringfence", "ctl": "See the references", "note": "The strongest policy support for tidal stream."},
    "US": {"co": "Ormat, Fervo Energy, Eco Wave Power (pilot in Los Angeles), Ocean Power Technologies", "gov": "Google has agreed to buy up to 150 MW of geothermal power from Ormat through NV Energy", "ctl": "See the references", "note": "The market for geothermal for data centres."},
    "IE": {"co": "SEAI (Atlantic Marine Energy Test Site)", "gov": "SEAI is developing a test site off Annagh Head, Belmullet, County Mayo, for wave devices and floating wind, and Ireland also has test sites in Cork and Galway Bay", "ctl": "See the references",
           "note": "Irish activity is testing, not generation."},
}
HYPE = [
    ("5", "Decades of operation", "A plant that has run for decades", "La Rance and Sihwa tidal barrages", "ok"),
    ("4", "Revenue and contracts", "A company with real revenue and signed buyers", "Ormat's $989.6 million and its Google contract", "ok"),
    ("3", "A contract with a guaranteed price", "A government or buyer commits to a price", "UK tidal stream rounds at £172 per MWh", "dis"),
    ("2", "A pilot in the water", "A device is deployed for tests", "Eco Wave Power in Los Angeles", "dis"),
    ("1", "A very large future plant", "A target for a first big plant", "Fervo's Cape Station, due to be built", "tgt"),
]
SHOVELS = [
    ("Test sites", "SEAI's Atlantic Marine Energy Test Site", "Ireland", "A full-scale open-ocean test site planned off County Mayo"),
    ("Tidal stream operators", "MeyGen (Ampeak Energy)", "Scotland", "6 MW operating, with 59 MW more awarded support"),
    ("Geothermal equipment and operators", "Ormat", "United States and others", "1,340 MW of geothermal and solar plants"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    C = dict(
        slug="tide", name="Tide", as_of=AS_OF, live=LIVE, refs=REFS, scen=SCEN, companies=COMPANIES, ladder=LADDER, hype=HYPE, shovels=SHOVELS,
        tiles=TILES, names=NAMES, country=COUNTRY, map_default="IE",
        order=["OPTT", "WAVE", "ORA", "FRVO", "NVDA"], default=["OPTT", "WAVE", "ORA", "FRVO"],
        tm_assets=[["OPTT", "Ocean Power Technologies"], ["WAVE", "Eco Wave Power"], ["ORA", "Ormat"], ["FRVO", "Fervo Energy"], ["NVDA", "Nvidia"]],
        tm_default={"OPTT": "2016-01-04", "WAVE": px_first("WAVE"), "ORA": "2016-01-04", "FRVO": px_first("FRVO"), "NVDA": "2022-10-10"},
        runs_for=("OPTT", "WAVE", "ORA", "FRVO", "NVDA"),
        mult=[("Nvidia, 2022 to 2024", "NVDA", "ref"), ("Ormat", "ORA", "lay"), ("Ocean Power Technologies", "OPTT", "quantum"), ("Eco Wave Power", "WAVE", "quantum"), ("Fervo Energy", "FRVO", "quantum")],
        index_groups=[("Wave and ocean names", ["OPTT", "WAVE"], "var(--amber)"), ("Geothermal names", ["ORA"], "var(--teal)")],
        tech=TB.tide_html(cite),
        data_note="Capacity, contract and company figures were checked against the sources listed. Some company results come from secondary summaries and are marked as such.",
        notice="We explain wave, tidal and geothermal energy and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.",
        facts=[("Ocean energy worldwide", "494 MW"), ("Geothermal worldwide", "about 15 GW"), ("UK tidal stream, round 6", "28 MW"), ("Ormat revenue 2025", "$989.6m")],
        bands=[("rance-barrage.jpg", "The old guard", "The tidal barrage on the Rance, in France.", "The tidal barrage on the Rance"),
               ("powerbuoy.jpg", "On the water", "A PowerBuoy floating off the coast.", "A PowerBuoy floating at sea"),
               ("pelamis-emec.jpg", "The snake", "A Pelamis wave energy converter at the European Marine Energy Centre.", "A Pelamis wave energy converter"),
               ("francis-runner.jpg", "The turbine", "The runner of a Francis turbine in a hydropower plant.", "A Francis turbine runner"),
               ("nesjavellir.jpg", "Heat from below", "The Nesjavellir geothermal power plant in Iceland.", "The Nesjavellir geothermal power plant")],
        hero=dict(h1="The sea is huge, and its power plants are <em>very small</em>",
                  lead="The world had 494 megawatts of ocean energy at the end of 2024, all of it from two tidal barrages. Geothermal is about thirty times bigger and is being bought by data centres. Here is what works, what is a pilot, and who is paid.",
                  img="rance-barrage.jpg", art=art_more.hero_reactor(),
                  stats=[(494, "megawatts of ocean energy installed worldwide at the end of 2024, according to IRENA", "", " MW"), (15, "gigawatts of geothermal capacity worldwide at the end of 2024", "about ", " GW"),
                         (28, "megawatts of tidal stream won UK contracts in the sixth auction", "", " MW"),
                         (150, "megawatts: the most Ormat agreed to supply to Google's data centres", "up to ", " MW")]),
        ch1=dict(sub="Water moves, heat flows, and only some of it pays.",
                 intro=f'''<p>Tides, waves and the heat inside the Earth are huge sources of energy. Getting it out is hard. At the end of 2024 the world had 494 megawatts of ocean energy installed, according to IRENA, and that equals two tidal barrages: La Rance in France (240 MW) and Sihwa in South Korea (254 MW).{cite(10)} In 2024 the world added 1.6 megawatts.{cite(11)}</p>
{note("Why it is attractive", "<p>Tides are predictable, and geothermal heat runs day and night. Both can supply steady power when the wind is still.</p>")}
<p>Geothermal is far larger: about 15 gigawatts worldwide at the end of 2024, and 16 GW at the end of 2025.{cite(12)} Data centres are buying it. Ormat has agreed to supply up to 150 MW to Google through NV Energy.{cite(17)}</p>
{note("The catch", "<p>Wave and tidal devices must survive the sea and sell power at a price a grid will pay. The few companies in the water report very small revenues.</p>")}''',
                 photos=[("rance-barrage.jpg", "Aerial view of the tidal barrage on the Rance and of Saint-Malo."), ("powerbuoy.jpg", "A PB40 PowerBuoy, built by Ocean Power Technologies, floating off the coast."),
                         ("pelamis-emec.jpg", "A Pelamis wave energy converter at the European Marine Energy Centre.")],
                 paths_nav="Kinds", paths_title="The kinds of energy",
                 paths=[("Tidal barrage", f"La Rance (240 MW) and Sihwa (254 MW) make up IRENA's whole global total.{cite(10)}"),
                        ("Tidal stream", f"MeyGen in Scotland has 6 MW operating and has won support for 59 MW more.{cite(13)}"),
                        ("Wave energy", f"Eco Wave Power's 2025 revenue was $38,000. Ocean Power Technologies' fiscal 2026 revenue was about $4.1 million.{cite(16)}{cite(15)}"),
                        ("Geothermal", f"About 15 GW worldwide. Ormat's geothermal and solar plants total 1,340 MW.{cite(12)}{cite(17)}")],
                 limits=[("Tiny scale", f"Ocean energy added 1.6 MW in 2024.{cite(11)}"),
                         ("Small revenues", f"Eco Wave Power had $38,000 of revenue in 2025 and Ocean Power Technologies lost $43.7 million in fiscal 2026, on secondary summaries.{cite(16)}{cite(15)}"),
                         ("Subsidy dependence", f"UK tidal stream contracts pay £172 per megawatt hour in the sixth round.{cite(14)}"),
                         ("New geothermal is unproven at scale", f"Fervo had $140,000 of revenue in 2025 and is still building its first large plant.{cite(18)}")],
                 history=[("Decades ago", f"La Rance and Sihwa tidal barrages begin generating.{cite(10)}", ""),
                          ("2025", f"Eco Wave Power lowers its floaters in the Port of Los Angeles.{cite(16)}", ""),
                          ("12 May 2026", f"Fervo Energy prices its IPO at $27 a share.{cite(21)}", "big"),
                          ("2026", f"Ormat agrees up to 150 MW for Google and about 13 MW for Switch.{cite(17)} The UK's sixth round awards 28 MW to tidal stream.{cite(14)}", "big"),
                          ("2027 to 2029", f"MeyGen's next phases are due.{cite(13)}", "fut")],
                 key=("Geothermal pays, the sea mostly does not yet", "The sea holds enormous energy and small revenue. Geothermal has real revenue, and data centres are the new buyers.")),
        ch2=dict(cards=[("What changed", f"Data centres are signing long contracts for geothermal power.{cite(17)}"),
                        ("What has not", f"Ocean energy is essentially unchanged: 494 MW, of which 1.6 MW was added in 2024.{cite(10)}{cite(11)}"),
                        ("What is new", f"Fervo, a geothermal developer, raised about $2.2 billion on the stock market in May 2026.{cite(21)}")],
                 photo=("geothermal-us.jpg", "A geothermal power plant at Geyserville in the United States."),
                 key=("Heat is winning over waves", "The money and the contracts are in geothermal. Waves and tides are still pilots, apart from the old barrages.")),
        ch3=dict(sub="Our judgement from the pipeline. Not a forecast.",
                 timeline=[("Now: geothermal contracts", f"Ormat signed agreements with Google and Switch in early 2026.{cite(17)}", "fut"),
                           ("2027 to 2029: tidal stream", f"MeyGen's next phases are due, with 59 MW awarded.{cite(13)}", "fut"),
                           ("2026: Fervo's Cape Station", f"The first 500 MW phase is under construction in Utah.{cite(18)}", "fut")],
                 ireland=[("The test site", f"SEAI is developing the Atlantic Marine Energy Test Site off Annagh Head, Belmullet, County Mayo, for full-scale wave devices and floating wind.{cite(19)}"),
                          ("Other sites", f"Ireland also has test facilities in Cork and Galway Bay.{cite(20)}"),
                          ("The watch", "Irish activity is in testing. We found no operating Irish wave or tidal plant.")],
                 prepare=[("As a citizen", "Expect wind and storage, not waves, to supply Irish power this decade."),
                          ("As a business", "Data-centre buyers are signing geothermal contracts abroad. Watch whether that spreads to Europe."),
                          ("As an investor", "The wave names have tiny revenues. The geothermal names are very different from each other.")],
                 key=("Geothermal now, tides later", "The near term is geothermal contracts. Tidal stream is next. Waves are furthest away.")),
        ch4=dict(sub="Two wave names, an established geothermal producer and a new, large geothermal bet.",
                 extra="", prices_title="Share prices since listing", prices_blurb="Four listed names in this sector, with Nvidia for scale.",
                 booms_caption="Log scale, from weekly closes, adjusted for splits. Fervo has traded for only about five months.",
                 ladder_caption="Geothermal is on the upper rungs. Wave energy is on the second.",
                 good=["A signed contract with a price.", "A first plant runs for a year.", "Costs per megawatt fall with each plant.", "Revenue grows without share sales."],
                 bad=["A pilot is described as a project.", "Revenue is a few thousand dollars.", "A newly listed share falls well below its issue price.", "Funding comes only from selling shares."],
                 map_key='<span><i style="border-color:var(--teal)"></i>plants, policy or test sites</span><span><i style="border-color:var(--violet)"></i>partner</span><span><i style="border-color:var(--red)"></i>none</span>',
                 key=("One real business, three promises", "Ormat has revenue and contracts. The other three are pilots or a very large build with no revenue yet.")),
        ch5=dict(sub="Scale, survival at sea, price and money.",
                 cards=[("Scale", f"Ocean energy added 1.6 MW in 2024.{cite(11)}"),
                        ("Revenue", f"Eco Wave Power had $38,000 of revenue in 2025.{cite(16)}"),
                        ("Losses", f"Ocean Power Technologies lost $43.7 million in fiscal 2026, on secondary summaries.{cite(15)}"),
                        ("Support", f"UK tidal stream contracts depend on a guaranteed £172 per megawatt hour.{cite(14)}"),
                        ("Pre-revenue risk", f"Fervo had $140,000 of revenue and a $57.8 million loss in 2025.{cite(18)}"),
                        ("Curtailment", f"Ormat's gross margin fell to 27.6% in 2025, partly because of curtailment at US plants.{cite(17)}")],
                 photo=("francis-runner.jpg", "The runner of the Francis turbine at the Imatrankoski power plant."),
                 line="A device has to survive the sea or the rock, and sell power at a price that beats wind with storage. Only the oldest tidal plants and the geothermal industry have shown that for years.",
                 key=("Survival and price", "Waves and tides must survive and be cheap. Geothermal must prove new drilling methods work at scale.")),
        ch6=dict(n_word="four", expect=[("Likely, about 75%", "More geothermal contracts with data centres. More tidal stream built in Scotland. More pilots of wave devices."),
                                        ("Even odds, about 50%", "Fervo's first Cape Station phase delivers power to a customer."),
                                        ("Unlikely, under 10%", "Wave energy supplies a meaningful share of any national grid.")],
                 pull="The sea will stay a research subject for a while. The heat under our feet is already a business.",
                 why=[("Why we lean that way", "Our scenarios put the chance of each company ending the three years below today's price at {lo} to {hi}. Several of these shares are tiny and volatile."),
                      ("Who is exposed", "Wave companies with very small revenue, and any company that must keep raising money."),
                      ("If it goes right", "Cape Station delivers on time and costs fall, and geothermal wins a larger share of new demand."),
                      ("The test", "For each claim, ask how many megawatts are in the water or the ground, and what price a buyer pays.")],
                 mind="A tidal or wave array running for years at a stated price. Cape Station's first power. A change in UK tidal support.",
                 key=("Geothermal rises. The sea waits", "We expect geothermal to keep winning contracts and the sea to keep running pilots.")),
    )
    return _gen.build(C, cite)
