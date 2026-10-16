"""Frontier Bot: robots and physical AI. Voice rules: docs/VOICE.md.
Facts were checked against the cited sources on 16 October 2026. Do not add a number without a source in REFS."""
from __future__ import annotations

from frontier import art_more, charts
from frontier.components import band, chapter, fig, note, photo
from frontier.scenarios import Scenario
from frontier import sitekit as K
from sites.quantum_extra import tile_map
from sites import tech_bot as TB

TITLE = "Frontier Bot"
AS_OF = "16 October 2026"

LIVE = {"cik": {"SYM": 1837240, "SERV": 1832483, "TER": 97210, "ISRG": 1035267, "ROK": 1024478},
        "aliases": {"SYM": ["symbotic"], "SERV": ["serve robotics"], "TER": ["teradyne"], "ISRG": ["intuitive surgical", "da vinci"],
                    "ROK": ["rockwell automation"]},
        "arxiv_terms": ["humanoid robot", "robot manipulation", "vision-language-action"], "arxiv_cat": "cs.RO"}

REFS = [
    (1, "Rockwell Automation (2025). Fourth quarter and full year 2025 results.", "https://www.rockwellautomation.com/en-us/company/news/press-releases/Rockwell-Automation-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Introduces-Fiscal-2026-Guidance.html"),
    (2, "Central Statistics Office (Ireland). Statistics.", "https://www.cso.ie/en/"),
    (3, "Seeking Alpha (2025). Figure raises $1B+ in Series C, hits $39B valuation.", "https://seekingalpha.com/news/4495255-figure-raises-1b-in-series-c-hits-39b-valuation-to-scale-humanoid-robot-deployment"),
    (4, "Brohan et al. (2023). RT-2: vision-language-action models transfer web knowledge to robotic control.", "https://arxiv.org/abs/2307.15818"),
]
REFS = REFS + TB.BOT_REFS
cite = K.cite_factory(REFS)
fmt_p = K.fmt_p

SCEN = {
    "SYM": [Scenario("bear", "The main customer slows orders and margins stay thin", 0.35, -0.45, 0.75),
            Scenario("base", "The order book converts to revenue on schedule", 0.40, 0.05, 0.75),
            Scenario("bull", "New customers join and margins widen", 0.25, 0.50, 0.75)],
    "SERV": [Scenario("bear", "Cash burns faster than revenue and it sells more shares", 0.50, -0.55, 0.75),
             Scenario("base", "The fleet grows and revenue stays small", 0.30, 0.00, 0.75),
             Scenario("bull", "Delivery revenue scales with the fleet", 0.20, 0.60, 0.75)],
    "TER": [Scenario("bear", "Chip test demand falls and robotics keeps shrinking", 0.30, -0.25, 0.75),
            Scenario("base", "Test business carries earnings, robotics is flat", 0.45, 0.08, 0.75),
            Scenario("bull", "Chip test and robotics both grow", 0.25, 0.30, 0.75)],
    "ISRG": [Scenario("bear", "Procedure growth slows and rivals take share", 0.25, -0.20, 0.75),
             Scenario("base", "Steady growth in procedures and systems", 0.50, 0.10, 0.75),
             Scenario("bull", "New systems and new markets extend the growth", 0.25, 0.28, 0.75)],
    "ROK": [Scenario("bear", "Factory spending stays flat or falls", 0.30, -0.20, 0.75),
            Scenario("base", "Gradual recovery in factory automation", 0.45, 0.08, 0.75),
            Scenario("bull", "A factory-building boom lifts orders", 0.25, 0.28, 0.75)],
}

COMPANIES = [
    {"t": "SYM", "name": "Symbotic", "kind": "Warehouse automation",
     "rivals": "Ocado, AutoStore, KION's Dematic, Amazon's own systems",
     "profit": f"Install robotic warehouse systems for large retailers. Walmart was about 85% of its revenue in fiscal 2025, and its backlog was $22.5 billion, most of it from Walmart and one joint venture.{cite(14)}",
     "watch": "Customer concentration, order backlog, margins, new customers.",
     "rank": "A large listed warehouse robot firm with a very concentrated customer base.",
     "verdict": "A big order book and one big customer"},
    {"t": "SERV", "name": "Serve Robotics", "kind": "Sidewalk delivery robots",
     "rivals": "Starship, Coco, and human couriers",
     "profit": f"Run a fleet of delivery robots at a cost per delivery below a courier's. It reported 2,000 robots deployed by the end of 2025 and full-year revenue of $2.7 million.{cite(16)}",
     "watch": "Revenue per robot, cash runway, share sales, partner cities.",
     "rank": "A young listed company with a large fleet and very small revenue so far.",
     "verdict": "A fleet, not yet a profit"},
    {"t": "TER", "name": "Teradyne", "kind": "Chip test equipment and robots",
     "rivals": "Advantest in test, and other makers of robot arms",
     "profit": f"In 2025 revenue was $3,190 million. Semiconductor Test was 79% of it and Robotics, at $308 million, was about 10% and down 15.5% on 2024.{cite(15)}",
     "watch": "AI chip test demand, robotics revenue and margin.",
     "rank": "A chip-test company with a robotics business attached.",
     "verdict": "Robots are the side business"},
    {"t": "ISRG", "name": "Intuitive Surgical", "kind": "Surgical robots",
     "rivals": "Medtronic, Johnson & Johnson, CMR Surgical",
     "profit": f"Sell da Vinci systems and earn on instruments and service each time they are used. At the end of 2025 it had 11,106 da Vinci systems installed, and 3.15 million procedures were done on them that year.{cite(12)}",
     "watch": "Procedure growth, new system launches, rival approvals, pricing.",
     "rank": "The established leader.",
     "verdict": "The proof that robots can be a great business"},
    {"t": "ROK", "name": "Rockwell Automation", "kind": "Factory automation and controls",
     "rivals": "Siemens, Schneider Electric, ABB, Mitsubishi Electric",
     "profit": f"Sell the controllers, drives and software that run factories. It reports three segments: Intelligent Devices, Software & Control, and Lifecycle Services. Fiscal 2025 sales grew 1%.{cite(1)}",
     "watch": "Orders, factory investment, software share of revenue.",
     "rank": "A large supplier of the equipment around robots, rather than the robots.",
     "verdict": "The steady one"},
]

LADDER = [("Demo", "Works in a|video"), ("Pilot", "Works at a|customer site"), ("Reliable", "Runs for months|with little help"),
          ("Paid at scale", "Thousands of|units sold"), ("Cheaper than labour", "Costs less than the|person it replaces"),
          ("Fleet", "Factories build|robots in volume"), ("Profit", "Owners earn their|return")]

TILES = {"US": (1, 1, "mixed"), "IE": (3, 0, "restrictive"), "DE": (6, 0, "friendly"), "SG": (9, 2, "friendly"),
         "CN": (9, 1, "friendly"), "KR": (10, 0, "friendly"), "JP": (11, 1, "friendly")}
NAMES = {"US": "United States", "IE": "Ireland", "DE": "Germany", "SG": "Singapore", "CN": "China", "KR": "South Korea", "JP": "Japan"}
COUNTRY = {
    "KR": {"co": "See the IFR report", "gov": "The highest robot density in the world: 1,012 per 10,000 factory workers in 2023", "ctl": "See the references", "note": "Ranked first by the IFR."},
    "SG": {"co": "See the IFR report", "gov": "770 robots per 10,000 factory workers in 2023, ranked second", "ctl": "See the references", "note": "A small workforce, so a high density from a small base."},
    "CN": {"co": "See the IFR report", "gov": "Installed 295,000 industrial robots in 2024, 54% of the world's installations. Density 470 per 10,000 in 2023", "ctl": "Made 94% of the world's sintered permanent magnets in 2024, which robot motors use",
           "note": "The biggest buyer and the biggest magnet supplier."},
    "DE": {"co": "See the IFR report", "gov": "Density 429 per 10,000 in 2023", "ctl": "See the references", "note": "Fourth by density."},
    "JP": {"co": "See the IFR report", "gov": "Density 419 per 10,000 in 2023", "ctl": "See the references", "note": "Fifth by density."},
    "US": {"co": "Amazon, Intuitive Surgical, Symbotic, Figure, Boston Dynamics (Hyundai-owned)", "gov": "Density 295 per 10,000 in 2023, ranked tenth by the IFR", "ctl": "See the references",
           "note": "Home of the largest warehouse fleet and the best-funded humanoid start-up we found."},
    "IE": {"co": "No data found", "gov": "We found no IFR density figure for Ireland", "ctl": "See the references", "note": "Look up official labour statistics at the CSO."},
}
HYPE = [
    ("5", "Years of paid operation at scale", "Thousands of units doing a job for customers who renew", "Amazon's one million robots, Intuitive's 11,106 systems", "ok"),
    ("4", "Repeat orders from large customers", "A customer commits to a large programme", "Walmart with Symbotic", "ok"),
    ("3", "Pilot with a named customer", "A trial at a factory or warehouse", "Humanoid pilots reported at car plants", "dis"),
    ("2", "A demonstration video", "A robot doing a task, filmed", "Folding laundry, making coffee", "tgt"),
    ("1", "Production target", "A number of units to be built", "A stated units-a-year target", "tgt"),
]
SHOVELS = [
    ("Permanent magnets", "Chinese magnet makers", "China", "China made 94% of the world's sintered permanent magnets in 2024. Robot motors use them"),
    ("Onboard AI models and chips", "NVIDIA (Isaac GR00T)", "United States", "NVIDIA offers foundation models for humanoid robots"),
]


def px_first(sym):
    from frontier import prices
    return prices.load()[sym]["d"][0]


def build():
    order = ["SYM", "SERV", "TER", "ISRG", "ROK", "TSLA", "NVDA"]
    px, stat, sims, data_js = K.prep(SCEN, order, ["AAPL", "NVDA"], ["SYM", "SERV", "TER", "ISRG", "ROK"],
                                     [["SYM", "Symbotic"], ["SERV", "Serve Robotics"], ["TER", "Teradyne"], ["ISRG", "Intuitive Surgical"],
                                      ["ROK", "Rockwell Automation"], ["TSLA", "Tesla"], ["NVDA", "Nvidia"]],
                                     {"SYM": px_first("SYM"), "SERV": px_first("SERV"), "TER": "2016-01-04", "ISRG": "2016-01-04", "ROK": "2016-01-04",
                                      "TSLA": "2016-01-04", "NVDA": "2022-10-10"},
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Facts", "ctl": "Supply", "note": "Read"}, "IE")
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in ("SYM", "SERV", "TER", "ISRG", "TSLA", "NVDA")}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
            ("Tesla", f"from {runs['TSLA']['from']}", runs["TSLA"]["multiple"], "lay"),
            ("Intuitive Surgical", f"from {runs['ISRG']['from']}", runs["ISRG"]["multiple"], "lay"),
            ("Teradyne", f"from {runs['TER']['from']}", runs["TER"]["multiple"], "lay"),
            ("Serve Robotics", f"from {runs['SERV']['from']}", runs["SERV"]["multiple"], "quantum"),
            ("Symbotic", f"from {runs['SYM']['from']}", runs["SYM"]["multiple"], "quantum")]
    idx_svg = K.index_svg(px, [("Robot makers and operators", ["SYM", "SERV", "ISRG"], "var(--amber)"), ("Automation suppliers", ["TER", "ROK"], "var(--teal)")])

    hero = K.hero("Frontier / Bot", "Robots are everywhere except where <em>people live</em>",
                  "More than half a million industrial robots went into factories in 2024, and Amazon says it runs a million in its warehouses. Now AI is being used to teach them to cope with the messy world outside the cage. Here is what works, who is paid, and what is still a video.",
                  "robonaut-2.jpg", art_more.hero_reactor(),
                  [(542076, "industrial robots installed worldwide in 2024", "", ""), (1, "million robots in Amazon's fleet, announced July 2025", "", " million"),
                   (round(runs["SYM"]["multiple"]), "times Symbotic rose from low to high in under two years", "", "x"),
                   (16000, "dollars: the launch price of the base Unitree G1 humanoid, in 2024", "about $", "")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Sense, decide, move. The first is solved, the second is being solved and the third is expensive.", f'''
<p>A robot is a machine that senses its surroundings, decides what to do and moves something to do it. The first industrial robot, Unimate, started work at a General Motors plant in 1961.{cite(20)} Today's robots have cameras, force sensors and software that adjusts to what it sees. The newest idea is to let large AI models, trained on images, text and recorded movement, plan the next action. Google DeepMind showed one, RT-2, in 2023.{cite(21)}</p>
{note("Why it is attractive", "<p>A robot works through the night, does not tire and gets cheaper to make with volume. In places where workers are scarce, a robot that can do a varied job is worth a lot.</p>")}
<p>The International Federation of Robotics counted 542,076 new industrial robots in 2024 and 4.66 million in use. China took 54% of the new ones.{cite(10)} South Korea had the highest density in 2023, 1,012 robots for every 10,000 manufacturing workers. The United States had 295.{cite(11)}</p>
{note("The catch", "<p>The robots that work today do one thing in one place. A robot that copes with a different job each day has been shown in videos and pilots. We found no independent figures for humanoids at scale.</p>")}
<div class="fx-photos wide">
{photo("kuka-palletising.jpg", caption="Industrial robots stacking loaves of bread in a bakery. The job is the same every time, which is what these machines are good at.")}
{photo("robonaut-2.jpg", caption="Robonaut 2, built by NASA and General Motors, working with a tool.")}
{photo("valkyrie.jpg", caption="NASA's Valkyrie humanoid robot, built for research into disaster response.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Waves" style="margin-top:36px">Four kinds of success</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Arms in cages</h3><p>The biggest market by count. The IFR counts 542,076 installed in 2024.{cite(10)}</p></div>
<div class="card rv"><h3>Robots that move</h3><p>Amazon announced its millionth warehouse robot in July 2025 and an AI model, DeepFleet, that it says cuts fleet travel time by 10%.{cite(17)}</p></div>
<div class="card rv"><h3>Robots in medicine</h3><p>Intuitive had 11,106 da Vinci systems installed at the end of 2025, with about 3.15 million procedures in the year.{cite(12)}</p></div>
<div class="card rv"><h3>Robots that learn</h3><p>RT-2 turns camera images and spoken instructions into robot actions. It is a research result, not a product.{cite(21)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Concentration</h3><p>Symbotic took about 85% of its fiscal 2025 revenue from Walmart.{cite(14)}</p></div>
<div class="card rv"><h3>Small revenue</h3><p>Serve Robotics had 2,000 robots deployed at the end of 2025 and revenue of $2.7 million for the year.{cite(16)}</p></div>
<div class="card rv"><h3>Shrinking robotics</h3><p>Teradyne's robotics revenue fell 15.5% in 2025, to $308 million.{cite(15)}</p></div>
<div class="card rv"><h3>Supply</h3><p>China made 94% of the world's sintered permanent magnets in 2024.{cite(19)}</p></div>
</div>
{TB.bot_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1961</div><p>Unimate, the first industrial robot, starts work at a General Motors plant in Ewing Township, New Jersey.{cite(20)}</p></div>
<div class="ev"><div class="yr">2000</div><p>The US FDA clears the da Vinci surgical system for general laparoscopic surgery.{cite(13)}</p></div>
<div class="ev"><div class="yr">2012</div><p>Amazon agrees to buy Kiva Systems, the warehouse robot maker, for about $775 million.{cite(23)}</p></div>
<div class="ev"><div class="yr">2020</div><p>Boston Dynamics starts selling Spot. Hyundai takes a controlling stake in the company.{cite(24)}</p></div>
<div class="ev big"><div class="yr">2023</div><p>Google DeepMind shows RT-2, a model that turns camera images and a spoken instruction into robot motion.{cite(21)}</p></div>
<div class="ev big"><div class="yr">2024 to 2025</div><p>Unitree launches a humanoid with a base price of about $16,000.{cite(22)} Figure AI raises over $1 billion at a $39 billion valuation.{cite(3)}</p></div>
<div class="ev big"><div class="yr">2025</div><p>Amazon announces its millionth robot.{cite(17)} ISO publishes a revised industrial robot safety standard, ISO 10218.{cite(18)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The first tests of whether humanoids can work for months without help. See chapter 6.</p></div>
</div>''', K.key_idea("Great at one job, learning to do many",
        "Robots are a mature business in factories, warehouses and operating theatres. The new bet is that AI will let one robot do many different "
        "jobs. That has been shown in research and pilots, and we found no independent figures at scale."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>AI models can now turn what a camera sees and a spoken instruction into a movement, in research.{cite(21)}</p></div>
<div class="card rv"><h3>What has not</h3><p>The robots earning money are specialists. We found no independent uptime or cost figures for humanoids.</p></div>
<div class="card rv"><h3>What is new</h3><p>Large funding rounds for humanoid makers, and a base humanoid launched at about $16,000.{cite(3)}{cite(22)}</p></div>
</div>
<div class="wide">{photo("canadarm2.jpg", caption="An astronaut riding Canadarm2, the robotic arm on the International Space Station.")}</div>''',
        K.key_idea("Many robots, few general ones",
                   "The robots earning money today are specialists. The general-purpose humanoid is being tested in factories and has not yet "
                   "been shown, in public figures, to pay for itself."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Warehouses and factories first, homes last. Our judgement, not a forecast.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now: warehouses and logistics</div><p>Robots that move boxes and pallets are already at large scale. Amazon alone has about a million.{cite(17)}</p></div>
<div class="ev fut"><div class="yr">Next: factories</div><p>Humanoids and mobile arms handle the jobs between machines. Pilots become repeat orders, or they do not.</p></div>
<div class="ev fut"><div class="yr">After that: care, hospitality and homes</div><p>Each needs a robot to work near people without supervision. Safety rules matter here. The revised ISO 10218 covers industrial robots and cooperative work.{cite(18)}</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The data</h3><p>The IFR publishes robot density by country. In 2023 the EU average was 219 and the United States 295.{cite(11)} We found no IFR figure for Ireland.</p></div>
<div class="card rv"><h3>The jobs</h3><p>Official employment and earnings data are published by the CSO.{cite(2)}</p></div>
<div class="card rv"><h3>The watch</h3><p>Watch for orders and pilots in warehousing, delivery and manufacturing, where the first exposure is.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a worker</h3><p>Tasks that repeat in a fixed place go first. Jobs that need judgement and a different setting each hour go last.</p></div>
<div class="card rv"><h3>As a business</h3><p>Ask a supplier for uptime and cost per task in a customer site like yours, not for a demonstration. Start with one narrow job.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Robotics shares fall into established suppliers with earnings and young firms with promises. They have behaved very differently.</p></div>
</div>''', K.key_idea("Narrow jobs first, then wider ones",
        "Robots move into the jobs that are repetitive and in a predictable place, then into the ones that need more judgement. "
        "The order is clear. The dates are not."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Established suppliers with earnings, and young firms valued on a plan.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The humanoid makers<span>Mostly private</span></h3>
<dl><dt>Who</dt><dd>Tesla (Optimus), Figure, Agility Robotics, Boston Dynamics (controlled by Hyundai), Unitree and others.{cite(24)}</dd>
<dt>The money</dt><dd>Figure AI raised over $1 billion in September 2025 at a $39 billion valuation.{cite(3)}</dd>
<dt>Use</dt><dd>Treat production targets as targets. Tesla is a car company first, and its robot plans are a small part of its price today.</dd></dl><span class="verdict">The excitement, mostly off the exchange</span></article></div>
{K.prices_block("s-prices", "Share prices", "Five robotics companies, with Tesla and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. The young names rose far faster than the established ones, and fell far faster too.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Warehouse and surgical robots are on the upper rungs. Humanoids are between the second and the third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Customers reorder after a pilot.</li><li>Uptime and cost per task are published.</li><li>A robot costs less than the work it replaces within two years.</li><li>Revenue grows without share sales.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Demonstration videos with no failure rate.</li><li>Production targets with no factory.</li><li>Valuations set by a single customer.</li><li>Prices rise on a rival's announcement.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>high robot density</span><span><i style="border-color:var(--violet)"></i>mid-table</span><span><i style="border-color:var(--red)"></i>no data found</span>', "Pick a country. Robot density figures are the IFR's, for 2023.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("Surgeons and warehouses pay. Humanoids are still a promise",
        "The companies with revenue sell to hospitals, warehouses and factories. The humanoid makers are mostly private, "
        "and the listed names that rose on them have moved far more than their results."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Concentration, small revenue, supply and proof.", f'''
<div class="cols wide">
<div class="card rv"><h3>One big customer</h3><p>Walmart was about 85% of Symbotic's fiscal 2025 revenue.{cite(14)}</p></div>
<div class="card rv"><h3>Fleets without revenue</h3><p>Serve Robotics ran 2,000 robots by the end of 2025 and reported $2.7 million of revenue for the year.{cite(16)}</p></div>
<div class="card rv"><h3>A shrinking robot business</h3><p>Teradyne's robotics revenue fell 15.5% in 2025.{cite(15)}</p></div>
<div class="card rv"><h3>Supply</h3><p>China made 94% of the world's sintered permanent magnets in 2024.{cite(19)}</p></div>
<div class="card rv"><h3>Safety rules</h3><p>ISO revised its industrial robot safety standard in 2025, and it now includes the content of the earlier collaborative-robot specification.{cite(18)}</p></div>
<div class="card rv"><h3>Proof</h3><p>We found no independent uptime or cost-per-task figures for humanoid robots.</p></div>
</div>
<div class="fx-photos wide">{photo("valkyrie.jpg", caption="Valkyrie, a research humanoid.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>A robot has to do the job for less than a person costs, every day, with little supervision. That is shown by months of operation, not minutes of video.</p></div></div>''',
        K.key_idea("A reliability problem more than an intelligence problem",
                   "A smart robot that fails one time in ten is not a product. The firms that win will be the ones with the most hours of "
                   "dull, dependable operation."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 80%</h3><p>More warehouse and logistics robots. More factory pilots of humanoids. New AI models for robot control.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>At least one firm publishes uptime and cost figures for a humanoid fleet of over 1,000 units at paying customers.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>A general-purpose home robot sold in large numbers and used for chores without supervision.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">Robots will keep taking jobs that repeat. The robot that does anything is further off than its demos suggest.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. The young names have fallen steeply from their peaks and need more money.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Firms with one big customer, or with large losses and small revenue. Intuitive and Rockwell have earnings that carry them.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A humanoid that repeats the same quality of work for months would open the market for factory and logistics labour.</p></div>
<div class="card rv"><h3>The test</h3><p>For each firm, ask for three numbers: units in paid use, hours between interventions, and cost per task against the wage it replaces.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A large customer publishing uptime and cost for a humanoid fleet. A reorder at ten times pilot scale. A published safety standard for walking robots near the public.</div>''',
        K.key_idea("Steady growth for the proven, a long wait for the promised",
                   "We expect the proven robot businesses to keep growing and the humanoid story to produce more pilots than profits. "
                   "The prices of the young names reflect the story at its best."), short="Outlook")

    bands = [band("kuka-palletising.jpg", "Where robots work now", "Doing the same task every time, in the same place.", "Industrial robots palletising bread"),
             band("robonaut-2.jpg", "Hands", "The hardest part to copy from a person.", "NASA's Robonaut 2 working with a tool"),
             band("canadarm2.jpg", "In orbit", "A robot arm on the space station.", "An astronaut on the Canadarm2 robotic arm"),
             band("valkyrie.jpg", "Two legs", "A research humanoid built for disaster response.", "NASA's Valkyrie humanoid robot"),
             band("robonaut-2.jpg", "Three years", "Time enough to see if pilots become fleets.", "NASA's Robonaut 2")]
    foot = K.foot(REFS, AS_OF, "Frontier Bot", "bot",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Robot counts and company facts were checked against the sources listed and are rounded. Where sources disagreed the text says so.")
    nf = K.notice("We explain how robots and physical AI work and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Industrial robots installed 2024", "542,076"), ("Amazon robots", "about 1 million"), ("Top density 2023", "South Korea"), ("Humanoids at scale", "not shown")]
    body = K.assemble("bot", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
