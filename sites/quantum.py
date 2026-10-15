"""Content and assembly for the quantum computing site. All numbers that come from prices are computed here."""
from __future__ import annotations

import json

from frontier import art, charts, prices
from sites import quantum_extra as X
from sites import quantum_extra2 as X2
from frontier.scenarios import Scenario, simulate

TITLE = "Frontier Quantum"
AS_OF = "15 October 2026"

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
]


def cite(*ids):
    return "".join(f'<sup><a href="#r{i}" title="{next(r[1] for r in REFS if r[0] == i)}">[{i}]</a></sup>' for i in ids)


def fmt_p(v):
    return f"${v:,.2f}" if v < 100 else f"${v:,.0f}"


# Author judgement: scenario probabilities and yearly drift. Documented on the page.
SCEN = {
    "IONQ": [Scenario("bear", "Milestones slip, more share sales", 0.40, -0.45, 0.75),
             Scenario("base", "Steady progress, slow revenue", 0.35, 0.10, 0.75),
             Scenario("bull", "Error-correction targets met, revenue ramps", 0.25, 0.55, 0.75)],
    "RGTI": [Scenario("bear", "Falls behind rivals, funding squeeze", 0.45, -0.50, 0.75),
             Scenario("base", "Keeps pace on accuracy", 0.35, 0.00, 0.75),
             Scenario("bull", "Wins a breakthrough or buyer", 0.20, 0.60, 0.75)],
    "QBTS": [Scenario("bear", "Annealing demand stalls", 0.35, -0.40, 0.75),
             Scenario("base", "Revenue grows, gate-model still early", 0.40, 0.05, 0.75),
             Scenario("bull", "Gate-model prototype lands and sales ramp", 0.25, 0.50, 0.75)],
    "QUBT": [Scenario("bear", "Stays research-stage, dilution", 0.50, -0.55, 0.75),
             Scenario("base", "Small product revenue", 0.33, 0.00, 0.75),
             Scenario("bull", "Photonic chips find real buyers", 0.17, 0.60, 0.75)],
}

COMPANIES = [
    {"t": "IONQ", "name": "IonQ", "kind": "Trapped ions", "rivals": "Quantinuum (private, owned mostly by Honeywell), QuEra and Atom Computing (neutral atoms), IBM and Google (circuits)",
     "profit": "Show hundreds of error-corrected qubits on its own hardware, turn government and cloud contracts into repeat revenue, and stop selling new shares to fund losses.",
     "watch": "Gate accuracy, logical-qubit demonstrations, quarterly revenue against cash burn, share count growth, acquisitions being absorbed.",
     "rank": "Strong second tier. Its ions are among the most accurate qubits, but scaling the machine is unproven.",
     "verdict": "Most likely of the four to still matter in 2029"},
    {"t": "RGTI", "name": "Rigetti", "kind": "Superconducting circuits", "rivals": "IBM and Google (much larger budgets), AWS, Alice &amp; Bob",
     "profit": "Hold high two-qubit accuracy as chip size grows past a few hundred qubits, and win a customer base that is not mainly government grants.",
     "watch": "Two-qubit accuracy at scale, multi-chip roadmap dates met, revenue mix, cash runway.",
     "rank": "Third tier on technology. Cheap per share is not the same as cheap per unit of progress.",
     "verdict": "Highest risk of being overtaken or bought"},
    {"t": "QBTS", "name": "D-Wave", "kind": "Quantum annealing, plus a gate-model effort", "rivals": "Classical optimisation software (Gurobi, quantum-inspired solvers), IBM, IonQ for gate-model",
     "profit": "Prove customers pay repeatedly for optimisation that beats classical solvers, and show a working gate-model chip so growth is not capped by annealing.",
     "watch": "Revenue growth and customer renewals, independent benchmarks against classical solvers, gate-model results.",
     "rank": "Leads on commercial sales today because annealers are useful for a narrow set of problems now.",
     "verdict": "Best near-term revenue story, narrowest technology"},
    {"t": "QUBT", "name": "Quantum Computing Inc", "kind": "Photonic chips", "rivals": "PsiQuantum, Xanadu (photonic computers), and photonic chip foundries",
     "profit": "Move from prototypes and small orders to a product line that customers reorder, and show its chips matter to quantum computing as well as sensing.",
     "watch": "Revenue and gross margin, named repeat customers, peer-reviewed results, share sales.",
     "rank": "Earliest stage of the four. Little independently checked technical progress so far.",
     "verdict": "Most speculative of the four"},
]

LADDER = [("Lab result", "Qubit made|and measured"), ("Beats classical|on a test", "Advantage on a|useless task"),
          ("Errors fall|as code grows", "Shown by Google,|Dec 2024"), ("Dozens of|logical qubits", "Shown in small|experiments"),
          ("Hundreds,|long programs", "Targets 2028 to|2029"), ("Paid, useful|advantage", "Chemistry or|materials first"),
          ("Repeat revenue|and profit", "Needs all of|the above")]


def build():
    px = prices.load()
    stat = {t: prices.stats(px[t]) for t in px}
    runs = {t: prices.best_run(px[t]) for t in ("IONQ", "RGTI", "QBTS", "QUBT", "NVDA", "AAPL", "BTC-USD")}
    sims = {}
    for t, sc in SCEN.items():
        sims[t] = simulate(px[t]["c"][-1], prices.annual_vol(px[t]), sc, years=3)
    # price data for the interactive chart
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
               f"window.PRICE_ORDER={json.dumps(order)};window.PRICE_NAMES={json.dumps(names)};"
               f"window.SCEN={json.dumps(scen_js, separators=(',', ':'))};"
               f"window.TM_ASSETS={json.dumps(tm_assets)};window.TM_DEFAULT={json.dumps(tm_default)};"
               f"window.COUNTRY={json.dumps(X.COUNTRY)};window.COUNTRY_NAMES={json.dumps(X.NAMES)};")
    # equal-weight baskets, rebased to 100 at the first week where every member exists
    def basket(members):
        idx = {t: dict(zip(px[t]["d"], px[t]["c"])) for t in members}
        dates = [d for d in px[members[0]]["d"] if all(d in idx[t] for t in members)]
        dates = [d for d in dates if d >= max(px[t]["d"][0] for t in members)]
        lvl, out = 100.0, []
        for i, d in enumerate(dates):
            if i:
                lvl *= 1 + sum(idx[t][d] / idx[t][dates[i - 1]] - 1 for t in members) / len(members)
            out.append(lvl)
        return dates, out
    pd_d, pd_v = basket(["IONQ", "RGTI", "QBTS", "QUBT"])
    bg_d, bg_v = basket(["IBM", "GOOGL", "MSFT", "HON"])
    start = pd_d[0]
    bg = [(d, v) for d, v in zip(bg_d, bg_v) if d >= start]
    bg_v2 = [v / bg[0][1] * 100 for _, v in bg]
    idx_svg = charts.index_chart([("Pure-play quantum", pd_d, pd_v, "var(--amber)"), ("Large groups", [d for d, _ in bg], bg_v2, "var(--teal)")])

    nav = [("learn", "Learn"), ("simple", "Explained simply"), ("change", "How the world changes"),
           ("companies", "The companies"), ("hurdles", "Hurdles and power"), ("outlook", "Next three years"),
           ("disclosures", "Disclosures"), ("family", "More Frontier")]

    def counter(val, label, pre="", suf="", dec=0):
        return (f'<div class="stat"><b data-count="{val}" data-pre="{pre}" data-suf="{suf}" data-dec="{dec}">{pre}{val:,.{dec}f}{suf}</b>'
                f'<span>{label}</span></div>')

    ion, rig, dwv, qub = (stat[t] for t in ("IONQ", "RGTI", "QBTS", "QUBT"))
    body = []
    A = body.append

    # ---------- hero
    A(f'''<header class="hero">{art.hero_interference()}
<div class="hero-copy"><div class="eyebrow">Frontier series &middot; Quantum computing</div>
<h1>The computer that thinks in <em>waves</em></h1>
<p class="lead">What a quantum computer is, who is building one, what has really been shown, what the next three years could do to the companies, and how to get ready. Written for people who are not physicists.</p></div>
<div class="stats">
{counter(50, "error-corrected qubits shown so far, in small experiments", "about ")}
{counter(1000000, "noisy qubits needed to break RSA-2048 (2025 estimate)", "about ")}
{counter(runs["RGTI"]["multiple"], "times Rigetti rose from low to high in one year", "", "x")}
{counter(26, "kilowatts for one whole quantum computer, about the continuous load of 50 to 100 homes", "", " kW")}
</div></header>''')
    A('<div class="callout r rv"><b>Information only.</b> This site explains technology and shows how its companies and share prices have behaved. It is not investment advice and it makes no recommendation. Projections are scenarios, not forecasts, and you can lose all of any money you put into shares like these. See Disclosures at the foot of the page.</div>')

    # ---------- 1 learn
    A(f'''<section class="chapter" id="learn"><header><div class="no">1</div><div><h2>Learn it, start to finish</h2>
<p class="sub">The idea, the physics, the hardware, the history and the evidence, with the papers behind each claim.</p></div></header>
{X.KEY["learn"]}
<div class="cols">
<div class="card rv"><h3>The idea</h3><p>Ordinary computers store bits that are 0 or 1. A quantum computer stores qubits, which can hold a weighted blend of 0 and 1 until measured. Richard Feynman argued in 1981 that simulating nature needs a machine built from quantum parts.{cite(1)}</p></div>
<div class="card rv"><h3>The three tools</h3><p><b>Superposition</b> holds many possibilities at once. <b>Entanglement</b> ties qubits together. <b>Interference</b> makes wrong answers cancel and the right one stand out. Shor's 1994 factoring algorithm{cite(2)} and Grover's 1996 search{cite(3)} are built from these.</p></div>
<div class="card rv"><h3>The problem</h3><p>Qubits are fragile. Today's best make an error once in roughly 100 to 1,000 steps. Useful programs need about one in a trillion, so many physical qubits must be combined into one error-corrected logical qubit.{cite(4, 5)}</p></div>
</div>
<figure class="fig"><div class="cols" style="align-items:center">
<div>{art.bloch()}</div><div><h3>A qubit as a sphere</h3><p>The arrow can point anywhere on the sphere. The north pole is 0, the south pole is 1, and everything between is a blend. Measuring snaps it to a pole, with odds set by how close the arrow was.</p></div>
</div><figcaption>Drawn from the standard Bloch-sphere picture of one qubit.</figcaption></figure>
<h3 style="margin-top:36px">Five ways to build a qubit</h3>
<div class="cols c4">
<div class="card rv">{art.modality("sc")}<h3>Superconducting circuits</h3><span class="tag">IBM</span><span class="tag">Google</span><span class="tag">Rigetti</span><p>Fast, built in chip factories, needs a fridge colder than space.</p></div>
<div class="card rv">{art.modality("ion")}<h3>Trapped ions</h3><span class="tag">Quantinuum</span><span class="tag">IonQ</span><p>Most accurate gates. Slower, harder to scale.</p></div>
<div class="card rv">{art.modality("atom")}<h3>Neutral atoms</h3><span class="tag">QuEra</span><span class="tag">Atom Computing</span><p>Thousands of atoms in laser tweezers. Large arrays, slower gates.</p></div>
<div class="card rv">{art.modality("photon")}<h3>Photons</h3><span class="tag">PsiQuantum</span><span class="tag">Xanadu</span><p>Light in chips, mostly room temperature, needs near-perfect detectors.</p></div>
</div>
<figure class="fig">{art.fridge()}<figcaption>Superconducting machines sit in a dilution refrigerator. The chip is held near 0.01 K, colder than deep space (2.7 K). Most of the electricity goes here.{cite(18)}</figcaption></figure>
<h3>The evidence so far</h3>
<div class="scroll"><table><thead><tr><th>Milestone</th><th>Who and when</th><th>Status</th><th>What to know</th></tr></thead><tbody>
<tr><td>Beats a supercomputer on a test task</td><td>Google 2019{cite(6)}</td><td><span class="tag dis">Disputed</span></td><td>Task had no use. Classical methods later closed most of the gap.</td></tr>
<tr><td>Useful-scale results before error correction</td><td>IBM 2023{cite(7)}</td><td><span class="tag dis">Contested</span></td><td>Classical simulations later reproduced the result.</td></tr>
<tr><td>48 logical qubits on an atom array</td><td>Harvard and QuEra 2023{cite(8)}</td><td><span class="tag ok">Shown</span></td><td>Small codes, short programs.</td></tr>
<tr><td>Errors fall as the code gets bigger</td><td>Google Dec 2024{cite(9)}</td><td><span class="tag ok">Shown</span></td><td>The sign error correction can scale. One logical qubit, held briefly.</td></tr>
<tr><td>Verifiable speed-up on a physics measurement</td><td>Google Oct 2025{cite(14)}</td><td><span class="tag ok">Shown</span></td><td>Output can be checked by another machine. Not yet commercial.</td></tr>
<tr><td>Low-overhead error-correcting code design</td><td>IBM 2024{cite(10)}</td><td><span class="tag ok">Designed</span></td><td>Roughly ten times fewer physical qubits than the surface code, if the hardware reaches it.</td></tr>
<tr><td>Topological qubit</td><td>Microsoft 2025{cite(15)}</td><td><span class="tag dis">Contested</span></td><td>If real, it cuts error-correction cost. Independent physicists want stronger evidence.</td></tr>
<tr><td>Fault-tolerant machine with useful programs</td><td>IBM and Quantinuum: 2029 target{cite(19, 20)}</td><td><span class="tag tgt">Target</span></td><td>The goal the whole field is working toward.</td></tr>
</tbody></table></div>
<h3 style="margin-top:36px">History</h3>
<div class="tl">
<div class="ev"><div class="yr">1981 to 1985</div><p>Benioff, Feynman, Manin and Deutsch set out the idea of a quantum computer.{cite(1)}</p></div>
<div class="ev big"><div class="yr">1994</div><p>Shor shows a quantum computer could break the encryption that protects the internet.{cite(2)} Governments and companies start paying attention.</p></div>
<div class="ev"><div class="yr">1995 to 1996</div><p>Quantum error correction is invented. Grover publishes quantum search.{cite(3)}</p></div>
<div class="ev"><div class="yr">1999</div><p>First superconducting qubit, the design IBM and Google use.</p></div>
<div class="ev"><div class="yr">2011</div><p>D-Wave sells the first commercial quantum annealer, to Lockheed Martin.</p></div>
<div class="ev big"><div class="yr">2016</div><p>IBM puts a 5-qubit processor on the cloud for anyone to use.</p></div>
<div class="ev big"><div class="yr">2019</div><p>Google claims quantum supremacy with 53 qubits.{cite(6)} IBM disputes the 10,000-year estimate.</p></div>
<div class="ev"><div class="yr">2021</div><p>IonQ, Rigetti and D-Wave reach the stock market through mergers with blank-cheque companies.</p></div>
<div class="ev big"><div class="yr">Dec 2024</div><p>Google's Willow chip shows errors falling as the error-correcting code grows.{cite(9)}</p></div>
<div class="ev"><div class="yr">2025</div><p>Microsoft's Majorana 1{cite(15)}, Amazon's Ocelot, Google's Quantum Echoes{cite(14)}, IBM's Nighthawk and Loon, Quantinuum's Helios. The Nobel Prize in Physics goes to Clarke, Devoret and Martinis for the circuit physics behind superconducting qubits.</p></div>
<div class="ev fut"><div class="yr">2026 onward</div><p>The race to error-corrected machines. See chapter 6.</p></div>
</div></section>''')

    # ---------- 2 simple
    A(f'''<section class="chapter" id="simple"><header><div class="no">2</div><div><h2>Explained without the physics</h2>
<p class="sub">Four pictures that cover what you need to know.</p></div></header>
{X.KEY["simple"]}
<div class="cols">
<figure class="fig rv" style="margin:0">{art.coin_vs_spin()}<figcaption><b>The spinning coin.</b> A bit is a coin lying flat: heads or tails. A qubit is the coin in mid-air, neither until it lands.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art.maze()}<figcaption><b>The maze.</b> A normal computer walks every route in turn. A quantum computer sets up the maze so the wrong routes cancel each other and the right one is left.</figcaption></figure>
<figure class="fig rv" style="margin:0">{art.combo_lock()}<figcaption><b>The combination lock.</b> For some searches the quantum shortcut is a square root: a million tries become about a thousand.{cite(3)}</figcaption></figure>
</div>
<div class="cols" style="margin-top:20px">
<div class="card rv"><h3>What it will be good at</h3><p>Simulating atoms and molecules, which helps design medicines, fertiliser and batteries. Certain optimisation and sampling problems. Cracking some encryption.</p></div>
<div class="card rv"><h3>What it will not do</h3><p>Run your phone, make video faster, or replace the cloud. It will sit in a data centre and be rented by the minute for specific jobs.</p></div>
<div class="card rv"><h3>The thing to remember</h3><p>It is not "fast". It is a different shape of computer. For the right problem it is astronomically faster. For nearly every other problem it is slower and more expensive.</p></div>
</div></section>''')

    # ---------- 3 change & prepare
    A(f'''<section class="chapter" id="change"><header><div class="no">3</div><div><h2>How the world changes, and how to be ready</h2>
<p class="sub">If error-corrected machines arrive, here is what moves first and what you can do now. Most of the preparation is cheap.</p></div></header>
{X.KEY["change"]}
<div class="tl">
<div class="ev fut"><div class="yr">Now to 2030: security</div><p>Encrypted data stolen today can be read later once a large machine exists. Governments and banks are already moving to new encryption standards.{cite(13)} A machine able to break RSA-2048 is estimated to need about a million noisy qubits.{cite(11)}</p></div>
<div class="ev fut"><div class="yr">2028 to 2035: chemistry and materials</div><p>First useful gains are expected in simulating molecules: catalysts, battery materials, drug binding. Resource estimates for industrially relevant problems run to roughly 1,000 to 4,000 logical qubits.{cite(16, 17)}</p></div>
<div class="ev fut"><div class="yr">2030s: industry</div><p>Cheaper fertiliser and fuel chemistry, better batteries and solar materials, faster drug discovery. These come as slow improvements in existing industries, not as new gadgets.</p></div>
<div class="ev fut"><div class="yr">Beyond: unknown</div><p>Honest answer: nobody knows. The biggest uses of past computing were not predicted by its builders.</p></div>
</div>
<div class="cols">
<div class="card rv"><h3>You, at home</h3><p>Keep phones and computers updated, because post-quantum encryption arrives through software updates. Use a password manager and two-step sign-in. No quantum product needs buying.</p></div>
<div class="card rv"><h3>Your small business</h3><p>List data that must stay secret for 10 years or more (contracts, health, design files). Ask your software and cloud suppliers when they will support the NIST post-quantum standards.{cite(13)}</p></div>
<div class="card rv"><h3>Your career</h3><p>Python and linear algebra are the entry points. Qiskit is free and runs real programs on small machines.{cite(21)} Demand is for people who can pair domain skills (chemistry, finance, logistics) with this.</p></div>
<div class="card rv"><h3>Your savings</h3><p>Treat the sector as venture-style risk. Chapter 4 shows what past booms looked like and how often the early leaders failed. Keep any position small enough that losing all of it does not change your life.</p></div>
</div>
{X2.ch3_extra()}
</section>''')

    # ---------- 4 companies
    mult_items = [
        ("Apple, 1997 to 1999", f"from {runs['AAPL']['from']}", runs["AAPL"]["multiple"], "ref"),
        ("Nvidia, 2022 to 2024", f"from {runs['NVDA']['from']}", runs["NVDA"]["multiple"], "ref"),
        ("Bitcoin, 2016 to 2017", f"from {runs['BTC-USD']['from']}", runs["BTC-USD"]["multiple"], "ref"),
        ("IonQ", f"from {runs['IONQ']['from']}", runs["IONQ"]["multiple"], "quantum"),
        ("Quantum Computing Inc", f"from {runs['QUBT']['from']}", runs["QUBT"]["multiple"], "quantum"),
        ("Rigetti", f"from {runs['RGTI']['from']}", runs["RGTI"]["multiple"], "quantum"),
        ("D-Wave", f"from {runs['QBTS']['from']}", runs["QBTS"]["multiple"], "quantum"),
    ]
    A(f'''<section class="chapter" id="companies"><header><div class="no">4</div><div><h2>The companies, and what an explosion looks like</h2>
<p class="sub">Where each started, who it competes with, what has to happen before it makes money, and what past booms did to share prices.</p></div></header>
{X.KEY["companies"]}
<div class="callout r"><b>Information, not advice.</b> This is a plain-language map of a high-risk sector. It is not a recommendation to buy or sell anything. Most small listed companies in new technology lose most of their value or disappear.</div>
<div class="cols">''')
    for c in COMPANIES:
        s = stat[c["t"]]
        A(f'''<article class="card co rv"><h3>{c["name"]}<span>{c["t"]} &middot; {c["kind"]}</span></h3>
<dl><dt>Started at</dt><dd>{fmt_p(s["first"])} ({s["first_date"][:7]}); now {fmt_p(s["last"])}, peak {fmt_p(s["peak"])} in {s["peak_date"][:7]}, {s["pct_from_peak"]:.0f}% from the peak</dd>
<dt>Rivals</dt><dd>{c["rivals"]}</dd>
<dt>Needs for profit</dt><dd>{c["profit"]}</dd>
<dt>Watch</dt><dd>{c["watch"]}</dd>
<dt>How advanced</dt><dd>{c["rank"]}</dd></dl>
<span class="verdict">{c["verdict"]}</span></article>''')
    A(f'''<article class="card co rv"><h3>The big groups<span>IBM, Alphabet, Microsoft, Honeywell, Nvidia</span></h3>
<dl><dt>Position</dt><dd>IBM and Google lead on superconducting hardware and error correction; Honeywell owns most of Quantinuum, the leader in trapped ions; Microsoft is betting on a different qubit; Nvidia supplies the classical chips that decode errors.</dd>
<dt>Why they matter</dt><dd>Quantum is a small share of their value. Milestones move their shares by a few percent, not several-fold.</dd>
<dt>Use</dt><dd>A lower-risk way to hold exposure to the theme, at the cost of a much smaller upside if it works.</dd></dl>
<span class="verdict">Most advanced: Google and Quantinuum on error correction; IBM on the engineering roadmap</span></article>
</div>
<h3 style="margin-top:40px">Share prices since listing</h3>
<p>Weekly closes to <span id="lastdate"></span>, adjusted for splits. Histories of IonQ, Rigetti and D-Wave begin with the blank-cheque company they merged with.</p>
<div class="ctrl" id="tickers" role="group" aria-label="Companies"></div>
<div class="ctrl" role="group" aria-label="Chart options">
<button data-mode="growth" aria-pressed="true">Growth, 100 = start</button><button data-mode="price" aria-pressed="false">Price (US$)</button>
<button data-range="all" aria-pressed="false">Full history</button><button data-range="2021" aria-pressed="false">Since 2021</button>
<button data-range="2024" aria-pressed="true">Since 2024</button><button data-range="1y" aria-pressed="false">Last year</button></div>
<figure class="fig"><svg id="chart" viewBox="0 0 900 440" role="img" aria-label="Weekly share prices"></svg><div id="tip">Move across the chart to read values.</div></figure>
<h3 style="margin-top:36px">What an explosion looks like</h3>
<p>The biggest rises from a low to a later high within two years. The famous booms are in teal and violet; the quantum pure-plays did the same in 2024 and 2025. After the peak each fell sharply, and that is the other half of the picture.</p>
<figure class="fig">{charts.multiples(mult_items)}<figcaption>Log scale. Computed from weekly closes. Prices are adjusted for splits, so Apple's low looks tiny. Past rises do not repeat on schedule.</figcaption></figure>
<h3 style="margin-top:36px">The ladder: what has to happen before profit</h3>
<figure class="fig">{charts.ladder(LADDER, 3)}<figcaption>Each step has historically moved share prices in this sector: the early steps tend to be priced in before they are reached, and delays are punished hard. The field has reached step four in small experiments. Profits need step seven.</figcaption></figure>
<div class="cols">
<div class="card rv"><h3>Signs an explosion is starting</h3><ul><li>A company shows error-corrected programs long enough to be useful.</li><li>A named customer pays for results, not for a trial.</li><li>Revenue grows faster than the cash it burns.</li><li>A big group buys a small one at a clear premium.</li></ul></div>
<div class="card rv"><h3>Signs it is getting ahead of itself</h3><ul><li>Prices rise several-fold with no new technical result.</li><li>The company sells new shares into every rally.</li><li>Targets keep moving back a year at a time.</li><li>Claims rest on a result no one else has reproduced.</li></ul></div>
</div>
{X2.ch4_extra(idx_svg)}
</section>''')

    # ---------- 5 hurdles and power
    A(f'''<section class="chapter" id="hurdles"><header><div class="no">5</div><div><h2>What stands in the way, and the power bill</h2>
<p class="sub">The size of the gap, the engineering problems, and how much electricity a machine uses.</p></div></header>
{X.KEY["hurdles"]}
<figure class="fig">{charts.line_gap()}<figcaption>Log scale. Practical chips today have 100 to 150 usable qubits. Breaking RSA-2048 is estimated to need about a million noisy qubits{cite(11)}, down from 20 million in 2019.{cite(12)}</figcaption></figure>
<div class="cols">
<div class="card rv"><h3>Error rates</h3><p>About 1 error in 100 to 1,000 steps today, against roughly 1 in a trillion needed.</p></div>
<div class="card rv"><h3>Overhead</h3><p>Hundreds to thousands of physical qubits per logical qubit with the surface code{cite(5)}; IBM's newer code design aims much lower.{cite(10)}</p></div>
<div class="card rv"><h3>Wiring and cooling</h3><p>A fridge holds thousands of wires. A million qubits need electronics inside the cold or links between many fridges.</p></div>
<div class="card rv"><h3>Real-time decoding</h3><p>A classical computer must read error signals and respond within microseconds, continuously.</p></div>
<div class="card rv"><h3>Few algorithms</h3><p>Proven large speed-ups exist for a short list of problems. Loading big datasets in is slow.</p></div>
<div class="card rv"><h3>Money and talent</h3><p>Most listed pure-plays spend more than they earn, and the skilled workforce is small.</p></div>
</div>
<h3 style="margin-top:40px">Power</h3>
<p>One superconducting quantum computer draws about 15 to 30 kW, nearly all for cooling and control electronics. The chip itself uses almost nothing. Google put its 2019 apparatus at 26 kW in the worst case.{cite(18)}</p>
<figure class="fig">{charts.bars_h([("Human brain", 20), ("Laptop", 50), ("One AI server (8 GPUs)", 10200), ("Quantum computer, whole system", 25000), ("AI server rack", 120000), ("Summit supercomputer", 13e6), ("Frontier supercomputer", 22.7e6), ("Large AI data centre", 100e6)], lambda v: (f"{v / 1e6:g} MW" if v >= 1e6 else f"{v / 1e3:g} kW" if v >= 1e3 else f"{v:g} W"), highlight="Quantum computer, whole system", label="Power use in watts, log scale")}
<figcaption>Log scale. Approximate: Google 2019 supplement, Nvidia DGX H100 rating (10.2 kW), Top500 lists.</figcaption></figure>
<div class="callout"><b>Low power is not the same as efficient.</b> A quantum machine is cheap to run per hour and is the wrong tool for nearly all jobs. For the right job it could replace weeks of supercomputer time. A million-qubit system multiplies the cooling and control load, and published estimates of that draw vary widely, because none exists to measure.</div>
</section>''')

    # ---------- 6 outlook
    A('''<section class="chapter" id="outlook"><header><div class="no">6</div><div><h2>The next three years, in plain language</h2>
<p class="sub">The author's best estimate to October 2029. These are judgements with stated assumptions, not predictions and not advice.</p></div></header>''')
    A(X.KEY["outlook"])
    A(f'''<figure class="fig">{charts.roadmap()}<figcaption>Logical qubits by year, log scale. Hollow points are company targets, the solid point is the best result shown so far. Sources: IBM{cite(19)}, Quantinuum{cite(20)}, Bluvstein et al.{cite(8)}</figcaption></figure>
<h3>What I expect to happen to the technology</h3>
<div class="cols">
<div class="card rv"><h3>Likely (about 70%)</h3><p>Google, IBM and Quantinuum keep showing steady gains: more logical qubits, longer programs, lower error. Neutral-atom machines catch up on size. No machine runs a commercially decisive program yet.</p></div>
<div class="card rv"><h3>Roughly even (about 50%)</h3><p>A first useful result in chemistry or materials on error-corrected hardware appears by late 2029, but narrow and expensive.</p></div>
<div class="card rv"><h3>Unlikely (under 25%)</h3><p>A machine with a couple of hundred long-running logical qubits is running on the 2029 schedule. I expect most dates to slip 12 to 24 months.</p></div>
</div>
<h3 style="margin-top:40px">What it could mean for the four pure-play shares</h3>
<p>Each chart shows the last two years, then the spread of outcomes under three stories. The dashed lines are the median in each story; the shaded band is where the middle 80% of all outcomes fall once the stories are mixed by my probabilities. Volatility comes from each stock's own last two years, which is very high.</p>''')
    A(X2.ch6_interactive(sims, COMPANIES, fmt_p))
    A(f'''<h3 style="margin-top:40px">My plain-language view</h3>
<div class="cols">
<div class="card rv"><h3>The technology will probably get there. The share prices have already assumed it.</h3>
<p>I think error-corrected quantum computers are likely to be built, and that Google, IBM and Quantinuum are furthest along. But the four listed pure-plays were valued in 2024 and 2025 as though the finish line were close. The models above put the chance each ends the three years below today's price at {min(s["prob_below_start"] for s in sims.values()):.0%} to {max(s["prob_below_start"] for s in sims.values()):.0%}.</p></div>
<div class="card rv"><h3>Expect a shakeout.</h3>
<p>New technology booms usually leave a few giants and many casualties. Of the four, I would expect at least one to be bought cheaply, merged or to run short of cash by 2029, and the survivors to have sold a lot of new shares on the way, which weakens the gain for people already holding.</p></div>
<div class="card rv"><h3>If it goes right, who gains most?</h3>
<p>The leaders with real hardware gain, but a few-fold rise is a normal good outcome, not a 50-fold one: the rises already shown ({runs["RGTI"]["multiple"]:.0f}x for Rigetti, {runs["QBTS"]["multiple"]:.0f}x for D-Wave) borrowed from the future. The biggest winners may be companies not listed yet, or suppliers of lasers, cryogenics and chips.</p></div>
<div class="card rv"><h3>If you had been there in the 1990s</h3>
<p>Buying Apple in 1997 or Nvidia in 2022 worked because the company later earned vast profits. The question to ask each quantum company is the same: when does this earn real profit, and how many more shares must it sell first? Until the answer is clear, think of these as lottery tickets with a good story, and size them that way.</p></div>
</div>
<div class="callout t"><b>What would change my mind.</b> A company showing hundreds of long-running logical qubits ahead of schedule, a named customer paying a large recurring bill for useful results, or a second team independently reproducing the topological-qubit claim.</div>
</section>''')

    # ---------- footer
    A(X.disclosures(AS_OF))
    A(X.research())
    A(X.rail())
    refs = "".join(f'<li id="r{n}">[{n}] <a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for n, t, u in REFS)
    A(f'''<footer><h3 style="font-size:1.4rem">Sources, method and limits</h3>
<ol class="refs" style="list-style:none;padding:0">{refs}</ol>
<ul><li><b>Share prices:</b> Yahoo Finance weekly closes, split and dividend adjusted, retrieved {AS_OF}.</li>
<li><b>Scenarios:</b> three stories per company, with yearly drift and probability chosen by the author (typical yearly price change, from -55% in the bear stories to +60% in the bull stories). Volatility is the annualised standard deviation of the last 104 weekly returns, scaled to 75% for the forward view. 20,000 simulated paths per company. Change the assumptions and the range moves; it is a way to see what the assumptions imply, not a forecast.</li>
<li><b>Limits:</b> the 2026 hardware news was thin in the sources available. Several 2025 items are company claims. Qubit counts compare poorly across technologies. Company roadmaps change.</li>
<li><b>Not advice:</b> information only, and not a personal recommendation. Solas33 holds no position in any company named and carries no advertising.</li></ul>

<p style="margin-top:20px">Built by Solas33, {AS_OF}. Page generated by a Python build (frontier/): prices, charts, illustrations and scenario simulation are produced from code.</p></footer>''')

    return {"title": TITLE, "nav": nav, "body": "\n".join(body), "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
