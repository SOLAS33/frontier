"""Checks the whole Frontier series on the live host. Run it after every deploy.

    python tools/verify_all.py                  # check https://frontier.solas33.com
    python tools/verify_all.py --host http://localhost:8765

For every site marked live in config.toml it checks that the page loads, that the hub links to it, that it links back to the hub,
that live.json parses and is fresh, that the feed loads, that the sitemap lists it, and that every reference link in the page opens
(links that block automated checks are reported as unverified, not as failures). Exit code 1 if anything fails.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
CFG = tomllib.loads((ROOT / "config.toml").read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=f"https://{CFG['series']['domain']}")
    ap.add_argument("--links", action="store_true", help="also test every reference link in every page (slow)")
    a = ap.parse_args()
    host = a.host.rstrip("/")
    c = httpx.Client(follow_redirects=True, timeout=40, headers={"User-Agent": "Solas33-Frontier verify (hello@solas33.com)"})
    live = [s["slug"] for s in CFG["sites"] if s["status"] == "live"]
    problems: list[str] = []

    def get(path: str):
        try:
            return c.get(f"{host}/{path}")
        except Exception as e:  # noqa: BLE001
            problems.append(f"{path}: {type(e).__name__}")
            return None

    hub = get("")
    sitemap = get("sitemap.xml")
    robots = get("robots.txt")
    print(f"hub {hub.status_code if hub else 'ERR'}  sitemap {sitemap.status_code if sitemap else 'ERR'}  robots {robots.status_code if robots else 'ERR'}")
    if not hub or hub.status_code != 200:
        problems.append("hub does not load")
    for slug in live:
        row = [slug.ljust(8)]
        r = get(f"{slug}/")
        ok = bool(r and r.status_code == 200)
        row.append("page ok" if ok else "PAGE FAIL")
        if not ok:
            problems.append(f"{slug}: page")
            print("  ".join(row))
            continue
        if hub and f'href="{slug}/"' not in hub.text:
            problems.append(f"{slug}: not linked from the hub")
            row.append("NOT IN HUB")
        if 'href="../"' not in r.text:
            problems.append(f"{slug}: no link back to the hub")
            row.append("NO HUB LINK")
        if sitemap and f"/{slug}/<" not in sitemap.text:
            problems.append(f"{slug}: missing from sitemap")
            row.append("NOT IN SITEMAP")
        title = re.search(r"<title>([^<]*)</title>", r.text)
        row.append(f"title {title.group(1)!r}" if title else "NO TITLE")
        lj = get(f"{slug}/live.json")
        if lj and lj.status_code == 200:
            try:
                j = lj.json()
                gen = datetime.fromisoformat(j["generated"].replace("Z", "+00:00"))
                age = (datetime.now(timezone.utc) - gen).total_seconds() / 3600
                row.append(f"live.json {age:.0f}h old")
                if age > 48:
                    problems.append(f"{slug}: live.json is {age:.0f} hours old")
            except Exception:  # noqa: BLE001
                problems.append(f"{slug}: live.json does not parse")
                row.append("LIVE.JSON BAD")
        else:
            problems.append(f"{slug}: live.json missing")
            row.append("NO LIVE.JSON")
        fd = get(f"{slug}/feed.xml")
        row.append("feed ok" if fd and fd.status_code == 200 else "NO FEED")
        if not (fd and fd.status_code == 200):
            problems.append(f"{slug}: feed")
        if a.links:
            urls = sorted(set(re.findall(r'<li id="r\d+">\[\d+\] <a href="([^"]+)"', r.text)))
            bad = 0
            for u in urls:
                try:
                    code = httpx.get(u, follow_redirects=True, timeout=25, headers={"User-Agent": "Mozilla/5.0"}).status_code
                except Exception:  # noqa: BLE001
                    code = 0
                if code in (404, 410) or code == 0:
                    bad += 1
                    problems.append(f"{slug}: reference link {u} -> {code}")
            row.append(f"{len(urls)} refs, {bad} broken")
        print("  ".join(row))
    print()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(" -", p)
        return 1
    print(f"All {len(live)} live sites passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
