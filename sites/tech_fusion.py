"""Technical depth for Frontier Fusion: numbers, routes, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

FUSION_REFS = [
    (10, "US Department of Energy (2022). DOE National Laboratory makes history by achieving fusion ignition.", "https://www.energy.gov/articles/doe-national-laboratory-makes-history-achieving-fusion-ignition"),
    (11, "Lawrence Livermore National Laboratory. National Ignition Facility: frequently asked questions.", "https://lmf.llnl.gov/about/faqs"),
    (12, "Lawrence Livermore National Laboratory (2025). LLNL experts foster national fusion energy ecosystem at IFE-STAR conference.", "https://lmf.llnl.gov/news/llnl-experts-foster-national-fusion-energy-ecosystem-ife-star-conference"),
    (13, "EUROfusion. JET's final fusion campaigns set a new energy record.", "https://euro-fusion.org/eurofusion-news/jets-final-fusion-campaigns-set-a-new-energy-record-and-hand-iter-a-legacy-of-irreplaceable-data/"),
    (14, "ITER Organization. The DT shots heard around the world (JET 1997 and TFTR).", "https://iter.org/node/20780"),
    (15, "Commonwealth Fusion Systems. SPARC.", "https://cfs.energy/technology/sparc"),
    (16, "Commonwealth Fusion Systems (2021). World's strongest magnet, a viable path to commercial fusion power.", "https://cfs.energy/news-and-media/cfs-commercial-fusion-power-with-hts-magnet/"),
    (17, "Wendelstein 7-X sets world record for long plasma triple product. EUROfusion (2025).", "https://euro-fusion.org/eurofusion-news/wendelstein-7-x-sets-world-record-for-long-plasma-triple-product/"),
    (18, "Physics World (2025). China's EAST tokamak smashes fusion confinement record.", "https://www.physicsworld.com/a/chinas-experimental-advanced-superconducting-tokamak-smashes-fusion-confinement-record/"),
    (19, "ITER Organization. Advantages of fusion.", "https://www.iter.org/fusion-energy/advantages-fusion"),
    (20, "Wikipedia. Lawson criterion (D-T triple product values).", "https://en.wikipedia.org/wiki/Lawson_criterion"),
    (21, "Wikipedia. Nuclear fusion (D-T reaction energy).", "https://en.wikipedia.org/wiki/Nuclear_fusion"),
    (22, "Canadian Nuclear Laboratories (2025). Tritium supply for fusion. IAEA technical meeting contribution.", "https://conferences.iaea.org/event/385/contributions/35508"),
    (23, "Helion. Technology.", "https://www.helionenergy.com/technology/"),
    (24, "POWER Magazine. Pacific Fusion touts funding, technical achievements on way to fusion power.", "https://powermag.com/pacific-fusion-touts-funding-technical-achievements-on-way-to-fusion-power/"),
    (25, "American Nuclear Society. Focused Energy and Xcimer Energy: DOE's inertial fusion pilot picks.", "https://ans.org/news/tag-excimer%20lasers"),
]


def fusion_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Reaction used first", "Deuterium + tritium gives helium (3.5 MeV) and a neutron (14.1 MeV)" + cite(21), "17.6 MeV in all. Most of it leaves in the neutron"],
        ["Plasma temperature", "About 150 million degrees Celsius" + cite(19), "About ten times the temperature at the Sun's core"],
        ["Triple product", "About 3 x 10^21 keV s per cubic metre for deuterium-tritium, near 14 keV" + cite(20), "Density x temperature x confinement time. All three have to be high together"],
        ["Gain (Q)", "Fusion power out divided by heating power in", "Q = 1 is break-even in the plasma. A power plant needs much more once its own losses are counted"],
        ["Target gain at NIF", "3.15 MJ out from 2.05 MJ on the target (December 2022)" + cite(10) + cite(11), "The laser facility itself uses about 100 times more energy than the laser light it delivers" + cite(11)],
        ["Tritium", "Half-life about 12.3 years. Stock estimated at 20 to 30 kg worldwide", "CANDU heavy-water reactors in Canada and South Korea are the main source" + cite(22) + ". A plant has to breed its own from lithium. Estimates differ by source"],
        ["Neutron damage", "14 MeV neutrons strike the wall continuously", "Wall materials are activated. ITER expects them to be reusable or recyclable within about 100 years" + cite(19)],
    ])
    routes = _table(["Approach", "How it holds the fuel", "Examples", "Status"], [
        ["Tokamak", "A doughnut of magnetic field, with a current driven through the plasma", "ITER, JT-60SA, EAST, WEST, SPARC (Commonwealth Fusion Systems), Tokamak Energy", "Most research and most data"],
        ["Stellarator", "Twisted magnets alone hold the plasma, so no plasma current is needed", "Wendelstein 7-X, Proxima Fusion, Type One Energy", "W7-X holds the long-pulse triple-product record" + cite(17)],
        ["Laser (inertial)", "192 laser beams heat a fuel capsule so fast that it fuses before it flies apart" + cite(11), "NIF. Xcimer and Focused Energy were chosen for a US Department of Energy programme in 2023" + cite(25), "Target gain above 1 shown at NIF only"],
        ["Pulsed inertial (pulser-driven)", "An electric pulse compresses a small target, with no lasers or superconducting magnets", "Pacific Fusion, working with Sandia National Laboratories" + cite(24), "Company reports. Less public data"],
        ["Pulsed field-reversed configuration", "Two plasma rings are fired together and compressed. The expanding plasma pushes back on the magnetic field and induces electric current", "Helion", "Helion describes its Polaris machine as demonstrating electricity from fusion. Company claim" + cite(23)],
        ["Z-pinch", "A strong current squeezes the plasma", "Zap Energy", "Company reports"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Most fusion power from a magnetic device", "JET, 16 MW in 1997, with Q of about 0.65" + cite(14), _tag("ok"), "The 16 MW peak still stands as a record. Q has never reached 1 in a magnetic machine"],
        ["Fusion energy above the laser energy on the target", "NIF, 5 December 2022: 3.15 MJ out, 2.05 MJ in" + cite(10), _tag("ok"), "First laboratory ignition"],
        ["Highest target gain so far", "NIF, April 2025: 8.6 MJ out, 2.08 MJ in, gain above 4" + cite(12), _tag("ok"), "The facility as a whole still draws about 100 times the laser energy" + cite(11)],
        ["Most fusion energy from one experiment (magnetic)", "JET, 69 MJ over about 5 seconds, 2023" + cite(13), _tag("ok"), "JET entered decommissioning in December 2023"],
        ["Long-pulse records", "EAST 1,066 s high-confinement plasma (January 2025)" + cite(18) + ", WEST over 1,300 s (February 2025)", _tag("ok"), "At modest power. Long duration with high power has not been shown together"],
        ["Best triple product for pulses over 40 seconds", "Wendelstein 7-X, 43 seconds, 22 May 2025" + cite(17), _tag("ok"), "Tokamaks hold the highest values over a few seconds"],
        ["20 tesla large high-temperature superconducting magnet", "Commonwealth Fusion Systems and MIT, September 2021" + cite(16), _tag("ok"), "The reason compact tokamaks are plausible"],
        ["Q above 1 in a magnetic device", "SPARC, targeted for 2027 by its builder" + cite(15), _tag("tgt"), "Company target. Sources differ on whether first plasma comes before or in 2027"],
        ["Net electricity from fusion into a grid", "Helion (Orion plant, with a Microsoft agreement for 2028) and Commonwealth Fusion Systems (ARC, early 2030s)", _tag("tgt"), "Company targets. No plant has produced net power"],
    ])
    gl = _gloss([
        ("Plasma", "A gas hot enough that its atoms split into charged particles. Magnetic fields can hold it."),
        ("Q (gain)", "Fusion power divided by the power used to heat the plasma. It is not the plant's electrical gain."),
        ("Target gain", "Fusion energy out divided by laser energy delivered to the target. It leaves out the energy the laser facility uses."),
        ("Ignition", "Fusion that releases at least as much energy as was delivered to the target to start it." + cite(11)),
        ("Breeding blanket", "A lithium-bearing layer in the wall where neutrons make tritium."),
        ("HTS", "High-temperature superconductor. Wound into tape, it carries current with no loss and makes stronger magnets in a smaller space."),
        ("Triple product", "Density x temperature x confinement time. The figure of merit for how close a plasma is to ignition."),
        ("Offtake", "An agreement to buy a plant's future power. It is a promise to buy and does not show the plant will exist."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Two light nuclei, usually deuterium and tritium, fuse into helium and a neutron and release energy.{cite(21)} The nuclei repel one another, so the fuel has to be a plasma at about 150 million degrees, held away from the walls long enough that more energy comes out than went in.{cite(19)} The neutron carries most of the energy out. It is stopped in a lithium blanket, where it also makes the next tritium.</p>
{nums}
<p class="cap wide">Rounded, from the cited sources. Q is quoted for the plasma, not for the whole plant. Estimates of the tritium stock vary between sources, from about 20 to about 30 kg.</p>
<h3 class="wide" id="s-routes" data-nav="Routes" style="margin-top:36px">The main routes to fusion</h3>
{routes}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
