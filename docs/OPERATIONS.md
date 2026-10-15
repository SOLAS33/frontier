# Frontier: operations

## Where it runs

- Host: Cloudflare Worker `frontier` with static assets from `dist/`. Custom domain `frontier.solas33.com`.
  Also reachable at the workers.dev address for testing.
- Code and scheduled job: public repository `SOLAS33/frontier` on GitHub. Actions minutes are free for public repos.
- State: `state` branch of the same repository (a tarball of `data/live/`).

## Deploying by hand

From a PC that is logged in to Cloudflare with wrangler:

    python build.py quantum
    node wrangler.js deploy          # from the repository root; picks up wrangler.jsonc

`npx wrangler` fails on the founder PC with an npm lock error (ECOMPROMISED). Install wrangler in a temp folder
(`npm i wrangler@4 --cache <temp>`) and run `node_modules/wrangler/bin/wrangler.js deploy` instead.

## The scheduled job

`live.yml` runs at minute 17 of every third hour and on every push that touches code. Steps: tests, restore state,
refresh prices, live run, build, deploy (only when `CF_API_TOKEN` is real), save state. Until the token is set the job
still refreshes data and keeps state, but the site is not redeployed, so `live.json` on the live site stays at its last
manual deploy.

## Secrets and variables

See KEYS.md. Nothing is requested until every site is ready, then the keys are added together.

## Search indexing

Pages carry `noindex` and `robots.txt` disallows everything until `FRONTIER_INDEXABLE=1` is set (repository variable) or
`indexable = true` in `config.toml`. Flip it after the disclosures have been read.

## When something looks wrong

| Symptom | Check |
|---|---|
| Headlines or events missing | `live.json` `status` shows which source failed. Yahoo RSS and arXiv fail soft |
| No SEC filings | `SEC_CONTACT_EMAIL` is missing or not an address |
| Odds did not move | Events are only counted inside the 120 day window and above the classifier thresholds |
| Scorecard shows 0 scored | The first 3-month predictions fall due three months after the first ledger row |
| Ledger "BROKEN" | Someone edited `ledger.jsonl`. Restore from the state branch history |
| Page looks unstyled | `dist/` was built before CSS changed. Rebuild |

## Traffic

No analytics are added to the pages. Traffic is read from Cloudflare's own analytics for the zone.
