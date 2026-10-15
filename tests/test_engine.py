import pytest

from frontier import art, charts, prices
from frontier.scenarios import Scenario, simulate

SC = [Scenario("bear", "b", 0.4, -0.4, 0.75), Scenario("base", "m", 0.35, 0.1, 0.75), Scenario("bull", "u", 0.25, 0.5, 0.75)]


def test_simulation_is_deterministic_and_ordered():
    a, b = simulate(10.0, 0.9, SC, paths=4000), simulate(10.0, 0.9, SC, paths=4000)
    assert a["mix"]["p50"] == b["mix"]["p50"]
    for k in range(len(a["months"])):
        assert a["mix"]["p10"][k] <= a["mix"]["p25"][k] <= a["mix"]["p50"][k] <= a["mix"]["p75"][k] <= a["mix"]["p90"][k]
    assert a["mix"]["p50"][0] == 10.0
    bear, bull = a["by_scenario"]["bear"]["p50"][-1], a["by_scenario"]["bull"]["p50"][-1]
    assert bear < 10.0 < bull


def test_median_follows_stated_drift():
    r = simulate(100.0, 0.5, [Scenario("base", "m", 1.0, 0.10)], years=3, paths=20000)
    assert r["by_scenario"]["base"]["p50"][12] == pytest.approx(110.0, rel=0.03)


def test_probabilities_must_sum_to_one():
    with pytest.raises(AssertionError):
        simulate(10.0, 0.5, [Scenario("base", "m", 0.5, 0.0)])


def test_stats_and_best_run():
    s = {"d": ["2020-01-06", "2020-01-13", "2020-01-20", "2020-01-27"], "c": [10.0, 2.0, 8.0, 4.0]}
    st = prices.stats(s)
    assert st["peak"] == 10.0 and st["x_from_start"] == 0.4
    assert prices.best_run(s)["multiple"] == 4.0


def test_charts_and_art_return_svg():
    s = {"d": [f"2024-{m:02d}-01" for m in range(1, 13)] * 9, "c": [float(i + 1) for i in range(108)]}
    sim = simulate(s["c"][-1], 0.8, SC, paths=2000)
    for svg in (charts.fan_chart(s, sim, "x"), charts.roadmap(), charts.line_gap(),
                charts.multiples([("a", "from x", 10, "lay")]), art.hero_interference(), art.surface_code(), art.fridge()):
        assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
