"""Technical depth for Frontier Chip: numbers, kinds of chip business, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

CHIP_REFS = [
    (10, "Semiconductor Industry Association (2026). Global annual semiconductor sales increase 25.6% to $791.7 billion in 2025.", "https://www.semiconductors.org/global-annual-semiconductor-sales-increase-25-6-to-791-7-billion-in-2025/"),
    (11, "TSMC (2026). TSMC reports fourth quarter EPS of NT$19.50.", "https://pr.tsmc.com/english/news/3281"),
    (12, "ASML (2026). 2025 annual report: financials.", "https://www.asml.com/en/investors/annual-report/2025/financials"),
    (13, "Intel. Q4 2025 results as summarised by Converge Digest.", "https://convergedigest.com/intel-closes-2025-flat-as-data-center-and-ai-revenue-grows/"),
    (14, "Intel. Fab 34 and the Leixlip campus. The Irish Times (2023).", "https://irishtimes.com/business/2023/09/29/intel-opens-advanced-chip-facility-in-leixlip"),
    (15, "Lumentum (2026). Fourth quarter and full fiscal year 2026 results.", "https://s21.q4cdn.com/377324469/files/doc_news/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results-2026.pdf"),
    (16, "Nasdaq (2025). Applied Materials sets revenue record.", "https://www.nasdaq.com/articles/applied-materials-sets-revenue-record"),
    (17, "BetaNews (2025). US government to acquire nearly 10 percent stake in Intel.", "https://betanews.com/2025/08/23/us-government-to-acquire-nearly-10-percent-stake-in-intel/"),
    (18, "SiliconANGLE (2025). Nvidia faces $5.5B sales hit due to new constraints on H20 chip exports to China.", "https://siliconangle.com/2025/04/15/nvidia-faces-5-5b-sales-hit-due-new-constraints-h20-chip-exports-china/"),
    (20, "CEPA. Transatlantic chips alliance or chips battle (US CHIPS Act and EU Chips Act sums).", "https://cepa.org/article/transatlantic-chips-alliance-or-chips-battle/"),
    (21, "TechCrunch (2022). The future of the microchip industry and Made in America.", "https://techcrunch.com/2022/08/13/is-the-future-of-the-microchip-industry-going-to-be-made-in-america/"),
    (19, "Yahoo Finance / Reuters. Intel orders ASML system (High-NA EUV).", "https://tech.yahoo.com/general/articles/intel-orders-asml-system-well-125058207.html"),
]


def chip_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["World chip sales, 2025", "$791.7 billion, up 25.6% from $630.5 billion in 2024" + cite(10), "The Semiconductor Industry Association projects roughly $1 trillion for 2026"],
        ["Logic and memory", "Logic $301.9 billion. Memory $223.1 billion" + cite(10), "Logic is the largest category and memory the second"],
        ["TSMC revenue, fourth quarter 2025", "US$33.73 billion, with a 62.3% gross margin" + cite(11), "About 77% of wafer revenue came from chips made on 7 nanometre processes or smaller"],
        ["TSMC wafer revenue by process, Q4 2025", "3nm 28%, 5nm 35%, 7nm 14%" + cite(11), "The smallest processes bring most of the money"],
        ["TSMC capital budget for 2026", "US$52 billion to US$56 billion" + cite(11), "Spending on new factories and equipment"],
        ["ASML net sales, 2025", "32.7 billion euros. EUV system sales 11.6 billion euros, from 48 systems" + cite(12), "Its undelivered orders were 38.8 billion euros at the end of 2025"],
        ["Applied Materials revenue, fiscal 2025", "About $28.4 billion, with China about 29% of revenue" + cite(16), "China's share was 45% at its peak in fiscal 2024"],
    ])
    kinds = _table(["Part of the business", "What it does", "Examples", "Status"], [
        ["Foundry", "Makes chips designed by other firms", "TSMC. Intel Foundry" + cite(11) + cite(13), "TSMC is profitable at a 62.3% gross margin. Intel Foundry still lost money in 2025" + cite(13)],
        ["Chip design and sale", "Designs and sells processors", "Intel, Nvidia", "Intel's 2025 revenue was $52.9 billion, flat" + cite(13)],
        ["Lithography", "Prints the patterns onto silicon", "ASML is the only maker of EUV machines" + cite(19), "High-NA machines are estimated at $300 million or more each. ASML does not publish prices" + cite(19)],
        ["Deposition, etch and other equipment", "Builds the layers of a chip", "Applied Materials" + cite(16), "Record revenue in fiscal 2025"],
        ["Photonics", "Moves data as light, with lasers and optics", "Lumentum" + cite(15), "Fiscal 2026 revenue was $3.014 billion, up 83%"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Volume production at 2 nanometres", "TSMC, fourth quarter 2025", _tag("ok"), "Sources agree that it began. Yield figures are the company's own"],
        ["EUV lithography in Ireland", "Intel Fab 34, Leixlip, opened September 2023, a 17 billion euro investment" + cite(14), _tag("ok"), "Started with Intel 4, which uses EUV"],
        ["First Intel 18A products", "Panther Lake, ramping in 2025 and 2026" + cite(13), _tag("ok"), "Intel's CFO said yields were improving but below target"],
        ["US government stake in a chipmaker", "Intel, August 2025: 433.3 million shares at $20.47, about 9.9%" + cite(17), _tag("ok"), "Funded by CHIPS Act grants not yet paid and another award"],
        ["Export licence needed for a China-specific AI chip", "Nvidia H20, April 2025" + cite(18), _tag("dis"), "The US later began issuing licences, in August 2025"],
        ["A chip company with a trillion-dollar year", "World sales, 2026 projection" + cite(10), _tag("tgt"), "An industry projection, not a result"],
    ])
    gl = _gloss([
        ("Foundry", "A factory that makes chips for other companies to a customer's design."),
        ("Logic and memory", "Logic chips compute. Memory chips store data. They are the two biggest categories."),
        ("Process node", "A name for a generation of manufacturing technology, such as 3 nanometre. Companies use it as a label for the generation."),
        ("EUV", "Extreme ultraviolet lithography: the machines that print the finest patterns on advanced chips."),
        ("Wafer", "A thin disc of silicon on which many chips are made at once."),
        ("Photonics", "Moving and processing information with light instead of electric current."),
        ("Co-packaged optics", "Putting the lasers and optics inside the chip package, to move data between chips with less power."),
        ("Capex", "Money spent on factories and equipment."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A chip is made by printing patterns onto a silicon wafer, layer after layer, then cutting the wafer into chips. The finest patterns are printed with extreme ultraviolet light by machines that ASML alone makes.{cite(19)} A foundry such as TSMC makes chips to other firms' designs. Intel designs chips and also runs a foundry business.{cite(11)}{cite(13)}</p>
{nums}
<p class="cap wide">From the cited sources. Company results are for the periods shown. Machine prices are press estimates.</p>
<h3 class="wide" id="s-types" data-nav="Parts" style="margin-top:36px">The parts of the business</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
