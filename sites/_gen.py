"""Generic six-chapter Frontier site assembly. A site module supplies a config dict of already-sourced content;
this builds the page exactly as the hand-written sites do. Voice rules: docs/VOICE.md. No fact lives here."""
from __future__ import annotations

from frontier import charts
from frontier.components import band, chapter, fig, note, photo
from frontier import sitekit as K
from sites.quantum_extra import tile_map


def _cards(items, cls="card rv"):
    return "".join(f'<div class="{cls}"><h3>{t}</h3><p>{b}</p></div>' for t, b in items)


def _tl(events):
    return "".join(f'<div class="ev{" " + c if c else ""}"><div class="yr">{y}</div><p>{t}</p></div>' for y, t, c in events)


def _photos(items):
    return "".join(photo(f, caption=c) for f, c in items)


def build(C, cite):
    """C holds: slug, title, as_of, live, scen, companies, order, extra, tm_default, tm_assets, default, runs_for,
    mult (list of (label, ticker, kind)), index_groups, hero, ch1..ch6, map, shovels, hype, ladder, country, names, tiles, facts, notes."""
    px, stat, sims, data_js = K.prep(C["scen"], C["order"], ["AAPL", "NVDA"], C["default"], C["tm_assets"], C["tm_default"],
                                     C["country"], C["names"], {"co": "Firms", "gov": "Facts", "ctl": "Source", "note": "Read"}, C["map_default"])
    from frontier import prices
    runs = {t: prices.best_run(px[t]) for t in C["runs_for"]}
    lo_p = min(s["prob_below_start"] for s in sims.values())
    hi_p = max(s["prob_below_start"] for s in sims.values())
    mult = [(lab, f"from {runs[t]['from']}", runs[t]["multiple"], kind) for lab, t, kind in C["mult"]]
    idx_svg = K.index_svg(px, C["index_groups"])
    h = C["hero"]
    stats = [(v if not callable(v) else v(runs), lab, pre, suf) for v, lab, pre, suf in h["stats"]]
    hero = K.hero(f"Frontier / {C['name']}", h["h1"], h["lead"], h["img"], h["art"], stats)

    c1 = C["ch1"]
    ch1 = chapter("learn", 1, "How it works, and where it breaks", c1["sub"], f'''
{c1["intro"]}
<div class="fx-photos wide">{_photos(c1["photos"])}</div>
<h3 class="wide" id="s-paths" data-nav="{c1["paths_nav"]}" style="margin-top:36px">{c1["paths_title"]}</h3>
<div class="cols c4 wide">{_cards(c1["paths"])}</div>
<h3 class="wide" id="s-errors" data-nav="Limits" style="margin-top:44px">Where it breaks</h3>
<div class="cols c4 wide">{_cards(c1["limits"])}</div>
{C["tech"]}
<h3 class="wide" id="s-history" data-nav="History" style="margin-top:44px">History</h3>
<div class="tl wide">{_tl(c1["history"])}</div>''', K.key_idea(*c1["key"]), short="Basics")

    c2 = C["ch2"]
    ch2 = chapter("simple", 2, "The short version", "Three lines and a picture.", f'''
<div class="cols wide">{_cards(c2["cards"])}</div>
<div class="wide">{photo(c2["photo"][0], caption=c2["photo"][1])}</div>''', K.key_idea(*c2["key"]), short="Simple")

    c3 = C["ch3"]
    ch3 = chapter("change", 3, "What changes, and in what order", c3["sub"], f'''
<div class="tl wide">{_tl(c3["timeline"])}</div>
<h3 class="wide" id="s-ireland" data-nav="Ireland" style="margin-top:36px">Ireland</h3>
<div class="cols wide">{_cards(c3["ireland"])}</div>
<h3 class="wide" id="s-prepare" data-nav="Prepare" style="margin-top:44px">Be ready</h3>
<div class="cols wide">{_cards(c3["prepare"])}</div>''', K.key_idea(*c3["key"]), short="Change")

    c4 = C["ch4"]
    ch4 = chapter("companies", 4, "The companies, the money, the odds", c4["sub"], f'''
{c4.get("intro", "")}
<div class="cols wide">{K.company_cards(C["companies"], stat)}{c4["extra"]}</div>
{K.prices_block("s-prices", c4["prices_title"], c4["prices_blurb"])}
<h3 class="wide" id="s-booms" data-nav="Booms" style="margin-top:44px">What an explosion looks like</h3>
<p>The biggest rise from a low to a later high inside two years.</p>
{fig(charts.multiples(mult), c4["booms_caption"], 1)}
<h3 class="wide" id="s-ladder" data-nav="Ladder" style="margin-top:44px">The ladder to profit</h3>
{fig(charts.ladder(C["ladder"], 2), c4["ladder_caption"], 2)}
<div class="cols wide">
<div class="card rv"><h3>Signs a boom is starting</h3><ul>{"".join(f"<li>{x}</li>" for x in c4["good"])}</ul></div>
<div class="card rv"><h3>Signs it is running ahead of itself</h3><ul>{"".join(f"<li>{x}</li>" for x in c4["bad"])}</ul></div>
</div>
{K.live_block()}
<h3 class="wide" id="s-proof" data-nav="Proof" style="margin-top:44px">Hype or proof</h3>
<div class="scroll wide"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples</th><th>Weight</th></tr></thead><tbody>{K.hype_rows(C["hype"])}</tbody></table></div>
{K.map_block(tile_map(C["tiles"], C["names"]), c4["map_key"], "Pick a country. A summary from the cited public sources.")}
<h3 class="wide" id="s-suppliers" data-nav="Suppliers" style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll wide"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{K.table_rows(C["shovels"])}</tbody></table></div>
<p class="cap wide">Examples only. Not recommendations.</p>
<h3 class="wide" id="s-index" data-nav="Index" style="margin-top:44px">The Frontier Index</h3>
{fig(idx_svg, "Equal-weight baskets, weekly rebalanced, set to 100 at the start.", 3)}
{K.time_block()}''', K.key_idea(*c4["key"]), short="Money")

    c5 = C["ch5"]
    ch5 = chapter("hurdles", 5, "The limits, and what goes wrong", c5["sub"], f'''
<div class="cols wide">{_cards(c5["cards"])}</div>
<div class="fx-photos wide">{photo(c5["photo"][0], caption=c5["photo"][1])}
<div class="card" style="align-self:start"><h3>The problem in one line</h3><p>{c5["line"]}</p></div></div>''', K.key_idea(*c5["key"]), short="Limits")

    c6 = C["ch6"]
    why = [(t, b.format(lo=f"{lo_p:.0%}", hi=f"{hi_p:.0%}")) for t, b in c6["why"]]
    ch6 = chapter("outlook", 6, "Three years out", "Our best estimate to October 2029. Judgements with stated assumptions. Not predictions, and not advice.", f'''
<h3 class="wide">What we expect from the technology</h3>
<div class="cols wide">{_cards(c6["expect"])}</div>
<div class="callout r wide" style="margin-top:40px"><b>Read this first.</b> These are scenarios built from stated assumptions. They are not forecasts, recommendations or price targets. Past price behaviour does not predict the future. You can lose all of the money you put into shares like these. Solas33 holds no position in any company named and takes no payment from any of them.</div>
{K.scenarios_block(K.scenario_rows(C["companies"], sims), 4, c6["n_word"])}
<div class="pull wide">{c6["pull"]}<small>Our view</small></div>
<div class="cols wide">{_cards(why)}</div>
<div class="callout t wide"><b>What would change our mind.</b> {c6["mind"]}</div>''', K.key_idea(*c6["key"]), short="Outlook")

    bands = [band(f, k, l, a) for f, k, l, a in C["bands"]]
    foot = K.foot(C["refs"], C["as_of"], f"Frontier {C['name']}", C["slug"],
                  "Ranges come from stated assumptions and probabilities chosen by the editors, with volatility from each stock's last 104 weekly returns scaled to 75%.",
                  C["data_note"] + " Prices come from Yahoo Finance and are delayed. News is headlines and links only, with the publisher named. Photographs are public domain, mostly US government work, and credited under each picture. Figures were checked against the sources listed and are rounded. Where sources disagreed the text says so.")
    nf = K.notice(C["notice"])
    body = K.assemble(C["slug"], hero, nf, [ch1, ch2, ch3, ch4, ch5, ch6], bands, foot, C["facts"])
    return {"title": f"Frontier {C['name']}", "body": body, "data_js": data_js, "sims": sims, "stat": stat, "runs": runs}
