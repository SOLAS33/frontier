"""Shared assembly for Frontier sites, so a new site is mostly copy and data.

A site module defines: TITLE, SLUG, AS_OF, REFS, SCEN, COMPANIES, LIVE, and calls the helpers below from its build().
The six-chapter shape, the live layer, the interactive blocks and the disclosures footer are identical across the series.
"""
from __future__ import annotations

import json

from frontier import art, charts, prices
from frontier.components import band, chapter, fig, key_idea, note, photo, series_list, watch_promo  # noqa: F401  (re-exported)
from frontier.scenarios import simulate


def cite_factory(refs):
    titles = {n: t for n, t, _ in refs}

    def cite(*ids):
        return "".join(f'<sup><a href="#r{i}" title="{titles[i]}">[{i}]</a></sup>' for i in ids)
    return cite


def fmt_p(v):
    return f"${v:,.2f}" if v < 100 else f"${v:,.0f}"


def prep(scen, order, extra, default, tm_assets, tm_default, country, names, map_labels, map_default):
    """Everything computed from prices, plus the JavaScript globals the shared page script reads."""
    px = prices.load()
    stat = {t: prices.stats(px[t]) for t in px}
    sims = {t: simulate(px[t]["c"][-1], prices.annual_vol(px[t]), sc, years=3) for t, sc in scen.items()}
    pnames = {t: px[t]["name"] for t in order}
    all_t = list(dict.fromkeys(order + extra))
    series_js = {t: {"d": px[t]["d"], "c": [round(v, 3) for v in px[t]["c"]]} for t in all_t}
    scen_js = {}
    for t in scen:
        vol = prices.annual_vol(px[t])
        scen_js[t] = {"name": px[t]["name"], "price": px[t]["c"][-1], "tilt_pts": 0,
                      "hist": {"d": px[t]["d"][-104:], "c": [round(v, 3) for v in px[t]["c"][-104:]]},
                      "scen": [{"k": s.key, "label": s.label, "p": s.probability, "drift": s.drift, "sigma": round(vol * s.vol_mult, 4)} for s in scen[t]]}
    data_js = (f"window.PRICES={json.dumps(series_js, separators=(',', ':'))};"
               f"window.PRICE_ORDER={json.dumps(order)};window.PRICE_NAMES={json.dumps(pnames)};window.PRICE_DEFAULT={json.dumps(default)};"
               f"window.SCEN={json.dumps(scen_js, separators=(',', ':'))};"
               f"window.TM_ASSETS={json.dumps(tm_assets)};window.TM_DEFAULT={json.dumps(tm_default)};"
               f"window.COUNTRY={json.dumps(country)};window.COUNTRY_NAMES={json.dumps(names)};"
               f"window.MAP_LABELS={json.dumps(map_labels)};window.MAP_DEFAULT={json.dumps(map_default)};")
    return px, stat, sims, data_js


def basket(px, members):
    idx = {t: dict(zip(px[t]["d"], px[t]["c"])) for t in members}
    start = max(px[t]["d"][0] for t in members)
    dates = [d for d in px[members[0]]["d"] if d >= start and all(d in idx[t] for t in members)]
    lvl, out = 100.0, []
    for i, d in enumerate(dates):
        if i:
            lvl *= 1 + sum(idx[t][d] / idx[t][dates[i - 1]] - 1 for t in members) / len(members)
        out.append(lvl)
    return dates, out


def index_svg(px, groups):
    """groups: [(label, members, colour)] baskets rebased to 100 at the first week all baskets exist. A single symbol is a line."""
    built = []
    for label, members, colour in groups:
        d, v = basket(px, members) if len(members) > 1 else (px[members[0]]["d"], px[members[0]]["c"])
        built.append((label, d, v, colour))
    start = max(b[1][0] for b in built)
    series = []
    for label, d, v, colour in built:
        pairs = [(a, b) for a, b in zip(d, v) if a >= start]
        base = pairs[0][1]
        series.append((label, [a for a, _ in pairs], [b / base * 100 for _, b in pairs], colour))
    return charts.index_chart(series)


def hero(kicker, h1, lead, img, art_svg, stats):
    cells = "".join(f'<div class="stat"><b data-count="{v}" data-pre="{pre}" data-suf="{suf}">{pre}{v:,.0f}{suf}</b><span>{label}</span></div>'
                    for v, label, pre, suf in stats)
    return f'''<header class="fx-hero" id="top">
<div class="fx-hero-img"><img src="img/{img}" alt="" decoding="async"></div>{art_svg}
<div class="fx-hero-in"><div class="fx-kicker">{kicker}</div><h1>{h1}</h1><p class="lead">{lead}</p><div class="fx-stats">{cells}</div></div></header>
<div class="fx-ticker" aria-label="Live prices and announcements"><div class="fx-ticker-track" id="fx-ticker-track"><span>Prices and announcements load here.</span></div></div>'''


def notice(text):
    return f'<div class="callout r wide" style="margin-top:70px"><b>Information only.</b> {text} The disclosures are at the foot of the page.</div>'


def company_cards(companies, stat, how_label="How it stands"):
    out = []
    for c in companies:
        s = stat[c["t"]]
        out.append(f'''<article class="card co rv"><h3>{c["name"]}<span>{c["t"]} &middot; {c["kind"]}</span></h3>
<dl><dt>Started at</dt><dd>{fmt_p(s["first"])} in {s["first_date"][:7]}. Now {fmt_p(s["last"])}. Peak {fmt_p(s["peak"])} in {s["peak_date"][:7]}, so {abs(s["pct_from_peak"]):.0f}% below it.</dd>
<dt>Rivals</dt><dd>{c["rivals"]}</dd><dt>Needs for profit</dt><dd>{c["profit"]}</dd><dt>Watch</dt><dd>{c["watch"]}</dd>
<dt>{how_label}</dt><dd>{c["rank"]}</dd></dl><span class="verdict">{c["verdict"]}</span></article>''')
    return "".join(out)


def table_rows(rows, n_cols_right=()):
    return "".join("<tr>" + "".join(f'<td class="n">{c}</td>' if i in n_cols_right else f"<td>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)


def hype_rows(h):
    return "".join(f'<tr><td class="n">{lvl}</td><td><b>{name}</b><br><span class="muted">{desc}</span></td><td>{ex}</td>'
                   f'<td><span class="tag {cls}">{"strong" if cls == "ok" else "caution" if cls == "dis" else "weak"}</span></td></tr>' for lvl, name, desc, ex, cls in h)


def prices_block(heading_id, heading, blurb):
    return f'''<h3 class="wide" id="{heading_id}" data-nav="Prices" style="margin-top:44px">{heading}</h3>
<p class="wide">{blurb} Weekly closes to <span id="lastdate"></span>, adjusted for splits.</p>
<div class="ctrl wide" id="tickers" role="group" aria-label="Companies"></div>
<div class="ctrl wide" role="group" aria-label="Chart options">
<button data-mode="growth" aria-pressed="true">Growth, 100 = start</button><button data-mode="price" aria-pressed="false">Price (US$)</button>
<button data-range="all" aria-pressed="false">Full history</button><button data-range="2021" aria-pressed="false">Since 2021</button>
<button data-range="2024" aria-pressed="true">Since 2024</button><button data-range="1y" aria-pressed="false">Last year</button></div>
<figure class="fig wide"><svg id="chart" viewBox="0 0 900 440" role="img" aria-label="Weekly prices"></svg><div id="tip">Move across the chart to read values.</div></figure>'''


def live_block(what="filings and headlines"):
    return f'''<h3 class="wide" id="s-live" data-nav="Live" style="margin-top:44px">Live updates</h3>
<p class="wide">The page checks {what} and shows how they move the odds used in chapter 6. <span id="live-stamp">Loading the live layer.</span></p>
<div class="cols wide">
<div class="card"><h3>Announcements that moved the odds</h3><ul class="feed" id="live-events"><li>Loading.</li></ul></div>
<div class="card"><h3>Change log</h3><ul class="feed" id="live-log"><li>Loading.</li></ul></div>
<div class="card"><h3>Headlines (links to the publisher)</h3><ul class="feed" id="live-news"><li>Loading.</li></ul></div>
<div class="card"><h3>New research papers on the topic</h3><ul class="feed" id="live-papers"><li>Loading.</li></ul></div>
</div>
<p class="cap wide" id="live-status"></p>
<div class="scroll wide"><table id="live-react"></table></div>
<p class="cap wide">How these stocks moved after past filings of each type, against QQQ. The live layer uses it to size its nudges, with case counts shown.</p>'''


def map_block(tile_map_svg, key_html, intro):
    return f'''<h3 class="wide" id="s-map" data-nav="Map" style="margin-top:44px">The map</h3>
<p class="wide">{intro}</p>
<div class="map-wrap wide"><figure class="fig" style="margin:0">{tile_map_svg}<div class="map-key">{key_html}</div></figure><div class="card" id="map-panel"></div></div>'''


def time_block(sub="Past prices only."):
    return f'''<h3 class="wide" id="s-time" data-nav="Time" style="margin-top:44px">Time machine</h3>
<p>Pick an asset and a date. See what the money would be worth now, how high it went, and how far it fell on the way. {sub}</p>
<div class="ctrl wide"><label>Asset <select id="tm-asset"></select></label><label>From <input type="date" id="tm-date"></label><label>Amount (US$) <input type="number" id="tm-amt" value="1000" min="1" step="100"></label></div>
<figure class="fig wide"><svg id="tm-svg" viewBox="0 0 900 260" role="img" aria-label="Value of the investment over time"></svg><div id="tm-out" class="tmout"></div></figure>'''


def scenarios_block(rows, fig_no, n_companies_word):
    return f'''<h3 class="wide" id="s-scenarios" data-nav="Scenarios" style="margin-top:40px">What it could mean for the {n_companies_word} companies</h3>
<p>Pick a company and move the sliders to set your own odds. Dashed lines are the typical path in each story. The bands hold the middle 50% and 80% of outcomes once the stories are mixed.</p>
<figure class="fig wide" id="fan">
<div class="ctrl" id="fan-tabs" role="group" aria-label="Company"></div>
<svg id="fansvg" viewBox="0 0 900 440" role="img" aria-label="Recent price and three-year scenario range for the chosen company"></svg>
<div class="sliders">
<label>Chance of the bear story <input type="range" id="sl-bear" min="0" max="90" step="1"></label>
<label>Chance of the bull story <input type="range" id="sl-bull" min="0" max="90" step="1"></label>
<label>Volatility (100 = last two years, scaled) <input type="range" id="sl-vol" min="40" max="160" step="5"></label>
<button type="button" id="fan-reset" class="plain">Back to our odds</button></div>
<p id="fan-probs" class="cap"></p><p id="fan-read"></p><p id="fan-tilt" class="cap"></p>
<figcaption><b>Fig {fig_no}.</b> The live layer may tilt our odds by a few points because of dated announcements, never by more than 12.</figcaption></figure>
<div class="scroll wide"><table><thead><tr><th>Stock</th><th class="n">Low end (10th)</th><th class="n">Middle</th><th class="n">High end (90th)</th><th class="n">Below today</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cap wide">Three years from the build date, at our starting odds.</p>
<h3 class="wide" id="s-record" data-nav="Record" style="margin-top:36px">Our record</h3>
<div class="card wide"><p id="live-score">Loading the scorecard.</p>
<p class="cap">Every week the site writes down its 3, 6 and 12-month ranges in a hash-chained log before the outcome is known, then scores them.</p></div>'''


def scenario_rows(companies, sims):
    return "".join(f'<tr><td>{c["name"]} ({c["t"]})</td><td class="n">{fmt_p(sims[c["t"]]["end_p10"])}</td><td class="n">{fmt_p(sims[c["t"]]["end_p50"])}</td>'
                   f'<td class="n">{fmt_p(sims[c["t"]]["end_p90"])}</td><td class="n">{sims[c["t"]]["prob_below_start"]:.0%}</td></tr>' for c in companies)


def foot(refs, as_of, title, slug_label, scenario_note, data_note, extra_cards=""):
    items = "".join(f'<li id="r{n}">[{n}] <a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for n, t, u in refs)
    return f'''<footer class="fx-foot" id="disclosures"><div class="fx-foot-in">
<h2 style="font-size:1.6rem">Sources, method and disclosures</h2><ol>{items}</ol>
<div class="cols">
<div class="card"><h3>Information only</h3><p>This site is general information and education. It is not investment advice, a recommendation, an offer or a solicitation, and it takes no account of your circumstances. Speak to a licensed adviser before acting.</p></div>
<div class="card"><h3>Scenarios, not forecasts</h3><p>{scenario_note} Prices can fall to zero.</p></div>
<div class="card"><h3>Conflicts</h3><p>Solas33 holds no position in any company named and takes no payment from any of them. The only benefit to Solas33 is traffic to its own sites as a provider of information. There is no advertising. If any of that changes it will be stated here with the date.</p></div>
<div class="card"><h3>Data</h3><p>{data_note}</p></div>
<div class="card"><h3>Corrections</h3><p>Errors are fixed and logged. Write to <a href="mailto:hello@solas33.com">hello@solas33.com</a>. Editorial responsibility: Solas33. Content last reviewed {as_of}.</p></div>
<div class="card"><h3>For researchers and teachers</h3><p>Cite as Solas33, {title}, with the page date. The live layer is public: <a href="live.json">live.json</a> and an <a href="feed.xml">RSS feed</a>.</p></div>{extra_cards}
</div>
<p style="margin-top:28px">Part of <a href="../">Frontier</a>. Code is public at <a href="https://github.com/SOLAS33/frontier">github.com/SOLAS33/frontier</a>.</p>
</div></footer>'''


def assemble(slug, hero_html, notice_html, chapters, bands, foot_html, facts):
    """chapters: [ch1..ch6 html]; bands: [band for ch2..ch6]."""
    flow = f'<div class="fx-flow">{notice_html}{chapters[0]}</div>'
    for b, ch in zip(bands, chapters[1:]):
        flow += f'{b}<div class="fx-flow">{ch}</div>'
    frows = "".join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a, b in facts)
    rail = ('<aside class="fx-rail" id="fx-rail" aria-label="Live and series panels"><div id="fx-live" aria-live="polite"></div>'
            f'<section class="rp"><h4>Numbers to hold on to</h4>{frows}</section>'
            f'<section class="rp"><h4>In this series</h4><div class="rp-list">{series_list(slug)}</div></section></aside>')
    return (f'{hero_html}<nav class="fx-spine" id="fx-spine" aria-label="Chapters"></nav>{rail}{flow}'
            f'<div class="fx-flow">{watch_promo()}</div>{foot_html}')
