# Frontier

Plain-language emerging-technology sites with a live Python backend. One host (frontier.solas33.com), one folder per site.
Information only. No adverts. Every fact is sourced (see docs/SOURCING.md).

Live sites (14): Quantum, Coin, Chain, Cell, Mind, Bot, Atom, Fusion, Carbon, Tide, Gene, Orbit, Mine, Chip.
Registered, not built: Drone, Shield (held back by decision).

    python build.py quantum                # build dist/quantum and the hub from cached prices
    python build.py quantum --refresh      # fetch fresh weekly prices first
    python build.py quantum --check-links  # also test every reference link
    python -m frontier.live.run --site quantum   # collect, classify, adjust projections, write live.json
    python tools/voice_lint.py dist/quantum/index.html
    python tools/verify_all.py             # check every live site on the live host
    python -m pytest -q tests

- `config.toml`  domain, contact addresses, site list with topic and status, indexing. The one place to change how the series is wired.
- `docs/HANDOVER.md`  the API token, the links, and how to send information to Claude. Start here.
- `docs/SOURCING.md`  the rule: no fact from memory. `docs/AUDIT-2026-10-16.md`  what the audit found and changed.
- `docs/VOICE.md`  the house style for every site, enforced by `tools/voice_lint.py`.
- `docs/KEYS.md`  every key the series needs, in one list.
- `inbox/`  where information for Claude goes. GitHub issue forms: Correction, and Source or new information.
- `sites/_gen.py`  the shared six-chapter builder used by the newer sites. `sites/<slug>.py` holds one site's sourced content.
- `tools/find_images.py`  finds public-domain photographs on Wikimedia Commons; `optimise_images.py` shrinks them.
- `frontier/live/`  the backend. `frontier/charts.py`, `art.py`, `components.py`  the shared drawing and layout code.
