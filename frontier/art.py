"""Generated illustrations. Each function returns an SVG string drawn from real maths, not pasted artwork.

hero_interference: two wave sources; every dot's size is the summed wave amplitude at that point, so the bright
                   fringes are real constructive interference, the thing quantum algorithms are built to exploit.
"""
from __future__ import annotations

import math

import numpy as np


def hero_interference(w=900, h=520, cols=70, k=0.09, seed=3):
    rng = np.random.default_rng(seed)
    sx = [w * 0.30, w * 0.70]
    sy = h * 0.50
    dots = []
    xs = np.linspace(14, w - 14, cols)
    rows = int(cols * h / w)
    ys = np.linspace(14, h - 14, rows)
    for gi, y in enumerate(ys):
        for x in xs:
            r1 = math.hypot(x - sx[0], y - sy)
            r2 = math.hypot(x - sx[1], y - sy)
            a = (math.cos(k * r1) + math.cos(k * r2)) / 2          # -1..1
            amp = (a + 1) / 2                                        # 0..1
            if amp < 0.55:
                continue
            r = 1.2 + (amp - 0.55) / 0.45 * 4.2
            grp = int(rng.integers(0, 3))
            dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" class="hd g{grp}"/>')
    rings = []
    for i, sxi in enumerate(sx):
        for j in range(5):
            rings.append(f'<circle cx="{sxi:.0f}" cy="{sy:.0f}" r="20" class="ring" style="animation-delay:{-(j * 1.6 + i * 0.8):.1f}s"/>')
    srcs = "".join(f'<circle cx="{x:.0f}" cy="{sy:.0f}" r="6" class="src"/>' for x in sx)
    return (f'<svg class="hero-art" viewBox="0 0 {w} {h}" role="img" aria-label="Two wave sources whose ripples add and cancel, '
            f'leaving bright bands where the waves line up">{"".join(rings)}{"".join(dots)}{srcs}</svg>')


def bloch(size=300):
    return f'''<svg viewBox="0 0 300 300" class="art" role="img" aria-label="A qubit drawn as a sphere with its state arrow">
<g class="spin"><circle cx="150" cy="150" r="100" class="fillp"/><ellipse cx="150" cy="150" rx="100" ry="32" class="ln"/>
<ellipse cx="150" cy="150" rx="32" ry="100" class="ln dash"/></g>
<line x1="150" y1="30" x2="150" y2="270" class="axis"/>
<line x1="150" y1="150" x2="222" y2="86" class="arrow"/><polygon points="222,86 208,88 216,100" class="arrowhead"/>
<line x1="222" y1="86" x2="222" y2="150" class="ln dash amber"/><circle cx="150" cy="150" r="4" class="teal-f"/>
<text x="162" y="30" class="t-teal big">|0&#x27E9;</text><text x="162" y="278" class="t-teal big">|1&#x27E9;</text></svg>'''


def surface_code(d=5):
    s, n = 38, 2 * d - 1
    wd = n * s + 20
    g = []
    for r in range(n):
        for c in range(n):
            cx, cy = 20 + c * s, 20 + r * s
            if c < n - 1:
                g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + s}" y2="{cy}" class="ln"/>')
            if r < n - 1:
                g.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy + s}" class="ln"/>')
    for r in range(n):
        for c in range(n):
            cx, cy = 20 + c * s, 20 + r * s
            data = (r + c) % 2 == 0
            g.append(f'<circle cx="{cx}" cy="{cy}" r="11" class="{"q-data" if data else "q-check"}" '
                     f'style="animation-delay:{(r * n + c) * 0.025:.2f}s"/>')
    return f'<svg viewBox="0 0 {wd} {wd}" class="art" role="img" aria-label="Grid of {n * n} qubits: data qubits and checking qubits">{"".join(g)}</svg>'


def fridge():
    L = [("Room temperature", "300 K"), ("Plate one", "50 K"), ("Plate two", "4 K, liquid helium"), ("Still", "0.8 K"),
         ("Cold plate", "0.1 K"), ("Mixing chamber and chip", "0.01 K")]
    cx, g = 230, []
    for i, (a, b) in enumerate(L):
        y, wdt = 24 + i * 54, 360 - i * 48
        if i:
            g.append(f'<line x1="{cx}" y1="{y - 38}" x2="{cx}" y2="{y}" class="axis"/>')
        g.append(f'<rect x="{cx - wdt / 2}" y="{y}" width="{wdt}" height="16" class="{"fr-cold" if i == 5 else "fr"}"/>'
                 f'<text x="{cx + wdt / 2 + 14}" y="{y + 13}" class="t-fg lbl">{a}: {b}</text>')
    return f'<svg viewBox="0 0 860 360" class="art wide" role="img" aria-label="Dilution refrigerator plates from 300 kelvin down to 0.01 kelvin">{"".join(g)}</svg>'


def coin_vs_spin():
    return '''<svg viewBox="0 0 400 200" class="art" role="img" aria-label="A coin lying heads up beside a coin spinning in the air">
<ellipse cx="95" cy="150" rx="55" ry="14" class="fillp"/><ellipse cx="95" cy="142" rx="55" ry="14" class="coin"/>
<text x="80" y="147" class="t-fg big">H</text><text x="52" y="188" class="lbl">Ordinary bit: heads or tails</text>
<g class="coin-spin"><ellipse cx="300" cy="90" rx="46" ry="46" class="coin"/></g>
<ellipse cx="300" cy="170" rx="40" ry="7" class="shadow"/>
<text x="228" y="196" class="lbl">Qubit: spinning, both until it lands</text></svg>'''


def maze():
    return '''<svg viewBox="0 0 400 200" class="art" role="img" aria-label="A maze solved one path at a time, and a maze where every path is tried and the wrong ones fade">
<g class="ln"><rect x="10" y="20" width="170" height="150"/><path d="M10 70h110M60 120h120M120 70v50M60 20v50"/></g>
<path d="M18 45 H50 V95 H100 V145 H172" class="route"/><text x="14" y="190" class="lbl">One path at a time</text>
<g class="ln"><rect x="220" y="20" width="170" height="150"/><path d="M220 70h110M270 120h120M330 70v50M270 20v50"/></g>
<path d="M228 45 H260 V95 H310 V145 H382" class="route"/>
<path d="M228 45 H260 V145 H300" class="route fade1"/><path d="M228 95 H310 V50 H380" class="route fade2"/>
<text x="224" y="190" class="lbl">All paths, wrong ones cancel</text></svg>'''


def combo_lock():
    g = []
    for i in range(6):
        x = 40 + i * 52
        g.append(f'<rect x="{x}" y="50" width="38" height="70" class="fillp ln"/><text x="{x + 12}" y="95" class="t-fg big">{[7,3,9,1,5,2][i]}</text>')
    return ('<svg viewBox="0 0 380 190" class="art" role="img" aria-label="A six-digit lock: a million combinations to try one by one">'
            + "".join(g) +
            '<text x="40" y="160" class="lbl">1,000,000 combinations. A normal computer tries them</text>'
            '<text x="40" y="178" class="lbl">in turn; Grover search needs about 1,000 steps.</text></svg>')


def modality(kind):
    icons = {
        "sc": '<rect x="8" y="8" width="64" height="40" class="ln thick"/><path d="M20 28h12m8 0h12" class="ln thick"/><circle cx="36" cy="28" r="4" class="amber-f"/>',
        "ion": '<path d="M8 28h64" class="ln thick"/><circle cx="20" cy="28" r="6" class="teal-f"/><circle cx="40" cy="28" r="6" class="teal-f"/><circle cx="60" cy="28" r="6" class="teal-f"/><path d="M40 6v14" class="amber-s"/>',
        "atom": "".join(f'<circle cx="{16 + 16 * c}" cy="{14 + 16 * r}" r="4" class="teal-f"/>' for r in range(3) for c in range(4)),
        "photon": '<path d="M6 40 Q20 8 36 28 T72 16" class="amber-s" fill="none"/><circle cx="6" cy="40" r="4" class="teal-f"/><circle cx="72" cy="16" r="4" class="teal-f"/>',
        "spin": '<circle cx="40" cy="28" r="18" class="ln thick"/><path d="M40 14v28" class="amber-s"/><polygon points="40,10 34,20 46,20" class="amber-f"/>',
    }
    return f'<svg viewBox="0 0 80 56" class="icon">{icons[kind]}</svg>'


def hero_chain(w=900, h=520, seed=7):
    """A chain of linked blocks with a few glowing nodes: the hero art for crypto sites."""
    rng = np.random.default_rng(seed)
    g = []
    x = 40
    prev = None
    i = 0
    while x < w - 80:
        bw, bh = int(rng.integers(70, 120)), int(rng.integers(60, 110))
        y = int(h * 0.5 + rng.integers(-110, 110) - bh / 2)
        g.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" class="blk b{i % 3}"/>')
        for k in range(3):
            g.append(f'<line x1="{x + 10}" y1="{y + 16 + k * 14}" x2="{x + bw - 10 - int(rng.integers(0, 30))}" y2="{y + 16 + k * 14}" class="blkl"/>')
        if prev:
            g.append(f'<line x1="{prev[0]}" y1="{prev[1]}" x2="{x}" y2="{y + bh // 2}" class="chn"/>')
        prev = (x + bw, y + bh // 2)
        g.append(f'<circle cx="{x + bw}" cy="{y + bh // 2}" r="5" class="nd"/>')
        x += bw + int(rng.integers(26, 54))
        i += 1
    return (f'<svg class="hero-art chain" viewBox="0 0 {w} {h}" role="img" aria-label="A chain of linked blocks">{"".join(g)}</svg>')
