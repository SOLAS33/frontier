"""Technical depth for Frontier Mine: numbers, kinds of mineral business, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

MINE_REFS = [
    (10, "International Energy Agency. Rare earth elements: executive summary.", "https://www.iea.org/reports/rare-earth-elements/executive-summary"),
    (11, "Mining.com (2025). MP Materials lands multi-billion Pentagon deal.", "https://www.mining.com/mp-materials-lands-multi-billion-pentagon-deal/"),
    (12, "MP Materials (2026). Fourth quarter and full year 2025 results.", "https://mpmaterials.com/news/mp-materials-reports-fourth-quarter-and-full-year-2025-results"),
    (13, "Mining.com. Lithium Americas gets record $2.26 billion loan for Thacker Pass.", "https://www.mining.com/lithium-americas-gets-record-2-26-billion-loan-for-thacker-pass/"),
    (14, "Mining Weekly (2026). Lithium Americas sets up to $1.6bn 2026 capex for Thacker Pass.", "https://www.miningweekly.com/article/lithium-americas-sets-up-to-16bn-2026-capex-for-thacker-pass-2026-02-20"),
    (15, "Nasdaq (2025). Freeport-McMoRan plans 2026 Grasberg restart after deadly mud rush.", "https://www.nasdaq.com/articles/freeport-mcmoran-plans-2026-grasberg-restart-after-deadly-mud-rush"),
    (16, "Freeport-McMoRan. First quarter 2026 results, Form 8-K.", "https://www.sec.gov/Archives/edgar/data/0000831259/000083125926000021/a1q2026exhibit991.htm"),
    (17, "Cruxinvestor. Energy Fuels' White Mesa Mill produces first US terbium oxide in decades.", "https://www.cruxinvestor.com/posts/energy-fuels-white-mesa-mill-produces-first-us-terbium-oxide-in-decades-targets-commercial-heavy-rare-earth-output-by-2027"),
    (18, "Albemarle (2026). Fourth quarter and full year 2025 results.", "https://www.albemarle.com/au/en/news/albemarle-reports-fourth-quarter-and-full-year-2025-results"),
    (19, "Project Blue (2025). China to suspend rare earth export controls for one year.", "https://projectblue.com/blue/news-analysis/1356/china-to-suspend-rare-earth-export-controls-for-one-year-"),
    (20, "Hogan Lovells. The Critical Raw Materials Act: the EU wants to reduce dependency.", "https://hoganlovells.com/en/publications/critical-raw-materials-act-the-european-union-wants-to-reduce-dependency"),
    (21, "Boliden. Boliden Tara.", "https://www.boliden.com/operations/mines/boliden-tara"),
    (22, "Mining.com (2024). Boliden to restart Europe's largest zinc mine.", "https://mining.com/?p=1149466"),
]


def mine_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["China's share of magnet rare earths, 2024", "60% of mined output, 91% of refined output, and 94% of sintered permanent magnets" + cite(10), "Refining and magnet-making are more concentrated than mining"],
        ["MP Materials, 2025", "A record 2,599 tonnes of NdPr oxide, up 101%, and 50,692 tonnes of rare earth oxide in concentrate, up 12%" + cite(12), "It made its first magnets on commercial equipment at Independence in the fourth quarter"],
        ["US price floor for NdPr", "$110 per kilogram under a 10-year agreement with the Department of Defense" + cite(11), "The government also bought $400 million of preferred stock"],
        ["Thacker Pass loan", "About $2.26 billion from the US Department of Energy" + cite(13), "Lithium Americas guides $1.3 billion to $1.6 billion of capital spending for 2026" + cite(14)],
        ["Freeport's Grasberg, September 2025", "About 800,000 tonnes of wet material entered the block cave and seven workers died" + cite(15), "Freeport cut its 2026 copper sales estimate from 3.4 billion to about 3.1 billion pounds" + cite(16)],
        ["Albemarle, 2025", "Net sales about $5.1 billion on one summary, with lower lithium prices cutting energy storage profit" + cite(18), "Its 2026 outlook is given for lithium prices of $10, $20 and $30 per kilogram"],
        ["EU 2030 benchmarks", "10% of annual consumption from EU extraction, 40% from processing and 25% from recycling" + cite(20), "No more than 65% from any one non-EU country for each strategic material"],
    ])
    kinds = _table(["Part of the business", "What it does", "Examples", "Status"], [
        ["Rare earths", "Mines and separates the elements used in magnets", "MP Materials. Energy Fuels" + cite(12) + cite(17), "MP produced a record 2,599 tonnes of NdPr oxide in 2025"],
        ["Lithium", "Produces the metal for batteries", "Albemarle. Lithium Americas" + cite(18) + cite(13), "Prices fell in 2025. Thacker Pass is under construction"],
        ["Copper", "The metal in all wiring and motors", "Freeport-McMoRan" + cite(15), "Its biggest mine had a deadly accident in 2025"],
        ["Heavy rare earths", "Dysprosium and terbium for high-temperature magnets", "Energy Fuels at White Mesa" + cite(17), "First terbium oxide in March 2026, at small scale"],
        ["Zinc and base metals in Europe", "Mining inside the EU", "Boliden Tara Mines, near Navan, Ireland" + cite(21), "Halted in 2023, reopened around the end of 2024" + cite(22)],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["A US government stake and price floor for a rare earth miner", "MP Materials and the Department of Defense, July 2025" + cite(11), _tag("ok"), "$400 million of preferred stock, a $150 million loan, and a 10-year NdPr price floor at $110 per kilogram"],
        ["US magnets from a US mine's own output", "MP Materials, first magnets on commercial equipment, fourth quarter 2025" + cite(12), _tag("ok"), "A 10X magnet plant is planned in Texas"],
        ["A major mine accident cuts a big supplier", "Freeport's Grasberg, 8 September 2025" + cite(15), _tag("dis"), "Phased restart. Block 1 is targeted for 2027"],
        ["A US lithium mine under construction", "Thacker Pass, Nevada. Lithium Americas holds 62% and GM 38%" + cite(13), _tag("dis"), "Mechanical completion targeted for late 2027" + cite(14)],
        ["China pauses its October 2025 export-control expansion", "Suspended until 10 November 2026" + cite(19), _tag("dis"), "The pause expires soon. The April 2025 licensing remains"],
        ["Heavy rare earths separated outside China at small scale", "Energy Fuels, terbium oxide in March 2026" + cite(17), _tag("tgt"), "Commercial output is targeted for later"],
    ])
    gl = _gloss([
        ("NdPr", "Neodymium and praseodymium, the rare earths used in the strongest permanent magnets."),
        ("Heavy rare earths", "Dysprosium and terbium, which let magnets work at high temperatures."),
        ("Rare earth oxide", "A refined powder of one or more rare earth elements."),
        ("Sintered magnet", "A strong permanent magnet made by pressing and heating powder."),
        ("Price floor", "A guaranteed minimum price for what a producer sells."),
        ("Block cave", "An underground mining method that lets ore collapse under its own weight."),
        ("LCE", "Lithium carbonate equivalent: the standard unit for lithium."),
        ("Strategic project", "An EU-designated project that gets faster permitting and easier access to finance." + cite(20)),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Mining is only the first step. Refining and turning minerals into magnets is where the concentration lies. China mined 60% of the world's magnet rare earths in 2024, refined 91% and made 94% of sintered permanent magnets.{cite(10)} Governments in the US and EU are now paying to build a second supply chain: a price floor and an equity stake for MP Materials, and benchmarks for extraction, processing and recycling in the EU.{cite(11)}{cite(20)}</p>
{nums}
<p class="cap wide">From the cited sources. Company figures are for the periods shown. Some come from summaries and are marked as such.</p>
<h3 class="wide" id="s-types" data-nav="Parts" style="margin-top:36px">The parts of the business</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
