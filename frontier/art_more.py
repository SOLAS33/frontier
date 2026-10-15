"""Hero artwork for Mind, Atom and Cell. Same conventions as art.py: classes styled in frontier.css, drawn from simple maths."""
from __future__ import annotations

import math

import numpy as np


def hero_network(w=900, h=520, seed=5):
    """Layers of nodes joined by faint edges, a few lit: a neural network seen from the side."""
    rng = np.random.default_rng(seed)
    layers = [5, 8, 9, 8, 5]
    xs = np.linspace(80, w - 80, len(layers))
    pts = []
    for li, n in enumerate(layers):
        ys = np.linspace(70, h - 70, n) + rng.normal(0, 6, n)
        pts.append([(float(xs[li]), float(y)) for y in ys])
    g = []
    for a, b in zip(pts, pts[1:]):
        for p in a:
            for q in b:
                if rng.random() < 0.45:
                    g.append(f'<line x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}" class="nnl"/>')
    for li, layer in enumerate(pts):
        for p in layer:
            lit = rng.random() < 0.22
            g.append(f'<circle cx="{p[0]:.0f}" cy="{p[1]:.0f}" r="{7 if lit else 4.5}" class="{"nnd lit" if lit else "nnd"}"/>')
    return f'<svg class="hero-art net" viewBox="0 0 {w} {h}" role="img" aria-label="Layers of connected nodes, a few of them lit">{"".join(g)}</svg>'


def hero_reactor(w=900, h=520):
    """Concentric rings with orbiting dots: the glow around a reactor core."""
    cx, cy = w * 0.62, h * 0.5
    g = []
    for i, r in enumerate(range(40, 330, 38)):
        g.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" class="rr r{i % 3}"/>')
    rng = np.random.default_rng(2)
    for k in range(34):
        a = rng.random() * math.tau
        r = 60 + rng.random() * 250
        g.append(f'<circle cx="{cx + r * math.cos(a):.0f}" cy="{cy + r * math.sin(a):.0f}" r="{2 + rng.random() * 3:.1f}" class="rd"/>')
    g.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="22" class="rc"/>')
    return f'<svg class="hero-art reactor" viewBox="0 0 {w} {h}" role="img" aria-label="Glowing rings around a reactor core">{"".join(g)}</svg>'


def hero_cells(w=900, h=520, seed=9):
    """A grid of battery cells at different charge levels."""
    rng = np.random.default_rng(seed)
    g = []
    cols, rows = 12, 6
    cw, ch = 54, 74
    x0 = (w - cols * (cw + 14)) / 2 + 20
    y0 = (h - rows * (ch + 14)) / 2
    for r in range(rows):
        for c in range(cols):
            x, y = x0 + c * (cw + 14), y0 + r * (ch + 14)
            lvl = float(rng.random()) * 0.8 + 0.15
            g.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{cw}" height="{ch}" rx="5" class="bc"/>'
                     f'<rect x="{x + 18:.0f}" y="{y - 5:.0f}" width="18" height="5" class="bt"/>'
                     f'<rect x="{x + 5:.0f}" y="{y + 5 + (ch - 10) * (1 - lvl):.0f}" width="{cw - 10}" height="{(ch - 10) * lvl:.0f}" class="bf"/>')
    return f'<svg class="hero-art cells" viewBox="0 0 {w} {h}" role="img" aria-label="A grid of battery cells at different charge levels">{"".join(g)}</svg>'
