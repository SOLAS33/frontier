"""Technical depth for Frontier Bot: numbers, robot types, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

BOT_REFS = [
    (10, "International Federation of Robotics (2025). Global robot demand in factories doubles over 10 years (World Robotics 2025).", "https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years"),
    (11, "International Federation of Robotics (2024). Global robot density in factories doubled in seven years.", "https://ifr.org/ifr-press-releases/news/global-robot-density-in-factories-doubled-in-seven-years"),
    (12, "Intuitive Surgical. Annual report on Form 10-K for 2025.", "https://www.sec.gov/Archives/edgar/data/1035267/000103526726000010/isrg-20251231.htm"),
    (13, "Intuitive Surgical (2000). Intuitive Surgical announces second quarter results (FDA clearance of the da Vinci system, July 2000).", "https://investor.intuitivesurgical.com/news-releases/news-release-details/intuitive-surgical-announces-second-quarter-results"),
    (14, "Symbotic. Annual report on Form 10-K for fiscal 2025.", "https://www.sec.gov/Archives/edgar/data/1837240/000183724025000278/sym-20250927.htm"),
    (15, "Teradyne. Annual report on Form 10-K for 2025.", "https://www.sec.gov/Archives/edgar/data/97210/000119312526059002/ter-20251231.htm"),
    (16, "Serve Robotics (2026). Fourth quarter and full year 2025 results.", "https://investors.serverobotics.com/news-releases/news-release-details/serve-robotics-announces-fourth-quarter-and-full-year-2025"),
    (17, "Amazon (2025). Amazon deploys its one millionth robot and launches DeepFleet.", "https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model"),
    (18, "Association for Advancing Automation. Updated ISO 10218: answers to frequently asked questions.", "https://www.automate.org/robotics/blogs/updated-iso-10218-faq"),
    (19, "International Energy Agency. Rare earth elements: executive summary.", "https://www.iea.org/reports/rare-earth-elements/executive-summary"),
    (20, "Wikipedia. Unimation (first industrial robot at General Motors, Ewing Township, 1961).", "https://en.wikipedia.org/wiki/Unimation"),
    (21, "Google DeepMind (2023). RT-2: new model translates vision and language into action.", "https://deepmind.google/discover/blog/rt-2-new-model-translates-vision-and-language-into-action"),
    (22, "heise online (2024). Humanoid robot Unitree G1 costs 16,000 dollars.", "https://heise.de/-9720187"),
    (23, "Bloomberg (2012). Amazon to buy Kiva Systems in biggest deal since Zappos.", "https://www.bloomberg.com/news/articles/2012-03-19/amazon-acquires-kiva-systems-in-second-biggest-takeover"),
    (24, "The Boston Globe (2020). Hyundai buys controlling stake in Boston Dynamics.", "https://www.bostonglobe.com/2020/12/11/business/hyundai-buys-controlling-stake-boston-dynamics-valuing-company-11-billion"),
    (25, "NVIDIA. Isaac GR00T: foundation models for humanoid robots.", "https://developer.nvidia.com/isaac/gr00t"),
]


def bot_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Industrial robots installed in 2024", "542,076" + cite(10), "More than double the number ten years earlier. China took 54%, or 295,000"],
        ["Industrial robots in use worldwide", "4.66 million at the end of 2024" + cite(10), "Up 9% on the year before"],
        ["Robot density, 2023", "South Korea 1,012 per 10,000 factory workers. Singapore 770. China 470. Germany 429. Japan 419. United States 295" + cite(11), "The world average was 162. The US ranked tenth"],
        ["Amazon's fleet", "One million robots, announced July 2025" + cite(17), "Amazon says its DeepFleet AI model should cut fleet travel time by 10%"],
        ["Intuitive's da Vinci", "11,106 systems installed and about 3.15 million procedures in 2025" + cite(12), "The clearest commercial success of surgical robots"],
        ["A humanoid on sale", "Unitree G1 launched at a base price of about $16,000 (2024)" + cite(22), "A launch price. Extras such as dexterous hands cost more"],
        ["Rare-earth magnets", "China made 94% of the world's sintered permanent magnets in 2024" + cite(19), "Robot motors use these magnets"],
    ])
    kinds = _table(["Type", "What it does", "Examples", "Status"], [
        ["Industrial arm", "Welds, paints, lifts and places, usually in a fenced cell", "Counted by the IFR: 542,076 installed in 2024" + cite(10), "Mature and cyclical"],
        ["Warehouse mobile robot", "Moves shelves, totes and pallets", "Amazon's Hercules, Pegasus and Proteus. Symbotic" + cite(17) + cite(14), "Large scale. Amazon alone has about a million robots"],
        ["Surgical robot", "A surgeon steers instruments through small cuts", "Intuitive da Vinci" + cite(12), "Mature at the leader"],
        ["Delivery robot", "Carries food and parcels on pavements", "Serve Robotics, with 2,000 robots by the end of 2025" + cite(16), "Commercial, with tiny revenue so far"],
        ["Legged and mobile manipulator", "Walks or rolls and picks things up", "Boston Dynamics Spot, first sold in 2020, and Atlas" + cite(24), "Selling to industry"],
        ["Humanoid", "Walks on two legs and uses tools made for people", "Unitree G1, Figure, Agility Digit, Tesla Optimus", "Pilots reported. Not yet shown at scale"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["First industrial robot at work", "Unimate at a General Motors plant in Ewing Township, New Jersey, 1961" + cite(20), _tag("ok"), "It lifted hot die-cast parts. Sources differ on whether it was sold in 1960 or shipped in 1961"],
        ["Robot-assisted surgery cleared", "da Vinci, US FDA, 11 July 2000, for general laparoscopic surgery" + cite(13), _tag("ok"), "About 3.15 million da Vinci procedures in 2025" + cite(12)],
        ["Large-scale warehouse robots", "Amazon agreed to buy Kiva Systems for about $775 million in 2012" + cite(23), _tag("ok"), "Amazon announced its millionth robot in July 2025" + cite(17)],
        ["Robots from a lab sold commercially", "Boston Dynamics Spot, 2020" + cite(24), _tag("ok"), "Hyundai took a controlling stake the same year"],
        ["A model that turns images and words into robot actions", "Google DeepMind RT-2, July 2023" + cite(21), _tag("ok"), "A research result"],
        ["Humanoids in paid pilots", "Several companies, 2024 on", _tag("dis"), "Pilots are reported. We found no independent figures for uptime or cost"],
        ["A humanoid doing varied work for months without help", "No one yet", _tag("tgt"), "The test that matters for the business case"],
    ])
    gl = _gloss([
        ("Actuator", "The motor and gearbox that moves a joint."),
        ("Degrees of freedom", "The number of independent ways a robot can move."),
        ("Cobot", "A collaborative robot, built to work beside people at limited force and speed. ISO 10218 was revised in 2025 and now covers them." + cite(18)),
        ("Robot density", "Robots per 10,000 manufacturing employees. The IFR's standard comparison between countries." + cite(11)),
        ("Teleoperation", "A person steers the robot, often to produce training data."),
        ("Imitation learning", "The robot learns from recordings of a person doing the task."),
        ("VLA model", "Vision-language-action model: one network that takes camera images and an instruction and outputs motions." + cite(21)),
        ("Foundation model for robots", "A large model trained on many tasks and robot types, then adapted to one robot." + cite(25)),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A robot is a loop. Sensors such as cameras, force sensors and joint encoders measure the world. Software decides what to do next. Motors and gearboxes move the joints. For a fixed task, such as welding the same seam, the decision step is simple. For a changing task, such as unloading a mixed truck, the decision step is the hard part, and that is where recent AI models are being used.{cite(21)}</p>
{nums}
<p class="cap wide">From the cited sources. Density is robots per 10,000 manufacturing employees.</p>
<h3 class="wide" id="s-types" data-nav="Types" style="margin-top:36px">The main kinds of robot</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
