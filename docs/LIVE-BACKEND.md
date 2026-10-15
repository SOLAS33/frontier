# The live backend

`python -m frontier.live.run` is the job that keeps a site current. It runs every three hours from
`.github/workflows/live.yml`, or by hand.

## What it does

1. **Collects** (every source is free and fails soft: a failed source is reported in `status`, the run continues)
   - SEC EDGAR filings for each company (needs `SEC_CONTACT_EMAIL` in the environment; the SEC rejects requests without it).
   - Headlines from Yahoo Finance's per-ticker RSS feed. Headline text and link only, publisher named.
   - New quant-ph papers on arXiv that mention the named companies.
   - Daily prices (yfinance) for the companies and the QQQ benchmark.
2. **Classifies** each filing and headline by rules (`classify.py`): share sale, contract, technical result,
   acquisition, earnings, leadership, legal risk, policy. Noise forms (insider forms, proxies) are dropped. A headline
   is attached to a company only if it names it.
3. **Measures** how the stocks actually moved after past filings of each type (`impact.py`): 1-day and 5-day abnormal
   return against QQQ, with filings after 4pm New York time dated to the next session. Reported with case counts.
4. **Tilts** the scenario probabilities (`state.py`)
   - Each event has a nudge in probability points (prior from the rules, replaced by the measured reaction when there
     are enough cases and the t-statistic is at least 1.5).
   - Nudges halve every 30 days, the total is capped at plus or minus 12 points, and no story falls below 5%.
   - A tilt moves mass between the bear and bull stories only. It never moves a price.
5. **Logs** every projection change of a whole point or more to `changelog.jsonl` with its causes.
6. **Records predictions** each ISO week: the 3, 6 and 12 month 10th, 50th and 90th percentile prices, in an append-only,
   hash-chained `ledger.jsonl`. Rows are scored when due: did the real price land inside the 10th to 90th range.
7. **Publishes** `live.json` (what the page reads), `feed.xml` (RSS) and `digest.html` (weekly digest, not sent anywhere yet).

## Files

| File | Where | Purpose |
|---|---|---|
| `data/live/events.json` | state branch | Every classified event in the window |
| `data/live/state.json` | state branch | Last published probabilities |
| `data/live/changelog.jsonl` | state branch | Append-only projection change log |
| `data/live/ledger.jsonl` | state branch | Hash-chained predictions |
| `dist/<site>/live.json` | deploy | What the page reads |

State is kept on a `state` branch as a tarball so the scheduled job can restore it, add to it, and save it.

## Honesty rules (from CLAUDE-style house rules)

- No hindsight: events are dated by when they were public.
- Nulls are reported: "too few cases" is shown when a filing type has fewer than 8 cases.
- Predictions are never edited. A broken hash chain is shown on the page.
- Scenario odds are the editors' judgement. The backend tilts them within caps. It does not replace them.

## Extending to a new site

A site module supplies `SCEN` (tickers and their scenarios). Add the tickers' SEC CIK numbers and headline aliases to
`frontier/live/sources.py` and `classify.py`, and point `OUT` at the site's folder. See NEW-SITE-CHECKLIST.md.
