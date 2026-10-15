"""Illustrations for Frontier Coin. Same rules as art.py: theme variables, drawn from simple shapes."""
from __future__ import annotations


def ledger():
    g = []
    for i in range(5):
        x = 20 + i * 76
        g.append(f'<rect x="{x}" y="40" width="62" height="70" class="fillp ln"/>'
                 f'<line x1="{x + 8}" y1="60" x2="{x + 54}" y2="60" class="ln"/><line x1="{x + 8}" y1="76" x2="{x + 44}" y2="76" class="ln"/>'
                 f'<line x1="{x + 8}" y1="92" x2="{x + 50}" y2="92" class="ln"/>')
        if i:
            g.append(f'<line x1="{x - 14}" y1="75" x2="{x}" y2="75" class="ln amber"/>')
    return ('<svg viewBox="0 0 400 170" class="art" role="img" aria-label="Five pages chained together, each pointing at the one before">'
            + "".join(g) + '<text x="20" y="150" class="lbl">Each page carries a fingerprint of the page before.</text>'
            '<text x="20" y="166" class="lbl">Change an old page and every later fingerprint breaks.</text></svg>')


def signature():
    return ('<svg viewBox="0 0 400 170" class="art" role="img" aria-label="A private key signs a message and a public key checks it">'
            '<rect x="20" y="30" width="110" height="60" class="fillp ln"/><text x="36" y="66" class="t-fg big">pay 1 coin</text>'
            '<path d="M130 60 H190" class="ln amber"/><polygon points="190,52 206,60 190,68" class="amber-f"/>'
            '<rect x="206" y="30" width="170" height="60" class="fillp ln"/><text x="220" y="56" class="t-fg lbl">message + signature</text>'
            '<text x="220" y="76" class="lbl">only your private key</text>'
            '<text x="20" y="130" class="lbl">Anyone can check the signature with your public key.</text>'
            '<text x="20" y="148" class="lbl">Nobody can forge it without the private key.</text></svg>')


def peg():
    return ('<svg viewBox="0 0 400 170" class="art" role="img" aria-label="A stablecoin held level against the dollar while Bitcoin swings">'
            '<line x1="20" y1="70" x2="380" y2="70" class="ln dash"/><text x="22" y="62" class="lbl">$1.00</text>'
            '<path d="M20 72 L80 69 L140 71 L200 70 L260 72 L320 69 L380 70" class="route"/>'
            '<path d="M20 120 Q60 40 100 100 T180 60 T260 140 T340 50 T380 110" fill="none" class="route fade1" stroke-width="3"/>'
            '<text x="20" y="160" class="lbl">A stablecoin tries to sit on the line. Bitcoin does not.</text></svg>')
