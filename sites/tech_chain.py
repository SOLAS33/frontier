"""Technical depth for Frontier Chain: numbers, building blocks, evidence and a short glossary. Same shape as tech_blocks.py."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

CHAIN_REFS = [
    (10, "Ethereum Foundation. Ethereum documentation: scaling and rollups.", "https://ethereum.org/en/developers/docs/scaling/"),
    (11, "Ethereum Foundation. Zero-knowledge proofs.", "https://ethereum.org/en/zero-knowledge-proofs/"),
    (12, "rwa.xyz. Real-world asset tokenisation dashboard.", "https://app.rwa.xyz/"),
    (13, "European Securities and Markets Authority. DLT Pilot Regime.", "https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation"),
]


def chain_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Fingerprint (hash)", "256 bits, in practice a 64-character code", "Change one letter in a record and the code changes completely. That is what makes tampering visible"],
        ["Ethereum block time", "12 seconds", "A new batch of records is added about every twelve seconds"],
        ["Ethereum final settlement", "About 13 minutes", "The time before a transaction cannot be reversed without destroying a large amount of staked money"],
        ["Throughput on the base layer", "Roughly 15 to 30 transactions a second", "Visa's network is built for thousands. Volume has to move elsewhere" + cite(10)],
        ["Fees on rollups", "Cents or less", "Rollups batch many transactions into one posting on the base layer" + cite(10)],
        ["A zero-knowledge proof", "A few hundred bytes, checked in milliseconds", "Checking a proof is much cheaper than redoing the computation it covers" + cite(11)],
        ["Tokenised treasuries", "Several billion dollars by late 2025", "Small beside the trillions in the underlying market" + cite(12)],
    ])
    kinds = _table(["Building block", "What it does", "Examples", "Status"], [
        ["Public blockchain", "A ledger anyone can read and add to by the rules, with no owner", "Ethereum, Solana, Bitcoin", "Running for years, with large value held"],
        ["Smart contract", "A program on the ledger that moves assets when its conditions are met", "Lending pools, exchanges, token issuance", "Works. Bugs cost billions"],
        ["Rollup (layer 2)", "Runs transactions off the main chain and posts a summary, so fees are cheaper", "Base, Arbitrum, Optimism, zkSync, Starknet" + cite(10), "Carries most Ethereum activity now"],
        ["Zero-knowledge proof", "Proves a statement is true without revealing the data behind it", "zk-rollups, private payments, identity checks" + cite(11), "Working in production. Costly to compute"],
        ["Private or permissioned ledger", "A shared ledger run by a group of known firms", "Hyperledger Fabric, Canton, Broadridge DLR", "Used by banks. Several earlier consortia closed"],
        ["Oracle", "Feeds outside data, such as a price, to a contract", "Chainlink, Pyth", "A weak point if the data is wrong"],
        ["Tokenised asset", "A legal claim on a fund, bond or deposit recorded as a token", "BlackRock BUIDL, Franklin Templeton BENJI, tokenised bank deposits", "Growing from a small base"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["Smart contracts on a public chain", "Ethereum, 2015", _tag("ok"), "The base for most tokenisation"],
        ["A major bond issued on a public chain", "European Investment Bank, a 100 million euro digital bond, 2021", _tag("ok"), "A pilot-scale issue that settled on Ethereum"],
        ["A tokenised money-market fund open to many investors", "BlackRock BUIDL, from March 2024", _tag("ok"), "Passed two billion dollars in 2025"],
        ["A legal regime for tokenised securities trading", "EU DLT Pilot Regime, from March 2023" + cite(13), _tag("ok"), "Very few venues have used it so far"],
        ["Zero-knowledge rollups carrying real value", "Several networks, 2020 on", _tag("ok"), "Billions of dollars of value held"],
        ["Shipping consortium on a blockchain", "TradeLens (Maersk and IBM), shut 2023", _tag("dis"), "Closed because rivals would not join one firm's platform"],
        ["Replacing a stock exchange's clearing system with a blockchain", "ASX in Australia, scrapped 2022", _tag("dis"), "About 250 million Australian dollars written off"],
        ["Same-day settlement of most securities on a shared ledger", "Banks and exchanges, announced for the late 2020s", _tag("tgt"), "Requires rules, buyers and cash on the ledger"],
    ])
    gl = _gloss([
        ("Hash", "A short fixed-length code made from data. The same data always gives the same code, and a different file gives a different one."),
        ("Smart contract", "A program stored on a ledger that runs when the rules it holds are met."),
        ("Token", "A record on a ledger that stands for something, such as a coin, a fund share or a ticket."),
        ("Tokenisation", "Putting a claim on a real asset, such as a bond, onto a ledger as a token."),
        ("Rollup", "A network that runs transactions off the main chain and posts proof of the results to it."),
        ("Zero-knowledge proof", "A way to show a statement is true without showing the data that makes it true."),
        ("Atomic settlement", "Two sides of a trade, the asset and the payment, swap at the same instant or not at all."),
        ("Custody", "Safekeeping of the keys that control an asset. Whoever holds the keys controls the asset."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A blockchain is a list of records in batches. Each batch carries the fingerprint of the batch before it, so changing an old record would change every fingerprint after it. Many computers keep copies and agree on the next batch by a fixed rule, so no single party can rewrite the list. A smart contract is a program that sits on that list and moves tokens when its rules are met.{cite(10)} A zero-knowledge proof lets one party show that a computation was done correctly without anyone else redoing it, which is what lets a rollup post a short proof for thousands of transactions.{cite(11)}</p>
{nums}
<p class="cap wide">Rounded, from the cited sources. Speeds and fees change as the networks are upgraded.</p>
<h3 class="wide" id="s-types" data-nav="Blocks" style="margin-top:36px">The building blocks</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
