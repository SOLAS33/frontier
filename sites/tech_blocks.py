"""Technical depth for the Frontier sites: numbers, mechanisms, evidence tables and short glossaries.

Each *_html(cite) returns a block that sits in chapter 1 before the history. Each *_REFS list extends the site's references.
Numbers are rounded and from public sources; targets and company claims are labelled as such in the tables.
"""
from __future__ import annotations


def _table(head, rows, right=()):
    th = "".join(f'<th class="n">{h}</th>' if i in right else f"<th>{h}</th>" for i, h in enumerate(head))
    body = "".join("<tr>" + "".join(f'<td class="n">{c}</td>' if i in right else f"<td>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="scroll wide"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _gloss(items):
    return ('<div class="cols c4 wide">' + "".join(f'<div class="card rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + "</div>")


def _tag(kind):
    names = {"ok": "Shown", "dis": "Contested", "tgt": "Target"}
    return f'<span class="tag {kind}">{names[kind]}</span>'


# ---------------------------------------------------------------- Coin
COIN_REFS = [
    (13, "Poon and Dryja (2016). The Bitcoin Lightning Network: scalable off-chain instant payments.", "https://lightning.network/lightning-network-paper.pdf"),
    (14, "Buterin, V. (2014). Ethereum: a next-generation smart contract and decentralized application platform (white paper).", "https://ethereum.org/en/whitepaper/"),
    (15, "Ethereum Improvement Proposal 1559: fee market change.", "https://eips.ethereum.org/EIPS/eip-1559"),
    (16, "Narayanan, Bonneau, Felten, Miller, Goldfeder. Bitcoin and cryptocurrency technologies (free textbook, Princeton).", "https://bitcoinbook.cs.princeton.edu/"),
    (17, "Ethereum.org. The Merge: the move from proof of work to proof of stake.", "https://ethereum.org/en/roadmap/merge/"),
]


def coin_html(cite):
    nums = _table(["Part", "Bitcoin", "Ethereum"], [
        ["Who writes the next page", "Miners, by finding a hash below a target (proof of work)", "Validators who have locked up 32 ETH or more, picked at random (proof of stake)"],
        ["Page time", "About 10 minutes, kept steady by retargeting difficulty every 2,016 blocks", "12 seconds"],
        ["Final", "Convention is six pages deep, about an hour", "About 13 minutes (two epochs)"],
        ["Throughput on the main chain", "Roughly 3 to 7 transactions a second", "Roughly 15 to 30 transactions a second"],
        ["Supply rule", "21 million coins. The reward halves every 210,000 blocks (about four years)", "No hard cap. Part of every fee is burned (EIP-1559)" + cite(15)],
        ["Signatures", "ECDSA and Schnorr on the secp256k1 curve", "ECDSA on secp256k1, plus BLS for validators"],
        ["Programmable", "Limited scripting", "Full programs, called smart contracts" + cite(14)],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Working peer-to-peer electronic cash without a trusted party", "Nakamoto, 2008 to 2009" + cite(1), _tag("ok"), "Has run without a stoppage since January 2009"],
        ["Programmable money on a shared ledger", "Ethereum, 2015" + cite(14), _tag("ok"), "Most tokens, stablecoins and decentralised finance run here"],
        ["Cut energy use by over 99% by changing the consensus rule", "Ethereum Merge, Sept 2022" + cite(17), _tag("ok"), "Showed a major network can change its core without stopping"],
        ["Payment channels to move small payments off the main chain", "Lightning Network, 2018 on" + cite(13), _tag("ok"), "Works, but liquidity and routing limit its size"],
        ["Fee burn to tie fees to usage", "EIP-1559, Aug 2021" + cite(15), _tag("ok"), "Made fees more predictable. Did not lower them"],
        ["Rollups that settle thousands of transactions in one proof", "Optimistic and zero-knowledge rollups, 2021 on", _tag("ok"), "Lower fees, but a few operators sequence most of them"],
        ["Dollar tokens that hold their value without reserves", "Terra, 2020 to 2022", _tag("dis"), "Collapsed in May 2022 and took about $40 billion with it. Fiat-backed tokens survived"],
        ["Quantum-safe signatures on Bitcoin", "Proposals only", _tag("tgt"), "See chapter 3"],
    ])
    gl = _gloss([
        ("Hash", "A fixed-size fingerprint of any data. Change one bit and the fingerprint changes completely. SHA-256 is the one Bitcoin uses."),
        ("UTXO", "Unspent transaction output. Bitcoin has no accounts. It tracks pieces of coin that have not yet been spent, and a payment consumes some and creates new ones."),
        ("Mempool", "The waiting room for payments that have been broadcast but not yet written into a block."),
        ("Finality", "The point at which a payment can no longer be reversed in practice. Probabilistic in Bitcoin, explicit in Ethereum."),
        ("Gas", "The fee for computing on Ethereum, priced per step. Complicated programs cost more."),
        ("Slashing", "A penalty that destroys part of a validator's locked coins if it signs two conflicting pages."),
        ("Rollup", "A second chain that batches many transactions and posts a compact proof or record to the main chain."),
        ("MEV", "Maximal extractable value: profit a block builder can make by choosing the order of transactions."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A payment is a signed instruction. Your wallet signs it with a private key and broadcasts it. Nodes check the signature and that the coins exist and have not been spent, then pass it on. A miner collects waiting payments into a block of about four megabytes and tries trillions of hashes a second to find one below a target. When it succeeds the block is published, every node checks it, and the payments in it are final once enough blocks have been built on top.{cite(16)}</p>
<p>The target adjusts so that a block is found every ten minutes however much computing power joins. That is why total hash rate, now hundreds of exahashes a second, is a measure of how much it would cost to rewrite history.</p>
{nums}
<p class="cap wide">Rounded, from the protocol rules and public network data. The textbook in the references walks through each part in detail.</p>
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}
<div class="callout t wide"><b>Beyond money.</b> The same ledger technology is being tested for tokenised funds, bonds and bank deposits, and for proofs that let one party verify another's work without seeing the data. That is a broader subject than coin prices, and it will have its own Frontier site, Chain.</div>'''


# ---------------------------------------------------------------- Mind
MIND_REFS = [
    (12, "Krizhevsky, Sutskever, Hinton (2012). ImageNet classification with deep convolutional neural networks.", "https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html"),
    (13, "He et al. (2015). Deep residual learning for image recognition.", "https://arxiv.org/abs/1512.03385"),
    (14, "Devlin et al. (2018). BERT: pre-training of deep bidirectional transformers.", "https://arxiv.org/abs/1810.04805"),
    (15, "Brown et al. (2020). Language models are few-shot learners (GPT-3).", "https://arxiv.org/abs/2005.14165"),
    (16, "Ouyang et al. (2022). Training language models to follow instructions with human feedback.", "https://arxiv.org/abs/2203.02155"),
    (17, "Dao et al. (2022). FlashAttention: fast and memory-efficient exact attention with IO-awareness.", "https://arxiv.org/abs/2205.14135"),
    (18, "Fedus, Zoph, Shazeer (2021). Switch Transformers: scaling to trillion parameter models with simple and efficient sparsity.", "https://arxiv.org/abs/2101.03961"),
]


def mind_html(cite):
    nums = _table(["Quantity", "Rule of thumb", "Worked example"], [
        ["Training compute", "About 6 floating-point operations per parameter per training token" + cite(2), "A 175-billion-parameter model on 300 billion tokens: about 3 x 10^23 operations" + cite(15)],
        ["Best data per parameter", "Roughly 20 training tokens per parameter for a fixed compute budget" + cite(3), "A 70-billion-parameter model wants about 1.4 trillion tokens"],
        ["Memory to run a model", "Parameters times bytes per number", "70 billion at 16 bits: about 140 GB. At 4 bits: about 35 GB"],
        ["Speed of answering", "Limited by memory bandwidth, not arithmetic", "An accelerator moving 3 to 8 terabytes a second reads a 140 GB model 20 to 60 times a second"],
        ["Attention cost", "Grows with the square of the text length" + cite(1), "Doubling the context quadruples that part, which is why long inputs cost more"],
        ["Compute trend", "Training compute of leading models has grown about 4x a year" + cite(4), "Roughly a ten-million-fold rise in 15 years"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["A deep network wins an image contest by a wide margin", "Krizhevsky et al., 2012" + cite(12), _tag("ok"), "Trained on two graphics cards. Started the current era"],
        ["Very deep networks that train reliably", "He et al., 2015" + cite(13), _tag("ok"), "Residual connections are in almost every model since"],
        ["The transformer replaces recurrent networks", "Vaswani et al., 2017" + cite(1), _tag("ok"), "Parallel across the text, so it uses chips well"],
        ["Pre-training then fine-tuning as the standard recipe", "Devlin et al., 2018" + cite(14), _tag("ok"), "One model adapted to many tasks"],
        ["A model that does new tasks from a few examples in the prompt", "Brown et al., 2020" + cite(15), _tag("ok"), "175 billion parameters. The scaling story becomes concrete"],
        ["Models that follow instructions and are tuned on human feedback", "Ouyang et al., 2022" + cite(16), _tag("ok"), "Made chat products usable. Also the source of many failure modes"],
        ["Attention that fits modern memory hierarchies", "Dao et al., 2022" + cite(17), _tag("ok"), "A software change that made long inputs several times cheaper"],
        ["Sparse models that use a fraction of their weights per token", "Fedus et al., 2021" + cite(18), _tag("ok"), "More parameters at similar cost. Harder to serve"],
        ["Systems that act reliably over hours of work", "Company roadmaps", _tag("tgt"), "Short demonstrations exist. Reliable long tasks are not shown at scale"],
    ])
    gl = _gloss([
        ("Parameter", "One adjustable number inside the model. Today's large models have tens to hundreds of billions."),
        ("Token", "A piece of text, roughly three quarters of a word, which is what the model reads and writes."),
        ("FLOP", "One floating-point operation, a single multiplication or addition. Training is counted in total FLOPs, speed in FLOPs a second."),
        ("HBM", "High-bandwidth memory stacked next to the chip. Its supply is a bottleneck for AI accelerators."),
        ("Inference", "Using a trained model to answer. It is the larger bill for a popular product."),
        ("Fine-tuning", "Further training of a model on a narrower set of examples."),
        ("RLHF", "Reinforcement learning from human feedback: people rank answers and the model is nudged toward the preferred ones."),
        ("Mixture of experts", "A design where each token is sent to a few specialist sub-networks, so only part of the model runs."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A language model reads text as numbers and, at each layer, lets every position look at every other. Attention does this by comparing a query for each position with a key from every other position and using the result to weight their values.{cite(1)} The model is trained by repeatedly asking it to predict the next token and nudging its parameters to be less wrong, using gradient descent on thousands of chips at once. Nothing else in the loop is understood. That the model improves smoothly with more parameters, data and compute is an empirical finding, not a theorem.{cite(2)}</p>
{nums}
<p class="cap wide">Rule-of-thumb figures from the cited papers and public chip specifications. Real systems differ by large factors.</p>
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''


# ---------------------------------------------------------------- Atom
ATOM_REFS = [
    (10, "World Nuclear Association. Nuclear fuel cycle information: uranium enrichment.", "https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment"),
    (11, "World Nuclear Association. Information library: nuclear power reactors.", "https://world-nuclear.org/information-library/nuclear-fuel-cycle/nuclear-power-reactors/nuclear-power-reactors"),
    (12, "US Nuclear Regulatory Commission. Reactor concepts: how nuclear power plants work.", "https://www.nrc.gov/reactors/power.html"),
]


def atom_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Energy per fission", "About 200 MeV, or 3.2 x 10^-11 joules", "A kilogram fully fissioned releases about as much heat as 2,500 tonnes of coal"],
        ["Natural uranium", "0.71% uranium-235", "The rest is uranium-238, which does not sustain a chain reaction"],
        ["Fuel enrichment", "3 to 5% for ordinary reactors. 5 to 20% for HALEU" + cite(5), "Most advanced designs need the higher grade, and little is made outside Russia"],
        ["Neutron balance (k)", "Exactly 1 in steady operation", "Above 1 the power rises. About 0.65% of neutrons arrive delayed, which gives operators seconds, not microseconds, to react"],
        ["Thermal efficiency", "About 33% for water reactors. 40% or more for high-temperature designs", "A 1,000 MW electric plant gives off about 2,000 MW of heat to the sea or a cooling tower"],
        ["Capacity factor", "Over 90% in the US", "The highest of any source, because it runs almost all the time"],
        ["Cost of new build", "Lazard's recent range: about $140 to $220 per MWh" + cite(6), "Mostly the cost of money over a long build, not the fuel"],
    ], right=())
    types = _table(["Design", "Coolant and moderator", "Output temperature", "Status"], [
        ["Pressurised water reactor", "Water, water", "About 320 C", "Most of the fleet. Westinghouse, Framatome, Chinese and Korean variants"],
        ["Boiling water reactor", "Water, water", "About 290 C", "A quarter of the fleet. GE-Hitachi BWRX-300 is the small version"],
        ["Heavy water (CANDU)", "Heavy water, heavy water", "About 310 C", "Canada, India, Romania. Runs on unenriched uranium"],
        ["High-temperature gas", "Helium, graphite", "700 to 950 C", "A few operating, including in China. X-energy's Xe-100"],
        ["Sodium fast reactor", "Liquid sodium, none", "About 500 C", "Few built. TerraPower Natrium and Oklo's Aurora are of this family"],
        ["Molten salt", "Molten salt, graphite or none", "700 C or more", "Experimental. Several start-ups, no commercial plant"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["First controlled chain reaction", "Chicago Pile-1, December 1942", _tag("ok"), "Fermi's team, under a squash court"],
        ["First electricity from fission", "EBR-I, Idaho, 1951", _tag("ok"), "Four light bulbs"],
        ["A commercial-scale reactor feeding a grid", "Obninsk 1954, Shippingport 1957", _tag("ok"), "The start of the civil fleet"],
        ["About 440 reactors operating worldwide", "IAEA, 2025" + cite(1), _tag("ok"), "Roughly 9% of the world's electricity"],
        ["First new US reactors in a generation", "Vogtle 3 and 4, 2023 to 2024", _tag("ok"), "Late and about twice the original cost"],
        ["A small modular reactor design approved by the US regulator", "NuScale, 2023 and 2025" + cite(4), _tag("ok"), "No plant ordered and built. Its largest project was cancelled in 2023"],
        ["A final repository for spent fuel", "Onkalo, Finland" + cite(9), _tag("tgt"), "Trial operation expected. The first of its kind"],
        ["Factory-built reactors delivering power in the West", "Several developers, late 2020s", _tag("tgt"), "Dates have slipped before"],
    ])
    gl = _gloss([
        ("Moderator", "A material that slows neutrons so that they are more likely to split uranium-235. Water, heavy water and graphite are used."),
        ("Enrichment", "Raising the share of uranium-235 by spinning gaseous uranium hexafluoride in centrifuges."),
        ("SWU", "Separative work unit: the measure of the effort of enrichment. Price is quoted per SWU."),
        ("HALEU", "High-assay low-enriched uranium, between 5% and 20% U-235, for advanced designs."),
        ("Burnup", "How much heat a tonne of fuel gives before it is replaced, in gigawatt-days per tonne."),
        ("Capacity factor", "Actual output divided by what the plant would give running flat out."),
        ("Containment", "The strong building around the reactor that holds in any release."),
        ("Passive safety", "Cooling that works by gravity or natural convection with no pumps or power."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>Uranium-235 splits when it absorbs a neutron, releasing heat and two or three more neutrons. If, on average, exactly one of those goes on to split another atom, the reaction holds steady. Control rods that absorb neutrons, and the moderator that slows them, hold that balance.{cite(12)} The coolant carries the heat out to make steam.{cite(11)}</p>
{nums}
<p class="cap wide">Rounded, from the cited sources. Costs vary a great deal by country and by project.</p>
<h3 class="wide" id="s-types" data-nav="Designs" style="margin-top:36px">The main reactor designs</h3>
{types}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''


# ---------------------------------------------------------------- Cell
CELL_REFS = [
    (10, "Padhi, Nanjundaswamy, Goodenough (1997). Phospho-olivines as positive-electrode materials for rechargeable lithium batteries.", "https://doi.org/10.1149/1.1837571"),
    (11, "Goodenough, J. and Park, K. (2013). The Li-ion rechargeable battery: a perspective. J. Am. Chem. Soc.", "https://doi.org/10.1021/ja3091438"),
]


def cell_html(cite):
    chem = _table(["Chemistry", "Cell voltage", "Energy per kilogram (cell)", "Cycles to 80%", "Where it is used"], [
        ["Lead-acid", "2.0 V", "30 to 50 Wh", "300 to 800", "Starter batteries, backup power"],
        ["Lithium iron phosphate (LFP)" + cite(10), "3.2 V", "160 to 200 Wh", "3,000 to 6,000", "Grid storage, many cars, buses"],
        ["Nickel manganese cobalt (NMC)" + cite(11), "3.6 to 3.7 V", "230 to 300 Wh", "1,000 to 2,000", "Long-range cars, phones, tools"],
        ["Sodium-ion", "About 3.0 V", "100 to 160 Wh", "2,000 to 4,000 claimed", "Entering production, mainly stationary and cheap cars"],
        ["Solid-state lithium metal", "3.7 V or higher", "Target above 400 Wh", "Not shown at volume", "Developer targets, not products"],
        ["Zinc, iron-air and flow (long duration)", "1.0 to 1.6 V", "Low, but cheap per kWh", "Thousands, in some cases unlimited", "Storing 8 hours to days on the grid"],
    ])
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Energy of a cell", "Volts times amp-hours: a 3.7 V, 5 Ah cell holds 18.5 Wh", "A car pack of 60 kWh is about 3,000 such cells' worth of energy"],
        ["Round-trip efficiency", "85 to 95% at the cell, about 85% for a grid system", "Between 5% and 15% of the energy is lost as heat in each cycle"],
        ["Charge rate", "Quoted in C. 1C empties or fills a cell in an hour. 2C in half an hour", "Faster charging costs life and creates heat"],
        ["Pack price", "About $115 per kWh in 2024, against about $1,400 in 2010" + cite(3), "A 60 kWh pack costs roughly $7,000 today, against $84,000 in 2010"],
        ["Heat risk", "Thermal runaway can begin around 150 to 200 C in NMC and later in LFP", "Why chemistry, spacing and cooling matter, and why LFP is favoured for stationary storage"],
        ["Cost of storing a kWh", "Pack price divided by lifetime cycles: $115 over 4,000 cycles is under 3 cents", "That is why long-life chemistries win on the grid"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Layered oxide cathode for lithium cells", "Goodenough, 1980" + cite(11), _tag("ok"), "The base of the lithium-ion battery"],
        ["First commercial lithium-ion cell", "Sony, 1991" + cite(4), _tag("ok"), "Camcorders first, then phones and laptops"],
        ["Iron phosphate cathode", "Padhi, Goodenough et al., 1997" + cite(10), _tag("ok"), "Cheap and safe. The workhorse of storage today"],
        ["Pack prices below $150 per kWh", "Industry survey, 2020 on" + cite(3), _tag("ok"), "The point where electric cars matched petrol on price in some markets"],
        ["Grid battery capacity doubling in a year", "IEA, 2023 to 2024" + cite(2), _tag("ok"), "Led by California, Texas, China and Australia"],
        ["Sodium-ion cells in production", "Chinese makers, 2023 to 2025", _tag("ok"), "Lower energy density, no lithium"],
        ["Solid-state cells that pass automotive tests at volume", "Several developers", _tag("tgt"), "Samples shown. Third-party data is limited"],
        ["Long-duration storage cheaper than gas peakers", "Several start-ups", _tag("tgt"), "Pilots, not a market yet"],
    ])
    gl = _gloss([
        ("Anode and cathode", "The two electrodes. In a lithium-ion cell the anode is usually graphite and the cathode a metal oxide or iron phosphate."),
        ("Electrolyte", "The medium that carries lithium ions between electrodes. Liquid today, solid in solid-state designs."),
        ("SEI", "Solid electrolyte interphase: a film that forms on the anode in the first cycles. It protects the cell and slowly consumes lithium."),
        ("C-rate", "Charge or discharge speed relative to capacity. 1C is a full cycle in one hour."),
        ("State of health", "Remaining capacity compared with new. A cell is often retired at 70 to 80%."),
        ("Thermal runaway", "A self-heating chain reaction in a damaged or overheated cell that can spread to neighbours."),
        ("Round-trip efficiency", "Energy out divided by energy in across a full charge and discharge."),
        ("Duration", "How many hours a battery can deliver its rated power. Most grid lithium systems are 2 to 4 hours."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>When a lithium-ion cell charges, lithium ions leave the cathode, cross the electrolyte and sit between the layers of graphite in the anode while electrons are pushed round the outside circuit. On discharge the ions go back. The voltage is set by the chemistry of the two electrodes. The energy is that voltage times the charge stored. Almost every limit in a battery, from life to charging speed to fire risk, comes from what happens at the surface of those electrodes.{cite(11)}</p>
<h3 class="wide" id="s-chemtable" data-nav="Compare" style="margin-top:30px">Chemistries compared</h3>
{chem}
<p class="cap wide">Typical cell-level ranges from public sources. Pack-level energy is lower because of casings, cooling and wiring.</p>
<h3 class="wide" id="s-nums" data-nav="Numbers" style="margin-top:36px">The numbers that decide it</h3>
{nums}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
