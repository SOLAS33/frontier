"""The live job. `python -m frontier.live.run` collects, classifies, adjusts and writes the files the site reads.

  data/live/events.json       every classified event seen (kept, so tilts decay properly across runs)
  data/live/state.json        last published probabilities, for the change log
  data/live/changelog.jsonl   append-only record of every projection change and its cause
  data/live/ledger.jsonl      append-only, hash-chained predictions (3, 6 and 12 month bands, weekly)
  dist/quantum/live.json      what the page reads
  dist/quantum/feed.xml       RSS of changes and notable events
  dist/quantum/digest.html    weekly digest, ready to email
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from html import escape
from pathlib import Path

from frontier import prices
from frontier.live import classify, impact, sources, state

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "live"
OUT = ROOT / "dist" / "quantum"
EVENT_WINDOW_DAYS = 120


def _scen_for(ticker: str, scen_defs) -> list[dict]:
    return [{"k": s.key, "label": s.label, "base_p": s.probability, "drift": s.drift, "vm": s.vol_mult} for s in scen_defs[ticker]]


def _nudge(kind: str, table: dict, headline: bool) -> float:
    prior = classify.prior(kind)
    row = table.get(kind)
    sign = (1 if prior > 0 else -1 if prior < 0 else 0)
    mag = abs(prior)
    if row and row["enough"] and row["t_5d"] is not None and abs(row["t_5d"]) >= 1.5:
        sign = 1 if row["mean_5d"] > 0 else -1
        mag = max(mag, 1.0) * (1 + min(1.0, abs(row["median_5d"]) / 0.10))
    val = sign * mag
    return round(val * (0.5 if headline else 1.0), 3)


def run(today: date | None = None, offline: bool = False, scen_defs=None, weekly=None) -> dict:
    from sites.quantum import SCEN
    scen_defs = scen_defs or SCEN
    today = today or date.today()
    weekly = weekly or prices.load()
    status, filings, headlines, papers = {}, [], {}, []

    if not offline:
        if "@" in os.environ.get("SEC_CONTACT_EMAIL", ""):
            with sources._client(sources.sec_ua()) as sc:
                for t in scen_defs:
                    try:
                        filings += sources.edgar_filings(t, client=sc)
                        status[f"sec:{t}"] = "ok"
                    except Exception as e:
                        status[f"sec:{t}"] = f"failed {type(e).__name__}"
        else:  # the SEC rejects requests that do not declare a contact email
            status["sec"] = "skipped: SEC_CONTACT_EMAIL not set"
        with sources._client() as c:
            for t in scen_defs:
                try:
                    headlines[t] = sources.yahoo_headlines(t, client=c)
                    status[f"news:{t}"] = "ok"
                except Exception as e:
                    headlines[t], status[f"news:{t}"] = [], f"failed {type(e).__name__}"
            for term in sources.ARXIV_TERMS:
                try:
                    papers += sources.arxiv_papers(term, client=c)
                    status[f"arxiv:{term}"] = "ok"
                except Exception as e:
                    status[f"arxiv:{term}"] = f"failed {type(e).__name__}"
    seen_p, uniq_papers = set(), []
    for p in sorted(papers, key=lambda p: p["date"], reverse=True):
        if p["id"] not in seen_p:
            seen_p.add(p["id"])
            uniq_papers.append(p)

    # reaction table from history
    reactions_rows, table = [], {}
    try:
        px = impact.daily_prices(list(scen_defs) + ["QQQ"]) if not offline else {}
        df = impact.reactions(filings, px)
        reactions_rows = impact.table(df)
        table = {r["type"]: r for r in reactions_rows}
        daily_last = {t: float(px[t].iloc[-1]) for t in scen_defs if t in px and len(px[t])}
        daily_date = {t: str(px[t].index[-1].date()) for t in scen_defs if t in px and len(px[t])}
        status["prices:daily"] = "ok"
    except Exception as e:
        daily_last, daily_date = {}, {}
        status["prices:daily"] = f"failed {type(e).__name__}"
    for t in scen_defs:  # fall back to the cached weekly close
        daily_last.setdefault(t, float(weekly[t]["c"][-1]))
        daily_date.setdefault(t, weekly[t]["d"][-1])

    # events
    store = state.load_json(DATA / "events.json", {})
    cutoff = today - timedelta(days=EVENT_WINDOW_DAYS)
    for f in filings:
        kind = classify.classify_filing(f)
        if kind is None or date.fromisoformat(f["date"]) < cutoff or f["id"] in store:
            continue
        store[f["id"]] = {"id": f["id"], "ticker": f["ticker"], "date": f["date"], "type": kind, "source": "SEC filing",
                          "title": f"{f['form']}: {f['title']}"[:140], "url": f["url"], "nudge": _nudge(kind, table, False)}
    for t, hs in headlines.items():
        per_day = set()
        for h in hs:
            kind = classify.classify_headline(h["title"])
            key = (t, h["date"], kind)
            if kind is None or h["id"] in store or key in per_day or not h["date"] or not classify.mentions(h["title"], t):
                continue
            if date.fromisoformat(h["date"]) < cutoff:
                continue
            per_day.add(key)
            store[h["id"]] = {"id": h["id"], "ticker": t, "date": h["date"], "type": kind, "source": h["source"] or "News",
                              "title": h["title"][:140], "url": h["url"], "nudge": _nudge(kind, table, True)}
    store = {k: v for k, v in store.items() if date.fromisoformat(v["date"]) >= cutoff}

    # projections
    prev_state = state.load_json(DATA / "state.json", {})
    out_t, new_state, changes = {}, {}, []
    for t, defs in scen_defs.items():
        base = {s["k"]: s["base_p"] for s in _scen_for(t, scen_defs)}
        evs = [e for e in store.values() if e["ticker"] == t]
        tilt, top = state.active_tilt(evs, today)
        probs = state.apply_tilt(base, tilt)
        vol = prices.annual_vol(weekly[t])
        scen = [{**s, "p": round(probs[s["k"]], 4), "sigma": round(vol * s["vm"], 4)} for s in _scen_for(t, scen_defs)]
        price = daily_last[t]
        q = {m: state.mixture_quantiles(price, scen, m) for m in (3, 6, 12, 36)}
        w = weekly[t]["c"]
        out_t[t] = {"price": round(price, 4), "price_date": daily_date[t], "vol": round(vol, 4), "tilt_pts": round(tilt, 2),
                    "scen": scen, "quantiles": {str(m): v for m, v in q.items()},
                    "week_change": round(price / w[-2] - 1, 4) if len(w) > 1 else None, "top_events": top}
        new_state[t] = {k: round(v, 2) for k, v in probs.items()}
        old = prev_state.get(t)
        if old and any(round(old[k] * 100) != round(new_state[t][k] * 100) for k in new_state[t]):
            row = {"at": state.now_iso(), "ticker": t, "from": old, "to": new_state[t], "tilt_pts": round(tilt, 2),
                   "causes": [{"date": e["date"], "type": e["type"], "title": e["title"], "url": e["url"],
                               "effect_pts": round(e["contribution"], 2)} for e in top[:3]]}
            changes.append(row)
            state.append_jsonl(DATA / "changelog.jsonl", row)

    # weekly ledger rows (one per ticker per ISO week)
    wk = f"{today.isocalendar().year}-W{today.isocalendar().week:02d}"
    ledger_path = DATA / "ledger.jsonl"
    have = {(r["ticker"], r.get("week")) for r in state.read_jsonl(ledger_path)}
    for t, o in out_t.items():
        if (t, wk) in have:
            continue
        for m in (3, 6, 12):
            lo, mid, hi = o["quantiles"][str(m)]
            state.ledger_append(ledger_path, {"date": today.isoformat(), "week": wk, "ticker": t, "months": m,
                                              "price": o["price"], "p10": lo, "p50": mid, "p90": hi})
    score = state.score_ledger(state.read_jsonl(ledger_path), {t: o["price"] for t, o in out_t.items()}, today)
    score["chain_ok"] = state.ledger_verify(ledger_path)

    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "events.json").write_text(json.dumps(store, indent=1), encoding="utf-8")
    (DATA / "state.json").write_text(json.dumps(new_state, indent=1), encoding="utf-8")

    log = state.read_jsonl(DATA / "changelog.jsonl")[-30:][::-1]
    ev_list = sorted(store.values(), key=lambda e: e["date"], reverse=True)[:40]
    live = {"generated": state.now_iso(), "half_life_days": state.HALF_LIFE_DAYS, "tilt_cap_pts": state.CAP,
            "tickers": out_t, "events": ev_list, "headlines": {t: hs[:6] for t, hs in headlines.items()},
            "papers": uniq_papers[:10], "changelog": log, "reactions": reactions_rows, "scorecard": score, "status": status}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "live.json").write_text(json.dumps(live, separators=(",", ":")), encoding="utf-8")
    (OUT / "feed.xml").write_text(_rss(live), encoding="utf-8")
    (OUT / "digest.html").write_text(_digest(live), encoding="utf-8")
    return live


def _rss(live: dict) -> str:
    items = []
    for c in live["changelog"][:15]:
        title = f"{c['ticker']}: projection moved ({', '.join(f'{k} {c['from'][k]:.0%} to {c['to'][k]:.0%}' for k in c['to'])})"
        why = "; ".join(f"{x['type']}: {x['title']}" for x in c["causes"]) or "decay of earlier events"
        items.append(f"<item><title>{escape(title)}</title><description>{escape(why)}</description>"
                     f"<pubDate>{c['at']}</pubDate><guid>{c['at']}-{c['ticker']}</guid></item>")
    for e in live["events"][:15]:
        items.append(f"<item><title>{escape(e['ticker'] + ': ' + e['title'])}</title><link>{escape(e['url'])}</link>"
                     f"<description>{escape(e['type'])}</description><pubDate>{e['date']}</pubDate><guid>{escape(e['id'])}</guid></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Frontier Quantum: changes and announcements</title>'
            "<link>https://github.com/SOLAS33/frontier</link><description>Projection changes and tracked announcements. "
            f"Information only, not investment advice.</description>{''.join(items)}</channel></rss>")


def _digest(live: dict) -> str:
    rows = "".join(f"<tr><td>{t}</td><td>${o['price']:.2f}</td><td>{o['tilt_pts']:+.1f}</td>"
                   f"<td>${o['quantiles']['12'][0]:.2f} to ${o['quantiles']['12'][2]:.2f}</td></tr>" for t, o in live["tickers"].items())
    ev = "".join(f"<li>{escape(e['ticker'])} ({escape(e['type'])}): <a href=\"{escape(e['url'])}\">{escape(e['title'])}</a></li>"
                 for e in live["events"][:8])
    return ("<h2>Frontier Quantum: this week</h2><table border=1 cellpadding=6><tr><th>Stock</th><th>Price</th><th>News tilt (pts)</th>"
            f"<th>12-month range (10th to 90th)</th></tr>{rows}</table><h3>Announcements</h3><ul>{ev}</ul>"
            "<p>Information only, not investment advice. Ranges come from stated scenarios and are not forecasts.</p>")


if __name__ == "__main__":
    live = run(offline="--offline" in sys.argv)
    for t, o in live["tickers"].items():
        print(f"{t}: ${o['price']:.2f}  tilt {o['tilt_pts']:+.2f}  probs " + ", ".join(f"{s['k']} {s['p']:.0%}" for s in o["scen"]))
    print(f"{len(live['events'])} events, {len(live['changelog'])} changes, ledger rows {live['scorecard']['logged']}, status "
          + ", ".join(f"{k}={v}" for k, v in live["status"].items() if v != "ok" ) or "all ok")
