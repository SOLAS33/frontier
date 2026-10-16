"""Technical depth for Frontier Gene: numbers, kinds of therapy, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so. Not medical advice."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

GENE_REFS = [
    (10, "Precision Medicine Online (2026). Vertex, CRISPR Therapeutics record $115.8M in 2025 Casgevy sales.", "https://www.precisionmedicineonline.com/business-news/vertex-crispr-therapeutics-record-1158m-2025-casgevy-sales"),
    (11, "Children's Hospital of Philadelphia (2025). World's first patient treated with personalized CRISPR gene editing therapy.", "https://chop.edu/news/worlds-first-patient-treated-personalized-crispr-gene-editing-therapy-childrens-hospital"),
    (12, "Intellia Therapeutics. Quarterly report on Form 10-Q for the period ended 30 June 2026.", "https://www.sec.gov/Archives/edgar/data/0001652130/000119312526337952/ntla-20260630.htm"),
    (13, "Beam Therapeutics (2026). Second quarter 2026 financial results.", "https://investors.beamtx.com/news-releases/news-release-details/beam-therapeutics-reports-second-quarter-2026-financial-results"),
    (14, "Pharmaceutical Technology (2026). Eli Lilly soars past expectations to hit 45% sales growth in 2025.", "https://www.pharmaceutical-technology.com/newsletters/eli-lilly-soars-past-expectations-to-hit-45-sales-growth-in-2025"),
    (15, "Novo Nordisk. Financial report for 2025 (Form 6-K).", "https://www.sec.gov/Archives/edgar/data/353278/000035327826000006/caq42025.htm"),
    (16, "Novo Nordisk (2026). Novo Nordisk releases 2026 sales and operating profit outlook.", "https://www.biospace.com/press-releases/novo-nordisk-releases-2026-sales-and-operating-profit-outlook"),
    (17, "World Health Organization (2025). WHO issues global guideline on the use of GLP-1 medicines in treating obesity.", "https://www.who.int/news/item/01-12-2025-who-issues-global-guideline-on-the-use-of-glp-1-medicines-in-treating-obesity"),
    (18, "IDA Ireland. Lilly expands manufacturing footprint in Ireland with $1.8 billion investment.", "https://www.idaireland.com/latest-news/press-release/lilly-expands-manufacturing-footprint-in-ireland-with-$1-8-billion-investment"),
    (19, "STAT (2022). Anti-aging projects are drawing funding, but a much-discussed trial is overlooked.", "https://www.statnews.com/2022/08/09/anti-aging-projects-funding-much-discussed-trial-overlooked/"),
]


def gene_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Casgevy sales, 2024 and 2025", "$10.0 million from 5 patients in 2024. $115.8 million in 2025, with 64 patients infused" + cite(10), "The first CRISPR medicine on the market. Treatment is a one-off, and it is slow to scale"],
        ["Lilly's tirzepatide medicines, 2025", "Mounjaro $22.97 billion. Zepbound $13.54 billion" + cite(14), "Together 56% of Lilly's 2025 revenue"],
        ["Novo Nordisk, 2025", "Sales DKK 309.1 billion, up 10% at constant exchange rates. Operating profit DKK 127.7 billion" + cite(15), "It guides 2026 sales to fall by 5% to 13% at constant exchange rates" + cite(16)],
        ["People living with obesity", "More than 1 billion. Obesity linked to 3.7 million deaths in 2024" + cite(17), "WHO expects the number to double by 2030 without action"],
        ["Reach of GLP-1 medicines", "WHO projects they will reach fewer than 10% of the people who could benefit by 2030" + cite(17), "Price and supply limit access"],
        ["Beam Therapeutics cash", "$1.2 billion at the end of the second quarter of 2026, with a runway into mid-2029" + cite(13), "Gene editors fund long trials from cash they raised"],
    ])
    kinds = _table(["Kind of medicine", "What it does", "Examples", "Status"], [
        ["Gene editing, ex vivo", "Edits a patient's cells outside the body and returns them", "Casgevy (Vertex and CRISPR Therapeutics). Beam's risto-cel" + cite(10) + cite(13), "Casgevy is approved. Beam plans a US filing as early as the end of 2026"],
        ["Gene editing, in vivo", "Edits cells inside the body with a one-off infusion", "Intellia's nex-z. Beam's BEAM-302" + cite(12) + cite(13), "Intellia's nex-z trials were put on hold in October 2025 and later resumed"],
        ["Personalised editing", "A therapy built for one patient's mutation", "Baby KJ, treated at CHOP and Penn in 2025" + cite(11), "A single patient, with early results"],
        ["GLP-1 and related medicines", "Medicines for diabetes and obesity taken regularly", "Lilly's Mounjaro and Zepbound. Novo's Ozempic and Wegovy" + cite(14) + cite(15), "Very large sales. WHO issued a conditional guideline in December 2025" + cite(17)],
        ["Longevity drugs", "Aim to slow ageing", "Companies and trials such as TAME", "STAT reported in 2022 that there is no regulatory pathway for ageing as such. Drugs are tested against specific age-related diseases" + cite(19)],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["A CRISPR medicine reaches the market", "Casgevy, approved in 2023", _tag("ok"), "64 patients were infused in 2025" + cite(10)],
        ["A gene editor made for one patient", "CHOP and Penn, first dose February 2025, reported in the New England Journal of Medicine" + cite(11), _tag("ok"), "A base editor delivered to the liver. It corrects one of two copies of the CPS1 gene. Results come from one patient"],
        ["A safety stop in a large editing trial", "Intellia nex-z, FDA clinical holds on 29 October 2025" + cite(12), _tag("dis"), "A patient died on 5 November 2025. The investigator reported septic shock after a perforated ulcer. The holds were lifted in January and March 2026"],
        ["A second wave of editors reaching pivotal trials", "Beam's BEAM-302, first patient dosed in the pivotal cohort, August 2026" + cite(13), _tag("ok"), "For alpha-1 antitrypsin deficiency"],
        ["A WHO guideline on GLP-1 medicines", "1 December 2025, conditional" + cite(17), _tag("ok"), "Conditional because long-term data are limited and cost is high"],
        ["An approved ageing medicine", "None found", _tag("tgt"), "STAT reported in 2022 that there is no regulatory route for ageing itself" + cite(19)],
    ])
    gl = _gloss([
        ("CRISPR", "A tool that finds a chosen stretch of DNA and cuts it. It is used to disable or change a gene."),
        ("Base editing", "A gentler edit that changes one letter of DNA without cutting both strands."),
        ("Ex vivo and in vivo", "Ex vivo means cells are edited outside the body. In vivo means the edit happens inside the patient."),
        ("GLP-1", "A gut hormone. Medicines that copy it lower blood sugar and appetite."),
        ("Pivotal trial", "The large trial a regulator uses to decide whether to approve a medicine."),
        ("Clinical hold", "An order from a regulator to stop dosing patients in a trial until questions are answered."),
        ("Infused", "Given through a drip into a vein."),
        ("Rare disease", "A condition that affects few people. Medicines for them are tested in small trials."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Gene editing changes DNA in a patient's own cells. Casgevy edits cells outside the body and returns them. Newer medicines edit inside the body with a single infusion.{cite(10)}{cite(12)} GLP-1 medicines are a different thing: ordinary drugs taken repeatedly that act on appetite and blood sugar. Their sales are far larger than anything in gene editing so far.{cite(14)}{cite(15)}</p>
{nums}
<p class="cap wide">From the cited sources. Company results are for the periods shown. This site gives information, not medical advice.</p>
<h3 class="wide" id="s-types" data-nav="Kinds" style="margin-top:36px">The kinds of medicine</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
