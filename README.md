# Frontier

Plain-language emerging-technology sites with a live Python backend. One host (frontier.solas33.com), one folder per site.
Information only. No adverts.

    python build.py quantum                # build dist/quantum and the hub from cached prices
    python build.py quantum --refresh      # fetch fresh weekly prices first
    python -m frontier.live.run            # collect, classify, adjust projections, write live.json
    python tools/voice_lint.py dist/quantum/index.html
    python -m pytest -q tests

- `config.toml`  domain, contact addresses, site list, indexing. The one place to change how the series is wired.
- `docs/VOICE.md`  the house style for every site, enforced by `tools/voice_lint.py`.
- `docs/KEYS.md`  every key the series will need, in one list.
- `tools/find_images.py`  finds public-domain photographs on Wikimedia Commons; `optimise_images.py` shrinks them.
- `frontier/live/`  the backend. `frontier/charts.py`, `art.py`, `components.py`  the shared drawing and layout code.
