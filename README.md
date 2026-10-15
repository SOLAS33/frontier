# Frontier

Python build for a series of plain-language emerging-technology sites. Each site is a Python module in `sites/`
that returns content; `frontier/` turns prices into charts, runs scenario simulations and draws the illustrations.

    python build.py quantum                # build dist/quantum/index.html from cached prices
    python build.py quantum --refresh      # pull fresh weekly prices (Yahoo Finance via yfinance)
    python build.py quantum --check-links  # test every reference link
    python -m pytest -q tests

Modules: `prices` (cache, stats, volatility, best runs), `scenarios` (Monte Carlo from stated assumptions),
`charts` (SVG charts: fan, log bars, multiples, roadmap, ladder), `art` (generated illustrations),
`linkcheck`. Scenario probabilities and drifts are the author's judgement and are declared in `sites/<site>.py`.
Information only, not investment advice.
