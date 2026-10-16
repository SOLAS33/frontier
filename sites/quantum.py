"""Frontier Quantum: copy, data and assembly. Voice rules are in docs/VOICE.md and are checked by tools/voice_lint.py."""
from __future__ import annotations

import json

from frontier import art, charts, prices
from frontier.components import band, chapter, fig, key_idea, note, photo, series_list, watch_promo
from frontier.scenarios import Scenario, simulate
from sites import quantum_extra as X

TITLE = "Frontier Quantum"

# what the live backend needs to know about this site
LIVE = {"cik": {"IONQ": 1824920, "RGTI": 1838359, "QBTS": 1907982, "QUBT": 1758009},
        "aliases": {"IONQ": ["ionq"], "RGTI": ["rigetti"], "QBTS": ["d-wave", "dwave", "qbts"], "QUBT": ["quantum computing inc", "qubt"]},
        "arxiv_terms": ["IonQ", "Rigetti", "D-Wave", "Quantinuum", "Google Quantum AI", "IBM Quantum"], "arxiv_cat": "quant-ph"}
AS_OF = "16 October 2026"

REFS = [
    (1, "Feynman, R. (1982). Simulating physics with computers. Int. J. Theor. Phys.", "https://doi.org/10.1007/BF02650179"),
    (2, "Shor, P. (1994). Algorithms for quantum computation: discrete logarithms and factoring.", "https://arxiv.org/abs/quant-ph/9508027"),
    (3, "Grover, L. (1996). A fast quantum mechanical algorithm for database search.", "https://arxiv.org/abs/quant-ph/9605043"),
    (4, "Preskill, J. (2018). Quantum computing in the NISQ era and beyond. Quantum.", "https://arxiv.org/abs/1801.00862"),
    (5, "Fowler et al. (2012). Surface codes: towards practical large-scale quantum computation.", "https://arxiv.org/abs/1208.0928"),
    (6, "Arute et al. (2019). Quantum supremacy using a programmable superconducting processor. Nature.", "https://doi.org/10.1038/s41586-019-1666-5"),
    (7, "Kim et al. (2023). Evidence for the utility of quantum computing before fault tolerance. Nature (IBM).", "https://doi.org/10.1038/s41586-023-06096-3"),
    (8, "Bluvstein et al. (2023). Logical quantum processor based on reconfigurable atom arrays. Nature (Harvard, QuEra).", "https://arxiv.org/abs/2312.03982"),
    (9, "Google Quantum AI (2024). Quantum error correction below the surface code threshold. Nature.", "https://arxiv.org/abs/2408.13687"),
    (10, "Bravyi et al. (2024). High-threshold and low-overhead fault-tolerant quantum memory. Nature (IBM).", "https://arxiv.org/abs/2308.07915"),
    (11, "Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits.", "https://arxiv.org/abs/2505.15917"),
    (12, "Gidney and Ekera (2019). How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits.", "https://arxiv.org/abs/1905.09749"),
    (13, "NIST. Post-quantum cryptography standards (FIPS 203, 204, 205).", "https://csrc.nist.gov/projects/post-quantum-cryptography"),
    (14, "Google Quantum AI (2025). Constructive interference at the edge of quantum ergodic dynamics (Quantum Echoes).", "https://arxiv.org/abs/2506.10191"),
    (15, "Microsoft Azure Quantum (2025). Interferometric single-shot parity measurement in InAs-Al hybrid devices. Nature.", "https://doi.org/10.1038/s41586-024-08445-2"),
    (16, "Lee et al. (2021). Even more efficient quantum computations of chemistry through tensor hypercontraction. PRX Quantum.", "https://arxiv.org/abs/2011.03494"),
    (17, "Reiher et al. (2017). Elucidating reaction mechanisms on quantum computers. PNAS.", "https://arxiv.org/abs/1605.03590"),
    (18, "Google Quantum AI (2019). Supplementary information for the supremacy experiment, including power figures.", "https://arxiv.org/abs/1910.11333"),
    (19, "IBM Quantum. Roadmap and technology (Starling, Blue Jay).", "https://www.ibm.com/quantum/technology"),
    (20, "Quantinuum (2024). Accelerated roadmap to universal fault-tolerant quantum computing by 2030.", "https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030"),
    (21, "Qiskit, IBM's free open-source toolkit for learning and running quantum programs.", "https://www.ibm.com/quantum/qiskit"),
    (22, "Quantum Zeitgeist (2026). Quantinuum lists on Nasdaq at $60, 20x oversubscribed.", "https://quantumzeitgeist.com/quantinuum-lists-on-nasdaq-at-60-20x-oversubscribed/"),
    (23, "Quantinuum Inc. Registration statement on Form S-1/A (Helios: 98 physical qubits, 48 logical qubits; roadmap to Sol and Apollo).", "https://www.sec.gov/Archives/edgar/data/0002110105/000162828026037917/quantinuum-sx1a.htm"),
    (24, "D-Wave (2022). Completed transaction with DPCM Capital and began trading on the NYSE on 8 August 2022.", "https://ir.dwavesys.com/news/news-details/2022/D-Wave-Reports-Second-Quarter-and-First-Half-2022-Results-and-Provides-Business-Update/default.aspx"),
    (25, "Data Center Dynamics (2022). Rigetti SPAC deal closes, company debuts on Nasdaq.", "https://datacenterdynamics.com/en/news/rigetti-spac-deal-closes-quantum-computing-company-debuts-on-nasdaq"),
    (26, "Physics World (2025). Clarke, Devoret and Martinis win the 2025 Nobel Prize for Physics.", "https://physicsworld.com/a/john-clarke-michel-devoret-and-john-martinis-win-the-2025-nobel-prize-for-physics/"),
    (27, "HPCwire (2025). DARPA selects 11 participants for Quantum Benchmarking Initiative Stage B.", "https://www.hpcwire.com/2025/11/07/darpa-selects-11-participants-for-quantum-benchmarking-initiative-stage-b/"),
    (28, "Quantum Zeitgeist. A capital markets timeline of quantum computing (IonQ listing, October 2021).", "https://quantumzeitgeist.com/capital-markets-timeline-of-quantum-computing/"),
]
RTITLE = {n: t for n, t, _ in REFS}


def cite(*ids):
    return "".join(f'<sup><a href="#r{i}" title="{RTITLE[i]}">[{i}]</a></sup>' for i in ids)


def fmt_p(v):
    return f"${v:,.2f}" if v < 100 else f"${v:,.0f}"


# Scenario odds are the editors' judgement. They are the starting point; the live layer tilts them with dated news.
SCEN = {
    "IONQ": [Scenario("bear", "Milestones slip and more shares are sold", 0.40, -0.45, 0.75),
             Scenario("base", "Steady progress, slow revenue", 0.35, 0.10, 0.75),
             Scenario("bull", "Error-correction targets are met and revenue ramps", 0.25, 0.55, 0.75)],
    "RGTI": [Scenario("bear", "Rivals pull ahead and funding tightens", 0.45, -0.50, 0.75),
             Scenario("base", "Keeps pace on accuracy", 0.35, 0.00, 0.75),
             Scenario("bull", "A breakthrough or a buyer arrives", 0.20, 0.60, 0.75)],
    "QBTS": [Scenario("bear", "Demand for annealing stalls", 0.35, -0.40, 0.75),
             Scenario("base", "Revenue grows, gate-model stays early", 0.40, 0.05, 0.75),
             Scenario("bull", "A gate-model prototype lands and sales ramp", 0.25, 0.50, 0.75)],
    "QUBT": [Scenario("bear", "Stays in research, shares keep getting sold", 0.50, -0.55, 0.75),
             Scenario("base", "Small product revenue", 0.33, 0.00, 0.75),
             Scenario("bull", "Photonic chips find real buyers", 0.17, 0.60, 0.75)],
}

COMPANIES = [
    {"t": "IONQ", "name": "IonQ", "kind": "Trapped ions",
     "rivals": "Quantinuum (listed on Nasdaq in June 2026), QuEra and Atom Computing (neutral atoms), IBM and Google (circuits)",
     "profit": "Show hundreds of error-corrected qubits on its own hardware. Turn government and cloud contracts into repeat revenue. Stop selling new shares to pay the bills.",
     "watch": "Gate accuracy, logical-qubit results, quarterly revenue against cash burn, the share count, whether the acquisitions fit together.",
     "rank": "A strong second tier. Its ions are among the most accurate qubits built. Scaling them up is still unproven.",
     "verdict": "Most likely of the four to matter in 2029"},
    {"t": "RGTI", "name": "Rigetti", "kind": "Superconducting circuits",
     "rivals": "IBM and Google (far bigger budgets), AWS, Alice &amp; Bob",
     "profit": "Hold high two-qubit accuracy as chips grow past a few hundred qubits, and find customers who are not mainly grant-givers.",
     "watch": "Two-qubit accuracy at scale, multi-chip roadmap dates, revenue mix, cash runway.",
     "rank": "Third tier on technology. A low share price is not the same as a low price for the progress.",
     "verdict": "Highest risk of being overtaken or bought"},
    {"t": "QBTS", "name": "D-Wave", "kind": "Quantum annealing, plus a gate-model effort",
     "rivals": "Classical optimisation software (Gurobi, quantum-inspired solvers), IBM, IonQ",
     "profit": "Prove customers pay again and again for optimisation that beats classical solvers. Show a working gate-model chip so growth is not capped by annealing.",
     "watch": "Revenue growth, renewals, independent benchmarks against classical solvers, gate-model results.",
     "rank": "Leads on sales today, because an annealer does something useful now, for a narrow set of problems.",
     "verdict": "Best near-term revenue, narrowest technology"},
    {"t": "QUBT", "name": "Quantum Computing Inc", "kind": "Photonic chips",
     "rivals": "PsiQuantum and Xanadu (photonic computers), photonic chip foundries",
     "profit": "Move from prototypes and small orders to a product that customers reorder, and show its chips matter to quantum computing and not only to sensing.",
     "watch": "Revenue and margin, named repeat customers, peer-reviewed results, share sales.",
     "rank": "The earliest stage of the four. Little independently checked technical progress so far.",
     "verdict": "Most speculative of the four"},
]

LADDER = [("Lab result", "Qubit made|and measured"), ("Beats classical|on a test", "Advantage on a|useless task"),
          ("Errors fall|as code grows", "Shown by Google,|Dec 2024"), ("Dozens of|logical qubits", "Shown in small|experiments"),
          ("Hundreds,|long programs", "Targets 2028 to|2029"), ("Paid, useful|advantage", "Chemistry or|materials first"),
          ("Repeat revenue|and profit", "Needs all of|the above")]

KEY = {
    "learn": key_idea("A different kind of machine, not a faster one",
                      "A quantum computer stores information in things like atoms, ions and tiny superconducting circuits, which can sit in two states "
                      "at once. An algorithm arranges those states so the wrong answers cancel and the right one survives. That gives a huge shortcut "
                      "on a short list of problems, mostly simulating molecules and breaking certain codes. For almost everything else it is slower, "
                      "and costs far more, than the laptop you already own."),
    "simple": key_idea("A specialist tool",
                       "Think of a calculator for chemistry that lives in a data centre. You will rent time on one through the cloud for narrow jobs, "
                       "the way you rent a graphics card today. Ordinary computers will go on running your phone, your email and your video. "
                       "The quantum machine sits beside them and takes the hard problems."),
    "change": key_idea("Security first, gadgets much later",
                       "The first thing quantum computers disturb is encryption. Criminals and governments can already copy encrypted data and wait "
                       "for a machine that can open it. New codes exist and are being rolled out through software updates. After that the gains come "
                       "in chemistry and materials, and reach most people years later as cheaper fertiliser, better batteries and new drugs."),
    "companies": key_idea("Good science and a good investment are different things",
                          "A company can be right about the physics and still lose your money. These firms spend more than they earn and pay for it by "
                          "selling new shares, so each existing share owns a smaller slice. Milestones, cash runway and dilution decide how the story "
                          "ends, and the share price usually moves long before the science does."),
    "hurdles": key_idea("The gap is errors and engineering, not a missing idea",
                        "Qubits make mistakes all the time, roughly once in every thousand steps. Useful programs need about one mistake in a trillion. "
                        "Closing that gap means bundling hundreds of physical qubits into each reliable one, then wiring, cooling and controlling "
                        "millions of them. The ideas exist. The engineering is what is unfinished."),
    "outlook": key_idea("Steady progress, a shakeout, and no guarantees",
                        "We think the science keeps improving and a first useful machine arrives around 2029 to 2031, probably a year or two late. "
                        "The listed pure-plays were priced in 2024 and 2025 as if that were already done. So the likely path is real progress for "
                        "the field and a rough ride for several of the share prices."),
}


def build():
    px = prices.load()
    stat = {t: prices.stats(px[t]) for t in px}
    runs = {t: prices.best_run(px[t]) for t in ("IONQ", "RGTI", "QBTS", "QUBT", "NVDA", "AAPL", "BTC-USD")}
    sims = {t: simulate(px[t]["c"][-1], prices.annual_vol(px[t]), sc, years=3) for t, sc in SCEN.items()}

    order = ["IONQ", "RGTI", "QBTS", "QUBT", "IBM", "GOOGL", "MSFT", "NVDA", "HON"]
    names = {t: px[t]["name"] for t in order}
    all_t = order + ["AAPL", "BTC-USD"]
    series_js = {t: {"d": px[t]["d"], "c": [round(v, 3) for v in px[t]["c"]]} for t in all_t}
    scen_js = {}
    for t in SCEN:
        vol = prices.annual_vol(px[t])
        scen_js[t] = {"name": px[t]["name"], "price": px[t]["c"][-1], "tilt_pts": 0,
                      "hist": {"d": px[t]["d"][-104:], "c": [round(v, 3) for v in px[t]["c"][-104:]]},
                      "scen": [{"k": s.key, "label": s.label, "p": s.probability, "drift": s.drift, "sigma": round(vol * s.vol_mult, 4)} for s in SCEN[t]]}
    tm_assets = [["IONQ", "IonQ"], ["RGTI", "Rigetti"], ["QBTS", "D-Wave"], ["QUBT", "Quantum Computing Inc"], ["NVDA", "Nvidia"],
                 ["AAPL", "Apple"], ["BTC-USD", "Bitcoin"], ["IBM", "IBM"], ["GOOGL", "Alphabet (Google)"], ["MSFT", "Microsoft"]]
    tm_default = {"AAPL": "1997-12-22", "BTC-USD": "2016-01-25", "NVDA": "2022-10-10", "IONQ": px["IONQ"]["d"][0],
                  "RGTI": px["RGTI"]["d"][0], "QBTS": px["QBTS"]["d"][0], "QUBT": "2024-06-24"}
    data_js = (f"window.PRICES={json.dumps(series_js, separators=(',', ':'))};"
               f"window.PRICE_ORDER={json.dumps(order)};window.PRICE_NAMES={json.dumps(names)};window.PRICE_DEFAULT={json.dumps(order[:4])};"
               f"window.SCEN={json.dumps(scen_js, separators=(',', ':'))};"
               f"window.TM_ASSETS={json.dumps(tm_assets)};window.TM_DEFAULT={json.dumps(tm_default)};"
               f"window.COUNTRY={json.dumps(X.COUNTRY)};window.COUNTRY_NAMES={json.dumps(X.NAMES)};")

    def basket(members):
        idx = {t: dict(zip(px[t]["d"], px[t]["c"])) for t in members}
        start = max(px[t]["d"][0] for t in members)
        dates = [d for d in px[members[0]]["d"] if d >= start and all(d in idx[t] for t in members)]
        lvl, out = 100.0, []
        for i, d in enumerate(dates):
            if i:
                lvl *= 1 + sum(idx[t][d] / idx[t][dates[i - 1]] - 1 for t in members) / len(members)
            out.append(lvl)
        return dates, out
    pd_d, pd_v = basket(["IONQ", "RGTI", "QBTS", "QUBT"])
    bg_d, bg_v = basket(["IBM", "GOOGL", "MSFT", "HON"])
    bg = [(d, v) for d, v in zip(bg_d, bg_v) if d >= pd_d[0]]
    idx_svg = charts.index_chart([("Pure-plays", pd_d, pd_v, "var(--amber)"),
                                  ("Large groups", [d for d, _ in bg], [v / bg[0][1] * 100 for _, v in bg], "var(--teal)")])

    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult_items = [
        ("Apple, 1997 to 1999", f"from {runs['AAPL']['from']}", runs["AAPL"]["multiple"], "ref"),
        ("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
        ("Bitcoin, 2016 to 2017", f"from {runs['BTC-USD']['from']}", runs["BTC-USD"]["multiple"], "ref"),
        ("IonQ", f"from {runs['IONQ']['from']}", runs["IONQ"]["multiple"], "quantum"),
        ("Quantum Computing Inc", f"from {runs['QUBT']['from']}", runs["QUBT"]["multiple"], "quantum"),
        ("Rigetti", f"from {runs['RGTI']['from']}", runs["RGTI"]["multiple"], "quantum"),
        ("D-Wave", f"from {runs['QBTS']['from']}", runs["QBTS"]["multiple"], "quantum"),
    ]

    def stat_cell(val, label, pre="", suf=""):
        return (f'<div class="stat"><b data-count="{val}" data-pre="{pre}" data-suf="{suf}">{pre}{val:,.0f}{suf}</b><span>{label}</span></div>')

    # ---------------------------------------------------------------- hero
    hero = f'''<header class="fx-hero" id="top">
<div class="fx-hero-img"><img src="img/strontium-clock.jpg" alt="" decoding="async"></div>{art.hero_interference()}
<div class="fx-hero-in"><div class="fx-kicker">Frontier / Quantum</div>
<h1>What quantum computers <em>can</em> do now</h1>
<p class="lead">Some of quantum computing works. Some of it is a press release. Here is which is which, who is paid for each, and how much of it is already in the share price.</p>
<div class="fx-stats">
{stat_cell(48, "logical qubits Quantinuum reports on its Helios machine, a company figure")}
{stat_cell(1, "million noisy qubits to break RSA-2048, on the 2025 estimate", "about ", "m")}
{stat_cell(runs["RGTI"]["multiple"], "times Rigetti rose from low to high in one year", "", "x")}
{stat_cell(26, "kilowatts for a whole machine, the draw of 50 to 100 homes", "", " kW")}
</div></div></header>
<div class="fx-ticker" aria-label="Live prices and announcements"><div class="fx-ticker-track" id="fx-ticker-track"><span>Prices and announcements load here.</span></div></div>'''

    notice = ('<div class="callout r wide" style="margin-top:70px"><b>Information only.</b> We explain the technology and show how its '
              'companies and their shares have behaved. We do not recommend anything. Projections are scenarios, not forecasts, and money '
              'put into shares like these can be lost in full. The disclosures are at the foot of the page.</div>')

    # ---------------------------------------------------------------- 1 learn
    ch1 = chapter("learn", 1, "How it works, and where it breaks",
                  "The idea, the hardware, the history and the evidence, with the papers behind each claim.", f'''
<p>A normal computer stores bits. Each one is 0 or 1. A quantum computer stores qubits, which can hold a weighted blend of 0 and 1 until somebody measures them. Richard Feynman suggested in 1981 that simulating nature would need a machine built from quantum parts.{cite(1)} He was right about the problem. It took forty years to get anywhere near a machine.</p>
{note("Why it matters", "<p>Nature is quantum. Molecules, catalysts and batteries are all quantum systems, and classical computers choke on them. That is the commercial case.</p>")}
<p>Three effects do the work. <b>Superposition</b> lets a qubit hold both outcomes. <b>Entanglement</b> ties qubits together so that measuring one fixes the other. <b>Interference</b> is the trick: an algorithm arranges things so the wrong answers cancel out and the right one is left standing. Shor's 1994 factoring algorithm{cite(2)} and Grover's 1996 search{cite(3)} are built from these three.</p>
{note("Common mistake", "<p>A quantum computer does not try every answer at once and pick the best. If it did, you would still get one random answer when you looked. The skill is in the cancellation.</p>")}
<figure class="fig wide"><div class="cols" style="align-items:center"><div>{art.bloch()}</div><div><h3>A qubit as a sphere</h3>
<p>The arrow can point anywhere on the sphere. North is 0, south is 1, and everything between is a blend. Measuring snaps the arrow to a pole, with odds set by how close it was.</p></div></div>
<figcaption><b>Fig 1.</b> The standard picture of one qubit.</figcaption></figure>
<h3 class="wide" id="s-errors" data-nav="Errors" style="margin-top:20px">The problem is errors</h3>
<p>A physical qubit loses its state in microseconds to seconds. Today's best make a mistake roughly once in every 100 to 1,000 steps. Useful programs need about one in a trillion. So engineers bundle many physical qubits into one error-checked logical qubit.{cite(4, 5)} The field is judged on logical qubits now, because headline qubit counts say little.</p>
{note("The ratio", "<p>With the surface code, one logical qubit costs hundreds to thousands of physical ones. IBM's newer code design aims for roughly ten times fewer." + cite(10) + "</p>")}
{fig(art.surface_code(), "Forty-nine physical qubits protecting one logical qubit. Filled dots hold the data. Hollow dots keep checking their neighbours without reading the data. Google's 2024 Willow chip ran a 101-qubit version and showed, for the first time, that a bigger code made fewer errors than a smaller one." + cite(9), 2)}
<h3 class="wide" id="s-hardware" data-nav="Hardware" style="margin-top:36px">Five ways to build a qubit</h3>
<div class="cols c4 wide">
<div class="card rv">{art.modality("sc")}<h3>Superconducting circuits</h3><span class="tag">IBM</span><span class="tag">Google</span><span class="tag">Rigetti</span><p>Fast, made in chip factories, needs a fridge colder than space.</p></div>
<div class="card rv">{art.modality("ion")}<h3>Trapped ions</h3><span class="tag">Quantinuum</span><span class="tag">IonQ</span><p>The most accurate gates. Slower and harder to scale.</p></div>
<div class="card rv">{art.modality("atom")}<h3>Neutral atoms</h3><span class="tag">QuEra</span><span class="tag">Atom Computing</span><p>Thousands of atoms held by laser tweezers. Big arrays, slow gates.</p></div>
<div class="card rv">{art.modality("photon")}<h3>Photons</h3><span class="tag">PsiQuantum</span><span class="tag">Xanadu</span><p>Light in chips, mostly at room temperature. Needs near-perfect detectors.</p></div>
</div>
<div class="fx-photos wide">
{photo("ion-trap.jpg", caption="The trap that holds ions. A gold chip a few centimetres across, from a NIST quantum computing experiment.")}
{photo("ytterbium-clock.jpg", caption="Atoms held in a lattice of laser light. The same toolkit that neutral-atom quantum computers build on.")}
{photo("cold-atom-iss.jpg", caption="NASA's Cold Atom Laboratory on the space station, where atoms are cooled to near absolute zero.")}
</div>
{fig(art.fridge(), "A dilution refrigerator, drawn to show the stages. Superconducting machines hold the chip near 0.01 K, colder than deep space at 2.7 K. Most of the electricity goes here." + cite(18), 3)}
<h3 class="wide" id="s-evidence" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
<div class="scroll wide"><table><thead><tr><th>Milestone</th><th>Who and when</th><th>Status</th><th>The catch</th></tr></thead><tbody>
<tr><td>Beats a supercomputer on a test task</td><td>Google 2019{cite(6)}</td><td><span class="tag dis">Disputed</span></td><td>The task had no use. Classical methods later closed most of the gap.</td></tr>
<tr><td>Useful-scale results before error correction</td><td>IBM 2023{cite(7)}</td><td><span class="tag dis">Contested</span></td><td>Classical simulations later reproduced the result.</td></tr>
<tr><td>48 logical qubits on an atom array</td><td>Harvard and QuEra 2023{cite(8)}</td><td><span class="tag ok">Shown</span></td><td>Small codes and short programs.</td></tr>
<tr><td>48 logical qubits on a trapped-ion machine</td><td>Quantinuum Helios, 2025{cite(23)}</td><td><span class="tag dis">Company figure</span></td><td>From the company's own filing. Small codes and short programs.</td></tr>
<tr><td>Errors fall as the code gets bigger</td><td>Google Dec 2024{cite(9)}</td><td><span class="tag ok">Shown</span></td><td>One logical qubit, held briefly.</td></tr>
<tr><td>Verifiable speed-up on a physics measurement</td><td>Google Oct 2025{cite(14)}</td><td><span class="tag ok">Shown</span></td><td>Another machine can check the output. Not yet commercial.</td></tr>
<tr><td>Low-overhead error-correcting code</td><td>IBM 2024{cite(10)}</td><td><span class="tag ok">Designed</span></td><td>Needs hardware that does not exist yet.</td></tr>
<tr><td>Topological qubit</td><td>Microsoft 2025{cite(15)}</td><td><span class="tag dis">Contested</span></td><td>If real it cuts the cost of error correction. Independent physicists want more evidence.</td></tr>
<tr><td>Fault-tolerant machine running useful programs</td><td>IBM and Quantinuum, 2029 target{cite(19, 20)}</td><td><span class="tag tgt">Target</span></td><td>What everyone is working toward.</td></tr>
</tbody></table></div>
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:36px">History</h3>
<div class="tl wide">
<div class="ev"><div class="yr">1981 to 1985</div><p>Benioff, Feynman, Manin and Deutsch describe a quantum computer on paper.{cite(1)}</p></div>
<div class="ev big"><div class="yr">1994</div><p>Shor shows a quantum computer could break the encryption that protects the internet.{cite(2)} Governments start paying attention.</p></div>
<div class="ev"><div class="yr">1995 to 1996</div><p>Quantum error correction is invented. Grover publishes quantum search.{cite(3)}</p></div>
<div class="ev"><div class="yr">1999</div><p>First superconducting qubit, the design IBM and Google use today.</p></div>
<div class="ev"><div class="yr">2011</div><p>D-Wave sells the first commercial quantum annealer, to Lockheed Martin.</p></div>
<div class="ev big"><div class="yr">2016</div><p>IBM puts a 5-qubit processor online for anyone to use.</p></div>
<div class="ev big"><div class="yr">2019</div><p>Google claims quantum supremacy with 53 qubits.{cite(6)} IBM disputes the 10,000-year figure.</p></div>
<div class="ev"><div class="yr">2021 and 2022</div><p>IonQ lists in October 2021.{cite(28)} Rigetti follows in March 2022 and D-Wave on 8 August 2022, each by merging with a blank-cheque company.{cite(25)}{cite(24)}</p></div>
<div class="ev big"><div class="yr">Dec 2024</div><p>Google's Willow chip shows errors shrinking as the code grows.{cite(9)}</p></div>
<div class="ev"><div class="yr">2025</div><p>Microsoft's Majorana 1{cite(15)}, Amazon's Ocelot, Google's Quantum Echoes{cite(14)}, IBM's Nighthawk and Loon, Quantinuum's Helios. The Nobel Prize in Physics goes to Clarke, Devoret and Martinis for the circuit physics behind superconducting qubits.{cite(26)}</p></div>
<div class="ev big"><div class="yr">June 2026</div><p>Quantinuum lists on Nasdaq at $60 a share and raises about $1.68 billion, the largest quantum listing so far.{cite(22)}</p></div>
<div class="ev fut"><div class="yr">2026 on</div><p>The race to error-corrected machines. See chapter 6.</p></div>
</div>''', KEY["learn"], short="Basics")

    # ---------------------------------------------------------------- 2 simple
    ch2 = chapter("simple", 2, "The short version", "Four pictures. That is all you need to follow the rest.", f'''
<div class="cols wide">
<figure class="fig rv" style="margin:0">{art.coin_vs_spin()}<figcaption><b>The spinning coin.</b> A bit is a coin lying flat. A qubit is the coin in mid-air, neither side until it lands.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art.maze()}<figcaption><b>The maze.</b> A normal computer walks the routes one by one. A quantum computer sets the maze up so the wrong routes cancel.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art.combo_lock()}<figcaption><b>The combination lock.</b> For some searches the shortcut is a square root. A million tries become about a thousand.{cite(3)}</figcaption></figure>
</div>
<div class="cols wide" style="margin-top:20px">
<div class="card rv"><h3>Good at</h3><p>Simulating atoms and molecules, which matters for medicines, fertiliser and batteries. Certain optimisation and sampling problems. Breaking some encryption.</p></div>
<div class="card rv"><h3>Bad at</h3><p>Running your phone, speeding up video, replacing the cloud. It will sit in a data centre and be rented by the minute for specific jobs.</p></div>
<div class="card rv"><h3>Worth remembering</h3><p>It is not fast in general. For the right problem it is astronomically faster. For nearly everything else it is slower and costs more.</p></div>
</div>
<div class="wide">{photo("quantum-images.jpg", caption="A montage of laser images of quantum states, made at NIST. What a measured quantum state looks like in practice is a grainy picture, not a number.")}</div>''', KEY["simple"], short="Simple")

    # ---------------------------------------------------------------- 3 change
    ch3 = chapter("change", 3, "What changes, and in what order",
                  "If error-corrected machines arrive, security moves first, then chemistry, then everything that depends on chemistry.", f'''
<div class="tl wide">
<div class="ev fut"><div class="yr">Now to 2030: security</div><p>Encrypted data stolen today can be read later once a large machine exists. Governments and banks are already moving to new standards.{cite(13)} Breaking RSA-2048 is estimated to need about a million noisy qubits.{cite(11)}</p></div>
<div class="ev fut"><div class="yr">2028 to 2035: chemistry and materials</div><p>The first useful gains are expected in simulating molecules: catalysts, battery materials, drug binding. Published estimates for industrially relevant problems run to roughly 1,000 to 4,000 logical qubits.{cite(16, 17)}</p></div>
<div class="ev fut"><div class="yr">2030s: industry</div><p>Cheaper fertiliser and fuel chemistry, better batteries and solar materials, faster drug discovery. These show up as slow improvements in industries that already exist.</p></div>
<div class="ev fut"><div class="yr">After that</div><p>Nobody knows. The builders of the first computers did not predict the spreadsheet either.</p></div>
</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:30px">Be ready</h3>
<div class="cols wide">
<div class="card rv"><h3>At home</h3><p>Keep phones and computers updated, because post-quantum encryption arrives as software updates. Use a password manager and two-step sign-in. There is nothing quantum to buy.</p></div>
<div class="card rv"><h3>In a small business</h3><p>List the data that must stay secret for ten years or more: contracts, health records, design files. Ask your software and cloud suppliers when they will support the NIST standards.{cite(13)}</p></div>
<div class="card rv"><h3>In your career</h3><p>Python and linear algebra are the way in. Qiskit is free and runs real programs on small machines.{cite(21)} Employers want people who can pair chemistry, finance or logistics with this.</p></div>
<div class="card rv"><h3>With your savings</h3><p>Treat the sector as venture risk. Chapter 4 shows what past booms looked like and how often the early leaders failed. Size any position so that losing all of it changes nothing in your life.</p></div>
</div>
<h3 class="wide" id="s-security" data-nav="Security" style="margin-top:40px">The security clock</h3>
<div class="tl wide">
<div class="ev big"><div class="yr">Aug 2024</div><p>The US standards body NIST publishes the first post-quantum encryption standards: FIPS 203, 204 and 205.</p></div>
<div class="ev fut"><div class="yr">About 2030</div><p>Government roadmaps plan to retire today's public-key encryption for the most sensitive systems. The dates have moved before, so check the current NIST and EU ones.</p></div>
<div class="ev fut"><div class="yr">About 2035</div><p>The target for finishing migration in most roadmaps.</p></div>
</div>
<div class="callout wide"><b>Bitcoin and other coins.</b> They sign payments with the kind of cryptography a large quantum computer would break. Coins in addresses whose public key is already visible on the chain are the most exposed. The coin community is working on upgrades, but a change needs wide agreement, and that is slow. Frontier Coin will cover this in detail.</div>
<div class="fx-photos wide">{photo("qkd-system.jpg", caption="Alice and Bob, a NIST fibre quantum key distribution system. It uses quantum physics to protect messages. That is a different thing from post-quantum encryption, which is ordinary maths that quantum computers cannot break quickly.")}
<div class="card" style="align-self:start"><h3>Ireland</h3><p>Ireland published its national quantum strategy, Quantum 2030, in 2023. Equal1 in Dublin builds quantum chips on silicon. The Tyndall National Institute in Cork works on photonics and materials, and the large US technology firms run research teams here. Ireland also hosts a large share of Europe's data centres, so post-quantum migration is a local business issue as well as a research one.</p></div></div>
<h3 class="wide" id="s-jobs" data-nav="Jobs" style="margin-top:40px">Jobs and where to start</h3>
<div class="cols wide">
<div class="card rv"><h3>Who is hiring</h3><p>Hardware physicists and engineers, cryogenic and control-electronics engineers, compiler and software developers, and people who can turn a chemistry or finance problem into a quantum one. Security and cloud roles are open to anyone who learns the basics.</p></div>
<div class="card rv"><h3>Free ways to learn</h3><ul>{"".join(f'<li><a href="{u}" target="_blank" rel="noopener"><b>{n}</b></a>: {d}</li>' for n, d, u in X.JOBS)}</ul></div>
</div>
<h3 class="wide" id="s-control" data-nav="Control" style="margin-top:40px">Who controls it</h3>
<div class="cols wide">
<div class="card rv"><h3>Access</h3><p>Machines will be rented from a few firms and governments. Whoever holds the best hardware first gets an edge in chemistry, finance and intelligence work.</p></div>
<div class="card rv"><h3>Energy</h3><p>One machine draws little. A fleet of big ones could add real load. Gains in fertiliser, batteries and solar materials could outweigh that, if they come.</p></div>
<div class="card rv"><h3>Jobs and inequality</h3><p>Few jobs are replaced directly. The bigger effect is which chemistry and materials industries get cheaper, and which countries host them.</p></div>
</div>
<h3 class="wide" id="s-defence" data-nav="Defence" style="margin-top:40px">War, defence money and what you do not see</h3>
<div class="cols wide">
<div class="card rv"><h3>Governments are early customers</h3><p>Defence and intelligence agencies paid for much of the first quantum work and still set priorities. In the open record: the US DARPA Quantum Benchmarking Initiative, NSA guidance on post-quantum codes, and national programmes in China, the UK and the EU.</p></div>
<div class="card rv"><h3>Some progress is not published</h3><p>Code-breaking, secure communications and sensing for navigation without GPS are areas where results can be classified. The public record lags the real state of the art by an unknown amount. Company claims can also be shaped by contracts you cannot see.</p></div>
<div class="card rv"><h3>The signals you can see</h3><p>Government contract awards, export-control rules, lab hiring, and sudden changes in who may buy certain parts. They are visible even when the results are not.</p></div>
<div class="card rv"><h3>Why a race lifts some shares</h3><p>When governments frame quantum as a race with a rival, funding and procurement follow, and domestic companies gain. The same framing brings export bans and sanctions that can cut a company off from customers and parts. Both appear in the live feed as policy events.</p></div>
</div>
<div class="callout t wide"><b>Next on Frontier.</b> Drones, counter-drone systems, directed energy and high-power microwave weapons, and materials such as graphene and carbon nanotubes have the same defence funding and the same secrecy problem. Each gets its own site.</div>''', KEY["change"], short="Change")

    # ---------------------------------------------------------------- 4 companies
    cos = []
    for c in COMPANIES:
        s = stat[c["t"]]
        cos.append(f'''<article class="card co rv"><h3>{c["name"]}<span>{c["t"]} &middot; {c["kind"]}</span></h3>
<dl><dt>Started at</dt><dd>{fmt_p(s["first"])} in {s["first_date"][:7]}. Now {fmt_p(s["last"])}. Peak {fmt_p(s["peak"])} in {s["peak_date"][:7]}, so {abs(s["pct_from_peak"]):.0f}% below it.</dd>
<dt>Rivals</dt><dd>{c["rivals"]}</dd><dt>Needs for profit</dt><dd>{c["profit"]}</dd><dt>Watch</dt><dd>{c["watch"]}</dd>
<dt>How advanced</dt><dd>{c["rank"]}</dd></dl><span class="verdict">{c["verdict"]}</span></article>''')
    hype = "".join(f'<tr><td class="n">{lvl}</td><td><b>{name}</b><br><span class="muted">{desc}</span></td><td>{ex}</td>'
                   f'<td><span class="tag {cls}">{"strong" if cls == "ok" else "caution" if cls == "dis" else "target only"}</span></td></tr>'
                   for lvl, name, desc, ex, cls in X.HYPE)
    shovels = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in X.SHOVELS)
    ch4 = chapter("companies", 4, "The companies, the money, the odds",
                  "Where each started, who it competes with, what has to happen before it makes money, and what past booms did to share prices.", f'''
<div class="cols wide">{"".join(cos)}
<article class="card co rv"><h3>Quantinuum<span>QNT &middot; Trapped ions, listed June 2026</span></h3>
<dl><dt>What happened</dt><dd>It priced its IPO at $60 a share on 3 to 4 June 2026 and raised about $1.68 billion. Full-year 2025 revenue was $30.9 million with a net loss of $192.6 million.{cite(22)}</dd>
<dt>Technology</dt><dd>Its Helios machine has 98 physical qubits and, the company says, 48 logical qubits. It targets Sol in 2027 and Apollo, a fault-tolerant machine, in 2029.{cite(23)}</dd>
<dt>Why it is not modelled here</dt><dd>It has only a few months of price history, so it has no scenario range yet. Its IPO is the largest in this sector.</dd></dl><span class="verdict">The leader on ions, newly public</span></article>
<article class="card co rv"><h3>The big groups<span>IBM, Alphabet, Microsoft, Honeywell, Nvidia</span></h3>
<dl><dt>Position</dt><dd>IBM and Google lead on superconducting hardware and error correction. Quantinuum, the leader in trapped ions, listed on Nasdaq in June 2026, with Honeywell keeping about half the voting power. Microsoft is betting on a different kind of qubit. Nvidia sells the classical chips that decode errors.</dd>
<dt>Why they matter</dt><dd>Quantum is a small slice of their value. Milestones move their shares by a few per cent, not several-fold.</dd>
<dt>Use</dt><dd>A lower-risk way to hold the theme, with a much smaller upside if it works.</dd></dl>
<span class="verdict">Most advanced: Google and Quantinuum on error correction, IBM on the engineering roadmap</span></article></div>
<h3 class="wide" id="s-prices" data-nav="Prices" style="margin-top:44px">Share prices since listing</h3>
<p class="wide">Weekly closes to <span id="lastdate"></span>, adjusted for splits. IonQ, Rigetti and D-Wave histories begin with the blank-cheque company each one merged with: IonQ in October 2021, Rigetti in March 2022 and D-Wave in August 2022.</p>
<div class="ctrl wide" id="tickers" role="group" aria-label="Companies"></div>
<div class="ctrl wide" role="group" aria-label="Chart options">
<button data-mode="growth" aria-pressed="true">Growth, 100 = start</button><button data-mode="price" aria-pressed="false">Price (US$)</button>
<button data-range="all" aria-pressed="false">Full history</button><button data-range="2021" aria-pressed="false">Since 2021</button>
<button data-range="2024" aria-pressed="true">Since 2024</button><button data-range="1y" aria-pressed="false">Last year</button></div>
<figure class="fig wide"><svg id="chart" viewBox="0 0 900 440" role="img" aria-label="Weekly share prices"></svg><div id="tip">Move across the chart to read values.</div></figure>
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>These are the biggest rises from a low to a later high inside two years. Apple, Nvidia and Bitcoin are the famous ones. The quantum pure-plays did the same in 2024 and 2025, and then fell.</p>
{note("Reading it", "<p>Rigetti, D-Wave and Quantum Computing Inc rose 49x to 63x in one run. Nvidia, with real profits behind it, rose about 12x. The gap is the point.</p>")}
{fig(charts.multiples(mult_items), "Log scale, from weekly closes. Prices are adjusted for splits, which is why Apple's low looks tiny. Past rises do not repeat on a schedule.", 4)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:40px">The ladder to profit</h3>
{fig(charts.ladder(LADDER, 3), "Each step has moved prices in this sector. The early steps get priced in before they are reached, and delays are punished. The field has reached step four, in small experiments. Profit needs step seven.", 5)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul><li>A company shows error-corrected programs long enough to be useful.</li><li>A named customer pays for results, not for a trial.</li><li>Revenue grows faster than the cash it burns.</li><li>A big group buys a small one at a clear premium.</li></ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul><li>Prices rise several-fold with no new technical result.</li><li>The company sells new shares into every rally.</li><li>Targets keep slipping a year at a time.</li><li>The claim rests on a result nobody else has reproduced.</li></ul></div>
</div>
<h3 class="wide" id="s-live" data-nav="Live" style="margin-top:44px">Live updates</h3>
<p class="wide">The page checks filings, headlines and papers and shows how they move the odds used in chapter 6. <span id="live-stamp">Loading the live layer.</span></p>
<div class="cols wide">
<div class="card"><h3>Announcements that moved the odds</h3><ul class="feed" id="live-events"><li>Loading.</li></ul></div>
<div class="card"><h3>Change log</h3><ul class="feed" id="live-log"><li>Loading.</li></ul></div>
<div class="card"><h3>Headlines (links to the publisher)</h3><ul class="feed" id="live-news"><li>Loading.</li></ul></div>
<div class="card"><h3>New papers that mention these firms</h3><ul class="feed" id="live-papers"><li>Loading.</li></ul></div>
</div>
<p class="cap wide" id="live-status"></p>
<div class="scroll wide"><table id="live-react"></table></div>
<p class="cap wide">The table shows how these four stocks actually moved after past filings of each type, against QQQ as a market proxy. The live layer uses it to size its nudges. It is reported with case counts because small samples mislead.</p>
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<p>Every claim sits on a rung of evidence. The higher the rung, the more weight it earns.</p>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples on this page</th><th>Weight</th></tr></thead><tbody>{hype}</tbody></table></div>
<h3 class="wide" id="s-map" data-nav="Map" style="margin-top:44px">The race, country by country</h3>
<p class="wide">Pick a country. Teal marks leaders, violet marks major players, amber marks emerging ones. A summary from public sources, so treat the detail as approximate.</p>
<div class="map-wrap wide"><figure class="fig" style="margin:0">{X.tile_map()}</figure><div class="card" id="map-panel"></div></div>
<div class="callout t wide"><b>Why politics moves these shares.</b> Governments fund their own champions, restrict exports of key parts and sometimes block foreign buyers. The United States and China each treat quantum as a strategic race. One new restriction can cut a company off from customers or suppliers overnight. One new funding programme can lift a whole group.</div>
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{shovels}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
<p>Two equal-weight baskets set to 100 at the start. One holds the four pure-plays, the other the four large groups.</p>
{fig(idx_svg, "Weekly rebalanced equal-weight baskets. Pure-plays: IonQ, Rigetti, D-Wave, Quantum Computing Inc. Large groups: IBM, Alphabet, Microsoft, Honeywell.", 6)}
<h3 class="wide" id="s-time" data-nav="Time" style="margin-top:44px">Time machine</h3>
<p>Pick an asset and a date. See what the money would be worth now, how high it went, and how far it fell on the way.</p>
<div class="ctrl wide"><label>Asset <select id="tm-asset"></select></label><label>From <input type="date" id="tm-date"></label><label>Amount (US$) <input type="number" id="tm-amt" value="1000" min="1" step="100"></label></div>
<figure class="fig wide"><svg id="tm-svg" viewBox="0 0 900 260" role="img" aria-label="Value of the investment over time"></svg><div id="tm-out" class="tmout"></div></figure>''', KEY["companies"], short="Money")

    # ---------------------------------------------------------------- 5 hurdles
    power_items = [("Human brain", 20), ("Laptop", 50), ("One AI server (8 GPUs)", 10200), ("Quantum computer, whole system", 25000),
                   ("AI server rack", 120000), ("Summit supercomputer", 13e6), ("Frontier supercomputer", 22.7e6), ("Large AI data centre", 100e6)]
    ch5 = chapter("hurdles", 5, "The gap, and the power bill",
                  "How far today's chips are from useful machines, what is in the way, and how much electricity a machine uses.", f'''
{fig(charts.line_gap(), "Log scale. Practical chips today have 100 to 150 usable qubits. Breaking RSA-2048 needs about a million noisy qubits" + cite(11) + ", down from 20 million in the 2019 estimate." + cite(12), 7)}
<div class="cols wide">
<div class="card rv"><h3>Error rates</h3><p>About 1 error in 100 to 1,000 steps today. The target is roughly 1 in a trillion.</p></div>
<div class="card rv"><h3>Overhead</h3><p>Hundreds to thousands of physical qubits per logical qubit with the surface code.{cite(5)} IBM's newer design aims much lower.{cite(10)}</p></div>
<div class="card rv"><h3>Wiring and cooling</h3><p>A fridge holds a few thousand wires. A million qubits need electronics inside the cold, or links between many fridges.</p></div>
<div class="card rv"><h3>Decoding</h3><p>A classical computer must read the error signals and answer within microseconds, without a break.</p></div>
<div class="card rv"><h3>Algorithms</h3><p>Large speed-ups are proven for a short list of problems. Loading big datasets in is slow.</p></div>
<div class="card rv"><h3>Money and people</h3><p>Most listed pure-plays spend more than they earn, and the skilled workforce is small.</p></div>
</div>
<h3 class="wide" id="s-power" data-nav="Power" style="margin-top:44px">Power</h3>
<p>One superconducting quantum computer draws about 15 to 30 kW, almost all of it for cooling and control electronics. The chip itself uses next to nothing. Google put its whole 2019 apparatus at 26 kW in the worst case.{cite(18)}</p>
{note("Careful", "<p>Low power is not the same as efficient. The machine is cheap to run per hour and the wrong tool for nearly every job.</p>")}
{fig(charts.bars_h(power_items, lambda v: (f"{v / 1e6:g} MW" if v >= 1e6 else f"{v / 1e3:g} kW" if v >= 1e3 else f"{v:g} W"), highlight="Quantum computer, whole system", label="Power use in watts, log scale"), "Log scale, approximate. Sources: Google 2019 supplement, Nvidia DGX H100 rating (10.2 kW), Top500 lists.", 8)}
<div class="fx-photos wide">{photo("supercomputer.jpg", caption="NASA's Columbia supercomputer. A machine of this class is the yardstick a quantum computer has to beat for a chosen problem.")}
<div class="card" style="align-self:start"><h3>Fleets change the sum</h3><p>A million-qubit system multiplies the cooling and control load, and published estimates of its draw vary widely because none exists to measure. D-Wave argues one fridge can cool ever larger chips without raising power much. Superconducting groups mostly expect megawatt-class sites. For the right problem, a result that takes a supercomputer weeks could take a quantum machine minutes, and that would be a large saving.</p></div></div>''', KEY["hurdles"], short="Gap")

    # ---------------------------------------------------------------- 6 outlook
    rows = "".join(f'<tr><td>{c["name"]} ({c["t"]})</td><td class="n">{fmt_p(sims[c["t"]]["end_p10"])}</td><td class="n">{fmt_p(sims[c["t"]]["end_p50"])}</td>'
                   f'<td class="n">{fmt_p(sims[c["t"]]["end_p90"])}</td><td class="n">{sims[c["t"]]["prob_below_start"]:.0%}</td></tr>' for c in COMPANIES)
    ch6 = chapter("outlook", 6, "Three years out",
                  "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
{fig(charts.roadmap(), "Logical qubits by year, log scale. Hollow points are company targets and the solid point is the best result shown. Sources: IBM" + cite(19) + ", Quantinuum" + cite(20) + ", Bluvstein et al." + cite(8), 9)}
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">
<div class="card rv"><h3>Likely, about 70%</h3><p>Google, IBM and Quantinuum keep showing steady gains: more logical qubits, longer programs, lower error. Neutral-atom machines close the size gap. No machine runs a commercially decisive program yet.</p></div>
<div class="card rv"><h3>Even odds, about 50%</h3><p>A first useful result in chemistry or materials appears on error-corrected hardware by late 2029. It is narrow and expensive.</p></div>
<div class="card rv"><h3>Unlikely, under 25%</h3><p>A machine with a couple of hundred long-running logical qubits arrives on the 2029 schedule. We expect most dates to slip by 12 to 24 months.</p></div>
</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
<h3 class="wide" id="s-scenarios" data-nav="Scenarios" style="margin-top:40px">What it could mean for the four pure-play shares</h3>
<p>Pick a company and move the sliders to set your own odds. Dashed lines are the typical path in each story. The bands hold the middle 50% and 80% of outcomes once the stories are mixed.</p>
<figure class="fig wide" id="fan">
<div class="ctrl" id="fan-tabs" role="group" aria-label="Company"></div>
<svg id="fansvg" viewBox="0 0 900 440" role="img" aria-label="Recent price and three-year scenario range for the chosen company"></svg>
<div class="sliders">
<label>Chance of the bear story <input type="range" id="sl-bear" min="0" max="90" step="1"></label>
<label>Chance of the bull story <input type="range" id="sl-bull" min="0" max="90" step="1"></label>
<label>Volatility (100 = last two years, scaled) <input type="range" id="sl-vol" min="40" max="160" step="5"></label>
<button type="button" id="fan-reset" class="plain">Back to our odds</button></div>
<p id="fan-probs" class="cap"></p><p id="fan-read"></p><p id="fan-tilt" class="cap"></p>
<figcaption><b>Fig 10.</b> The live layer may tilt our odds by a few points because of dated announcements, never by more than 12.</figcaption></figure>
<div class="scroll wide"><table><thead><tr><th>Stock</th><th class="n">Low end (10th)</th><th class="n">Middle</th><th class="n">High end (90th)</th><th class="n">Below today</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cap wide">Three years from the build date, at our starting odds.</p>
<h3 class="wide" id="s-record" data-nav="Record" style="margin-top:36px">Our record</h3>
<div class="card wide"><p id="live-score">Loading the scorecard.</p>
<p class="cap">Every week the site writes down its 3, 6 and 12-month ranges in a hash-chained log before the outcome is known, then scores them. A 10th to 90th range should hold the real price about 80% of the time.</p></div>
<div class="pull wide">The science will probably get there. The share prices already assume it has.<small>Our view</small></div>
<div class="cols wide">
<div class="card rv"><h3>Why we lean that way</h3><p>We think error-corrected quantum computers are likely to be built, and that Google, IBM and Quantinuum are furthest along. The four listed pure-plays were priced in 2024 and 2025 as if the finish line were close. Our scenarios put the chance of each ending the three years below today's price at {lo_p:.0%} to {hi_p:.0%}.</p></div>
<div class="card rv"><h3>Expect a shakeout</h3><p>New technology booms leave a few giants and many casualties. Of the four, we would expect at least one to be bought cheaply, merged or short of cash by 2029. The survivors will have sold a lot of new shares on the way, which cuts the gain for people already holding.</p></div>
<div class="card rv"><h3>If it goes right</h3><p>The leaders with real hardware gain. A few-fold rise is a normal good outcome. The rises already seen, {runs["RGTI"]["multiple"]:.0f}x for Rigetti and {runs["QBTS"]["multiple"]:.0f}x for D-Wave, borrowed from the future. The biggest winners may be companies not listed yet, or the suppliers of lasers, cryogenics and chips.</p></div>
<div class="card rv"><h3>The 1990s test</h3><p>Apple in 1997 and Nvidia in 2022 worked because the company later earned vast profits. The test for each quantum company is the same. When does it earn real profit, and how many more shares does it have to sell first. Until that has an answer, these are lottery tickets with a good story, and should be sized like one.</p></div>
</div>
<div class="callout t wide"><b>What would change our mind.</b> A company showing hundreds of long-running logical qubits ahead of schedule. A named customer paying a large recurring bill for useful results. A second team reproducing the topological-qubit claim on its own.</div>''', KEY["outlook"], short="Outlook")

    # ---------------------------------------------------------------- assemble
    bands = {
        "ch2": band("laser-table.jpg", "Where it happens", "Behind every qubit headline there is a room like this one.", "A researcher at a laser table"),
        "ch3": band("clean-room.jpg", "Hardware is manufacturing", "Making the parts is an industrial job, and the supply chain is thin.", "A technician in a clean room"),
        "ch4": band("ion-trap.jpg", "Where the money is", "This gold chip holds a few ions. The companies that use ions build their own.", "A gold ion trap chip"),
        "ch5": band("ytterbium-clock.jpg", "Precision", "The tools are the same ones that built the world's best clocks.", "An atomic clock apparatus"),
        "ch6": band("cold-atom-lab.jpg", "Three years", "One hardware generation. Enough time to find out who is bluffing.", "An astronaut working on the Cold Atom Lab"),
    }
    foot = f'''<footer class="fx-foot" id="disclosures"><div class="fx-foot-in">
<h2 style="font-size:1.6rem">Sources, method and disclosures</h2>
<ol>{"".join(f'<li id="r{n}">[{n}] <a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for n, t, u in REFS)}</ol>
<div class="cols">
<div class="card"><h3>Information only</h3><p>This site is general information and education. It is not investment advice, a recommendation, an offer or a solicitation, and it takes no account of your circumstances. Speak to a licensed adviser before acting.</p></div>
<div class="card"><h3>Scenarios, not forecasts</h3><p>Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%. Share prices can fall to zero.</p></div>
<div class="card"><h3>Conflicts</h3><p>Solas33 holds no position in any company named and takes no payment from any of them. The only benefit to Solas33 is traffic to its own sites as a provider of information. There is no advertising. If any of that changes it will be stated here with the date.</p></div>
<div class="card"><h3>Data</h3><p>Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Claims are labelled as targets until verified.</p></div>
<div class="card"><h3>Corrections</h3><p>Errors are fixed and logged. Write to <a href="mailto:hello@solas33.com">hello@solas33.com</a>. Editorial responsibility: Solas33. Content last reviewed {AS_OF}.</p></div>
<div class="card"><h3>For researchers and teachers</h3><p>Cite as Solas33, Frontier Quantum, with the page date. The live layer is public: <a href="live.json">live.json</a> and an <a href="feed.xml">RSS feed</a>. Use your browser's Print for a clean copy of a chapter. Set the reading level at the top to Simple for younger students.</p></div>
</div>
<p style="margin-top:28px">Part of <a href="../">Frontier</a>. Code is public at <a href="https://github.com/SOLAS33/frontier">github.com/SOLAS33/frontier</a>.</p>
</div></footer>'''

    flow = (f'<div class="fx-flow">{notice}{ch1}</div>{bands["ch2"]}<div class="fx-flow">{ch2}</div>{bands["ch3"]}<div class="fx-flow">{ch3}</div>'
            f'{bands["ch4"]}<div class="fx-flow">{ch4}</div>{bands["ch5"]}<div class="fx-flow">{ch5}</div>{bands["ch6"]}<div class="fx-flow">{ch6}</div>')
    facts = [("Logical qubits reported", "48 (Quantinuum)"), ("Needed for RSA-2048", "about 1m physical"), ("Whole machine", "about 26 kW"),
             ("Fault-tolerant target", "2029")]
    rows = "".join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a, b in facts)
    rail = ('<aside class="fx-rail" id="fx-rail" aria-label="Live and series panels"><div id="fx-live" aria-live="polite"></div>'
            f'<section class="rp"><h4>Numbers to hold on to</h4>{rows}</section>'
            f'<section class="rp"><h4>In this series</h4><div class="rp-list">{series_list("quantum")}</div></section></aside>')
    body = (f'{hero}<nav class="fx-spine" id="fx-spine" aria-label="Chapters"></nav>{rail}{flow}'
            f'<div class="fx-flow">{watch_promo()}</div>{foot}')
    return {"title": TITLE, "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
