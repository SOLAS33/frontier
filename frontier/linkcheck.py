"""Checks that every reference link answers. Run with `python build.py quantum --check-links`.

Publishers block HEAD or bots often, so 403/405/429 count as 'reachable but unverified', not broken.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import httpx

SOFT = {401, 403, 405, 429, 999}


def check(urls: list[str], timeout: float = 20.0) -> dict[str, str]:
    def one(u: str) -> tuple[str, str]:
        try:
            with httpx.Client(follow_redirects=True, timeout=timeout, headers={"User-Agent": "Mozilla/5.0 frontier-linkcheck"}) as c:
                r = c.head(u)
                if r.status_code in SOFT or r.status_code >= 400:
                    r = c.get(u)
                if r.status_code < 400:
                    return u, "ok"
                return u, "unverified" if r.status_code in SOFT else f"broken {r.status_code}"
        except Exception as e:  # network trouble is reported, never raised
            return u, f"error {type(e).__name__}"

    with ThreadPoolExecutor(8) as ex:
        return dict(ex.map(one, urls))
