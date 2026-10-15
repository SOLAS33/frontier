# Frontier: architecture

Frontier is a series of plain-language emerging-technology sites. They are built by one Python project into one static
folder and served from one Cloudflare Worker at `frontier.solas33.com`, one path per site (`/quantum/`, `/coin/`, ...).
The series home page is `/`.

## Layout of the repository

| Path | What it holds |
|---|---|
| `config.toml` | The one file that wires the series: domain, contact addresses, indexing flag, the site list and the Watch cross-links |
| `build.py` | Builds the hub and any site into `dist/`; writes `_headers` and `robots.txt` |
| `sites/<slug>.py` | One module per site: copy, data, and a `build()` that returns the page body. Also exports `REFS`, `SCEN` |
| `frontier/components.py` | Shared HTML blocks: chapter, photo, band, note, figure, key idea, Watch panel, series list |
| `frontier/charts.py`, `art.py`, `tiles.py` | SVG drawn from numbers: fan, bars, ladder, roadmap, index chart, illustrations, hub tiles |
| `frontier/prices.py` | Weekly price cache (Yahoo Finance via yfinance), stats, volatility, best runs |
| `frontier/scenarios.py` | Monte Carlo scenario engine with stated drift, probability and volatility |
| `frontier/live/` | The live backend (see LIVE-BACKEND.md) |
| `frontier/assets/` | `site.css` (charts and legacy components), `frontier.css` (layout and design), `site.js` (charts, sliders, time machine, map), `motion.js` (hero, parallax, spine, rail), `img/` (photographs and `credits.json`) |
| `tools/` | `find_images.py`, `optimise_images.py`, `voice_lint.py` |
| `tests/` | Engine, live backend, charts |
| `.github/workflows/live.yml` | Scheduled job: restore state, refresh prices, run live job, build, deploy, save state |

## Page shape

Each site page is one HTML file with CSS and JavaScript inlined, plus `img/`, `live.json` and `feed.xml` beside it.
The frame has a photographic hero, a scrolling ticker, chapters with margin notes, full-bleed photo bands between
chapters, a chapter spine on the left and a live rail on the right (both appear above 1600px), then the disclosures.
Charts that need data (share prices, scenario fans, time machine, map) read variables injected by the site module
(`window.PRICES`, `window.SCEN`, `window.COUNTRY`) and then overlay anything in `live.json`.

## Why one host with paths

Cloudflare's free universal certificate covers one level of subdomain. `quantum.frontier.solas33.com` would be two
levels and would need a paid certificate, so each site lives at a path instead. The hub and all sites share one Worker,
one `_headers` file and one deploy.

## Adding a site

See NEW-SITE-CHECKLIST.md. In short: add the site to `config.toml`, create `sites/<slug>.py`, add photographs with
`tools/find_images.py`, run the voice lint, build, deploy.
