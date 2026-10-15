"""Build the Frontier series into dist/. One host, one folder per site.

  python build.py quantum                 build the quantum site and the hub from cached prices
  python build.py quantum --refresh       fetch fresh prices first
  python build.py quantum --check-links   also test every reference link
  python build.py hub                     rebuild only the series home page

Everything that varies (domain, contact address, which sites exist, indexing) is in config.toml.
"""
from __future__ import annotations

import argparse
import importlib
import os
import shutil
import tomllib
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "frontier" / "assets"
DIST = ROOT / "dist"
CFG = tomllib.loads((ROOT / "config.toml").read_text(encoding="utf-8"))
S = CFG["series"]

FONTS = ("https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
         "&family=Manrope:wght@500;700;800&display=swap")

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="16" r="9" fill="none" stroke="currentColor" stroke-width="2.4" opacity=".9"/>'
        '<circle cx="20" cy="16" r="9" fill="none" stroke="var(--violet)" stroke-width="2.4"/><circle cx="16" cy="16" r="2.6" fill="var(--teal)"/></svg>')


def indexable() -> bool:
    return os.environ.get("FRONTIER_INDEXABLE") == "1" or bool(S.get("indexable"))


def head(title: str, description: str, path: str) -> str:
    robots = "" if indexable() else '<meta name="robots" content="noindex, nofollow">\n'
    url = f"https://{S['domain']}/{path}"
    return (f"<title>{escape(title)}</title>\n<meta name=\"description\" content=\"{escape(description)}\">\n{robots}"
            f'<link rel="canonical" href="{url}">\n<meta property="og:title" content="{escape(title)}">\n'
            f'<meta property="og:description" content="{escape(description)}">\n<meta property="og:type" content="website">\n'
            f'<meta property="og:url" content="{url}">\n<meta name="theme-color" content="#060a1c">\n'
            f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="{FONTS}">')


def topbar(slug: str) -> str:
    home = "../" if slug != "hub" else "./"
    where = f"<small>{slug.title()}</small>" if slug != "hub" else ""
    levels = ""
    return (f'<div id="progress"></div><header class="fx-top"><a class="fx-brand" href="{home}">{LOGO}<span>Frontier</span>{where}</a>'
            f'{levels}<button id="theme" type="button">Light / dark</button></header>')


def page(title: str, description: str, path: str, slug: str, body: str, data_js: str = "") -> str:
    css = (ASSETS / "site.css").read_text(encoding="utf-8") + "\n" + (ASSETS / "frontier.css").read_text(encoding="utf-8")
    js = (ASSETS / "site.js").read_text(encoding="utf-8") + "\n" + (ASSETS / "motion.js").read_text(encoding="utf-8")
    return (f"{head(title, description, path)}\n<style>{css}</style>\n{topbar(slug)}\n<main>{body}</main>\n"
            f"<script>{data_js}</script>\n<script>{js}</script>\n")


def hub_body() -> str:
    from frontier import tiles
    from frontier.components import watch_promo
    cards = []
    for s in CFG["sites"]:
        live = s["status"] == "live"
        href = f'{s["slug"]}/' if live else "#"
        cards.append(f'<a class="{"" if live else "soon"}" href="{href}">{tiles.tile(s["slug"])}<div class="tile-body"><b>{escape(s["name"])}</b>'
                     f'<span>{escape(s["line"])}</span></div><em>{"Live" if live else "Coming"}</em></a>')
    how = (
        '<div class="fx-how"><div class="card"><h3>Plain language</h3><p>Each site explains one technology without the jargon, '
        'then follows the companies and the money.</p></div><div class="card"><h3>Sourced</h3><p>Every claim links to a paper, a filing or a '
        'dated announcement. Targets are labelled as targets.</p></div><div class="card"><h3>Kept current</h3><p>A backend reads filings, '
        'headlines and prices every few hours and logs every change to our odds.</p></div><div class="card"><h3>No adverts</h3><p>We hold no '
        'position in any company named. The only benefit to Solas33 is traffic to its own sites as a provider of information.</p></div></div>')
    return f'''<header class="fx-hero"><div class="fx-hero-img"><img src="quantum/img/laser-table.jpg" alt="" decoding="async"></div>
<div class="fx-hero-in"><div class="fx-kicker">Solas33</div><h1>What is being built, <em>who</em> is building it, and what it is worth</h1>
<p class="lead">Frontier explains emerging technology in plain language, then follows the companies and the money. One site per technology.</p></div></header>
<div class="fx-flow"><h2 style="margin-top:70px">The sites</h2><div class="fx-hub">{"".join(cards)}</div>{how}
{watch_promo()}
<div class="callout r" style="margin-top:50px"><b>Information only.</b> Nothing here is investment advice or a recommendation. Projections are scenarios, not forecasts. Money put into emerging-technology shares can be lost in full.</div></div>
<footer class="fx-foot"><div class="fx-foot-in"><p>Published by {escape(S["publisher"])}. Corrections: <a href="mailto:{S["contact_email"]}">{S["contact_email"]}</a>. Code: <a href="https://github.com/SOLAS33/frontier">github.com/SOLAS33/frontier</a>.</p></div></footer>'''


def write_root_files():
    DIST.mkdir(parents=True, exist_ok=True)
    nl = chr(10)
    (DIST / "_headers").write_text(nl.join([
        "/*", "  X-Content-Type-Options: nosniff", "  Referrer-Policy: strict-origin-when-cross-origin", "  X-Frame-Options: DENY",
        "  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'",
        "/*/img/*", "  Cache-Control: public, max-age=31536000, immutable", ""]), encoding="utf-8")
    (DIST / "robots.txt").write_text(nl.join(["User-agent: *", "Allow: /" if indexable() else "Disallow: /", ""]), encoding="utf-8")


def build_site(slug: str, a) -> dict:
    mod = importlib.import_module(f"sites.{slug}")
    ctx = mod.build()
    meta = next(s for s in CFG["sites"] if s["slug"] == slug)
    out = DIST / slug
    out.mkdir(parents=True, exist_ok=True)
    img = out / "img"
    if img.exists():
        shutil.rmtree(img)
    shutil.copytree(ASSETS / "img", img, ignore=shutil.ignore_patterns("sheet.jpg"))
    html = page(f"Frontier {meta['name']}", meta["line"], f"{slug}/", slug, ctx["body"], ctx["data_js"])
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {out / 'index.html'} ({len(html) / 1024:.0f} KB)")
    for t, s in ctx["sims"].items():
        print(f"  {t}: now {ctx['stat'][t]['last']:.2f}, 3y median {s['end_p50']:.2f} (10th {s['end_p10']:.2f}, 90th {s['end_p90']:.2f}), "
              f"below start {s['prob_below_start']:.0%}")
    if a.check_links:
        from frontier import linkcheck
        res = linkcheck.check([u for _, _, u in mod.REFS])
        for u, r in res.items():
            print(f"  {r:14s} {u}")
        (out / "links.txt").write_text("\n".join(f"{r}\t{u}" for u, r in res.items()), encoding="utf-8")
    return ctx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", help="a site slug from config.toml, or 'hub'")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--check-links", action="store_true")
    a = ap.parse_args()
    write_root_files()
    if a.site != "hub":
        from frontier import prices
        if a.refresh or not prices.CACHE.exists():
            prices.refresh()
        build_site(a.site, a)
    hub = page("Frontier", "Emerging technology in plain language, with the companies and the money. One site per technology.", "", "hub", hub_body())
    (DIST / "index.html").write_text(hub, encoding="utf-8")
    print(f"wrote {DIST / 'index.html'}")


if __name__ == "__main__":
    main()
