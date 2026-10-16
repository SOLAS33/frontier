"""Technical depth for Frontier Orbit: numbers, kinds of space business, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

ORBIT_REFS = [
    (10, "Space Foundation (2025). The Space Report 2025 Q2: record $613 billion global space economy for 2024.", "https://www.spacefoundation.org/2025/07/22/the-space-report-2025-q2/"),
    (11, "Satellite Today (2026). BryceTech report shows SpaceX accounted for 50% of launches in 2025.", "https://satellitetoday.com/launch/2026/04/10/brycetech-report-shows-spacex-accounted-for-50-of-launches-in-2025/"),
    (12, "MarketBeat (2026). Rocket Lab delivers record results but Neutron delay weighs on shares.", "https://www.marketbeat.com/articles/rklb-delivers-record-results-but-neutron-delay-weighs-on-shares/"),
    (13, "AST SpaceMobile (2026). Business update and first quarter 2026 results, 11 May 2026.", "https://www.sec.gov/Archives/edgar/data/0001780312/000119312526216946/asts-ex99_1.htm"),
    (22, "Satellite PRO ME (2026). AST SpaceMobile loses BlueBird 7 satellite following launch orbit issue.", "https://satelliteprome.com/news/ast-spacemobile-loses-bluebird-7-satellite-following-launch-orbit-issue/"),
    (14, "Business Wire (2026). Planet reports financial results for fourth quarter and full fiscal year 2026.", "https://www.businesswire.com/news/home/20260319782110/en/Planet-Reports-Financial-Results-for-Fourth-Quarter-and-Full-Fiscal-Year-2026"),
    (15, "Intuitive Machines (2026). Fourth quarter and full-year 2025 financial results.", "https://investors.intuitivemachines.com/news-releases/news-release-details/intuitive-machines-reports-fourth-quarter-and-full-year-2025"),
    (16, "Mexico Business News (2025). IM-2 lunar lander tips over after landing.", "https://mexicobusiness.news/aerospace/news/im-2-lunar-lander-tips-over-after-landing-revenue-rises-14"),
    (17, "Business Wire (2026). Redwire reports fourth quarter and full year 2025 financial results.", "https://www.businesswire.com/news/home/20260225862857/en/Redwire-Corporation-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results-Achieves-Top-End-of-2025-Revenue-Guidance-Range-with-Record-Contracted-Backlog"),
    (18, "WTTW (2026). Artemis II astronauts return from the Moon with a splashdown to close out a record-breaking lunar voyage.", "https://news.wttw.com/2026/04/10/artemis-ii-astronauts-return-moon-splashdown-close-out-record-breaking-lunar-voyage"),
    (19, "TechCentral (2025). Ireland commits 170 million euros to European space programmes.", "https://www.techcentral.ie/ireland-commits-e170m-to-european-space-programmes/"),
    (20, "Enterprise Ireland. Irish companies secure record 24 million euros in ESA contracts.", "https://www.enterprise-ireland.com/en/news/irish-companies-secure-record-24-million-in-european-space-agency-esa-contracts-as-ireland-marks-50-years-of-esa-membership"),
    (21, "Crypto Briefing (2026). SpaceX hits 12 million Starlink subscribers.", "https://cryptobriefing.com/spacex-starlink-12-million-subscribers/"),
]


def orbit_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Global space economy, 2024", "$613 billion, up 7.8%" + cite(10), "Government budgets were about $132 billion of it. The Space Foundation says the economy could pass $1 trillion as soon as 2032"],
        ["Orbital launches, 2025", "About 325 (BryceTech counted 325, another count 324)" + cite(11), "A record. Counts differ by a few depending on how failures are counted"],
        ["SpaceX launches, 2025", "165, nearly half of all orbital launches" + cite(11), "Trackers count about 122 of them as Starlink launches"],
        ["Rocket Lab, 2025", "Revenue $601.8 million, 21 Electron launches, backlog $1.85 billion" + cite(12), "Its Neutron rocket slipped to late 2026 after a tank failed in a test"],
        ["Planet Labs, fiscal 2026", "Revenue $307.7 million, up 26%. Backlog over $900 million" + cite(14), "Its first full year with positive adjusted EBITDA and free cash flow"],
        ["Redwire, 2025", "Revenue $335.4 million. Backlog $411.2 million. Net loss $226.6 million" + cite(17), "Guides 450 to 500 million dollars of revenue for 2026"],
        ["Artemis II, April 2026", "Launched 1 April, splashed down 10 April, reached about 252,756 miles from Earth" + cite(18), "A new distance record for a crewed spacecraft. It flew around the Moon and did not land"],
    ])
    kinds = _table(["Part of the business", "What it does", "Examples", "Status"], [
        ["Launch", "Puts payloads into orbit", "SpaceX. Rocket Lab (Electron, with Neutron planned)" + cite(11) + cite(12), "SpaceX flew about half of all launches in 2025"],
        ["Satellite services", "Sells data or connectivity from orbit", "Starlink. AST SpaceMobile. Planet Labs" + cite(13) + cite(14), "Planet is cash-positive. AST is still deploying"],
        ["Lunar landers", "Take cargo to the Moon", "Intuitive Machines" + cite(16), "IM-2 tipped over after landing in March 2025"],
        ["Space infrastructure and components", "Builds parts, docking systems and platforms", "Redwire" + cite(17), "Revenue growing, with net losses"],
        ["Crewed exploration", "Flies people beyond low Earth orbit", "NASA Artemis" + cite(18), "Artemis II flew in April 2026. NASA's stated goal is a landing from 2028"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["The first crewed lunar voyage since 1972", "Artemis II, 1 to 10 April 2026" + cite(18), _tag("ok"), "Four crew including Canada's Jeremy Hansen. It did not land"],
        ["A record 2025 for launches", "About 325 orbital launches" + cite(11), _tag("ok"), "SpaceX had 165 of them"],
        ["Electron's best year", "Rocket Lab, 21 successful launches in 2025" + cite(12), _tag("ok"), "All 21 succeeded, according to the company's results"],
        ["A direct-to-phone satellite network built out", "AST SpaceMobile, 2026: BlueBird 7 reached the wrong orbit on New Glenn" + cite(22), _tag("dis"), "The company said the altitude was too low to operate and the satellite would be deorbited. It targets about 45 BlueBirds in orbit in 2026" + cite(13)],
        ["A commercial lunar landing that stays upright", "Intuitive Machines IM-2 tipped over on 6 March 2025" + cite(16), _tag("dis"), "The company blamed altimeter signal problems and long shadows"],
        ["A new medium-lift rocket flying", "Rocket Lab Neutron, now planned for late 2026" + cite(12), _tag("tgt"), "A company target that has slipped"],
    ])
    gl = _gloss([
        ("Low Earth orbit", "Orbits a few hundred kilometres up, where most satellites and the space station fly."),
        ("Backlog", "Orders signed and not yet delivered or recognised as revenue."),
        ("Direct to cell", "A satellite that connects to an ordinary phone without a special dish."),
        ("Earth observation", "Satellites that photograph or measure the Earth."),
        ("Reusable rocket", "A rocket whose first stage lands and flies again."),
        ("Lander", "A spacecraft that lands on the Moon or another world."),
        ("Constellation", "A set of satellites working together."),
        ("CLPS", "NASA's Commercial Lunar Payload Services programme, which buys rides to the Moon from companies."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Most of the space economy is not rockets. It is satellites that sell connectivity, data and navigation, and the government budgets behind them.{cite(10)} A launch is a delivery service. In 2025 there were about 325 orbital launches, a record, and SpaceX flew 165 of them.{cite(11)}</p>
{nums}
<p class="cap wide">From the cited sources. Company results are for the periods shown.</p>
<h3 class="wide" id="s-types" data-nav="Parts" style="margin-top:36px">The parts of the business</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
