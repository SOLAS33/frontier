"""Build a Frontier site into dist/<site>/index.html (one self-contained file).

  python build.py quantum                 build from cached prices
  python build.py quantum --refresh       fetch fresh prices first
  python build.py quantum --check-links   also test every reference link
"""
from __future__ import annotations

import argparse
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "frontier" / "assets"

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800"
         "&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap")


import os
# Pages stay out of search results until the owner sets FRONTIER_INDEXABLE=1 (after the disclosures are signed off).
ROBOTS = "" if os.environ.get("FRONTIER_INDEXABLE") == "1" else '<meta name="robots" content="noindex, nofollow">'


def page(ctx: dict, description: str) -> str:
    nav = "".join(f'<a class="s" href="#{i}">{t}</a>' for i, t in ctx["nav"])
    css = (ASSETS / "site.css").read_text(encoding="utf-8")
    js = (ASSETS / "site.js").read_text(encoding="utf-8")
    return f"""<title>{ctx['title']}</title>
<meta name="description" content="{description}">
{ROBOTS}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="{FONTS}">
<style>{css}</style>
<div id="progress"></div>
<div class="wrap">
<nav class="bar" aria-label="Chapters"><a class="brand" href="#">{ctx['title']}</a>{nav}<span class="lvl" role="group" aria-label="Reading level"><button data-lv="s" type="button" aria-pressed="false">Simple</button><button data-lv="g" type="button" aria-pressed="true">General</button><button data-lv="e" type="button" aria-pressed="false">Expert</button></span><button id="theme" type="button">Light / dark</button></nav>
{ctx['body']}
</div>
<script>{ctx['data_js']}</script>
<script>{js}</script>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--check-links", action="store_true")
    a = ap.parse_args()
    from frontier import prices
    if a.refresh or not prices.CACHE.exists():
        prices.refresh()
    mod = importlib.import_module(f"sites.{a.site}")
    ctx = mod.build()
    html = page(ctx, "A plain-language guide to quantum computing: how it works, who is building it, what it could do to share prices.")
    out = ROOT / "dist" / a.site
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    (out / "_headers").write_text(
        "/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: DENY
"
        "  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'
", encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *
Allow: /
" if os.environ.get("FRONTIER_INDEXABLE") == "1" else "User-agent: *
Disallow: /
", encoding="utf-8")
    print(f"wrote {out / 'index.html'} ({len(html) / 1024:.0f} KB)")
    for t, s in ctx["sims"].items():
        print(f"  {t}: now {ctx['stat'][t]['last']:.2f}, 3y median {s['end_p50']:.2f} (10th {s['end_p10']:.2f}, 90th {s['end_p90']:.2f}), "
              f"below start {s['prob_below_start']:.0%}")
    if a.check_links:
        from frontier import linkcheck
        urls = [u for _, _, u in mod.REFS]
        res = linkcheck.check(urls)
        for u, r in res.items():
            print(f"  {r:14s} {u}")
        (out / "links.txt").write_text("\n".join(f"{r}\t{u}" for u, r in res.items()), encoding="utf-8")


if __name__ == "__main__":
    main()
