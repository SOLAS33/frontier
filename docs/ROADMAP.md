# Frontier: roadmap and open items

Updated 15 October 2026.

## Built

- Series hub at `/` with a generated tile for each planned site.
- **Quantum** (live): six chapters, 21 cited papers, interactive scenario view with your own odds, time machine, race map,
  evidence ladder, live announcements, change log, prediction ledger, 10 public-domain photographs.
- Live backend: filings, headlines, papers, reactions, capped tilt, change log, ledger, RSS.
- Voice guide and lint, image finder and optimiser, scheduled workflow, one-host path layout.

## Next sites, in order

1. **Coin**: crypto and tokenised assets, the quantum risk to Bitcoin, the 100x-token study. Built as the second site.
2. **Mind**: AI, chips and the power they use.
3. **Atom**: fission and small modular reactors.
4. **Cell**, **Bot**, **Fusion**, **Drone**, **Shield**, **Carbon**, **Tide**, **Gene**, **Orbit**, **Chip**.

## Open items for the owner

| Item | Why it is open |
|---|---|
| `CF_API_TOKEN` | The scheduled job cannot redeploy until this is a real value, so `live.json` on the live site is frozen at the last manual deploy |
| `FRONTIER_INDEXABLE=1` | Sites are noindex until the founder says go |
| `BREVO_API_KEY` | Weekly digest email is generated (`digest.html`) but not sent. Deliberately left until every site is ready |
| Photograph spot-check | Licence data comes from Wikimedia. Check the file page before commercial use |
| Subscriber list | Needed before the digest can be sent |

## Ideas not yet built

- Per-site email digest and a sign-up form.
- Embeds: a one-line share-price panel and the scenario chart for other sites.
- A shared "convergence map" showing which sites depend on each other (AI needs chips and power, quantum needs cooling and photonics).
- Frontier Index across sites, with a leaderboard.
- Photographs of company machines, once permission is arranged.
