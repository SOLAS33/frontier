"""Three-year share-price scenarios.

This is not a forecast engine. Each company gets named scenarios (what happens to its milestones), an assumed
yearly drift for each and a probability the author assigns. Volatility comes from the last two years of real
weekly prices, scaled down by `vol_mult` because the 2024-25 swings are unlikely to persist unabated. The Monte Carlo then turns those assumptions into a range of outcomes per month, so a reader
can see how wide the plausible spread is and what the assumptions imply. Change the assumptions, the range moves.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Scenario:
    key: str            # bear | base | bull
    label: str
    probability: float
    drift: float        # assumed TYPICAL (median) price change per year, e.g. -0.35 = falls 35% a year
    vol_mult: float = 1.0


def simulate(price: float, vol: float, scenarios: list[Scenario], years: int = 3, paths: int = 20000, seed: int = 11):
    """Returns {'months': [0..12*years], 'by_scenario': {key: {'p10','p50','p90'}}, 'mix': {'p10','p25','p50','p75','p90'},
    'prob_below_start': x, 'prob_double': x, 'prob_half': x} with prices at each month."""
    assert abs(sum(s.probability for s in scenarios) - 1) < 1e-9, "scenario probabilities must sum to 1"
    rng = np.random.default_rng(seed)
    steps = 12 * years
    dt = 1 / 12
    out, mix_paths = {}, []
    for s in scenarios:
        n = int(round(paths * s.probability))
        sigma = vol * s.vol_mult
        mu = np.log1p(s.drift)                       # median log growth per year; volatility then only widens the spread
        z = rng.standard_normal((n, steps))
        log_ret = mu * dt + sigma * np.sqrt(dt) * z
        p = price * np.exp(np.cumsum(log_ret, axis=1))
        p = np.concatenate([np.full((n, 1), price), p], axis=1)
        out[s.key] = {f"p{q}": np.percentile(p, q, axis=0).round(4).tolist() for q in (10, 50, 90)}
        mix_paths.append(p)
    allp = np.concatenate(mix_paths, axis=0)
    end = allp[:, -1]
    return {
        "months": list(range(steps + 1)),
        "by_scenario": out,
        "mix": {f"p{q}": np.percentile(allp, q, axis=0).round(4).tolist() for q in (10, 25, 50, 75, 90)},
        "prob_below_start": float((end < price).mean()),
        "prob_double": float((end >= 2 * price).mean()),
        "prob_half": float((end <= 0.5 * price).mean()),
        "end_p10": float(np.percentile(end, 10)), "end_p50": float(np.percentile(end, 50)),
        "end_p90": float(np.percentile(end, 90)),
    }
