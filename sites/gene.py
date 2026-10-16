"""Frontier Gene: gene editing, GLP-1 drugs and longevity. Voice rules: docs/VOICE.md. Information, not medical advice.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more
from frontier import sitekit as K
from frontier.components import note
from frontier.scenarios import Scenario
from sites import tech_gene as TB
from sites import _gen

TITLE = "Frontier Gene"
AS_OF = "16 October 2026"

LIVE = {"cik": {"CRSP": 1674416, "NTLA": 1652130, "BEAM": 1745999, "LLY": 59478, "NVO": 353278},
        "aliases": {"CRSP": ["crispr therapeutics", "casgevy"], "NTLA": ["intellia"], "BEAM": ["beam therapeutics"], "LLY": ["eli lilly", "lilly", "zepbound", "mounjaro"], "NVO": ["novo nordisk", "wegovy", "ozempic"]},
        "arxiv_terms": ["CRISPR", "base editing", "GLP-1"], "arxiv_cat": "q-bio.GN"}

REFS = TB.GENE_REFS
cite = K.cite_factory(REFS)

SCEN = {
    "CRSP": [Scenario("bear", "Casgevy stays small and new programmes fail", 0.40, -0.40, 0.75),
             Scenario("base", "Casgevy grows slowly, pipeline advances", 0.35, 0.05, 0.75),
             Scenario("bull", "In vivo programmes show strong data", 0.25, 0.55, 0.75)],
    "NTLA": [Scenario("bear", "Safety problems return and trials stall", 0.40, -0.45, 0.75),
             Scenario("base", "Trials continue under extra monitoring", 0.35, 0.05, 0.75),
             Scenario("bull", "Late-stage data support approval", 0.25, 0.60, 0.75)],
    "BEAM": [Scenario("bear", "Pivotal data disappoint", 0.35, -0.40, 0.75),
             Scenario("base", "Filings proceed on schedule", 0.40, 0.05, 0.75),
             Scenario("bull", "Two medicines reach approval", 0.25, 0.55, 0.75)],
    "LLY": [Scenario("bear", "Price cuts and rivals squeeze obesity sales", 0.25, -0.25, 0.75),
            Scenario("base", "Sales keep growing at a slower pace", 0.50, 0.10, 0.75),
            Scenario("bull", "New obesity medicines widen the market", 0.25, 0.28, 0.75)],
    "NVO": [Scenario("bear", "Sales fall as guided and share is lost", 0.40, -0.30, 0.75),
            Scenario("base", "Sales stabilise after 2026", 0.40, 0.05, 0.75),
            Scenario("bull", "The oral Wegovy and new medicines restore growth", 0.20, 0.35, 0.75)],
}

COMPANIES = [
    {"t": "CRSP", "name": "CRISPR Therapeutics", "kind": "Gene-editing medicines",
     "rivals": "Intellia, Beam, Editas and others",
     "profit": f"Casgevy, developed with Vertex, was the first CRISPR medicine on the market. Its sales were $10.0 million in 2024 and $115.8 million in 2025, with 64 patients infused in 2025.{cite(10)}",
     "watch": "Casgevy patient numbers, in vivo programme data, cash.", "rank": "The company with the only approved CRISPR medicine.",
     "verdict": "One approved product, a slow launch"},
    {"t": "NTLA", "name": "Intellia", "kind": "In vivo gene editing",
     "rivals": "CRISPR Therapeutics, Beam and others",
     "profit": f"Its phase 3 nex-z trials were put on FDA clinical hold on 29 October 2025 after a liver event and a patient death on 5 November. The investigator reported septic shock after a perforated ulcer. The holds were lifted in January and March 2026.{cite(12)}",
     "watch": "Enrolment in the two nex-z trials, liver safety data, other programmes.", "rank": "A leader in in vivo editing, with a safety question to answer.",
     "verdict": "Promise with a safety watch"},
    {"t": "BEAM", "name": "Beam Therapeutics", "kind": "Base editing",
     "rivals": "CRISPR Therapeutics, Intellia and others",
     "profit": f"Plans a US filing for risto-cel in sickle cell disease as early as year-end 2026. The first patient was dosed in the pivotal cohort of BEAM-302 in 2026. It had $1.2 billion of cash, with a runway into mid-2029.{cite(13)}",
     "watch": "The filing, BEAM-302 data, cash.", "rank": "A well-funded base-editing company approaching its first filing.",
     "verdict": "Funded to its first filing"},
    {"t": "LLY", "name": "Eli Lilly", "kind": "Pharmaceuticals and obesity medicines",
     "rivals": "Novo Nordisk, Pfizer and others",
     "profit": f"2025 sales of Mounjaro were $22.97 billion and of Zepbound $13.54 billion, together 56% of Lilly's revenue.{cite(14)} It is spending $1.8 billion on plants in Kinsale and Limerick, Ireland.{cite(18)}",
     "watch": "Obesity medicine sales, price pressure, new launches, Irish plants.", "rank": "The largest seller of GLP-1 medicines by the figures we found.",
     "verdict": "The obesity-drug leader"},
    {"t": "NVO", "name": "Novo Nordisk", "kind": "Diabetes and obesity medicines",
     "rivals": "Eli Lilly and others",
     "profit": f"2025 sales were DKK 309.1 billion, up 10% at constant exchange rates. For 2026 it guides adjusted sales to fall by 5% to 13%, citing lower prices and the loss of semaglutide exclusivity in some markets.{cite(15)}{cite(16)}",
     "watch": "Wegovy and Ozempic sales, the oral Wegovy launch, price rules in the US.", "rank": "The other large obesity-drug firm, now guiding to decline.",
     "verdict": "The incumbent under pressure"},
]

LADDER = [("Lab result", "Works in cells|or animals"), ("First patient", "Safe in a|first person"), ("Pivotal data", "Large trial|reports"),
          ("Approval", "A regulator|says yes"), ("Launch", "Patients are|treated"), ("Margin", "Sold above|cost of making"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "friendly"), "IE": (3, 0, "friendly"), "DK": (5, 0, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "DK": "Denmark"}
COUNTRY = {
    "US": {"co": "Eli Lilly, Intellia, Beam, CRISPR Therapeutics' US operations, CHOP and Penn", "gov": "The FDA put Intellia's trials on hold in October 2025 and let them resume in 2026", "ctl": "See the references", "note": "Home of most gene-editing trials."},
    "IE": {"co": "Eli Lilly (Kinsale and Limerick)", "gov": "Lilly announced $1.8 billion for its Kinsale ($800 million) and Limerick ($1 billion) sites, with Limerick production expected to start in 2026", "ctl": "See the references",
           "note": "A manufacturing site for diabetes and obesity medicines."},
    "DK": {"co": "Novo Nordisk", "gov": "Home of Novo Nordisk, with 2025 sales of DKK 309.1 billion", "ctl": "See the references", "note": "The home of Ozempic and Wegovy."},
}
HYPE = [
    ("5", "Approved and selling", "A regulator approved it and patients receive it", "Casgevy, Mounjaro, Wegovy", "ok"),
    ("4", "Pivotal trial running", "A large trial for approval is under way", "Intellia nex-z, Beam's BEAM-302", "ok"),
    ("3", "One-patient result", "A single patient treated and reported", "Baby KJ's personalised editor", "dis"),
    ("2", "Early-stage data", "A small first-in-human study", "Many pipeline programmes", "dis"),
    ("1", "A claim about ageing", "A company says it will slow ageing", "No approved ageing indication found", "tgt"),
]
SHOVELS = [
    ("Gene editors", "CRISPR Therapeutics, Intellia, Beam", "United States, Switzerland", "Casgevy is the only approved CRISPR medicine we found"),
    ("Obesity medicines", "Eli Lilly, Novo Nordisk", "United States, Denmark", "Sales of the two firms' obesity and diabetes medicines are in the tens of billions of dollars"),
    ("Manufacturing in Ireland", "Eli Lilly", "Ireland", "A planned $1.8 billion investment at Kinsale and Limerick"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    C = dict(
        slug="gene", name="Gene", as_of=AS_OF, live=LIVE, refs=REFS, scen=SCEN, companies=COMPANIES, ladder=LADDER, hype=HYPE, shovels=SHOVELS,
        tiles=TILES, names=NAMES, country=COUNTRY, map_default="IE",
        order=["CRSP", "NTLA", "BEAM", "LLY", "NVO", "NVDA"], default=["CRSP", "NTLA", "BEAM", "LLY", "NVO"],
        tm_assets=[["CRSP", "CRISPR Therapeutics"], ["NTLA", "Intellia"], ["BEAM", "Beam Therapeutics"], ["LLY", "Eli Lilly"], ["NVO", "Novo Nordisk"], ["NVDA", "Nvidia"]],
        tm_default={"CRSP": px_first("CRSP"), "NTLA": px_first("NTLA"), "BEAM": px_first("BEAM"), "LLY": "2016-01-04", "NVO": "2016-01-04", "NVDA": "2022-10-10"},
        runs_for=("CRSP", "NTLA", "BEAM", "LLY", "NVO", "NVDA"),
        mult=[("Nvidia, 2022 to 2024", "NVDA", "ref"), ("Novo Nordisk", "NVO", "lay"), ("Eli Lilly", "LLY", "lay"), ("Beam Therapeutics", "BEAM", "quantum"),
              ("Intellia", "NTLA", "quantum"), ("CRISPR Therapeutics", "CRSP", "quantum")],
        index_groups=[("Gene editors", ["CRSP", "NTLA", "BEAM"], "var(--amber)"), ("Obesity-drug makers", ["LLY", "NVO"], "var(--teal)")],
        tech=TB.gene_html(cite),
        data_note="Company results, trial events and public-health figures were checked against the sources listed. Nothing here is medical advice, and no medicine named is recommended.",
        notice="We explain gene editing and obesity medicines and show how the companies and their shares have behaved. This is information, not medical advice. We do not recommend any medicine, company or trade. Projections are scenarios, not forecasts.",
        facts=[("Casgevy sales 2025", "$115.8m"), ("Mounjaro sales 2025", "$22.97bn"), ("People with obesity", "over 1bn"), ("Casgevy patients 2025", "64")],
        bands=[("dna-helix.jpg", "The code", "A model of part of a DNA double helix.", "A space-filling model of DNA"),
               ("molbio-lab.jpg", "The lab", "A molecular biology laboratory.", "A molecular biology laboratory at MIT"),
               ("chromosomes.jpg", "The chromosomes", "A scientist counting chromosomes.", "A scientist counting chromosomes at the NIH"),
               ("dna-seq-iss.jpg", "Even in orbit", "DNA sequenced on the International Space Station.", "An astronaut sequencing DNA in space"),
               ("cell-plates.jpg", "Three years", "Time enough to see which pivotal trials succeed.", "Cell culture plates")],
        hero=dict(h1="Editing the code, and the drugs <em>already selling</em>",
                  lead="One CRISPR medicine is on the market and sold $115.8 million last year. Two obesity medicines from one company sold over $36 billion. Here is what gene editing has shown, what the weight-loss drugs earn, and who is paid.",
                  img="dna-seq-iss.jpg", art=art_more.hero_cells(),
                  stats=[(115.8, "million dollars: Casgevy sales in 2025, the first CRISPR medicine", "$", "m"), (36, "billion dollars: Lilly's Mounjaro and Zepbound sales in 2025", "over $", "bn"),
                         (1, "billion people live with obesity, according to WHO", "more than ", " bn"),
                         (64, "patients were infused with Casgevy in 2025", "", "")]),
        ch1=dict(sub="Editing DNA is slow and rare. Medicines for weight are fast and huge.",
                 intro=f'''<p>Gene editing changes DNA in a patient's own cells. The first CRISPR medicine, Casgevy, reached the market in 2023. In 2025 it earned $115.8 million, from 64 patients infused.{cite(10)} In 2025 a team at the Children's Hospital of Philadelphia and Penn treated an infant with a base editor built for his own mutation, the first such treatment.{cite(11)}</p>
{note("Why it is attractive", "<p>A one-off edit could cure an inherited disease. Medicines such as tirzepatide and semaglutide, taken regularly, have created the largest drug franchises in the world.</p>")}
<p>Obesity affects more than a billion people, according to WHO, and in December 2025 it issued its first guideline on GLP-1 medicines, with conditional recommendations.{cite(17)}</p>
{note("The catch", "<p>Editing is expensive and slow to scale, and safety questions remain. GLP-1 medicines face price pressure. This site gives information, not medical advice.</p>")}''',
                 photos=[("dna-seq-iss.jpg", "Astronaut Kate Rubins sequencing DNA on the International Space Station."), ("dna-helix.jpg", "A space-filling model of part of a DNA double helix."),
                         ("cell-plates.jpg", "Gloved hands holding well cell culture plates.")],
                 paths_nav="Kinds", paths_title="The kinds of medicine",
                 paths=[("Ex vivo editing", f"Casgevy edits cells outside the body and returns them. 64 patients were infused in 2025.{cite(10)}"),
                        ("In vivo editing", f"Intellia and Beam edit inside the body with an infusion. Intellia's phase 3 trials were put on hold in October 2025 and later resumed.{cite(12)}{cite(13)}"),
                        ("GLP-1 medicines", f"Mounjaro and Zepbound together made about $36.5 billion for Lilly in 2025.{cite(14)}"),
                        ("Longevity", f"There is no regulatory route for ageing itself, so companies test drugs against specific age-related diseases.{cite(19)}")],
                 limits=[("Slow launch", f"Casgevy had $115.8 million of sales in 2025, its second year.{cite(10)}"),
                         ("Safety", f"One patient in Intellia's phase 3 trial died on 5 November 2025. The investigator reported septic shock after a perforated ulcer, and the company says the death was not related to the liver event.{cite(12)}"),
                         ("Price and access", f"WHO projects GLP-1 medicines will reach fewer than 10% of the people who could benefit by 2030.{cite(17)}"),
                         ("Falling sales", f"Novo Nordisk guides 2026 adjusted sales to fall by 5% to 13%.{cite(16)}")],
                 history=[("2023", f"Casgevy, the first CRISPR medicine, reaches the market.{cite(10)}", "big"),
                          ("2025", f"CHOP and Penn treat an infant with a personalised base editor.{cite(11)} Intellia's phase 3 trials are put on hold.{cite(12)} WHO issues its first GLP-1 guideline.{cite(17)}", "big"),
                          ("2026", f"The holds on Intellia's trials are lifted. The oral Wegovy launches in the US in January. Beam doses its first pivotal patient.{cite(12)}{cite(16)}{cite(13)}", ""),
                          ("Late 2026", f"Beam plans a US filing for risto-cel as early as year-end.{cite(13)}", "fut")],
                 key=("Two businesses with one label", "Gene editing is early, slow and scientifically exciting. Obesity medicines are a huge business under price pressure. They share a sector and almost nothing else.")),
        ch2=dict(cards=[("What changed", f"One CRISPR medicine is approved and a personalised editor has treated a child.{cite(10)}{cite(11)}"),
                        ("What has not", f"Gene editing is a small business. Casgevy sold $115.8 million in 2025, while Lilly's two obesity medicines sold about $36.5 billion.{cite(10)}{cite(14)}"),
                        ("What is new", f"WHO has issued guidance on GLP-1 medicines, and Novo Nordisk is guiding to falling sales.{cite(17)}{cite(16)}")],
                 photo=("molbio-lab.jpg", "A molecular biology laboratory at the Massachusetts Institute of Technology."),
                 key=("Small science, big sales", "The scientific breakthroughs are in gene editing. The sales are in obesity medicines.")),
        ch3=dict(sub="Our judgement from the pipeline. Not a forecast.",
                 timeline=[("Now: the first approved edits", f"Casgevy treats a small number of patients a year.{cite(10)}", "fut"),
                           ("Late 2026: filings and pivotal data", f"Beam plans a US filing for risto-cel as early as year-end, and has dosed the first patient in its BEAM-302 pivotal cohort.{cite(13)}", "fut"),
                           ("2026 to 2027: nex-z trials", f"Intellia is enrolling both phase 3 trials, with MAGNITUDE-2 enrolment due in the second half of 2026.{cite(12)}", "fut")],
                 ireland=[("The plants", f"Lilly announced $1.8 billion for its Kinsale ($800 million) and Limerick ($1 billion) sites. Limerick production is expected to start in 2026.{cite(18)}"),
                          ("The people", f"When it announced the investment, Lilly had operated in Ireland for more than 45 years and had more than 3,000 employees there.{cite(18)}"),
                          ("The exposure", "Irish plants depend on global demand for diabetes and obesity medicines and on price decisions made elsewhere.")],
                 prepare=[("As a patient", "Speak to a doctor. Nothing here is medical advice."),
                          ("As a business", "Medicine makers in Ireland sell into price rules set in the US and the EU."),
                          ("As an investor", "Gene-editing shares move on trial news. Obesity-drug shares move on prices and prescriptions.")],
                 key=("Filings, data, then launch", "The next two years are about trial data and filings. Launches come after.")),
        ch4=dict(sub="Three gene editors, and the two makers of the biggest medicines of the decade.",
                 extra="", prices_title="Share prices", prices_blurb="Three gene editors and two obesity-medicine makers, with Nvidia for scale.",
                 booms_caption="Log scale, from weekly closes, adjusted for splits. The gene editors rose and fell by very large amounts.",
                 ladder_caption="Casgevy and the obesity medicines are on the upper rungs. Most gene-editing programmes are below.",
                 good=["Pivotal trials report on time.", "A regulator approves a second editing medicine.", "Patients treated per quarter rise steadily.", "Obesity medicines keep growing despite price cuts."],
                 bad=["A safety event stops a trial.", "A one-patient result is sold as a cure.", "Sales guidance falls.", "A company funds itself only by selling shares."],
                 map_key='<span><i style="border-color:var(--teal)"></i>makes or tests these medicines</span><span><i style="border-color:var(--violet)"></i>partner</span><span><i style="border-color:var(--red)"></i>none</span>',
                 key=("Obesity pays. Editing is a long bet", "The obesity-drug makers have revenue in the tens of billions. The gene editors have one approved product and several trials.")),
        ch5=dict(sub="Safety, access, price and proof.",
                 cards=[("Safety", f"A patient in Intellia's phase 3 trial died in November 2025 and the trials were held for months.{cite(12)}"),
                        ("Scale", f"Casgevy treated 64 patients in 2025.{cite(10)}"),
                        ("Access", f"GLP-1 medicines are projected to reach fewer than 10% of those who could benefit by 2030.{cite(17)}"),
                        ("Price", f"Novo Nordisk cites lower realised prices in its 2026 guidance.{cite(16)}"),
                        ("Proof", "A one-patient result does not show that a treatment is safe or lasting."),
                        ("Ageing", f"STAT reported in 2022 that there was no regulatory pathway for ageing as an indication.{cite(19)}")],
                 photo=("chromosomes.jpg", "A scientist counting chromosomes in laboratory research at the NIH."),
                 line="A medicine has to be safe, work, be made at scale and be paid for. Gene editing has shown the first two for a few patients. It has not shown the last two at scale.",
                 key=("Proof, scale and price", "The science is real. The business questions are how many patients, at what price, with what safety record.")),
        ch6=dict(n_word="five", expect=[("Likely, about 75%", "More gene-editing trial data. Beam files in the US. Obesity-medicine prices fall further."),
                                        ("Even odds, about 50%", "A second CRISPR-based medicine is approved in the US."),
                                        ("Unlikely, under 10%", "A medicine is approved for ageing itself.")],
                 pull="Obesity medicines pay the bills of this sector. Gene editing is where the long-term hope is.",
                 why=[("Why we lean that way", "Our scenarios put the chance of each company ending the three years below today's price at {lo} to {hi}. The gene editors are the most volatile."),
                      ("Who is exposed", "Gene editors that depend on one trial, and obesity-drug makers facing price cuts."),
                      ("If it goes right", "A second editing medicine reaches patients and obesity medicines keep growing."),
                      ("The test", "For any medicine, ask how many patients, what safety record and what price.")],
                 mind="A trial stopped for safety. A filing accepted and approved. A GLP-1 price cut deeper than guided.",
                 key=("Slow editing, fast pricing pressure", "We expect gene-editing news to stay uneven and obesity-medicine prices to fall.")),
    )
    return _gen.build(C, cite)
