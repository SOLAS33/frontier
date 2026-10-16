"""Technical depth for Frontier Carbon: numbers, forms of carbon, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

CARBON_REFS = [
    (10, "CORDIS (European Commission). The dawn of the graphene age.", "https://www.cordis.europa.eu/article/id/400867-the-dawn-of-the-graphene-age"),
    (11, "IEEE Spectrum. Europe has invested 1 billion euros into graphene but for what", "https://spectrum.ieee.org/europe-has-invested-1-billion-into-graphenebut-for-what"),
    (12, "Graphene Flagship. Bringing graphene and new materials to market.", "https://graphene-flagship.eu/materials/news/bringing-graphene-and-new-materials-to-market/"),
    (13, "Chemistry World. Graphene and the 2010 Nobel Prize.", "https://www.chemistryworld.com/features/cubanes-help-drugs-take-the-strain/4018554.article"),
    (14, "Trinity College Dublin. AMBER at Trinity in world first graphene innovation.", "https://www.tcd.ie/news_events/articles/amber-at-trinity-in-world-first-graphene-innovation/"),
    (15, "Chemical Engineering. LG Chem to expand carbon nanotube production capacity.", "https://www.chemengonline.com/lg-chem-to-expand-carbon-nanotube-production-capacity/"),
    (16, "Fastmarkets. China to impose export controls on graphite-related items.", "https://www.fastmarkets.com/insights/china-to-impose-export-controls-on-graphite-related-items/"),
    (17, "S&P Global (2025). US determines China is dumping graphite, imposes 93.5% tariff.", "https://www.spglobal.com/energy/en/news-research/latest-news/metals/071725-us-determines-china-is-dumping-graphite-imposes-935-tariff"),
    (18, "Novonix. Annual report on Form 20-F for 2025.", "https://www.sec.gov/Archives/edgar/data/1859795/000119312526072814/nvx-20251231.htm"),
    (19, "Westwater Resources (2026). Provides commercial update.", "https://www.streetinsider.com/Business+Wire/Westwater+Resources+Provides+Commercial+Update/26260221.html"),
    (20, "Mining Weekly (2026). NMG concludes funding package for Matawinie Phase 2 development.", "https://www.miningweekly.com/article/nmg-concludes-funding-package-for-matawinie-phase-2-development-2026-04-10"),
    (21, "Nouveau Monde Graphite. Form 6-K, 2026.", "https://www.sec.gov/Archives/edgar/data/0001649752/000110465926095952/tm2623165d1_ex99-1.htm"),
]


def carbon_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["The Graphene Flagship", "A 1 billion euro, ten-year European programme launched in 2013" + cite(11), "Its own impact study credited 5.8 billion euros of added value. The Commission's direct investment was 401 million euros" + cite(12)],
        ["Graphene products at the halfway point", "Over 25 commercial products reported by the Flagship. IEEE Spectrum counted nine companies and 46 products" + cite(11), "A modest but real result. Critics said graphene had not lived up to expectations"],
        ["Natural flake graphite output from China, 2022", "About 70% of the world's total" + cite(16), "China also supplied almost 96% of synthetic graphite anode material"],
        ["China's graphite export licence", "In force from 1 December 2023" + cite(16), "Exports of certain graphite and graphite products need a licence"],
        ["US anti-dumping duty on Chinese anode graphite", "93.5% preliminary rate, July 2025. Final countervailing duty on natural graphite anode material 66.68% in February 2026" + cite(17), "Affects imports worth about $347 million in 2023"],
        ["LG Chem carbon nanotube capacity", "A plan to reach 6,100 tonnes a year by early 2025" + cite(15), "A 2023 plan. We could not confirm the plant started"],
        ["Novonix cash, end of 2025", "$79.9 million, with $42.3 million claimed to date from a $100 million US Department of Energy grant" + cite(18), "Management said more funding would be needed"],
    ])
    kinds = _table(["Form of carbon", "What it is", "Where it is used", "Status"], [
        ["Graphene", "A single layer of carbon atoms in a honeycomb", "Composites, coatings, research", "Isolated in Manchester. Awarded the Nobel Prize in 2010" + cite(13)],
        ["Carbon nanotubes", "Rolled-up graphene sheets", "Conductive additive in lithium-ion batteries", "LG Chem says nanotubes cut the additive needed by about 30% and raise conductivity by about 10% against carbon black" + cite(15)],
        ["Graphite", "Stacked layers of carbon", "Battery anodes", "Supply is concentrated in China" + cite(16)],
        ["Carbon fibre", "Strong, light fibres of carbon", "Aircraft, wind blades, sport", "Made at scale. The US Department of Energy runs a carbon fibre technology facility at Oak Ridge"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Graphene isolated and a Nobel Prize", "Manchester, prize in 2010" + cite(13), _tag("ok"), "Isolated with sticky tape"],
        ["Graphene made in bulk by mixing", "AMBER at Trinity College Dublin, 2014" + cite(14), _tag("ok"), "A high-shear mixing method for defect-free graphene that the team said could scale to hundreds of litres"],
        ["A ten-year programme to take graphene to market", "Graphene Flagship, 2013 to 2023" + cite(11), _tag("dis"), "Dozens of products, with lack of standardisation named as an obstacle" + cite(11)],
        ["Graphite anode supply outside China", "Novonix, Westwater, Nouveau Monde: none found at full scale yet", _tag("tgt"), "Offtake deals have been ended and restructured. See chapter 4"],
        ["Export controls and trade duties on graphite", "China's licences from December 2023. US duties in 2025 and 2026" + cite(16) + cite(17), _tag("ok"), "Both are in force"],
    ])
    gl = _gloss([
        ("Graphene", "One layer of carbon atoms in a honeycomb. Very thin, strong and conductive."),
        ("Carbon nanotube", "A rolled-up sheet of graphene a few nanometres wide."),
        ("Anode", "The part of a battery that stores lithium ions while it charges. Most use graphite."),
        ("Synthetic graphite", "Graphite made by heating carbon to very high temperatures rather than mined."),
        ("Natural flake graphite", "Mined graphite, processed into shapes for batteries."),
        ("Offtake agreement", "A contract to buy a supplier's output. It is a promise to buy, not proof the plant exists."),
        ("Anti-dumping duty", "A tariff on imports sold below a fair price."),
        ("Liquid phase exfoliation", "Making graphene by mixing graphite in a liquid so the layers peel apart." + cite(14)),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Carbon comes in many forms, and the money is not where the headlines are. Graphene and nanotubes get the attention. Graphite, the plain carbon in a battery's anode, is where supply is tight and where governments are acting.{cite(16)}{cite(17)} Graphene has taken longer to reach products than its backers hoped.{cite(11)}</p>
{nums}
<p class="cap wide">From the cited sources. Company figures are for the periods shown.</p>
<h3 class="wide" id="s-types" data-nav="Forms" style="margin-top:36px">The forms of carbon</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
