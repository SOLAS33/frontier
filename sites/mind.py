"""Frontier Mind: artificial intelligence, the chips and the power they use. Voice rules: docs/VOICE.md."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, key_idea, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_blocks as TB

TITLE = "Frontier Mind"
AS_OF = "16 October 2026"

LIVE = {"cik": {"NVDA": 1045810, "AMD": 2488, "MU": 723125, "CRWV": 1769628, "SMCI": 1375365},
        "aliases": {"NVDA": ["nvidia"], "AMD": ["advanced micro devices", "amd"], "MU": ["micron"], "CRWV": ["coreweave"],
                    "SMCI": ["super micro", "supermicro"]},
        "arxiv_terms": ["large language model", "GPU cluster", "AI accelerator"], "arxiv_cat": "cs.AR"}

REFS = [
    (1, "Vaswani et al. (2017). Attention is all you need. NeurIPS.", "https://arxiv.org/abs/1706.03762"),
    (2, "Kaplan et al. (2020). Scaling laws for neural language models.", "https://arxiv.org/abs/2001.08361"),
    (3, "Hoffmann et al. (2022). Training compute-optimal large language models.", "https://arxiv.org/abs/2203.15556"),
    (4, "Epoch AI. Trends in machine learning: training compute, data and hardware.", "https://epoch.ai/trends"),
    (5, "Stanford HAI (2025). The AI Index report.", "https://hai.stanford.edu/ai-index/2025-ai-index-report"),
    (6, "International Energy Agency (2025). Energy and AI.", "https://www.iea.org/reports/energy-and-ai"),
    (7, "Central Statistics Office (2024). Data centres metered electricity consumption 2023.", "https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2023/"),
    (8, "European Union. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (the AI Act).", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
    (9, "International Energy Agency (2024). Electricity 2024: data centres, AI and cryptocurrencies.", "https://www.iea.org/reports/electricity-2024"),
    (10, "Solas33 (2026). World-State Engine AI stocks study: who gained from the AI boom, and the growth-for-price screen.", "https://frontier.solas33.com/mind/#study"),
    (11, "Cambridge Centre for Alternative Finance. Cambridge Bitcoin Electricity Consumption Index.", "https://ccaf.io/cbnsi/cbeci"),
]
REFS = REFS + TB.MIND_REFS + [(22, "Central Statistics Office (2026). Data centres metered electricity consumption 2025 (data centres used 23% of metered electricity, 7,663 GWh).", "https://www.irishtimes.com/business/2026/07/07/data-centres-account-for-almost-one-quarter-of-irish-electricity-usage-in-2025/"),
    (19, "Windows Central (2023). ChatGPT sets growth record, reportedly hitting 100 million users in January (UBS estimate).", "https://windowscentral.com/software-apps/chatgpt-sets-growth-record-reportedly-hitting-100-million-users-in-january"),
    (20, "Sidley (2026). EU lawmakers reach provisional agreement to delay key EU AI Act obligations.", "https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/"),
    (21, "Silicon Canals (2026). Four US tech giants spent roughly 410 billion on capital expenditure last year and are steering toward roughly 725 billion in 2026.", "https://siliconcanals.com/m-four-us-tech-giants-spent-roughly-410-billion-on-capital-expenditure-last-year-much-of-it-tied-to-ai-and-are-steering-toward-roughly-725-billion-in-2026/")]
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "NVDA": [Scenario("bear", "Spending on AI chips pauses and rivals take share", 0.30, -0.30, 0.75),
             Scenario("base", "Spending keeps growing, margins ease", 0.45, 0.10, 0.75),
             Scenario("bull", "Demand outruns supply for another cycle", 0.25, 0.35, 0.75)],
    "AMD": [Scenario("bear", "Falls further behind in AI accelerators", 0.35, -0.35, 0.75),
            Scenario("base", "Wins a steady slice of the market", 0.40, 0.05, 0.75),
            Scenario("bull", "A large customer commits to its next chips", 0.25, 0.45, 0.75)],
    "MU": [Scenario("bear", "The memory cycle turns and prices fall", 0.40, -0.40, 0.75),
           Scenario("base", "High-bandwidth memory stays tight", 0.35, 0.00, 0.75),
           Scenario("bull", "Shortages persist through 2027", 0.25, 0.40, 0.75)],
    "CRWV": [Scenario("bear", "Debt and a customer pause bite", 0.40, -0.45, 0.75),
             Scenario("base", "Backlog converts and debt stays manageable", 0.35, 0.00, 0.75),
             Scenario("bull", "It becomes a core AI cloud for several big buyers", 0.25, 0.50, 0.75)],
    "SMCI": [Scenario("bear", "Thin margins and governance worries return", 0.40, -0.40, 0.75),
             Scenario("base", "Revenue grows, margins stay thin", 0.40, 0.00, 0.75),
             Scenario("bull", "Liquid-cooled racks win large orders", 0.20, 0.40, 0.75)],
}

COMPANIES = [
    {"t": "NVDA", "name": "Nvidia", "kind": "AI chips and software",
     "rivals": "AMD, Broadcom and the chips Google and Amazon design for themselves",
     "profit": "Already hugely profitable. The question is how long its customers keep spending at this rate, and whether they keep buying from it.",
     "watch": "Data-centre revenue, big-customer spending plans, gross margin, export rules on China, the share of customers building their own chips.",
     "rank": "The default supplier for training large models, with a software lock-in rivals are working to break.",
     "verdict": "The standard, and priced as one"},
    {"t": "AMD", "name": "AMD", "kind": "Chips",
     "rivals": "Nvidia, Intel, in-house chips at the cloud firms",
     "profit": "Win enough AI accelerator orders to make a second large business beside its processors.",
     "watch": "Accelerator revenue guidance, named customers, software support, memory supply.",
     "rank": "The only broad alternative to Nvidia in training chips. Well behind on share.",
     "verdict": "The credible second source"},
    {"t": "MU", "name": "Micron", "kind": "Memory chips",
     "rivals": "SK Hynix and Samsung",
     "profit": "Memory is a boom-and-bust business. AI needs fast stacked memory, which is in short supply and sells at a premium.",
     "watch": "Prices for high-bandwidth memory, capacity additions across the industry, inventory.",
     "rank": "One of three makers of the memory AI chips depend on.",
     "verdict": "A cyclical business with a good tailwind"},
    {"t": "CRWV", "name": "CoreWeave", "kind": "AI cloud",
     "rivals": "Microsoft Azure, Amazon, Google, Oracle, and other new AI clouds",
     "profit": "Fill the chips it has bought on long contracts, and pay down the debt it borrowed to buy them.",
     "watch": "Contract backlog, debt and interest cost, how much comes from one or two customers, power sites coming online.",
     "rank": "A fast-growing renter of Nvidia chips, financed largely by debt. Listed in 2025, so the history is short.",
     "verdict": "Revenue is real, so is the borrowing"},
    {"t": "SMCI", "name": "Super Micro", "kind": "AI servers",
     "rivals": "Dell, HPE, and the factories that build servers for the cloud firms",
     "profit": "Win share without giving away margin, and keep clean accounts.",
     "watch": "Gross margin, filing delays, the biggest customers, liquid-cooling product ramps.",
     "rank": "Quick to ship new Nvidia designs. Margins are thin and it has had accounting and audit problems.",
     "verdict": "Fast, thin-margined and watched closely"},
]

LADDER = [("Research", "Papers and|benchmarks"), ("Demos", "Chatbots that|impress"), ("Products", "Paid tools|people use daily"),
          ("Spending", "Hundreds of billions|on chips and power"), ("Visible gains", "Productivity shows|up in the data"),
          ("Profit for users", "Customers earn|more than they spend"), ("Profit for builders", "The spenders|earn it back")]

TILES = {"CA": (1, 0, "major"), "US": (1, 1, "leader"), "IE": (3, 0, "emerging"), "GB": (4, 0, "major"), "NL": (5, 0, "major"),
         "DE": (6, 0, "major"), "FR": (4, 1, "major"), "IL": (7, 1, "major"), "AE": (7, 2, "emerging"), "KR": (10, 0, "major"),
         "CN": (9, 1, "leader"), "JP": (11, 1, "major"), "TW": (10, 2, "major"), "IN": (8, 2, "emerging"), "SG": (9, 2, "emerging")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "NL": "Netherlands", "DE": "Germany", "FR": "France",
         "IL": "Israel", "AE": "United Arab Emirates", "KR": "South Korea", "CN": "China", "JP": "Japan", "TW": "Taiwan", "IN": "India", "SG": "Singapore"}
COUNTRY = {
    "US": {"co": "Nvidia, AMD, Microsoft, Alphabet, Amazon, Meta, OpenAI, Anthropic", "gov": "Large public research funding and a light-touch federal approach; states write their own rules",
           "ctl": "Export controls on the most advanced AI chips to China, changed several times", "note": "Most of the leading labs, the chip designers and the capital."},
    "CN": {"co": "Alibaba, Baidu, DeepSeek, Huawei, Tencent", "gov": "National plan to lead in AI by 2030, with licensing for public-facing models",
           "ctl": "Limited access to the best chips, so it builds its own and writes efficient software", "note": "Strong in applications and open models; short of the top chips."},
    "TW": {"co": "TSMC, which makes almost all of the most advanced AI chips", "gov": "Treats chip making as a national asset",
           "ctl": "Exports are tied to US controls", "note": "The single most important factory in the chain. A political risk too."},
    "KR": {"co": "Samsung, SK Hynix (the leading high-bandwidth memory maker)", "gov": "Large chip subsidies", "ctl": "Follows US controls", "note": "Memory is the quiet bottleneck."},
    "NL": {"co": "ASML, the only maker of the most advanced chip-printing machines", "gov": "Export licensing on its machines", "ctl": "Does not sell its most advanced tools to China", "note": "One company, one choke point."},
    "JP": {"co": "Chip materials and equipment makers, SoftBank", "gov": "Large subsidies for domestic chip plants", "ctl": "Follows US controls", "note": "Hidden strength in the materials chips need."},
    "GB": {"co": "DeepMind (Google), Arm, a strong university base", "gov": "AI Safety Institute and a pro-innovation, sector-by-sector regulatory approach", "ctl": "Follows US controls", "note": "Research and chip design rather than hardware."},
    "FR": {"co": "Mistral AI", "gov": "Large AI strategy with public computing funding", "ctl": "EU rules", "note": "The strongest European model builder."},
    "DE": {"co": "Industrial users, SAP, Aleph Alpha", "gov": "EU AI Act applies", "ctl": "EU rules", "note": "Big on industrial applications."},
    "IE": {"co": "European bases for most large technology firms, and most of the data centres", "gov": "EU AI Act applies; the Irish regulators share enforcement",
           "ctl": "Grid limits on new data-centre connections around Dublin", "note": "Hosts the computers more than it builds the models. See the power chart."},
    "IL": {"co": "Mobileye, AI start-ups, large chip design teams", "gov": "National AI programme", "ctl": "Export licensing", "note": "Strong in chip design and software."},
    "AE": {"co": "G42 and state-backed funds", "gov": "National AI strategy; large buyer of AI chips", "ctl": "US licences for chip imports", "note": "Spending oil money on compute."},
    "IN": {"co": "Large IT services firms, a big engineering workforce", "gov": "National AI mission", "ctl": "None of note", "note": "Demand and talent more than supply."},
    "SG": {"co": "Regional data-centre hub", "gov": "National AI strategy", "ctl": "Strict re-export rules", "note": "A hub with power limits of its own."},
    "CA": {"co": "Research labs founded by the pioneers of deep learning", "gov": "National AI strategy and compute funding", "ctl": "Follows US controls", "note": "Much of the early research was done here."},
}
HYPE = [
    ("5", "Reproduced benchmark", "A result several independent groups can rerun", "Open-model scores on public tests", "ok"),
    ("4", "Peer-reviewed or audited", "A refereed paper or an audited financial result", "Architecture papers, company 10-Ks", "ok"),
    ("3", "Vendor benchmark", "A company's own test on its own terms", "Speed claims in launch slides", "dis"),
    ("2", "Company forecast", "A statement about what will happen", "Revenue guidance, roadmap dates", "tgt"),
    ("1", "Demo or social post", "A video, a cherry-picked example, an influencer's view", "'AGI next year'", "tgt"),
]
SHOVELS = [
    ("Chip making", "TSMC, Samsung, Intel Foundry", "Taiwan, Korea, US", "Makes nearly all leading AI chips"),
    ("Chip tools", "ASML, Applied Materials, Lam Research", "Netherlands, US", "Without them nobody makes advanced chips"),
    ("Memory", "SK Hynix, Samsung, Micron", "Korea, US", "High-bandwidth memory is a bottleneck"),
    ("Networking", "Nvidia, Broadcom, Arista", "US", "Moves data between thousands of chips"),
    ("Cooling and power gear", "Vertiv, Schneider Electric, Eaton", "US, France, Ireland", "A rack of AI chips draws far more heat than a normal one"),
    ("Data-centre landlords", "Equinix, Digital Realty", "US", "Rent space and power"),
]


def build():
    order = ["NVDA", "AMD", "MU", "CRWV", "SMCI", "MSFT", "GOOGL", "AMZN", "META"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["BTC-USD", "AAPL"], ["NVDA", "AMD", "MU", "CRWV", "SMCI"],
                                     [["NVDA", "Nvidia"], ["AMD", "AMD"], ["MU", "Micron"], ["CRWV", "CoreWeave"], ["SMCI", "Super Micro"],
                                      ["MSFT", "Microsoft"], ["GOOGL", "Alphabet (Google)"], ["AMZN", "Amazon"], ["META", "Meta"], ["AAPL", "Apple"]],
                                     {"NVDA": "2022-10-10", "AMD": "2015-01-05", "MU": "2022-10-10", "CRWV": px_first("CRWV"), "SMCI": "2022-10-10",
                                      "MSFT": "2022-10-10", "GOOGL": "2022-10-10", "AMZN": "2022-10-10", "META": "2022-10-31", "AAPL": "1997-12-22"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Rules", "ctl": "Chip controls", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("NVDA", "AMD", "MU", "SMCI", "AAPL")}
    nv = stat["NVDA"]
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Apple, 1997 to 1999", f"from {runs['AAPL']['from']}", runs["AAPL"]["multiple"], "ref"),
            ("Nvidia", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "quantum"),
            ("AMD", f"from {runs['AMD']['from']}", runs["AMD"]["multiple"], "quantum"),
            ("Micron", f"from {runs['MU']['from']}", runs["MU"]["multiple"], "quantum"),
            ("Super Micro", f"from {runs['SMCI']['from']}", runs["SMCI"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("AI pure-plays", ["NVDA", "AMD", "MU", "SMCI"], "var(--amber)"), ("The four spenders", ["MSFT", "GOOGL", "AMZN", "META"], "var(--teal)")])

    hero = K.hero("Frontier / Mind", "The chips behind the <em>machines</em> that learn",
                  "Artificial intelligence is a few clever ideas, a very large number of chips and a great deal of electricity. Here is who sells what, who is paying, and what happens if they stop.",
                  "cray-2.jpg", art_more.hero_network(),
                  [(410, "billion dollars: combined capital spending in 2025 by Amazon, Microsoft, Alphabet and Meta, much of it for AI, on one tracker's estimate", "about ", ""),
                   (round(nv["x_from_start"]), "times Nvidia has risen since 2010, split-adjusted", "", "x"),
                   (23, "per cent of Irish electricity used by data centres in 2025", "", "%"),
                   (945, "terawatt-hours a year for data centres by 2030, on the IEA's central case", "about ", " TWh")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "From a 2017 paper to a global buying spree: the idea, the chips and the weak points.", f'''
<p>Almost all of the AI in the news comes from one idea: build a very large network of simple numbers, show it a huge amount of text, images and code, and nudge it until it predicts the next piece well. The design that made this work at scale, the transformer, was published by Google researchers in 2017.{cite(1)} The rest has been size.</p>
{note("Why size matters", "<p>Performance has improved as a smooth function of the data, the model and the computing power used. That regularity is why companies keep buying chips.{cite_2}</p>".replace("{cite_2}", cite(2, 3)))}
<p>There are two jobs. <b>Training</b> builds the model and takes months on thousands of chips. <b>Inference</b> is every later use, a question answered. Training compute for the largest models has grown roughly fourfold a year.{cite(4)} Inference is the larger and steadier bill once a product is popular.</p>
{note("What a chip does", "<p>An AI chip is a machine for multiplying large grids of numbers very quickly. Memory speed matters as much as arithmetic speed.</p>")}
<div class="fx-photos wide">
{photo("eniac-women.jpg", caption="Circuit boards from the first four US Army computers, held by the women who programmed them, in 1962.")}
{photo("oracle-computer.jpg", caption="The ORACLE computer at Oak Ridge in the 1950s. It filled a room and ran at a few thousand operations a second.")}
{photo("wafer-researcher.jpg", caption="A silicon wafer, the disc from which all modern chips are cut.")}
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:36px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Wrong, with confidence</h3><p>Models state false things fluently. They need a check that does not come from the model.</p></div>
<div class="card rv"><h3>Data</h3><p>The easily scraped text has largely been used. More has to come from licensed, synthetic or private sources.</p></div>
<div class="card rv"><h3>Cost per answer</h3><p>A useful answer can cost far more than a web search, which limits free products.</p></div>
<div class="card rv"><h3>Power</h3><p>The chips are limited by electricity as much as by silicon. See chapter 5.</p></div>
</div>
{TB.mind_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1956</div><p>The phrase "artificial intelligence" is coined at a summer workshop at Dartmouth.</p></div>
<div class="ev"><div class="yr">1997</div><p>IBM's Deep Blue beats Garry Kasparov at chess.</p></div>
<div class="ev big"><div class="yr">2012</div><p>A deep network trained on graphics chips wins an image recognition contest by a wide margin. The modern era starts.</p></div>
<div class="ev"><div class="yr">2016</div><p>DeepMind's AlphaGo beats the world champion at Go.</p></div>
<div class="ev big"><div class="yr">2017</div><p>The transformer paper is published.{cite(1)}</p></div>
<div class="ev big"><div class="yr">Nov 2022</div><p>ChatGPT launches on 30 November. UBS estimates it reached 100 million monthly users by January 2023.{cite(19)}</p></div>
<div class="ev"><div class="yr">2023 to 2025</div><p>Chip orders and data-centre building surge. Open models close much of the gap with closed ones.</p></div>
<div class="ev"><div class="yr">2024 to 2028</div><p>The EU AI Act phases in.{cite(8)} In 2026 lawmakers agreed to delay the high-risk duties, to December 2027 for stand-alone systems and August 2028 for those built into regulated products.{cite(20)} Spending on power for AI becomes a national topic. The four largest US buyers spend about $410 billion in 2025.{cite(21)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The test of whether the spending earns its keep. See chapter 6.</p></div>
</div>''', K.key_idea("A few ideas, a lot of chips",
        "Today's AI learns by adjusting billions of numbers until it predicts well. It works better the more data and computing power it gets, which is why "
        "the companies building it are buying chips and power on a scale the industry has not seen. The ideas are not secret. The chips, the memory and the "
        "electricity are the scarce things."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "What you need to follow the rest.", f'''
<div class="cols wide">
<div class="card rv"><h3>What it is good at</h3><p>Writing, summarising, translating, coding, spotting patterns in images and sound, and answering questions from large piles of text.</p></div>
<div class="card rv"><h3>What it is bad at</h3><p>Knowing when it is wrong, remembering reliably across long tasks, and anything that needs a physical, real-time check on the world.</p></div>
<div class="card rv"><h3>Why it is a money story</h3><p>Four companies are spending hundreds of billions of dollars a year on the buildings, chips and power. Their suppliers' sales are their spending. If it slows, so does everyone below them.</p></div>
</div>
<div class="wide">{photo("supercomputer.jpg", caption="NASA's Columbia supercomputer around 2004. A single rack of today's AI chips is more powerful than this whole room.")}</div>''',
        K.key_idea("A new tool and a very large bet",
                   "Some of AI is useful today and getting better. Some is a bet that it will become far more useful before the money runs out. The "
                   "suppliers have been paid. Whether the buyers earn it back is the open question."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Tools first, then jobs, then rules and power.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2027: tools</div><p>Coding assistants, customer service, document search and translation become routine. Gains show up first as time saved in tasks, not as new products.</p></div>
<div class="ev fut"><div class="yr">2026 to 2029: rules</div><p>The EU AI Act applies in stages and sets duties for the biggest models and for high-risk uses. A 2026 agreement delays the high-risk duties, and final adoption was still pending in June 2026.{cite(8)}{cite(20)} Other countries write their own, and they differ.</p></div>
<div class="ev fut"><div class="yr">2027 to 2030: jobs</div><p>Tasks change before jobs do. Roles built on routine writing, coding and analysis change most, and new roles appear around checking and directing the tools.</p></div>
<div class="ev fut"><div class="yr">Throughout: power</div><p>Data centres ask for more electricity than grids were planned for. Where and how that power is built becomes the real limit.{cite(6)}</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>Where the computers are</h3><p>Data centres used 23% of Ireland's metered electricity in 2025, up from 21% in 2023.{cite(22)}{cite(7)} Most are run for US firms serving Europe.</p></div>
<div class="card rv"><h3>The grid limit</h3><p>The grid operator has limited new connections in the Dublin region. Operators are looking to generate their own power or build elsewhere.</p></div>
<div class="card rv"><h3>The rules</h3><p>The EU AI Act applies here, and several Irish regulators share the enforcement. Many global firms have their European legal base in Ireland, so the Irish decisions travel.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>At work</h3><p>Learn what the tools do well in your own job. The skill that pays is knowing what to check. Keep the work that requires judgement and accountability.</p></div>
<div class="card rv"><h3>In a small business</h3><p>Pick one repeated task, test a tool on it for a month and measure the time saved. Do not put customer data into a tool whose terms you have not read.</p></div>
<div class="card rv"><h3>In your career</h3><p>Pair a domain, such as law, medicine or engineering, with fluency in using these systems. That pairing is scarcer than either alone.</p></div>
<div class="card rv"><h3>With savings</h3><p>Index funds already hold the large buyers. The pure-plays in chapter 4 are concentrated bets on a spending cycle. Size accordingly.</p></div>
</div>''', K.key_idea("Work changes before the economy does",
        "The first effects are on individual tasks: writing, coding, searching and answering. Whole jobs change more slowly. The harder limits are rules and "
        "electricity, and they differ by country. For most people the decision this decade is what to learn, not what to buy."), short="Change")

    study = [("Chip tools and equipment", "+109%"), ("Servers and networking", "+81%"), ("AI chips", "+67%"), ("Quantum computing", "-72%"),
             ("China AI", "-30%"), ("Companies AI may disrupt", "-28%"), ("Power and nuclear", "-19%")]
    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Who sells to the spenders, what has to happen for them to keep earning, and what past booms did to their shares.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The four spenders<span>Microsoft, Alphabet, Amazon, Meta</span></h3>
<dl><dt>Position</dt><dd>They buy most of the chips, own the data centres and run the products people use. Their combined capital spending is several hundred billion dollars a year.</dd>
<dt>Why they matter</dt><dd>They are the customers. If they cut spending, every company on this page feels it within a quarter or two.</dd>
<dt>Use</dt><dd>A diversified way to hold the theme, with AI as one profit line among many.</dd></dl><span class="verdict">The customers whose budgets matter most</span></article></div>
{K.prices_block("s-prices", "Share prices since 2010", "AI has been good for some shares and unkind to others.")}
<h3 class="wide" id="study" data-nav="Study" style="margin-top:44px">Who got paid in the boom</h3>
<p>Our own study of about 150 AI-related companies found the money went to the builders of the picks and shovels.{cite(10)}</p>
<div class="cols wide">
<div class="card rv"><h3>The median over the last year</h3><ul>{"".join(f"<li>{a}: {b}</li>" for a, b in study)}</ul></div>
<div class="card rv"><h3>Growth for the price</h3><p>Ranking companies by revenue growth divided by price-to-sales put Super Micro, Micron, CoreWeave, Dell and Constellation Energy at the top. The top third beat the bottom third in 59% of quarters since 2016, by a median 5 percentage points over six months. It failed in 2018 and 2019. A lean, not a forecast.</p></div>
<div class="card rv"><h3>What moves them</h3><p>Of 495 sudden moves in AI stocks since 2022, four in five traced to the company's own announcements or news about it. Few came from the macroeconomy.</p></div>
</div>
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 3), "AI has reached spending. Visible gains in the wider economy, and profit for the builders, are the next rungs.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs the spending is paying off</h3><ul><li>Customers renew and expand without discounts.</li><li>Inference revenue grows faster than training spending.</li><li>Cloud firms report AI revenue that covers its capital cost.</li><li>Productivity figures start to move.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Chip makers invest in their own customers.</li><li>Debt funds data centres on a thin base of contracts.</li><li>Orders are announced in gigawatts, not dollars.</li><li>One customer is most of a supplier's revenue.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>leader</span><span><i style="border-color:var(--violet)"></i>major</span><span><i style="border-color:var(--amber)"></i>emerging</span>', "Pick a country. Teal marks leaders, violet marks major players, amber marks emerging ones. A summary from public sources, so treat the detail as approximate.")}
<div class="callout t wide"><b>Why politics moves these shares.</b> One factory in Taiwan makes nearly every leading AI chip, one company in the Netherlands makes the machines that print them, and the United States restricts what can be sold to China. A change in any one of those is a change in every company on this page.</div>
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("The suppliers have been paid. The buyers have not yet",
        "Chip, memory and server makers booked real sales and profit from the spending. The companies doing the spending are betting that customers will "
        "pay enough for AI to earn it back. Until that shows in their accounts, the safest statement is that the demand is real and the return is unproven."), short="Money")

    power = [("A human brain", 0.00000017), ("Bitcoin network, estimate", 150), ("Irish data centres, 2023", 6.3), ("All Irish electricity use", 30),
             ("All data centres, 2024 (IEA)", 415), ("All data centres, 2030 (IEA central case)", 945)]
    ch5 = chapter("hurdles", 5, "The limits, and the power bill", "What is in the way, and how much electricity it draws.", f'''
<div class="cols wide">
<div class="card rv"><h3>Power and the grid</h3><p>New data centres wait years for a grid connection. The scarcest input is often a substation, not a chip.</p></div>
<div class="card rv"><h3>Chips and memory</h3><p>One factory and one tool maker are on the critical path. High-bandwidth memory has been short.</p></div>
<div class="card rv"><h3>Money</h3><p>Spending is large against current AI revenue. Some of it is funded by debt and circular deals between suppliers and customers.</p></div>
<div class="card rv"><h3>Reliability and liability</h3><p>Models make confident mistakes, so many uses need a human check, which eats the saving.</p></div>
<div class="card rv"><h3>Law</h3><p>Copyright cases and the EU AI Act set what data can be used and how.{cite(8)}</p></div>
<div class="card rv"><h3>Efficiency surprises</h3><p>If models become much cheaper to run, demand for chips could rise or fall. Both have happened in past computing eras.</p></div>
</div>
<h3 class="wide" id="s-power" data-nav="Power" style="margin-top:44px">Power</h3>
<p>Data centres used roughly 415 terawatt-hours in 2024, about 1.5% of the world's electricity, and the IEA's central case roughly doubles that by 2030.{cite(6)} Part of the growth is AI. Part is ordinary cloud.</p>
{note("The Irish number", "<p>Irish data centres drew about 6.3 TWh in 2023, a fifth of the country's metered electricity.{cite_7}</p>".replace("{cite_7}", cite(7)))}
{fig(charts.bars_h([("Irish data centres, 2023", 6.3), ("All Irish electricity use", 30), ("Bitcoin network, estimate", 150), ("All data centres, 2024", 415), ("All data centres, 2030 (IEA central case)", 945)],
                   lambda v: f"{v:g} TWh", lo_exp=0, hi_exp=3, highlight="All data centres, 2024", label="Electricity use in terawatt-hours a year, log scale", left=300),
     "Log scale, approximate, per year. Sources: IEA" + cite(6, 9) + ", Cambridge index" + cite(11) + ", Central Statistics Office" + cite(7) + ".", 4)}
<div class="fx-photos wide">{photo("cray-2.jpg", caption="A Cray-2 supercomputer at NASA Ames in 1987, cooled by immersing its circuit boards in liquid. Cooling has been the limit for a long time.")}
<div class="card" style="align-self:start"><h3>Why the grid is the story</h3><p>A modern AI rack draws many times the power of an ordinary one and needs liquid cooling. A campus of them can need as much electricity as a small city. Whether the grid, gas and nuclear projects can be built in time decides how much of the spending turns into computing. That is why Frontier Atom and Frontier Cell sit next to this site.</p></div></div>''',
        K.key_idea("Chips are made of sand, but they need a grid",
                   "The limiting resource for AI is moving from chips to electricity. A chip can be made in a year. A power station and its lines take much longer. "
                   "That is why the biggest buyers are signing deals for nuclear plants and gas turbines."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology and the spending</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 70%</h3><p>Models keep improving and getting cheaper to run. AI is built into most office software. Total chip and data-centre spending is higher in 2029 than in 2026.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>At least one year in the next three sees spending growth stall or fall at the biggest buyers, and the chip stocks drop by a third or more before recovering.</p></div>
<div class="card rv"><h3>Unlikely, under 25%</h3><p>AI replaces most of a large profession within three years, or an investment collapse leaves several data-centre builders insolvent.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 5, "five")}
<div class="pull wide">The chips are real and the demand is real. The return on the spending is still a promise.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. Most of these shares sit near their highs after a very large run, and volatility is high.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>The companies that borrowed to buy chips, and the suppliers who rely on one or two customers, take the worst of a slowdown. Memory makers swing with their own cycle.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>The leaders with real technology and clean accounts keep earning. A few-fold rise from here is a normal good outcome, not a repeat of the last three years.</p></div>
<div class="card rv"><h3>The test</h3><p>Ask of each company how much of its revenue comes from customers spending borrowed money, and what happens to it if those customers cut by a third.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A large buyer cutting its capital spending plan. A major AI firm failing to refinance its debt. Evidence of a wide productivity gain in national statistics.</div>''',
        K.key_idea("A real boom with a question mark at the end",
                   "We expect AI to keep spreading and the computing bill to keep rising. We also expect at least one scare along the way, when buyers pause "
                   "and the suppliers' shares fall hard. The long-run technology and the three-year share prices are different questions."), short="Outlook")

    bands = [band("oracle-computer.jpg", "Where it started", "Every computer was a room once. This one drew less power than a single AI chip does now.", "The ORACLE computer"),
             band("wafer-researcher.jpg", "Where it is made", "A disc of silicon is the raw material of the whole boom.", "A silicon wafer in a clean room"),
             band("eniac-women.jpg", "Who builds it", "The first programmers were mostly women, and mostly unnamed.", "Women holding parts of early Army computers"),
             band("supercomputer.jpg", "The power bill", "Cooling and electricity decide how much of this can be built.", "A supercomputer room"),
             band("cray-2.jpg", "Three years", "One chip generation. Enough time to see who was selling and who was buying.", "A Cray-2 supercomputer")]
    foot = K.foot(REFS, AS_OF, "Frontier Mind", "mind",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain and credited under each picture. Our AI stocks study covers companies we selected as AI-related, so it has selection bias.")
    nf = K.notice("We explain how AI works and show how its suppliers and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Data-centre use 2024", "about 415 TWh"), ("Irish share, 2025", "23%"), ("Nvidia since 2010", f"{nv['x_from_start']:.0f}x"), ("Training compute", "about 4x a year")]
    body = K.assemble("mind", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]
