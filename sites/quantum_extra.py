"""Added sections for the quantum site: live feed, race map, hype-versus-proof, supply chain, Ireland, jobs,
security clock, society and defence, reading levels, disclosures, research page and the next-frontier rail."""
from __future__ import annotations

# --- country tiles (col, row) on a rough world grid; role drives the colour -------------------------------------
TILES = {
    "CA": (1, 0, "major"), "US": (1, 1, "leader"), "IE": (3, 0, "emerging"), "GB": (4, 0, "major"), "NL": (5, 0, "major"),
    "DE": (6, 0, "major"), "FI": (7, 0, "major"), "FR": (4, 1, "major"), "CH": (5, 1, "major"), "IL": (7, 1, "major"),
    "KR": (10, 0, "emerging"), "CN": (9, 1, "leader"), "JP": (11, 1, "major"), "IN": (8, 2, "emerging"),
    "SG": (9, 2, "emerging"), "AU": (10, 3, "major"),
}
NAMES = {"CA": "Canada", "US": "United States", "IE": "Ireland", "GB": "United Kingdom", "NL": "Netherlands", "DE": "Germany",
         "FI": "Finland", "FR": "France", "CH": "Switzerland", "IL": "Israel", "KR": "South Korea", "CN": "China",
         "JP": "Japan", "IN": "India", "SG": "Singapore", "AU": "Australia"}
# Approximate and from public sources; marked as such on the page.
COUNTRY = {
    "US": {"co": "IBM, Google, Microsoft, IonQ, Rigetti, D-Wave (US and Canada), Quantum Computing Inc, PsiQuantum, Quantinuum (US and UK)",
           "gov": "National Quantum Initiative Act (2018). DARPA moved 11 companies, including IBM, IonQ and Quantinuum, to Stage B of its Quantum Benchmarking Initiative in November 2025",
           "ctl": "Export controls on advanced quantum computers and some components (2024)", "note": "Leads on company count, private capital and chip-making links."},
    "CN": {"co": "USTC (Zuchongzhi, Jiuzhang), Origin Quantum, Baidu, Tencent",
           "gov": "State-funded national lab at Hefei and long-term five-year plans; spending figures are not transparent",
           "ctl": "Its own controls on some critical materials; targeted by US export rules", "note": "Leads in satellite quantum communication; companies are mostly state-linked and not open to outside investors."},
    "GB": {"co": "Quantinuum (Cambridge), Oxford Ionics (IonQ agreed to buy it in 2025), Riverlane, Oxford Quantum Circuits, Universal Quantum",
           "gov": "National Quantum Strategy (2023) with 2.5 billion pounds over ten years, 2024 to 2034", "ctl": "National security investment screening", "note": "Strong university base and many spin-outs."},
    "DE": {"co": "IQM (German arm), planqc, Toptica (lasers)", "gov": "National quantum programme: one 2026 overview gives about 2 billion euros, other reports give 3 billion", "ctl": "EU dual-use export rules", "note": "Strong in lasers and industrial partners."},
    "FR": {"co": "Pasqal, Alice & Bob, Quandela", "gov": "National strategy of about 1.8 billion euros (2021)", "ctl": "EU dual-use export rules", "note": "Several well-funded neutral-atom and photonic start-ups."},
    "NL": {"co": "QuTech (Delft), Qblox, QuantWare", "gov": "Quantum Delta NL programme", "ctl": "EU dual-use export rules; chip-tool controls", "note": "Control electronics and chip foundry services."},
    "FI": {"co": "IQM, Bluefors (dilution fridges)", "gov": "VTT national programme", "ctl": "EU dual-use export rules", "note": "Bluefors is a main supplier of the cooling machines."},
    "CH": {"co": "Zurich Instruments, ETH Zurich spin-outs", "gov": "National quantum initiative", "ctl": "Follows EU and US controls", "note": "Precision electronics and research."},
    "IL": {"co": "Quantum Machines, Classiq, Quantum Source", "gov": "National quantum programme (2018 onward)", "ctl": "Export licensing for dual-use items", "note": "Software and control systems."},
    "CA": {"co": "D-Wave (Burnaby), Xanadu (Toronto), Photonic Inc", "gov": "National Quantum Strategy (2023)", "ctl": "Allied export controls", "note": "Home of the first commercial annealer."},
    "JP": {"co": "Fujitsu and RIKEN, NTT, Toshiba", "gov": "National quantum strategy and a large public research base", "ctl": "Allied export controls", "note": "Strong in superconducting circuits and components."},
    "KR": {"co": "Samsung and SK research groups, university labs", "gov": "National quantum strategy (2023)", "ctl": "Allied export controls", "note": "Chip-making strength could matter later."},
    "IN": {"co": "TIFR, IISc groups and start-ups", "gov": "National Quantum Mission (2023)", "ctl": "Developing", "note": "Large programme, early hardware."},
    "AU": {"co": "PsiQuantum (Brisbane site), Silicon Quantum Computing, Quantum Brilliance", "gov": "Large public funding for a PsiQuantum facility (2024)", "ctl": "Allied export controls", "note": "Silicon spin and photonic bets."},
    "SG": {"co": "Centre for Quantum Technologies, start-ups", "gov": "National Quantum Strategy", "ctl": "Strict re-export rules", "note": "Research hub and finance interest."},
    "IE": {"co": "Equal1 (Dublin, silicon spin chips), Tyndall National Institute (Cork), IBM Ireland research", "gov": "Quantum 2030, national quantum strategy (2023)", "ctl": "EU dual-use export rules",
           "note": "Small but real hardware and photonics expertise; strong data-centre sector."},
}


def tile_map(tiles=None, names=None) -> str:
    tiles = tiles or TILES
    names = names or NAMES
    s, g = 62, []
    for cc, (c, r, role) in tiles.items():
        x, y = 12 + c * (s + 6), 12 + r * (s + 6)
        g.append(f'<g class="tile {role}" data-cc="{cc}" tabindex="0" role="button" aria-label="{names[cc]}">'
                 f'<rect x="{x}" y="{y}" width="{s}" height="{s}"/><text x="{x + s / 2}" y="{y + s / 2 + 5}" text-anchor="middle" class="t-fg tl-cc">{cc}</text></g>')
    return (f'<svg viewBox="0 0 {12 + 12 * (s + 6)} {12 + 4 * (s + 6)}" class="tilemap" role="img" '
            f'aria-label="Tile map of countries active in quantum computing">{"".join(g)}</svg>')


def level(simple: str, general: str, expert: str) -> str:
    return (f'<span class="lv s">{simple}</span><span class="lv g">{general}</span><span class="lv e">{expert}</span>')


def key_idea(title, simple, general, expert) -> str:
    return f'<aside class="keyidea rv"><div class="eyebrow">Key idea</div><h3>{title}</h3><p>{level(simple, general, expert)}</p></aside>'


KEY = {
    "learn": key_idea("A quantum computer is a different kind of machine, not a faster one",
                      "It uses tiny things like atoms that can be in two states at once. For a few special puzzles that gives it a huge shortcut.",
                      "Qubits hold weighted blends of 0 and 1, and algorithms use interference to make correct answers likely. The gain exists only for specific problems.",
                      "Speed-ups come from structure: Shor gives a super-polynomial gain for factoring, Grover a quadratic one for unstructured search. Most workloads see none."),
    "simple": key_idea("Think of it as a specialist tool",
                       "Like a calculator for chemistry. You will never use it for email.",
                       "It will be rented through the cloud for narrow jobs such as molecule simulation, the way you rent a GPU today.",
                       "Expect hybrid workflows: classical pre- and post-processing around a quantum kernel, with error decoding on classical hardware in real time."),
    "change": key_idea("The first effect is on security, not on gadgets",
                       "Secret codes protecting your data could one day be opened. The fix is new codes, already designed.",
                       "Harvested encrypted data is a risk now. Migration to post-quantum encryption is the main practical task before useful machines arrive.",
                       "Plan around NIST FIPS 203, 204 and 205, crypto-agility, and the 2030 to 2035 deprecation windows in published roadmaps."),
    "companies": key_idea("Great technology and a great investment are different things",
                          "A company can be right about the science and still lose your money.",
                          "These firms spend more than they earn and sell shares to fund it. Milestones, cash runway and dilution decide outcomes.",
                          "Evaluate on cash burn against runway, share-count growth, backlog quality and technical milestones with independent verification."),
    "hurdles": key_idea("The gap is mostly about errors and engineering, not a missing idea",
                        "Qubits make mistakes constantly. Fixing them takes lots of extra qubits and very careful engineering.",
                        "Error correction works in principle and has been shown to scale; the open problems are overhead, wiring, cooling and speed.",
                        "Key numbers: physical error near 1e-3, target logical error near 1e-12, overhead of order 10^2 to 10^3 per logical qubit for surface-code style schemes."),
    "outlook": key_idea("A reasonable guess is steady progress, a shakeout, and no certainty",
                        "The science will probably keep improving. Many share prices may not.",
                        "Technology likely advances on a roughly 2029 to 2031 horizon; listed pure-plays priced in success, so a bumpy ride is the central case.",
                        "Scenarios here are priors with stated probabilities; the live layer tilts them with dated events under caps, and the ledger scores them."),
}

HYPE = [
    ("5", "Reproduced independently", "Result confirmed by another team or method", "Error rates falling with code size, shown on a second platform", "ok"),
    ("4", "Peer-reviewed, single group", "Published in a refereed journal by one team", "Google Quantum Echoes (2025), Bluvstein atom-array logical processor (2023)", "ok"),
    ("3", "Contested", "Published but disputed, or later matched by classical methods", "IBM utility paper (2023), Microsoft Majorana (2025), 2019 supremacy claim", "dis"),
    ("2", "Preprint or company blog", "Technical report, not yet refereed", "Many new qubit-count and fidelity announcements", "tgt"),
    ("1", "Press release or roadmap", "A target, not a result", "Fault-tolerant machine by 2029", "tgt"),
]

SHOVELS = [
    ("Dilution refrigerators", "Bluefors", "Finland", "Cooling to 10 millikelvin; few suppliers"),
    ("Dilution refrigerators", "Maybell, Oxford Instruments (until its 2025 sale of the unit), others", "US, UK", "Same job, different makers"),
    ("Control electronics", "Quantum Machines, Qblox, Zurich Instruments", "Israel, Netherlands, Switzerland", "Every qubit needs fast, precise signals"),
    ("Lasers and optics", "Toptica, Coherent", "Germany, US", "Needed for ions and neutral atoms"),
    ("Classical chips and decoding", "Nvidia", "US", "GPUs decode errors and run simulations"),
    ("Isotopes", "Helium-3 supply", "US, Russia (limited)", "Needed for the coldest stage, a real bottleneck"),
]

JOBS = [
    ("Qiskit", "IBM's free toolkit and course for learning quantum programming.", "https://www.ibm.com/quantum/qiskit"),
    ("Cirq", "Google's open-source library for writing circuits.", "https://quantumai.google/cirq"),
    ("PennyLane", "Open-source library that links quantum circuits to machine learning.", "https://pennylane.ai"),
    ("Quantum Country", "A free essay-style textbook with spaced-repetition memory prompts.", "https://quantum.country"),
]

NEXT_SITES = [
    ("Quantum", "quantum", "live now"), ("Crypto", "coin", "next"), ("Batteries", "cell", "planned"), ("AI", "mind", "planned"),
    ("Robotics", "bot", "planned"), ("Fission and small reactors", "atom", "planned"), ("Fusion", "fusion", "planned"),
    ("Drones", "drone", "planned"), ("Counter-drone and directed energy", "shield", "planned"), ("Graphene and nanotubes", "carbon", "planned"),
    ("Wave, tidal and new energy harvesters", "tide", "planned"), ("Gene editing and longevity", "gene", "planned"), ("Space", "orbit", "planned"), ("Semiconductors", "chip", "planned"),
]


def rail(active="quantum") -> str:
    cards = "".join(f'<a class="{"on" if k == active else ""}" href="#"><b>{n}</b><span>{k} &middot; {s}</span></a>' for n, k, s in NEXT_SITES)
    return (f'<section class="chapter" id="family"><header><div><h2>The Frontier series</h2><p class="sub">One site per emerging technology, '
            f'the same layout and the same rules. No adverts.</p></div></header><div class="fam">{cards}</div></section>')


def disclosures(as_of: str) -> str:
    return f'''<section class="chapter" id="disclosures"><header><div><h2>Disclosures and how to use this site</h2></div></header>
<div class="cols">
<div class="card"><h3>Information only</h3><p>This site is general information and education. It is not investment advice, a recommendation, an offer or a solicitation, and it takes no account of your circumstances. Speak to a licensed adviser before acting.</p></div>
<div class="card"><h3>Projections are scenarios</h3><p>Ranges come from stated assumptions and probabilities chosen by the author. They are not forecasts and carry no guarantee. Share prices can fall to zero.</p></div>
<div class="card"><h3>No conflicts</h3><p>Solas33 and the author hold no position in any company named, receive no payment from any of them, and carry no advertising. If that changes it will be stated here with the date.</p></div>
<div class="card"><h3>How it is made</h3><p>Drafted with AI assistance and generated by open Python code at github.com/SOLAS33/frontier. Every projection change is logged with its cause, and predictions are recorded in advance and scored afterwards.</p></div>
<div class="card"><h3>Corrections</h3><p>Errors are fixed and logged. Report one at github.com/SOLAS33/frontier/issues. Content was last reviewed on {as_of}.</p></div>
<div class="card"><h3>Sources and delays</h3><p>Prices are from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Company statements are labelled as targets until verified.</p></div>
</div></section>'''


def research() -> str:
    return '''<section class="chapter" id="research"><header><div><h2>For researchers, teachers and journalists</h2></div></header>
<div class="cols">
<div class="card"><h3>How to cite</h3><p>Solas33 Frontier, Quantum. Page version dated with the "last updated" stamp above. github.com/SOLAS33/frontier. Quote the page date, not just the year.</p></div>
<div class="card"><h3>Method</h3><p>Prices: weekly closes. Reactions: 5-day abnormal return against QQQ for filings, with case counts. Scenarios: lognormal mixtures with stated drift and volatility scaled to 75% of the last two years. All code and assumptions are public.</p></div>
<div class="card"><h3>Data</h3><p>The live layer is a public JSON file, <a href="live.json">live.json</a>, plus an <a href="feed.xml">RSS feed</a>. Fields: <code>tickers</code> (price, scenarios, quantiles), <code>events</code>, <code>changelog</code>, <code>reactions</code>, <code>scorecard</code>.</p></div>
<div class="card"><h3>Classroom</h3><p>Use your browser's Print for a clean one-page copy of any chapter. Set the reading level at the top to Simple for younger students or Expert for a graduate course.</p></div>
</div></section>'''


def defence() -> str:
    return f'''<h3 style="margin-top:36px">War, defence money and what you do not see</h3>
<div class="cols">
<div class="card rv"><h3>Governments are early customers</h3><p>Defence and intelligence agencies funded much of the first quantum work and still set priorities. Examples in the open record: the US DARPA Quantum Benchmarking Initiative, NSA guidance on post-quantum codes, and national programmes in China, the UK and the EU.</p></div>
<div class="card rv"><h3>Some progress will not be public</h3><p>Code-breaking, secure communications and quantum sensing for navigation without GPS are areas where results can be classified. The public record therefore lags the real state of the art by an unknown amount, and company claims can be shaped by contracts you cannot see.</p></div>
<div class="card rv"><h3>How to read the signals</h3><p>Watch government contract awards, export-control rules, university and lab hiring, and sudden changes in who may buy or sell certain parts. These are visible even when the results are not.</p></div>
<div class="card rv"><h3>Why a race lifts some shares</h3><p>When governments frame quantum as a race with a rival, funding and procurement follow, and domestic companies can benefit. It also invites export bans and sanctions that cut companies off from customers and parts. Both effects show up in the live feed as policy events.</p></div>
</div>
<div class="callout"><b>Related technologies coming in this series.</b> Drones, counter-drone systems, directed energy and high-power microwave weapons, and advanced materials such as graphene and carbon nanotubes all have large defence funding and the same secrecy problem. Each will get its own Frontier site.</div>'''
