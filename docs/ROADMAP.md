# Frontier: roadmap and open items

Updated 15 October 2026 (end of session).

## Live at frontier.solas33.com (indexable, sitemap published)

| Site | Path | Notes |
|---|---|---|
| Hub | `/` | Generated tile per site, Watch panel |
| Quantum | `/quantum/` | First site. Evidence table, 21 cited papers, race map, scenarios, live layer |
| Coin | `/coin/` | Includes the 652-token study and the quantum risk to Bitcoin |
| Mind | `/mind/` | AI chips, power, the AI stocks study |
| Atom | `/atom/` | Fission and small reactors, fuel bottleneck |
| Cell | `/cell/` | Batteries, chemistries, grid storage |

All five have an "Under the hood" technical section (Coin, Mind, Atom, Cell added 15 Oct) and are products on solas33.com
(Education) and in the Atelier under Alchemy > Frontier.

## Registered, not built

Chain (blockchain beyond money), Bot, Fusion, Drone, Shield, Carbon, Tide, Gene, Orbit, Chip.

Notes for the next session:
- **Chain** is the agreed next site: tokenised funds and bonds, smart contracts, rollups, zero-knowledge proofs. Link it from Coin.
- **Bot** and **Fusion** are ready to start. Prices for Bot (SYM, SERV, TER, ISRG, ROK) and Fusion-adjacent suppliers (AMSC, BRKR, LASR)
  are already cached in `frontier/prices.py`. Public-domain photographs for both are downloaded (robonaut-2, valkyrie,
  kuka-palletising, canadarm2, nif-laser-bay, nif-hohlraum, tftr, tftr-vessel). Fusion has almost no listed pure-plays,
  so it should say so and follow private funding instead.
- **Drone, Shield** (counter-drone, directed energy) are not being built. A safety classifier stopped work on the drone site
  during the 15 Oct session. Do not restart them without the founder deciding to, and keep any defence content to
  published, non-operational information.
- Every new site needs a technical section (see `sites/tech_blocks.py`) as well as the headline copy.

## Open items for the owner

| Item | State |
|---|---|
| `CF_API_TOKEN` | Reaches the workflow as an empty string (0 characters). Redo with `Get-Clipboard \| gh secret set CF_API_TOKEN --repo SOLAS33/frontier`, then `gh workflow run live`. Until then deploys are done by hand with wrangler from the founder PC |
| `BREVO_API_KEY` | Deliberately not requested. Weekly digest is generated (`digest.html`) but not sent |
| Photograph spot-check | Licence data comes from Wikimedia Commons. Check a file page before commercial use |
| Legal | Founder confirmed the series is cleared (15 Oct). Re-check topic-specific points per new site (see EDITORIAL-AND-RISK.md) |
| Subscriber list | Needed before any email digest |

## Ideas not yet built

- Per-site email digest and sign-up form (after the keys are added together).
- Embeds: a one-line price panel and the scenario chart for other sites.
- A convergence map across sites (AI needs chips and power, quantum needs cooling, Cell and Atom supply the power).
- Photographs of company machines, once permission is arranged.
