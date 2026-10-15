"""SVG charts drawn from numbers. Every colour is a CSS variable, so charts follow the page theme.

Lines carry `pathLength="1"` and class `draw`; the page script animates them in when scrolled to.
"""
from __future__ import annotations

import math
from datetime import date

FONT = 'font-family="var(--mono)"'


def _svg(w, h, body, label):
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid meet">'
            f"{body}</svg>")


def _num(v):
    if v >= 1e6:
        return f"{v / 1e6:g} million"
    if v >= 1000:
        return f"{v:,.0f}"
    if v >= 100:
        return f"{v:.0f}"
    if v >= 10:
        return f"{v:.0f}"
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _ord(d: str) -> float:
    y, m, dd = map(int, d.split("-"))
    return date(y, m, dd).toordinal()


def _log_ticks(lo, hi):
    out, e = [], math.floor(math.log10(lo))
    while 10 ** e <= hi * 1.001:
        for k in (1, 2, 5):
            v = k * 10 ** e
            if lo * 0.999 <= v <= hi * 1.001:
                out.append(v)
        e += 1
    return out


def fan_chart(hist: dict, sim: dict, name: str, w=900, h=420, history_weeks=104):
    """Last two years of real prices, then the scenario range for three years.
    Bands: 10th to 90th percentile of all scenarios mixed by the stated probabilities, and 25th to 75th."""
    m = {"l": 64, "r": 112, "t": 18, "b": 34}
    hd, hc = hist["d"][-history_weeks:], hist["c"][-history_weeks:]
    n_hist = len(hd)
    months = sim["months"]
    lo = min(min(hc), min(sim["mix"]["p10"]) * 0.9)
    hi = max(max(hc), max(sim["mix"]["p90"]) * 1.05)
    y0, y1 = math.log10(lo), math.log10(hi)
    total = n_hist - 1 + len(months) - 1 + 0  # x in weeks: history weeks, then months*4.345
    x_hist_w = n_hist - 1
    x_fut_w = (len(months) - 1) * 4.345
    span = x_hist_w + x_fut_w

    def X(wk):
        return m["l"] + wk / span * (w - m["l"] - m["r"])

    def Y(v):
        return m["t"] + (1 - (math.log10(max(v, lo * 0.5)) - y0) / (y1 - y0)) * (h - m["t"] - m["b"])

    g = []
    for t in _log_ticks(lo, hi):
        g.append(f'<line x1="{m["l"]}" x2="{w - m["r"]}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="grid"/>'
                 f'<text x="{m["l"] - 8}" y="{Y(t) + 4:.1f}" text-anchor="end">${_num(t)}</text>')
    today = X(x_hist_w)
    g.append(f'<line x1="{today:.1f}" x2="{today:.1f}" y1="{m["t"]}" y2="{h - m["b"]}" class="today"/>')
    g.append(f'<text x="{today + 6:.1f}" y="{m["t"] + 12}" class="t-amber">Today</text>')
    g.append(f'<text x="{m["l"]}" y="{h - 10}">{hd[0][:7]}</text>')
    g.append(f'<text x="{w - m["r"]}" y="{h - 10}" text-anchor="end">{36} months ahead</text>')

    def fut_pts(series):
        return [(X(x_hist_w + k * 4.345), Y(v)) for k, v in zip(months, series)]

    def band(upper, lower, cls):
        up, lw = fut_pts(upper), fut_pts(lower)
        pts = up + lw[::-1]
        return f'<polygon class="{cls}" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '"/>'

    g.append(band(sim["mix"]["p90"], sim["mix"]["p10"], "band-wide"))
    g.append(band(sim["mix"]["p75"], sim["mix"]["p25"], "band-mid"))
    for key, cls in (("bear", "sc-bear"), ("base", "sc-base"), ("bull", "sc-bull")):
        if key in sim["by_scenario"]:
            pts = fut_pts(sim["by_scenario"][key]["p50"])
            g.append(f'<path class="{cls} draw" pathLength="1" d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + '"/>')
    hp = [(X(i), Y(v)) for i, v in enumerate(hc)]
    g.append('<path class="hist draw" pathLength="1" d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in hp) + '"/>')
    g.append(f'<circle cx="{today:.1f}" cy="{Y(hc[-1]):.1f}" r="5" class="dot"/>')
    for key, lab, cls in (("p90", "90th", "t-teal"), ("p50", "middle", "t-fg"), ("p10", "10th", "t-red")):
        v = sim["mix"][key][-1]
        g.append(f'<text x="{w - m["r"] + 8}" y="{Y(v) + 4:.1f}" class="{cls}">${_num(v)} {lab}</text>')
    return _svg(w, h, "".join(g), f"{name}: recent price and three-year scenario range")


def bars_h(items, unit_fmt, w=900, bar_h=34, gap=10, left=250, lo_exp=1, hi_exp=8, highlight=None, label="Bar chart"):
    """Horizontal bars on a log scale. items: [(label, value)]."""
    right = 110
    h = 20 + len(items) * (bar_h + gap) + 36
    X = lambda v: left + (math.log10(v) - lo_exp) / (hi_exp - lo_exp) * (w - left - right)
    g = []
    for e in range(lo_exp, hi_exp + 1):
        x = X(10 ** e)
        g.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="10" y2="{h - 30}" class="grid"/>'
                 f'<text x="{x:.1f}" y="{h - 12}" text-anchor="middle">{unit_fmt(10 ** e)}</text>')
    for i, (lab, v) in enumerate(items):
        y = 20 + i * (bar_h + gap)
        cls = "bar-hi" if lab == highlight else "bar"
        g.append(f'<rect x="{left}" y="{y}" width="{X(v) - left:.1f}" height="{bar_h}" class="{cls} grow"/>'
                 f'<text x="{left - 10}" y="{y + bar_h / 2 + 4:.1f}" text-anchor="end" class="t-fg lbl">{lab}</text>'
                 f'<text x="{X(v) + 8:.1f}" y="{y + bar_h / 2 + 4:.1f}">about {unit_fmt(v)}</text>')
    return _svg(w, h, "".join(g), label)


def multiples(items, w=900, bar_h=34, gap=12, label="Biggest rises"):
    """items: [(label, from_text, multiple, kind)] drawn on a log axis from 1x to 100x."""
    left, right = 250, 130
    h = 20 + len(items) * (bar_h + gap) + 40
    X = lambda v: left + math.log10(v) / 2 * (w - left - right)
    g = []
    for k in (1, 2, 5, 10, 20, 50, 100):
        x = X(k)
        g.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="10" y2="{h - 34}" class="grid"/>'
                 f'<text x="{x:.1f}" y="{h - 14}" text-anchor="middle">{k}x</text>')
    for i, (lab, frm, mult, kind) in enumerate(items):
        y = 20 + i * (bar_h + gap)
        cls = {"lay": "bar", "quantum": "bar-hi", "ref": "bar-ref"}[kind]
        g.append(f'<rect x="{left}" y="{y}" width="{X(min(mult, 100)) - left:.1f}" height="{bar_h}" class="{cls} grow"/>'
                 f'<text x="{left - 10}" y="{y + 15}" text-anchor="end" class="t-fg lbl">{lab}</text>'
                 f'<text x="{left - 10}" y="{y + 30}" text-anchor="end">{frm}</text>'
                 f'<text x="{X(min(mult, 100)) + 8:.1f}" y="{y + bar_h / 2 + 4:.1f}" class="t-fg">{mult:.0f}x</text>')
    return _svg(w, h, "".join(g), label)


def roadmap(w=900, h=420):
    m = {"l": 70, "r": 30, "t": 20, "b": 40}
    x0, x1 = 2023, 2034
    X = lambda y: m["l"] + (y - x0) / (x1 - x0) * (w - m["l"] - m["r"])
    Y = lambda v: m["t"] + (1 - math.log10(v) / 5) * (h - m["t"] - m["b"])
    g = []
    for e in range(0, 6):
        g.append(f'<line x1="{m["l"]}" x2="{w - m["r"]}" y1="{Y(10 ** e):.1f}" y2="{Y(10 ** e):.1f}" class="grid"/>'
                 f'<text x="{m["l"] - 8}" y="{Y(10 ** e) + 4:.1f}" text-anchor="end">{10 ** e:,}</text>')
    for y in range(x0, x1 + 1):
        g.append(f'<text x="{X(y):.1f}" y="{h - m["b"] + 20}" text-anchor="middle">{y}</text>')
    g.append(f'<rect x="{m["l"]}" y="{Y(4000):.1f}" width="{w - m["l"] - m["r"]}" height="{Y(1000) - Y(4000):.1f}" class="band-amber"/>'
             f'<text x="{m["l"] + 8}" y="{Y(4000) - 6:.1f}" class="t-amber">Estimated need for useful chemistry: about 1,000 to 4,000 logical qubits</text>')
    pts = [(2025, 50, "Best shown so far: about 50", True), (2028, 1600, "IonQ target 1,600", False),
           (2029, 200, "IBM Starling target 200", False), (2030, 80000, "IonQ claim up to 80,000", False),
           (2033, 2000, "IBM Blue Jay target 2,000", False)]
    line = sorted([(X(a), Y(b)) for a, b, _, t in pts if not t])
    for i, (a, b, lab, solid) in enumerate(pts):
        x, y = X(a), Y(b)
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" class="{"pt-solid" if solid else "pt-hollow"}"/>'
                 f'<text x="{min(x + 14, w - 200):.1f}" y="{y + (-12 if a == 2030 else 5):.1f}" class="t-fg lbl">{lab}</text>')
    g.append(f'<text x="{m["l"] - 52}" y="{m["t"] + 8}" transform="rotate(-90 {m["l"] - 52} {m["t"] + 8})" text-anchor="end">Logical qubits (log scale)</text>')
    return _svg(w, h, "".join(g), "Logical qubits by year: best shown and company targets")


def ladder(steps, here, w=900, h=340):
    """A staircase of milestones. steps: [(title, note)], here: index of the step the field has reached."""
    n = len(steps)
    sw = (w - 40) / n
    g = []
    for i, (t, note) in enumerate(steps):
        x = 20 + i * sw
        sh = 40 + i * (h - 130) / (n - 1)
        y = h - 50 - sh
        cls = "step-done" if i <= here else "step-todo"
        g.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{sw - 6:.1f}" height="{sh:.1f}" class="{cls} grow"/>'
                 f'<text x="{x + 10:.1f}" y="{y + 20:.1f}" class="t-fg lbl step-t">{t}</text>')
        for k, line in enumerate(note.split("|")):
            g.append(f'<text x="{x + 10:.1f}" y="{y + 38 + k * 15:.1f}" class="step-n">{line}</text>')
    hx = 20 + here * sw + sw / 2
    g.append(f'<text x="{hx:.1f}" y="{h - 24}" text-anchor="middle" class="t-amber">&#9650; The field is here</text>')
    return _svg(w, h, "".join(g), "Milestone ladder from lab result to profit")


def line_gap(w=900, h=300):
    m = {"l": 90, "r": 20, "t": 20, "b": 64}
    bars = [("Practical chips today", 150, "bar"), ("Largest chip (Condor)", 1121, "bar"),
            ("RSA-2048, 2025 estimate", 1e6, "bar-hi"), ("RSA-2048, 2019 estimate", 2e7, "bar-ref")]
    Y = lambda v: m["t"] + (1 - math.log10(v) / 8) * (h - m["t"] - m["b"])
    g = []
    names = {0: "1", 1: "10", 2: "100", 3: "1,000", 4: "10,000", 5: "100,000", 6: "1 million", 7: "10 million", 8: "100 million"}
    for e in range(0, 9):
        g.append(f'<line x1="{m["l"]}" x2="{w - m["r"]}" y1="{Y(10 ** e):.1f}" y2="{Y(10 ** e):.1f}" class="grid"/>'
                 f'<text x="{m["l"] - 8}" y="{Y(10 ** e) + 4:.1f}" text-anchor="end">{names[e]}</text>')
    bw = 120
    gap = (w - m["l"] - m["r"] - len(bars) * bw) / (len(bars) + 1)
    for i, (lab, v, cls) in enumerate(bars):
        x = m["l"] + gap + i * (bw + gap)
        y = Y(v)
        g.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{h - m["b"] - y:.1f}" class="{cls} growv"/>'
                 f'<text x="{x + bw / 2:.1f}" y="{y - 6:.1f}" text-anchor="middle" class="t-fg">{v:,.0f}</text>'
                 f'<text x="{x + bw / 2:.1f}" y="{h - m["b"] + 20}" text-anchor="middle" class="lbl">{lab}</text>')
    return _svg(w, h, "".join(g), "Qubits on chips today against the estimated need to break RSA-2048")
