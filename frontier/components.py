"""HTML building blocks shared by every Frontier site, so the series looks and behaves the same way."""
from __future__ import annotations

import json
from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"


def credits() -> dict[str, dict]:
    p = ASSETS / "img" / "credits.json"
    if not p.exists():
        return {}
    return {c["file"]: c for c in json.loads(p.read_text(encoding="utf-8"))}


CREDITS = credits()


def credit_line(file: str) -> str:
    c = CREDITS.get(file)
    if not c:
        return ""
    who = (c.get("artist") or c.get("credit") or "").split("\n")[0][:70]
    return f'<a href="{c["page"]}" target="_blank" rel="noopener">{who}, {c["licence"]}</a>'


def photo(file: str, alt: str = "", caption: str = "", cls: str = "") -> str:
    c = CREDITS.get(file, {})
    alt = alt or c.get("alt", "")
    cap = f"{caption} " if caption else ""
    return (f'<figure class="fx-photo {cls}"><div class="fx-ph"><img src="img/{file}" alt="{alt}" loading="lazy" decoding="async"></div>'
            f'<figcaption>{cap}<span class="credit">Photo: {credit_line(file)}</span></figcaption></figure>')


def band(file: str, kicker: str, line: str, alt: str = "") -> str:
    c = CREDITS.get(file, {})
    return (f'<div class="fx-band" role="img" aria-label="{alt or c.get("alt", "")}"><div class="fx-band-img"><img src="img/{file}" alt="" '
            f'loading="lazy" decoding="async"></div><div class="fx-band-in"><div class="fx-kicker">{kicker}</div><p class="fx-band-line">{line}</p></div>'
            f'<span class="fx-credit">Photo: {credit_line(file)}</span></div>')


def note(label: str, html: str) -> str:
    return f'<aside class="note"><span class="note-l">{label}</span>{html}</aside>'


def fig(svg: str, caption: str, num: int | str = "", wide: bool = True) -> str:
    n = f'<b>Fig {num}.</b> ' if num != "" else ""
    return f'<figure class="fig {"wide" if wide else ""}">{svg}<figcaption>{n}{caption}</figcaption></figure>'


def chapter(cid: str, no: int, title: str, sub: str, body: str, key: str = "") -> str:
    return (f'<section class="fx-ch" id="{cid}" data-title="{title}"><header class="fx-ch-head wide"><div class="fx-no">{no:02d}</div>'
            f'<div><h2>{title}</h2><p class="fx-sub">{sub}</p></div></header>{key}{body}</section>')


def level(simple: str, general: str, expert: str) -> str:
    return f'<span class="lv s">{simple}</span><span class="lv g">{general}</span><span class="lv e">{expert}</span>'


def key_idea(title: str, simple: str, general: str, expert: str) -> str:
    return (f'<aside class="keyidea wide"><div class="fx-kicker">The idea in one breath</div><h3>{title}</h3>'
            f'<p>{level(simple, general, expert)}</p></aside>')
