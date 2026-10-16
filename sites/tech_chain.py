"""Technical depth for Frontier Chain: numbers, building blocks, evidence and a short glossary. Same shape as tech_blocks.py.
Every number here was checked against the cited source on 16 October 2026. Where sources disagree the text says so."""
from __future__ import annotations

from sites.tech_blocks import _gloss, _table, _tag

CHAIN_REFS = [
    (10, "Ethereum Foundation. Ethereum documentation: scaling and rollups.", "https://ethereum.org/en/developers/docs/scaling/"),
    (11, "Ethereum Foundation. Zero-knowledge proofs.", "https://ethereum.org/en/zero-knowledge-proofs/"),
    (12, "rwa.xyz. Real-world asset tokenisation dashboard.", "https://app.rwa.xyz/"),
    (13, "ESMA. Markets in Crypto-Assets Regulation (MiCA).", "https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica"),
    (15, "Crowdfund Insider. BlackRock's tokenized fund BUIDL hits $1b AUM.", "https://www.crowdfundinsider.com/?p=237449"),
    (16, "The Block (2021). EIB issues digital bond on Ethereum blockchain.", "https://www.theblock.co/news/ecosystems/2021-04-28-european-investment-bank-bond-public-blockchain-103151"),
    (17, "Finextra (2021). EIB issues digital bond on public blockchain.", "https://finextra.com/newsarticle/37960/eib-issues-digital-bond-on-public-blockchain"),
    (18, "Seatrade Maritime (2022). Maersk and IBM pull the plug on TradeLens.", "https://www.seatrade-maritime.com/technology/maersk-and-ibm-pull-plug-tradelens"),
    (19, "The Block (2022). ASX cancels years-long blockchain settlement and clearing system project.", "https://www.theblock.co/news/business/2022-11-16-asx-cancels-years-long-blockchain-settlement-and-clearing-system-project-187809"),
    (20, "Decrypt (2022). Cross-chain crypto bridge hacks hit $2 billion in 2022, Chainalysis.", "https://decrypt.co/106718/cross-chain-crypto-bridge-hacks-hit-2-billion-2022-chainalysis"),
    (21, "Infosecurity Magazine (2023). Record $3.8bn stolen via crypto in 2022.", "https://www.infosecurity-magazine.com/news/record-38bn-was-stolen-crypto/"),
    (22, "Central Bank of Ireland (2026). Navigating and responding to change: resilience, innovation and regulation in the funds sector. BIS review.", "https://www.bis.org/review/r260610b.htm"),
    (23, "HM Treasury (2026). Update on the digital gilt instrument (DIGIT) pilot issuance.", "https://www.gov.uk/government/publications/update-on-the-digital-gilt-instrument-digit-pilot-issuance/update-on-the-digital-gilt-instrument-digit-pilot-issuance"),
    (24, "Baker McKenzie (2023). MAS Project Guardian.", "https://www.bakermckenzie.com/en/newsroom/2023/11/mas-project-guardian"),
    (25, "Julius Baer. Swiss regulations give greater certainty to digital tokens.", "https://juliusbaer.com/en/business-navigator/regulation/swiss-regulations-give-greater-certainty-to-digital-tokens"),
    (26, "ESMA (2024). ESMA proposes to move to T+1 by October 2027.", "https://www.esma.europa.eu/node/214007"),
    (27, "Fortune (2025). Robinhood tokenized stocks, Arbitrum and a layer 2 for Europe.", "https://fortune.com/crypto/2025/06/30/robinhood-tokenized-stocks-arbitrum-blockchain-l2-europe"),
    (28, "Fox News (2025). GENIUS Act: Trump signs stablecoin bill into law.", "https://www.fox5ny.com/news/genius-stablecoin-act-trump-signs-law"),
    (29, "Chainspect. Ethereum: finality, block time and throughput.", "https://chainspect.app/chain/ethereum"),
]


def chain_html(cite):
    nums = _table(["Quantity", "Number", "What it means"], [
        ["Fingerprint (hash)", "256 bits, written as 64 hexadecimal characters", "Change one letter in a record and the code changes completely. Bitcoin uses the SHA-256 hash for this"],
        ["Ethereum block time", "12 seconds per slot" + cite(29), "A new batch of records is proposed about every twelve seconds"],
        ["Ethereum final settlement", "About 13 minutes (two epochs). One source lists 16 minutes" + cite(29), "The time before a transaction cannot be reversed without destroying a large amount of staked money"],
        ["Throughput on the base layer", "About 15 transactions a second measured, as of a recent reading" + cite(29), "Volume has to move to rollups" + cite(10)],
        ["A zero-knowledge proof", "Lets a verifier check a computation without redoing it" + cite(11), "This is what lets a rollup post a short proof for many transactions"],
        ["BlackRock BUIDL", "Launched March 2024 on Ethereum. Passed $1 billion in March 2025" + cite(15), "The first tokenised fund from a Wall Street firm to reach that size"],
        ["Tokenised assets", "Tracked by rwa.xyz" + cite(12), "Totals depend on the measure used. Read the definitions before quoting a number"],
    ])
    kinds = _table(["Building block", "What it does", "Examples", "Status"], [
        ["Public blockchain", "A ledger anyone can read and add to by the rules, with no owner", "Ethereum, Bitcoin", "Running for years, with large value held"],
        ["Smart contract", "A program on the ledger that moves assets when its conditions are met", "Token issuance, exchanges, lending", "Works. Bugs and bridge hacks have cost billions" + cite(20)],
        ["Rollup (layer 2)", "Runs transactions off the main chain and posts a summary, so fees are lower", "Arbitrum, Optimism, Base" + cite(10), "Where Robinhood put its tokenised stocks (Arbitrum One)" + cite(27)],
        ["Zero-knowledge proof", "Proves a statement is true without revealing the data behind it", "zk-rollups, private checks" + cite(11), "Working in production"],
        ["Tokenised fund", "A fund share recorded as a token", "BlackRock BUIDL" + cite(15), "Growing from a small base"],
        ["Digitally native bond", "A bond issued on a ledger from the start", "EIB 2021 on Ethereum" + cite(16) + "; UK DIGIT planned by Q1 2027" + cite(23), "Pilot scale"],
    ])
    ev = _table(["Milestone", "Who and when", "Status", "What to know"], [
        ["A bond issued on a public chain by a major institution", "European Investment Bank, 100 million euros, two years, April 2021" + cite(16), _tag("ok"), "Goldman Sachs, Santander and Societe Generale led it. It matured in April 2023" + cite(17)],
        ["A tokenised fund from a Wall Street firm passing $1 billion", "BlackRock BUIDL, March 2025" + cite(15), _tag("ok"), "Launched in March 2024"],
        ["Tokenised US shares for retail customers in the EU", "Robinhood, from 30 June 2025, on Arbitrum One" + cite(27), _tag("ok"), "Holders get dividends but no voting rights. The token is a claim on a share held by a US broker-dealer"],
        ["A legal basis for crypto-assets in the EU", "MiCA, in full application from December 2024" + cite(13), _tag("ok"), "Covers issuers and service providers"],
        ["Government-backed tokenisation tests with banks", "Singapore, Project Guardian, from 2022" + cite(24), _tag("ok"), "Includes a cross-border pilot with DBS, UBS and SBI"],
        ["A UK sandbox for digital securities in live use", "HSBC approved to go live in the Digital Securities Sandbox, July 2026" + cite(23), _tag("ok"), "The Bank of England and the FCA run it"],
        ["A shipping platform on a blockchain", "TradeLens, from Maersk and IBM. Wind-down announced 29 November 2022, offline by the end of Q1 2023" + cite(18), _tag("dis"), "The firms said that full global industry collaboration was not achieved"],
        ["A stock exchange replacing its clearing system with a blockchain", "ASX in Australia, scrapped November 2022" + cite(19), _tag("dis"), "ASX wrote off between A$245 million and A$255 million before tax"],
        ["A government gilt issued natively on a ledger", "UK DIGIT pilot, first transaction by Q1 2027" + cite(23), _tag("tgt"), "Planned, on HSBC's platform"],
    ])
    gl = _gloss([
        ("Hash", "A short fixed-length code made from data. The same data always gives the same code, and different data gives a different one."),
        ("Smart contract", "A program stored on a ledger that runs when the rules it holds are met."),
        ("Token", "A record on a ledger that stands for something, such as a coin, a fund share or a ticket."),
        ("Tokenisation", "Putting a claim on a real asset, such as a bond or a share, onto a ledger as a token."),
        ("Rollup", "A network that runs transactions off the main chain and posts proof of the results to it." + cite(10)),
        ("Zero-knowledge proof", "A way to show a statement is true without showing the data that makes it true." + cite(11)),
        ("Settlement", "The final swap of the asset and the payment after a trade."),
        ("Custody", "Safekeeping of the keys that control an asset. Whoever holds the keys controls the asset."),
    ])
    return f'''
<h3 class="wide" id="s-tech" data-nav="Technical" style="margin-top:44px">Under the hood</h3>
<p>A blockchain is a list of records in batches. Each batch carries the fingerprint of the batch before it, so changing an old record would change every fingerprint after it. Many computers keep copies and agree on the next batch by a fixed rule, so no single party can rewrite the list. A smart contract is a program that sits on that list and moves tokens when its rules are met.{cite(10)} A zero-knowledge proof lets one party show that a computation was done correctly without anyone else redoing it, which is what lets a rollup post a short proof for many transactions.{cite(11)}</p>
{nums}
<p class="cap wide">Speeds and fees change as the networks are upgraded. Tokenised-asset totals depend on which measure is used.</p>
<h3 class="wide" id="s-types" data-nav="Blocks" style="margin-top:36px">The building blocks</h3>
{kinds}
<h3 class="wide" id="s-tech2" data-nav="Evidence" style="margin-top:36px">The evidence so far</h3>
{ev}
<h3 class="wide" id="s-gloss" data-nav="Glossary" style="margin-top:36px">Terms worth knowing</h3>
{gl}'''
