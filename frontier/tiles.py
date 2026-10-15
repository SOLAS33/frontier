"""Small generated illustrations, one per Frontier site, used on the series home page and in the rail.

Each function returns an SVG that uses theme variables, so tiles follow light and dark. They are drawn from simple
maths (rings, lattices, orbits) rather than pasted artwork.
"""
from __future__ import annotations

import math
import random

W, H = 400, 240
TEAL, VIO, AMB, LINE = "var(--teal)", "var(--violet)", "var(--amber)", "var(--line)"


def _wrap(body: str, label: str) -> str:
    return (f'<svg viewBox="0 0 {W} {H}" class="tile-art" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid slice">'
            f'<rect width="{W}" height="{H}" fill="var(--bg2)"/>{body}</svg>')


def quantum():
    g = []
    for s, cx in enumerate((150, 250)):
        for r in range(14, 190, 16):
            g.append(f'<circle cx="{cx}" cy="120" r="{r}" fill="none" stroke="{TEAL if s == 0 else VIO}" stroke-width="1.3" opacity=".55"/>')
    g.append(f'<circle cx="150" cy="120" r="5" fill="{AMB}"/><circle cx="250" cy="120" r="5" fill="{AMB}"/>')
    return _wrap("".join(g), "Two sets of ripples overlapping")


def coin():
    g = []
    for i in range(6):
        x, y = 40 + i * 58, 150 - (i % 2) * 42
        g.append(f'<rect x="{x}" y="{y}" width="46" height="46" fill="none" stroke="{TEAL}" stroke-width="2"/>')
        if i:
            g.append(f'<line x1="{x - 12}" y1="{y + 23 + (42 if i % 2 else -42)}" x2="{x}" y2="{y + 23}" stroke="{VIO}" stroke-width="2"/>')
    g.append(f'<circle cx="200" cy="60" r="26" fill="none" stroke="{AMB}" stroke-width="3"/><text x="200" y="68" text-anchor="middle" fill="{AMB}" '
             f'style="font:700 22px var(--display)">B</text>')
    return _wrap("".join(g), "A chain of linked blocks")


def cell():
    g = []
    for r in range(3):
        for c in range(6):
            x, y = 36 + c * 56, 40 + r * 62
            lvl = 0.25 + ((r * 6 + c) % 5) * 0.18
            g.append(f'<rect x="{x}" y="{y}" width="44" height="50" rx="4" fill="none" stroke="{LINE}" stroke-width="2"/>'
                     f'<rect x="{x + 4}" y="{y + 4 + 42 * (1 - lvl):.0f}" width="36" height="{42 * lvl:.0f}" fill="{TEAL}" opacity=".8"/>'
                     f'<rect x="{x + 16}" y="{y - 5}" width="12" height="5" fill="{LINE}"/>')
    return _wrap("".join(g), "A grid of battery cells at different charge")


def mind():
    rnd = random.Random(4)
    pts = [(40 + rnd.random() * 320, 30 + rnd.random() * 180) for _ in range(26)]
    g = []
    for i, a in enumerate(pts):
        for b in pts[i + 1:i + 5]:
            if math.dist(a, b) < 120:
                g.append(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{VIO}" stroke-width="1" opacity=".6"/>')
    g += [f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{3 + (i % 3) * 2}" fill="{TEAL if i % 4 else AMB}"/>' for i, (x, y) in enumerate(pts)]
    return _wrap("".join(g), "A network of connected nodes")


def bot():
    g = [f'<rect x="60" y="190" width="120" height="14" fill="{LINE}"/>',
         f'<line x1="120" y1="190" x2="170" y2="120" stroke="{TEAL}" stroke-width="12" stroke-linecap="round"/>',
         f'<line x1="170" y1="120" x2="250" y2="90" stroke="{VIO}" stroke-width="10" stroke-linecap="round"/>',
         f'<line x1="250" y1="90" x2="300" y2="130" stroke="{AMB}" stroke-width="7" stroke-linecap="round"/>']
    for x, y in ((120, 190), (170, 120), (250, 90)):
        g.append(f'<circle cx="{x}" cy="{y}" r="13" fill="var(--bg2)" stroke="var(--fg)" stroke-width="3"/>')
    g.append(f'<path d="M300 130 l14 -10 m-14 10 l14 10" stroke="var(--fg)" stroke-width="4" fill="none"/>')
    return _wrap("".join(g), "A robot arm with three joints")


def atom():
    g = [f'<circle cx="200" cy="120" r="14" fill="{AMB}"/>']
    for k, rot in enumerate((0, 60, 120)):
        g.append(f'<ellipse cx="200" cy="120" rx="130" ry="46" fill="none" stroke="{TEAL if k != 1 else VIO}" stroke-width="2" '
                 f'transform="rotate({rot} 200 120)"/>')
        a = math.radians(rot + 40 * (k + 1))
        g.append(f'<circle cx="{200 + 130 * math.cos(a) * math.cos(math.radians(rot)) - 46 * math.sin(a) * math.sin(math.radians(rot)):.0f}" '
                 f'cy="{120 + 130 * math.cos(a) * math.sin(math.radians(rot)) + 46 * math.sin(a) * math.cos(math.radians(rot)):.0f}" r="6" fill="var(--fg)"/>')
    return _wrap("".join(g), "An atom with three electron orbits")


def fusion():
    g = [f'<ellipse cx="200" cy="120" rx="120" ry="78" fill="none" stroke="{LINE}" stroke-width="16"/>',
         f'<ellipse cx="200" cy="120" rx="90" ry="50" fill="none" stroke="{AMB}" stroke-width="5" opacity=".9"/>',
         f'<ellipse cx="200" cy="120" rx="60" ry="26" fill="none" stroke="{TEAL}" stroke-width="3" opacity=".8"/>']
    return _wrap("".join(g), "A doughnut-shaped fusion plasma chamber")


def drone():
    g = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = 200 + sx * 84, 120 + sy * 52
            g.append(f'<line x1="200" y1="120" x2="{x}" y2="{y}" stroke="{LINE}" stroke-width="6"/>'
                     f'<ellipse cx="{x}" cy="{y - 8}" rx="40" ry="7" fill="{TEAL}" opacity=".55"/><circle cx="{x}" cy="{y}" r="7" fill="var(--fg)"/>')
    g.append(f'<rect x="178" y="104" width="44" height="32" rx="8" fill="{VIO}"/><circle cx="200" cy="120" r="6" fill="{AMB}"/>')
    return _wrap("".join(g), "A four-rotor drone seen from above")


def shield():
    g = [f'<path d="M200 28 L296 62 V124 C296 170 252 204 200 222 C148 204 104 170 104 124 V62 Z" fill="none" stroke="{TEAL}" stroke-width="4"/>',
         f'<path d="M200 56 L268 80 V124 C268 156 238 180 200 194 C162 180 132 156 132 124 V80 Z" fill="none" stroke="{VIO}" stroke-width="3" opacity=".8"/>']
    for r in (30, 52, 74):
        g.append(f'<path d="M{200 - r} 120 A{r} {r} 0 0 1 {200 + r} 120" fill="none" stroke="{AMB}" stroke-width="2" opacity="{1 - r / 110:.2f}"/>')
    return _wrap("".join(g), "A shield with radiating waves")


def carbon():
    g = []
    r = 22
    for row in range(5):
        for col in range(9):
            cx = 30 + col * r * 1.74 + (r * 0.87 if row % 2 else 0)
            cy = 36 + row * r * 1.5
            pts = " ".join(f"{cx + r * math.cos(math.radians(60 * k + 30)):.1f},{cy + r * math.sin(math.radians(60 * k + 30)):.1f}" for k in range(6))
            g.append(f'<polygon points="{pts}" fill="none" stroke="{TEAL}" stroke-width="1.8" opacity=".85"/>')
    return _wrap("".join(g), "A honeycomb lattice of carbon atoms")


def tide():
    g = []
    for k in range(6):
        y = 70 + k * 24
        d = "M0 %d " % y + " ".join(f"Q{x + 25} {y - 18 if (x // 50) % 2 == 0 else y + 18} {x + 50} {y}" for x in range(0, 400, 50))
        g.append(f'<path d="{d}" fill="none" stroke="{TEAL if k % 2 == 0 else VIO}" stroke-width="2.4" opacity="{0.9 - k * 0.1:.2f}"/>')
    g.append(f'<circle cx="320" cy="40" r="18" fill="{AMB}"/>')
    return _wrap("".join(g), "Layers of ocean waves under the sun")


def gene():
    g = []
    for i in range(0, 400, 20):
        y1 = 120 + 60 * math.sin(i / 38)
        y2 = 120 - 60 * math.sin(i / 38)
        g.append(f'<line x1="{i}" y1="{y1:.0f}" x2="{i}" y2="{y2:.0f}" stroke="{LINE}" stroke-width="2"/>'
                 f'<circle cx="{i}" cy="{y1:.0f}" r="5" fill="{TEAL}"/><circle cx="{i}" cy="{y2:.0f}" r="5" fill="{AMB}"/>')
    return _wrap("".join(g), "A double helix")


def orbit():
    g = [f'<circle cx="150" cy="130" r="48" fill="{TEAL}" opacity=".85"/>',
         f'<ellipse cx="170" cy="120" rx="170" ry="60" fill="none" stroke="{VIO}" stroke-width="2" transform="rotate(-18 170 120)"/>',
         f'<circle cx="305" cy="62" r="8" fill="{AMB}"/><circle cx="55" cy="190" r="5" fill="var(--fg)"/>']
    return _wrap("".join(g), "A planet with a satellite on an elliptical orbit")


def chip():
    g = [f'<rect x="140" y="70" width="120" height="100" fill="none" stroke="{TEAL}" stroke-width="3"/><rect x="170" y="95" width="60" height="50" fill="{VIO}" opacity=".7"/>']
    for k in range(5):
        x = 150 + k * 25
        g.append(f'<line x1="{x}" y1="70" x2="{x}" y2="40" stroke="{LINE}" stroke-width="3"/><line x1="{x}" y1="170" x2="{x}" y2="200" stroke="{LINE}" stroke-width="3"/>')
    for k in range(4):
        y = 85 + k * 25
        g.append(f'<line x1="140" y1="{y}" x2="108" y2="{y}" stroke="{LINE}" stroke-width="3"/><line x1="260" y1="{y}" x2="292" y2="{y}" stroke="{LINE}" stroke-width="3"/>')
    g.append(f'<path d="M20 205 H90 V150 H108 M380 40 H310 V100 H292" fill="none" stroke="{AMB}" stroke-width="2"/>')
    return _wrap("".join(g), "A microchip with connecting traces")


def chain():
    g = []
    for i in range(4):
        x = 30 + i * 90
        g.append(f'<rect x="{x}" y="90" width="70" height="60" rx="6" fill="none" stroke="{TEAL if i % 2 else VIO}" stroke-width="3"/>')
        if i:
            g.append(f'<line x1="{x - 20}" y1="120" x2="{x}" y2="120" stroke="{AMB}" stroke-width="3" stroke-dasharray="4 3"/>')
    g.append(f'<path d="M30 60 H380 M30 180 H380" stroke="{LINE}" stroke-width="2" stroke-dasharray="3 6"/>')
    return _wrap("".join(g), "Blocks linked in a chain with proofs above and below")


ART = {"chain": chain, "quantum": quantum, "coin": coin, "cell": cell, "mind": mind, "bot": bot, "atom": atom, "fusion": fusion, "drone": drone,
       "shield": shield, "carbon": carbon, "tide": tide, "gene": gene, "orbit": orbit, "chip": chip}


def tile(slug: str) -> str:
    return ART[slug]()
