"""Technical depth for Frontier Tide: numbers, kinds of energy harvest, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

TIDE_REFS = [
    (10, "IRENA. Ocean energy.", "https://www.irena.org/ocean"),
    (11, "REN21. Global Status Report 2025: ocean power.", "https://www.ren21.net/gsr-2025/technologies/ocean-power/"),
    (12, "IRENA (2026). Renewable capacity highlights 2026, as reported by Mercom.", "https://mercomindia.com/solar-and-wind-additions-push-global-renewable-energy-capacity-to-5-2-tw"),
    (13, "Tethys (PNNL). MeyGen tidal energy project.", "https://tethys.pnnl.gov/project-sites/meygen-tidal-energy-project"),
    (14, "Marine Energy Council / Offshore Energy. UK Allocation Round 6 results for tidal stream.", "https://offshore-energy.biz/?p=732651"),
    (15, "Ocean Power Technologies (2026). Fiscal 2026 results, Form 8-K.", "https://www.sec.gov/Archives/edgar/data/0001378140/000149315226034425/ex99-2.htm"),
    (16, "Eco Wave Power (2026). Strong operational progress and 2025 annual report on Form 20-F.", "https://www.newsfilecorp.com/release/288248/Eco-Wave-Power-Reports-Strong-Operational-Progress-and-Files-2025-Annual-Report-on-Form-20F"),
    (17, "Ormat Technologies (2026). Fourth quarter and year-end 2025 financial results.", "https://investor.ormat.com/news-events/news/news-details/2026/Ormat-Technologies-Reports-Fourth-Quarter-and-Year-End-2025-Financial-Results/default.aspx"),
    (18, "Quartz (2026). Fervo Energy IPO Nasdaq debut.", "https://qz.com/fervo-energy-ipo-nasdaq-debut-geothermal-051426"),
    (19, "Mayo County Council. Atlantic Marine Energy Test Site (AMETS).", "https://mayo.ie/marine/offshore-projects/amets"),
    (20, "Ocean Energy Ireland. Atlantic Marine Energy Test Site and Irish test facilities.", "https://www.oceanenergyireland.com/test-facilities/atlantic-marine-energy-test-site"),
    (21, "Barchart (2026). Fervo Energy announces pricing of its upsized initial public offering.", "https://www.barchart.com/story/news/1890062/fervo-energy-announces-pricing-of-its-upsized-initial-public-offering"),
]


def tide_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Ocean energy installed worldwide, end of 2024", "494 megawatts (IRENA). REN21 estimates about 513 MW" + cite(10) + cite(11), "IRENA's total equals two tidal barrages: La Rance in France (240 MW) and Sihwa in South Korea (254 MW)"],
        ["Ocean energy added in 2024", "1.6 megawatts" + cite(11), "Almost nothing, against the whole installed base"],
        ["Tidal stream output in Europe, 2024", "13.4 gigawatt hours" + cite(11), "Cumulative European tidal stream output was 106 GWh"],
        ["MeyGen, Scotland", "6 megawatts in operation, with 59 MW more awarded contracts for 2027 to 2029" + cite(13), "The next phase is in addition to the 6 MW operating"],
        ["UK sixth allocation round, tidal stream", "28 megawatts at £172 per megawatt hour" + cite(14), "The third round in a row with a ringfence for tidal stream"],
        ["Geothermal capacity worldwide", "About 15 GW at the end of 2024 and 16 GW at the end of 2025" + cite(12), "It grew 1.7% in 2025, by 0.3 GW"],
        ["Ormat, 2025", "Revenue $989.6 million. Geothermal and solar portfolio 1,340 MW" + cite(17), "A 15-year agreement of up to 150 MW to supply Google's data centres through NV Energy"],
    ])
    kinds = _table(["Kind of energy", "How it works", "Examples", "Status"], [
        ["Tidal barrage", "A dam across an estuary lets the tide drive turbines", "La Rance (France), Sihwa (South Korea)" + cite(10), "Built decades ago. These two make up IRENA's whole global total"],
        ["Tidal stream", "Turbines on the seabed or floating, driven by tidal currents", "MeyGen (Scotland). Orbital's Eday project (Orkney)" + cite(13) + cite(14), "Small and growing, helped by UK auctions"],
        ["Wave energy", "Floats or buoys move with waves and drive a generator", "Ocean Power Technologies, Eco Wave Power" + cite(15) + cite(16), "Pilots. Very small revenues"],
        ["Geothermal", "Hot rock or water drives turbines", "Ormat's plants. Fervo's Cape Station in Utah" + cite(17) + cite(18), "About 16 GW worldwide. New technology is being tested"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Tidal barrage power", "La Rance and Sihwa", _tag("ok"), "Together 494 MW, the whole IRENA total" + cite(10)],
        ["A tidal stream array with contracts for more", "MeyGen, 6 MW operating and 59 MW awarded support" + cite(13), _tag("ok"), "Phases due in 2027, 2028 and 2029"],
        ["Tidal stream gets its own UK auction ringfence", "UK rounds 4, 5 and 6" + cite(14), _tag("ok"), "28 MW awarded in round 6 at £172 per megawatt hour"],
        ["A wave pilot in a US port", "Eco Wave Power, Port of Los Angeles, floaters lowered in 2025" + cite(16), _tag("dis"), "The company's 2025 revenue was $38,000"],
        ["A geothermal company's listing", "Fervo Energy, priced 12 May 2026 at $27 a share" + cite(21), _tag("ok"), "It raised about $2.2 billion including the extra shares, on 2025 revenue of $140,000" + cite(18)],
        ["Data-centre geothermal contracts", "Ormat with Google (up to 150 MW) and Switch (about 13 MW), 2026" + cite(17), _tag("ok"), "Fifteen and twenty year agreements"],
    ])
    gl = _gloss([
        ("Tidal barrage", "A dam across a tidal estuary with turbines in it."),
        ("Tidal stream", "Turbines placed in fast tidal currents, like underwater wind turbines."),
        ("Wave energy converter", "A device that turns the motion of waves into electricity."),
        ("Geothermal", "Energy from heat inside the Earth."),
        ("Enhanced geothermal", "Drilling into hot dry rock and creating the pathways for water, so that water can carry heat to the surface."),
        ("Contract for Difference", "A UK scheme that guarantees a generator a fixed price per megawatt hour."),
        ("Capacity", "The most power a plant can produce at once, in megawatts."),
        ("Offtake", "A contract to buy a plant's power. It is a promise to buy, not proof the plant exists."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Ocean energy is tiny. The world had 494 megawatts of it at the end of 2024, and that is just two tidal barrages built decades ago.{cite(10)} Tidal stream and wave devices added 1.6 megawatts in 2024.{cite(11)} Geothermal is far larger, at about 15 gigawatts, and is the part of this sector that data centres are buying.{cite(12)}{cite(17)}</p>
{nums}
<p class="cap wide">From the cited sources. Totals differ a little between agencies because of how they count.</p>
<h3 class="wide" id="s-types" data-nav="Kinds" style="margin-top:36px">The kinds of energy</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
