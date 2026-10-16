"""Frontier Bot: robots and physical AI. Voice rules: docs/VOICE.md."""
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
    (1, "International Federation of Robotics. World Robotics report (annual).", "https://ifr.org/worldrobotics/"),
    (2, "International Federation of Robotics. Robot density in manufacturing (press release).", "https://ifr.org/ifr-press-releases/"),
    (3, "Amazon (2025). Amazon deploys its one millionth robot.", "https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model"),
    (4, "Intuitive Surgical. Investor relations and annual report.", "https://isrg.intuitive.com/"),
    (5, "Symbotic. Annual report on Form 10-K.", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1837240&type=10-K"),
    (6, "Brohan et al. (2023). RT-2: vision-language-action models transfer web knowledge to robotic control.", "https://arxiv.org/abs/2307.15818"),
    (7, "Unitree Robotics. Humanoid robot G1.", "https://www.unitree.com/g1"),
    (8, "US Bureau of Labor Statistics. Occupational employment and wages.", "https://www.bls.gov/oes/"),
    (9, "Central Statistics Office (Ireland). Industrial production and turnover.", "https://www.cso.ie/en/"),
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
    "TER": [Scenario("bear", "Chip test demand falls and robotics stays loss-making", 0.30, -0.25, 0.75),
            Scenario("base", "Test business carries earnings, robotics is flat", 0.45, 0.08, 0.75),
            Scenario("bull", "Chip test and robotics both grow", 0.25, 0.30, 0.75)],
    "ISRG": [Scenario("bear", "Procedure growth slows and rivals take share", 0.25, -0.20, 0.75),
             Scenario("base", "Steady growth in procedures and systems", 0.50, 0.10, 0.75),
             Scenario("bull", "New systems and new markets extend the growth", 0.25, 0.28, 0.75)],
    "ROK": [Scenario("bear", "Factory spending stays flat or falls", 0.30, -0.20, 0.75),
            Scenario("base", "Gradual recovery in factory automation", 0.45, 0.08, 0.75),
            Scenario("bull", "A factory-building boom in the US lifts orders", 0.25, 0.28, 0.75)],
}

COMPANIES = [
    {"t": "SYM", "name": "Symbotic", "kind": "Warehouse automation",
     "rivals": "Ocado, AutoStore, Dematic (KION), Amazon's own systems",
     "profit": "Install robotic warehouse systems for large retailers, then collect software and service fees. Most of its revenue comes from one customer, Walmart.",
     "watch": "Customer concentration, order backlog, margins, new customers.",
     "rank": "One of the larger listed warehouse robot firms, with a very concentrated customer base.",
     "verdict": "A big order book and one big customer"},
    {"t": "SERV", "name": "Serve Robotics", "kind": "Sidewalk delivery robots",
     "rivals": "Starship, Coco, Avride, and human couriers",
     "profit": "Run a fleet of delivery robots at a cost per delivery below a courier's. Revenue is small compared with its costs.",
     "watch": "Revenue per robot, cash runway, share sales, partner cities.",
     "rank": "A young listed company with a larger fleet than most rivals and large losses.",
     "verdict": "A fleet, not yet a profit"},
    {"t": "TER", "name": "Teradyne", "kind": "Chip test equipment and robots",
     "rivals": "Advantest in test. FANUC, ABB, Doosan in robot arms",
     "profit": "Mostly earns from testing semiconductors. Its robotics group, Universal Robots and Mobile Industrial Robots, is a small part and has struggled to grow.",
     "watch": "AI chip test demand, robotics revenue and margin.",
     "rank": "A chip-test company with a robotics business attached.",
     "verdict": "Robots are the side business"},
    {"t": "ISRG", "name": "Intuitive Surgical", "kind": "Surgical robots",
     "rivals": "Medtronic, Johnson & Johnson, CMR Surgical, Asensus",
     "profit": "Sell da Vinci systems, then earn on instruments and service every time one is used. Most revenue is recurring.",
     "watch": "Procedure growth, new system launches, rival approvals, pricing.",
     "rank": "The established leader, with more than 10,000 systems installed.",
     "verdict": "The proof that robots can be a great business"},
    {"t": "ROK", "name": "Rockwell Automation", "kind": "Factory automation and controls",
     "rivals": "Siemens, Schneider Electric, ABB, Mitsubishi Electric",
     "profit": "Sell the controllers, drives and software that run factories. Customers spend when they build or upgrade plants.",
     "watch": "Orders, factory investment, software share of revenue.",
     "rank": "A large, steady supplier of the equipment around robots, rather than the robots.",
     "verdict": "The steady one"},
]

LADDER = [("Demo", "Works in a|video"), ("Pilot", "Works at a|customer site"), ("Reliable", "Runs for months|with little help"),
          ("Paid at scale", "Thousands of|units sold"), ("Cheaper than labour", "Costs less than the|person it replaces"),
          ("Fleet", "Factories build|robots in volume"), ("Profit", "Owners earn their|return")]

TILES = {"CA": (1, 0, "mixed"), "US": (1, 1, "friendly"), "IE": (3, 0, "restrictive"), "GB": (4, 0, "mixed"), "FR": (4, 1, "mixed"),
         "DE": (6, 0, "friendly"), "CH": (5, 1, "friendly"), "CN": (9, 1, "friendly"), "KR": (10, 0, "friendly"), "JP": (11, 1, "friendly")}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "FR": "France", "DE": "Germany",
         "CH": "Switzerland", "CN": "China", "KR": "South Korea", "JP": "Japan"}
COUNTRY = {
    "CN": {"co": "Unitree, UBTech, Estun, Siasun, Midea (owns KUKA), DJI", "gov": "National robotics plans, large subsidies and the largest market: more than half of the world's new industrial robots",
           "ctl": "Controls most rare-earth magnet supply that robot motors need", "note": "The biggest buyer and a fast-rising maker, including cheap humanoids."},
    "JP": {"co": "FANUC, Yaskawa, Kawasaki, Nachi, Harmonic Drive Systems", "gov": "Long-standing industrial robot policy and an ageing workforce", "ctl": "Dominates precision gearboxes",
           "note": "The long-time leader in arms and in the gearboxes inside every robot."},
    "KR": {"co": "Hyundai (owns Boston Dynamics), Doosan Robotics, Rainbow Robotics", "gov": "Backs robotics as a national industry", "ctl": "Follows allied rules",
           "note": "The highest robot density in the world in manufacturing, at over 1,000 per 10,000 workers."},
    "DE": {"co": "KUKA (owned by Midea), Siemens, Festo, Neura Robotics", "gov": "Strong industrial base and European funding", "ctl": "EU rules", "note": "Large user and a leading maker of arms and factory systems."},
    "CH": {"co": "ABB Robotics, Comau-linked suppliers, Sensirion", "gov": "Research strength in robotics at ETH Zurich", "ctl": "EU-aligned", "note": "Home of ABB and a deep research base."},
    "US": {"co": "Tesla, Figure, Agility Robotics, Apptronik, Amazon, Intuitive, Symbotic, Boston Dynamics (Hyundai-owned)", "gov": "Policy debate on tariffs and a national robotics strategy; large venture funding",
           "ctl": "Depends on imported magnets, gearboxes and arms", "note": "The most humanoid start-ups and the most funding, with a lower robot density than many peers."},
    "GB": {"co": "Ocado, CMR Surgical, Dyson research, Extend Robotics", "gov": "Research funding through UKRI", "ctl": "Follows allied rules", "note": "Strong in warehouse systems and surgical robots, with a lower factory density."},
    "FR": {"co": "Exotec, Wandercraft, Pollen Robotics", "gov": "National AI and robotics funding", "ctl": "EU rules", "note": "A small but active group of start-ups."},
    "CA": {"co": "Kinova, Clearpath (Rockwell), Sanctuary AI", "gov": "Research funding", "ctl": "Follows allied rules", "note": "Strong research base, few large producers."},
    "IE": {"co": "Medtech and pharmaceutical plants that use robots, and a small number of start-ups", "gov": "Enterprise Ireland and IDA support automation", "ctl": "EU rules",
           "note": "A heavy automation user in medical devices and pharma, with few robot makers of its own."},
}
HYPE = [
    ("5", "Years of paid operation at scale", "Thousands of units doing a job for customers who renew", "Warehouse robots, surgical robots, industrial arms", "ok"),
    ("4", "Repeat orders from large customers", "A customer buys again after a pilot", "Amazon and Walmart fleets", "ok"),
    ("3", "Pilot with a named customer", "A trial at a factory or warehouse", "Humanoid pilots in car plants", "dis"),
    ("2", "A demonstration video", "A robot doing a task, filmed", "Folding laundry, making coffee", "tgt"),
    ("1", "Production target", "A number of units to be built", "'A million humanoids a year'", "tgt"),
]
SHOVELS = [
    ("Gearboxes and joints", "Harmonic Drive Systems, Nabtesco, Schaeffler", "Japan, Germany", "Precision gearing is the largest cost in an arm"),
    ("Rare-earth magnets", "JL Mag, Shin-Etsu, Neo Performance", "China, Japan", "China produces about nine tenths of the world's permanent magnets"),
    ("Sensors and vision", "Cognex, Hesai, Ouster, Sony, Keyence", "US, China, Japan", "Cameras and lidar are how a robot sees"),
    ("Onboard chips", "NVIDIA, Qualcomm, Intel", "US", "Robots run vision models locally"),
    ("Batteries", "CATL, Panasonic, LG Energy Solution", "China, Japan, Korea", "Runtime is the weak point for mobile robots"),
    ("Integrators", "Many small firms", "Everywhere", "The people who make a robot useful in a particular plant"),
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
                                     COUNTRY, NAMES, {"co": "Firms", "gov": "Policy", "ctl": "Supply and trade", "note": "Read"}, "IE")
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
                  "Half a million industrial robots go into factories every year, and a million more work in Amazon's warehouses. Now AI is being used to teach them to cope with the messy world outside the cage. Here is what works, who is paid, and what is still a video.",
                  "robonaut-2.jpg", art_more.hero_reactor(),
                  [(542, "thousand industrial robots installed worldwide in 2024, roughly", "about ", ""), (1, "million robots working in Amazon's warehouses, roughly", "about ", " million"),
                   (round(runs["SYM"]["multiple"]), "times Symbotic rose from low to high in under two years", "", "x"),
                   (16, "thousand dollars: the starting price of a Unitree humanoid", "about $", "k")])

    ch1 = chapter("learn", 1, "How it works, and where it breaks", "Sense, decide, move. The first is solved, the second is being solved and the third is expensive.", f'''
<p>A robot is a machine that senses its surroundings, decides what to do and moves something to do it. The first robots, from 1961, repeated one motion inside a cage. Today's robots have cameras, force sensors and software that adjusts to what it sees. The newest idea is to let large AI models, trained on images, text and recorded movement, plan the next action for any robot body.{cite(6)}</p>
{note("Why it is attractive", "<p>A robot works through the night, does not tire and gets cheaper to make with volume. In places where workers are scarce or ageing, a robot that can do a varied job is worth a lot.</p>")}
<p>The International Federation of Robotics counted about 542,000 new industrial robots in 2024 and a working stock of over four million. China took more than half of the new ones.{cite(1)} South Korea has the highest density, more than 1,000 robots for every 10,000 manufacturing workers.{cite(2)}</p>
{note("The catch", "<p>The robots that work today do one thing in one place. A robot that copes with a different job each day has been demonstrated in videos and pilots, not yet at scale.</p>")}
<div class="fx-photos wide">
{photo("kuka-palletising.jpg", caption="Industrial robots stacking loaves of bread in a bakery. The job is the same every time, which is what these machines are good at.")}
{photo("robonaut-2.jpg", caption="Robonaut 2, built by NASA and General Motors, working with a tool. It flew to the International Space Station in 2011.")}
{photo("valkyrie.jpg", caption="NASA's Valkyrie humanoid robot, built for research into disaster response.")}
</div>
<h3 class="wide" id="s-paths" data-nav="Waves" style="margin-top:36px">Three waves</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Arms in cages</h3><p>Fast, accurate and fixed in place. Car plants and electronics factories run on them. This market is mature and cyclical.{cite(1)}</p></div>
<div class="card rv"><h3>Robots that move</h3><p>Warehouse robots that carry shelves, and delivery robots on pavements. Amazon alone runs about a million.{cite(3)}</p></div>
<div class="card rv"><h3>Robots that learn</h3><p>Arms and humanoids that pick up new tasks from demonstrations and instructions. Still mostly in trials.</p></div>
<div class="card rv"><h3>Robots in medicine</h3><p>Surgeon-controlled systems are the clearest commercial success of the field. Intuitive has more than 10,000 in hospitals.{cite(4)}</p></div>
</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">
<div class="card rv"><h3>Hands</h3><p>The human hand has 27 degrees of freedom and a fine sense of touch. Robot hands have fewer joints and much less touch. Many everyday tasks depend on both.</p></div>
<div class="card rv"><h3>Data</h3><p>Language models learned from the internet. There is no internet of robot movement, so firms record humans and run simulations instead.</p></div>
<div class="card rv"><h3>Reliability</h3><p>A task that works nine times in ten is useless in a factory. A robot needs to work thousands of times in a row.</p></div>
<div class="card rv"><h3>Safety</h3><p>A strong machine near people must stop reliably. Standards for walking humanoids are still being written.{cite(10)}</p></div>
</div>
{TB.bot_html(cite)}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1961</div><p>Unimate, the first industrial robot, starts work at a General Motors plant.</p></div>
<div class="ev"><div class="yr">2000</div><p>The da Vinci surgical system is approved in the US.</p></div>
<div class="ev"><div class="yr">2012</div><p>Amazon buys Kiva Systems, the warehouse robot maker, and begins to build its own fleet.</p></div>
<div class="ev"><div class="yr">2020</div><p>Boston Dynamics starts selling Spot, a four-legged robot.</p></div>
<div class="ev big"><div class="yr">2023</div><p>Google shows a model that turns camera images and a spoken instruction into robot motion.{cite(6)}</p></div>
<div class="ev big"><div class="yr">2024 to 2025</div><p>Humanoid start-ups raise billions of dollars. Pilots start in car plants and warehouses. Chinese firms sell humanoids at a fraction of Western prices.{cite(7)}</p></div>
<div class="ev big"><div class="yr">2025</div><p>Amazon passes one million robots.{cite(3)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The first tests of whether humanoids can work for months without help. See chapter 6.</p></div>
</div>''', K.key_idea("Great at one job, learning to do many",
        "Robots are a mature business in factories, warehouses and operating theatres. The new bet is that AI will let one robot do many different "
        "jobs. That has been shown in videos and pilots, and has not yet been shown at scale."), short="Basics")

    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">
<div class="card rv"><h3>What changed</h3><p>AI models can now turn what a camera sees and a spoken instruction into a movement, so a robot can be taught by showing it.</p></div>
<div class="card rv"><h3>What has not</h3><p>Hands, battery life, reliability and cost are still far from what a general worker needs.</p></div>
<div class="card rv"><h3>What is new</h3><p>Billions of dollars from investors, car makers and governments for humanoid robots, and prices from China starting near US$16,000.{cite(7)}</p></div>
</div>
<div class="wide">{photo("canadarm2.jpg", caption="An astronaut riding Canadarm2, the robotic arm on the International Space Station. It has worked in orbit since 2001.")}</div>''',
        K.key_idea("Many robots, few general ones",
                   "The robots earning money today are specialists. The general-purpose humanoid is being tested in factories and has not yet "
                   "been shown to pay for itself."), short="Simple")

    ch3 = chapter("change", 3, "What changes, and in what order", "Warehouses first, factories second, homes last.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2028: warehouses and logistics</div><p>Robots that move boxes and pallets spread through large distribution centres. This is where the money is today.</p></div>
<div class="ev fut"><div class="yr">2027 to 2030: factories</div><p>Humanoid and mobile manipulators handle the jobs between machines, such as feeding parts and moving totes. Pilots become repeat orders, or they do not.</p></div>
<div class="ev fut"><div class="yr">2028 to 2032: care and hospitality</div><p>Cleaning, hospital logistics and food service. Each needs a robot to work near people without supervision.</p></div>
<div class="ev fut"><div class="yr">Late 2020s to 2030s: homes</div><p>Company targets only. Price, safety and trust all have to be solved.</p></div>
</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">
<div class="card rv"><h3>The industry</h3><p>Ireland's factory output is dominated by pharmaceuticals, medical devices and electronics, which already use precision automation.{cite(9)} It has few robot makers.</p></div>
<div class="card rv"><h3>The jobs</h3><p>Warehouse, delivery and manufacturing jobs are the first exposed to robots. Pay and employment figures are in the official labour statistics.{cite(8)}</p></div>
<div class="card rv"><h3>The chance</h3><p>Software, integration and testing of robots for medtech and food are areas where an Irish firm could build a niche.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>As a worker</h3><p>Tasks that repeat in a fixed place go first. Jobs that need judgement, touch and a different setting each hour go last.</p></div>
<div class="card rv"><h3>As a business</h3><p>Ask a supplier for uptime and cost per task in a customer site like yours, not for a demonstration. Start with one narrow job.</p></div>
<div class="card rv"><h3>As an investor</h3><p>Robotics shares fall into established suppliers with earnings and young firms with promises. They have behaved very differently.</p></div>
</div>''', K.key_idea("Narrow jobs first, then wider ones",
        "Robots move into the jobs that are repetitive, dull and in a predictable place, then into the ones that need more judgement. "
        "The order is clear. The dates are not."), short="Change")

    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Established suppliers with earnings, and young firms valued on a plan.", f'''
<div class="cols wide">{K.company_cards(COMPANIES, stat)}
<article class="card co rv"><h3>The humanoid makers<span>Mostly private</span></h3>
<dl><dt>Who</dt><dd>Tesla (Optimus), Figure, Agility Robotics, Apptronik, 1X, Boston Dynamics (owned by Hyundai), Unitree and UBTech in China, and others.{cite(12)}</dd>
<dt>Why they matter</dt><dd>They are the reason for much of the excitement, and the reason many listed robotics names rose in 2025. Few have revenue beyond pilots.</dd>
<dt>Use</dt><dd>Treat production targets as targets. Tesla is a car company first, and its robot plans are a small part of its price today.</dd></dl><span class="verdict">The excitement, mostly off the exchange</span></article></div>
{K.prices_block("s-prices", "Share prices", "Five robotics companies, with Tesla and Nvidia for scale.")}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), "Log scale, from weekly closes, adjusted for splits. The young names rose far faster than the established ones, and fell far faster too.", 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 2), "Warehouse and surgical robots are on the upper rungs. Humanoids are between the second and the third.", 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>Customers reorder after a pilot.</li><li>Uptime and cost per task are published.</li><li>A robot costs less than the work it replaces within two years.</li><li>Revenue grows without share sales.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Demonstration videos with no failure rate.</li><li>Production targets of a million units a year with no factory.</li><li>Valuations set by a single customer.</li><li>Prices rise on a rival's announcement.</li></ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(HYPE)}</tbody></table></div>
{K.map_block(tile_map(TILES, NAMES), '<span><i style="border-color:var(--teal)"></i>leading maker or user</span><span><i style="border-color:var(--violet)"></i>strong in part</span><span><i style="border-color:var(--red)"></i>few makers</span>', "Pick a country. A summary from public sources, so treat the detail as approximate.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(SHOVELS)}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea("Surgeons and warehouses pay. Humanoids are still a promise",
        "The companies with revenue sell to hospitals, warehouses and factories. The humanoid makers are mostly private, "
        "and the listed names that rose on them have moved far more than their results."), short="Money")

    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", "Hands, data, uptime, safety and cost.", f'''
<div class="cols wide">
<div class="card rv"><h3>Uptime</h3><p>A robot that needs rescuing every hour costs more than the person it replaced. Published uptime figures are rare.</p></div>
<div class="card rv"><h3>Hands and touch</h3><p>Picking an unfamiliar object without damage is a skill robots do not yet have. It limits what a humanoid can do.</p></div>
<div class="card rv"><h3>Cost and parts</h3><p>The cost is in actuators, gearboxes and sensors, with magnets mostly from China.{cite(13)}</p></div>
<div class="card rv"><h3>Safety rules</h3><p>Industrial robot standards exist and are being extended to cooperating machines. Rules for walking robots near the public are still being drafted.{cite(10)}</p></div>
<div class="card rv"><h3>Data</h3><p>Teaching one robot to do a task takes hours of human demonstration. Doing it across many tasks takes much more.</p></div>
<div class="card rv"><h3>Competition</h3><p>A simple wheeled robot with one arm often beats a humanoid on cost and reliability for a given job.</p></div>
</div>
<div class="fx-photos wide">{photo("valkyrie.jpg", caption="Valkyrie, a research humanoid. Walking on two legs is expensive and unstable, and many tasks are done better by a machine on wheels.")}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>A robot has to do the job for less than a person costs, every day, with little supervision. Cheaper hardware helps. The harder part is a robot that does not need help, and that is shown by months of operation, not minutes of video.</p></div></div>''',
        K.key_idea("A reliability problem more than an intelligence problem",
                   "A smart robot that fails one time in ten is not a product. The firms that win will be the ones with the most hours of "
                   "dull, dependable operation."), short="Limits")

    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 80%</h3><p>More warehouse and logistics robots. More factory pilots of humanoids. Cheaper arms from China. New AI models for robot control.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>At least one firm reports a humanoid fleet of over 1,000 units working at paying customers for a year.</p></div>
<div class="card rv"><h3>Unlikely, under 15%</h3><p>A general-purpose home robot sold in large numbers and used for chores without supervision.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(COMPANIES, sims), 4, "five")}
<div class="pull wide">Robots will keep taking jobs that repeat. The robot that does anything is further off than its demos suggest.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>Our scenarios put the chance of each company ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}. The young names have fallen steeply from their peaks and need more money.</p></div>
<div class="card rv"><h3>Who is exposed</h3><p>Firms with one big customer, or with large losses and no revenue to speak of. Intuitive and Rockwell have earnings that carry them.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>A humanoid that repeats the same quality of work for months would open the market for factory and logistics labour. The beneficiaries include parts makers more than robot brands.</p></div>
<div class="card rv"><h3>The test</h3><p>For each firm, ask for three numbers: units in paid use, hours between interventions, and cost per task against the wage it replaces.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A large customer publishing uptime and cost for a humanoid fleet. A reorder at ten times pilot scale. A published safety standard for walking robots near the public.</div>''',
        K.key_idea("Steady growth for the proven, a long wait for the promised",
                   "We expect the proven robot businesses to keep growing and the humanoid story to produce more pilots than profits. "
                   "The prices of the young names reflect the story at its best."), short="Outlook")

    bands = [band("kuka-palletising.jpg", "Where robots work now", "Doing the same task every time, in the same place.", "Industrial robots palletising bread"),
             band("robonaut-2.jpg", "Hands", "The hardest part to copy from a person.", "NASA's Robonaut 2 working with a tool"),
             band("canadarm2.jpg", "In orbit", "Robot arms have worked on the space station for over twenty years.", "An astronaut on the Canadarm2 robotic arm"),
             band("valkyrie.jpg", "Two legs", "Walking is a costly way to move for a machine.", "NASA's Valkyrie humanoid robot"),
             band("robonaut-2.jpg", "Three years", "Time enough to see if pilots become fleets.", "NASA's Robonaut 2")]
    foot = K.foot(REFS, AS_OF, "Frontier Bot", "bot",
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  "Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Robot counts and company facts are from public sources and are rounded.")
    nf = K.notice("We explain how robots and physical AI work and show how the companies and their shares have behaved. We do not recommend any company or trade. Projections are scenarios, not forecasts.")
    facts = [("Industrial robots a year", "about 540,000"), ("Amazon robots", "about 1 million"), ("Top density", "South Korea"), ("Humanoids at scale", "none yet")]
    body = K.assemble("bot", hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, facts)
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
