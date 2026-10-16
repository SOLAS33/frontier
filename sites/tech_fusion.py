"""Technical depth for Frontier Fusion: numbers, routes, evidence and a short glossary. Same shape as tech_blocks.py."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

FUSION_REFS = [
    (10, "Lawrence Livermore National Laboratory. National Ignition Facility achieves fusion ignition.", "https://www.llnl.gov/article/49051/national-ignition-facility-achieves-fusion-ignition"),
    (11, "ITER Organization. The ITER schedule and cost baseline.", "https://www.iter.org/"),
    (12, "EUROfusion (2024). Final JET experiments deliver new energy record.", "https://euro-fusion.org/"),
    (13, "Commonwealth Fusion Systems. SPARC.", "https://cfs.energy/technology/sparc"),
]


def fusion_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Reaction used first", "Deuterium + tritium gives helium (3.5 MeV) and a neutron (14.1 MeV)", "17.6 MeV in all. A kilogram of the fuel releases roughly as much heat as 10,000 tonnes of coal"],
        ["Plasma temperature", "About 100 to 150 million degrees Celsius", "Ten times hotter than the centre of the Sun, because a power plant cannot squeeze fuel as hard as the Sun does"],
        ["Triple product", "About 3 x 10^21 keV s per cubic metre for ignition", "Density x temperature x confinement time. All three have to be high together"],
        ["Gain (Q)", "Fusion power out divided by heating power in", "Q = 1 is break-even in the plasma. A power plant needs a Q of about 10 or more once losses are counted"],
        ["Deuterium", "About 33 grams per cubic metre of seawater", "Effectively unlimited"],
        ["Tritium", "Half-life 12.3 years. A few tens of kilograms exist worldwide", "A plant has to breed its own from lithium inside its walls. Nobody has shown that at scale"],
        ["Neutron damage", "14 MeV neutrons strike the wall continuously", "Materials swell and turn radioactive. How long they last is an open engineering question"],
    ])
    routes = _table(["Approach", "How it holds the fuel", "Examples", "Status"], [
        ["Tokamak", "A doughnut of magnetic field, with a current driven through the plasma", "ITER, JT-60SA, EAST, KSTAR, WEST, SPARC", "Most research and most data. Steady operation is hard"],
        ["Stellarator", "Twisted magnets alone hold the plasma, so no plasma current is needed", "Wendelstein 7-X, Proxima Fusion, Type One Energy", "Steady in principle. Very hard to build the magnets"],
        ["Laser (inertial)", "Lasers or X-rays squeeze a fuel pellet for a billionth of a second", "NIF, Xcimer, Marvel Fusion, Focused Energy", "Gain above 1 at the target shown at NIF. A plant needs several shots a second"],
        ["Pulsed magnetic", "A current pulse squeezes or collides plasma", "Helion, Zap Energy, Pacific Fusion", "Smaller machines and faster iteration. Less data so far"],
        ["Beam-driven plasma ring", "A self-confined ring of plasma held by neutral beams", "TAE Technologies", "Aims at hydrogen-boron fuel, which makes few neutrons but needs far higher temperatures"],
        ["Magnetised target", "A liquid metal liner is imploded around the plasma", "General Fusion", "A smaller programme that has had funding difficulty"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Fusion in the lab", "Many devices, since the 1950s", _tag("ok"), "Neutron-producing fusion has been routine for decades"],
        ["Fusion power close to the heating power", "JET 1997, Q of about 0.67" + cite(12), _tag("ok"), "No magnetic device has yet reached Q above 1"],
        ["Fusion energy above the laser energy on the target", "NIF, December 2022 and later shots" + cite(10), _tag("ok"), "The first shot gave about 1.5 times the laser energy delivered. The lasers drew about a hundred times more from the wall"],
        ["Most fusion energy from one magnetic experiment", "JET, 69 megajoules over 5 seconds, 2023" + cite(12), _tag("ok"), "The machine has since been shut down"],
        ["Long-pulse records", "EAST 1,066 s and WEST 1,337 s, both in 2025", _tag("ok"), "At modest power. Long duration and high power have not yet been shown together"],
        ["20 tesla large high-temperature superconducting magnet", "Commonwealth Fusion Systems and MIT, 2021", _tag("ok"), "The reason compact tokamaks are plausible"],
        ["Q above 1 in a magnetic device", "SPARC, first plasma targeted for 2026 to 2027" + cite(13), _tag("tgt"), "A company target that has moved before"],
        ["Q of 10 in sustained burn", "ITER, deuterium-tritium operation from the late 2030s" + cite(11), _tag("tgt"), "The schedule was reset in 2024 at a higher cost"],
        ["Net electricity from fusion into a grid", "Helion, Commonwealth Fusion Systems and others, 2028 to the early 2030s", _tag("tgt"), "Company targets, some with named buyers. No plant has produced net power"],
    ])
    gl = _gloss([
        ("Plasma", "A gas hot enough that its atoms split into charged particles. Magnetic fields can hold it."),
        ("Q (gain)", "Fusion power divided by the power used to heat the plasma. It is not the plant's electrical gain."),
        ("Ignition", "A burn that heats itself from the helium nuclei it makes, so outside heating can stop."),
        ("Breeding blanket", "A lithium-bearing layer in the wall where neutrons make tritium."),
        ("HTS", "High-temperature superconductor. Wound into tape, it carries current with no loss and makes stronger magnets in a smaller space."),
        ("Divertor", "The part of a tokamak that takes the exhaust. It sees heat loads comparable to a rocket nozzle."),
        ("Wall-plug efficiency", "Energy out divided by electricity drawn from the grid. NIF is far below 1 on this measure."),
        ("Offtake", "An agreement to buy a plant's future power. It is a promise to buy and does not show the plant will exist."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Two light nuclei, usually deuterium and tritium, fuse into helium and a neutron and release energy. The nuclei repel one another, so the fuel has to be a plasma at about 100 million degrees, held away from the walls long enough that more energy comes out than went in.{cite(10)} The neutron carries most of the energy out. It is stopped in a lithium blanket, where it also makes the next tritium.{cite(11)}</p>
{nums}
<p class="cap wide">Rounded, from the cited sources. Q is quoted for the plasma, not for the whole plant.</p>
<h3 class="wide" id="s-routes" data-nav="Routes" style="margin-top:36px">The main routes to fusion</h3>
{routes}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
