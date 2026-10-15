"""Reads config.toml once, so every module sees the same series settings."""
from __future__ import annotations

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = tomllib.loads((ROOT / "config.toml").read_text(encoding="utf-8"))
SERIES = CFG["series"]
SITES = CFG["sites"]
WATCH = CFG.get("watch", {})
WATCH_SITES = CFG.get("watch_sites", [])
