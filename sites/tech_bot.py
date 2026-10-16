"""Technical depth for Frontier Bot: numbers, robot types, evidence and a short glossary. Same shape as tech_blocks.py."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

BOT_REFS = [
    (10, "International Organization for Standardization. ISO 10218: safety requirements for industrial robots.", "https://www.iso.org/standard/73933.html"),
    (11, "NVIDIA. Isaac GR00T: foundation models for humanoid robots.", "https://developer.nvidia.com/isaac/gr00t"),
    (12, "Boston Dynamics. Spot, Stretch and Atlas.", "https://bostondynamics.com/"),
    (13, "International Energy Agency. Global critical minerals outlook.", "https://www.iea.org/reports/global-critical-minerals-outlook-2025"),
]


def bot_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Industrial arm accuracy", "Repeats a position to within about 0.02 to 0.1 mm", "Far better than a human hand, but only for the same task in the same place"],
        ["Collaborative robot payload", "About 3 to 30 kg", "Built to work next to people, so force and speed are limited" + cite(10)],
        ["Human hand", "27 degrees of freedom, and a sense of touch across the skin", "The best robot hands have about 20 joints and much less touch. Hands are still the hardest part"],
        ["Humanoid size", "About 1.5 to 1.8 m and 50 to 90 kg", "Battery life is typically two to four hours of mixed work"],
        ["Actuator cost", "Often a third or more of a robot's cost", "Gearboxes, motors and sensors. They rely on rare-earth magnets, mostly from China" + cite(13)],
        ["Compute", "Onboard chips of hundreds to over a thousand trillion operations a second", "Enough to run vision and language models on the robot itself" + cite(11)],
        ["Training data", "Thousands of hours of human demonstration, plus simulation", "Language has trillions of words online. Robot movement data does not exist at that scale"],
    ])
    kinds = _table(["Type", "What it does", "Examples", "Status"], [
        ["Industrial arm", "Welds, paints, lifts and places in a fenced cell", "FANUC, ABB, KUKA, Yaskawa", "Mature. About half a million installed a year worldwide"],
        ["Collaborative robot", "A lighter arm that works beside people without a cage", "Universal Robots (Teradyne), Doosan, FANUC CRX", "Established, but a small share of arm sales"],
        ["Warehouse mobile robot", "Moves shelves, totes and pallets", "Amazon, Symbotic, Locus, Ocado", "Large scale. Amazon alone runs about a million robots"],
        ["Surgical robot", "A surgeon steers instruments through small cuts", "Intuitive da Vinci, Medtronic Hugo, CMR Surgical", "Mature at the leader, with new entrants"],
        ["Delivery and sidewalk robot", "Carries food and parcels short distances", "Serve Robotics, Starship", "Commercial in some cities, small revenue"],
        ["Legged and mobile manipulator", "Walks or rolls and picks things up", "Boston Dynamics Spot and Stretch" + cite(12), "Selling in small numbers to industry"],
        ["Humanoid", "Walks on two legs and uses tools made for people", "Tesla Optimus, Figure, Agility Digit, Apptronik, Unitree, UBTech", "Pilots in factories and warehouses. Not yet proven at scale"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["First industrial robot at work", "Unimate at a General Motors plant, 1961", _tag("ok"), "Die casting and welding, in a cage"],
        ["Robot-assisted surgery approved", "da Vinci, US FDA 2000", _tag("ok"), "Now used in millions of operations"],
        ["Robots in a warehouse in the hundreds of thousands", "Amazon, 2012 on", _tag("ok"), "About a million by mid 2025"],
        ["Robots from a lab sold commercially", "Boston Dynamics Spot, 2020", _tag("ok"), "In the thousands of units"],
        ["Robot arms that learn new tasks from demonstrations", "Several labs and start-ups, 2023 on", _tag("ok"), "Works on narrow tasks. Reliability varies"],
        ["Humanoid robots in paid factory pilots", "Agility, Figure, Apptronik and others, 2024 on", _tag("dis"), "Pilots with named customers. Volume and uptime figures are not public"],
        ["A humanoid doing varied work for months without help", "No one yet", _tag("tgt"), "The test that matters for the business case"],
        ["A home robot that does chores unattended", "Several firms, announced for the late 2020s", _tag("tgt"), "Company targets"],
    ])
    gl = _gloss([
        ("Actuator", "The motor and gearbox that moves a joint."),
        ("Degrees of freedom", "The number of independent ways a robot can move. A human arm has seven."),
        ("Cobot", "A collaborative robot, built to work beside people at limited force and speed."),
        ("Teleoperation", "A person steers the robot, often to produce training data."),
        ("Imitation learning", "The robot learns from recordings of a person doing the task."),
        ("Sim-to-real", "Training in a physics simulation, then moving the result to a real robot."),
        ("VLA model", "Vision-language-action model: one network that takes camera images and an instruction and outputs motions."),
        ("Payload", "The weight a robot can carry at full reach."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A robot is a loop. Sensors such as cameras, force sensors and joint encoders measure the world. Software decides what to do next. Motors and gearboxes move the joints. The loop runs hundreds of times a second. For a fixed task, such as welding the same seam, the decision step is simple and the robot is superb. For a changing task, such as unloading a mixed truck, the decision step is the hard part, and that is where recent AI models are being used.{cite(11)}</p>
{nums}
<p class="cap wide">Rounded, from public sources and manufacturer data sheets. Ranges vary by model.</p>
<h3 class="wide" id="s-types" data-nav="Types" style="margin-top:36px">The main kinds of robot</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
