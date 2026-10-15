from datetime import date

import pandas as pd
import pytest

from frontier.live import classify, impact, state


def test_classify_filings_and_headlines():
    assert classify.classify_filing({"form": "8-K", "items": "3.02,9.01"}) == "share_sale"
    assert classify.classify_filing({"form": "8-K", "items": "2.02,9.01"}) == "earnings"
    assert classify.classify_filing({"form": "424B5", "items": ""}) == "share_sale"
    assert classify.classify_filing({"form": "4", "items": ""}) is None
    assert classify.classify_headline("IonQ prices $1 billion offering of shares") == "share_sale"
    assert classify.classify_headline("Quantinuum shows 50 logical qubits with error correction") == "technical"
    assert classify.classify_headline("Local weather turns warm") is None


def test_tilt_decays_and_is_capped():
    today = date(2026, 10, 15)
    ev = [{"date": "2026-10-15", "nudge": 2.0}, {"date": "2026-09-15", "nudge": 2.0}]
    net, top = state.active_tilt(ev, today)
    assert net == pytest.approx(2.0 + 1.0, abs=0.05)        # a 30 day old event counts half
    big = [{"date": "2026-10-15", "nudge": 5.0}] * 10
    assert state.active_tilt(big, today)[0] == state.CAP
    assert state.active_tilt([{"date": "2026-10-15", "nudge": -50}], today)[0] == -state.CAP


def test_apply_tilt_keeps_probabilities_valid():
    base = {"bear": 0.40, "base": 0.35, "bull": 0.25}
    up = state.apply_tilt(base, 10)
    assert sum(up.values()) == pytest.approx(1.0) and up["bull"] == pytest.approx(0.35) and up["bear"] == pytest.approx(0.30)
    low = state.apply_tilt({"bear": 0.08, "base": 0.5, "bull": 0.42}, 12)
    assert low["bear"] >= state.FLOOR - 1e-9
    assert state.apply_tilt(base, -12)["bull"] >= state.FLOOR


def test_mixture_quantiles_order_and_single_scenario_median():
    scen = [{"p": 1.0, "drift": 0.10, "sigma": 0.5}]
    q = state.mixture_quantiles(100.0, scen, 12)
    assert q[0] < q[1] < q[2]
    assert q[1] == pytest.approx(110.0, rel=0.01)


def test_ledger_chain_detects_tampering(tmp_path):
    p = tmp_path / "ledger.jsonl"
    for i in range(3):
        state.ledger_append(p, {"date": "2026-10-15", "ticker": "X", "months": 3, "price": 1.0 + i, "p10": 0.5, "p50": 1.0, "p90": 2.0})
    assert state.ledger_verify(p)
    txt = p.read_text().replace('"price":2.0', '"price":9.0')
    p.write_text(txt)
    assert not state.ledger_verify(p)


def test_scoring_only_counts_due_rows():
    rows = [{"date": "2026-01-01", "ticker": "X", "months": 3, "p10": 5, "p50": 10, "p90": 20},
            {"date": "2026-10-01", "ticker": "X", "months": 3, "p10": 5, "p50": 10, "p90": 20}]
    s = state.score_ledger(rows, {"X": 25.0}, date(2026, 10, 15))
    assert s["logged"] == 2 and s["scored"] == 1 and s["rows"][0]["result"] == "above" and s["coverage"] == 0.0


def test_effective_date_after_close_moves_to_next_session():
    f = {"date": "2026-10-14", "accepted": "2026-10-14T21:30:00.000Z"}   # 5:30pm New York
    assert impact.effective_date(f) == pd.Timestamp("2026-10-15")
    g = {"date": "2026-10-14", "accepted": "2026-10-14T13:00:00.000Z"}   # 9am New York
    assert impact.effective_date(g) == pd.Timestamp("2026-10-14")


def test_reaction_table_counts_and_flags_small_samples():
    idx = pd.bdate_range("2024-01-01", periods=120)
    stock = pd.Series(100.0, index=idx)
    bench = pd.Series(100.0, index=idx)
    stock.iloc[41:] = 110.0                                   # +10% the day after a filing on idx[40]
    f = [{"ticker": "X", "date": str(idx[40].date()), "accepted": None, "form": "8-K", "items": "3.02"}]
    df = impact.reactions(f, {"X": stock, "QQQ": bench})
    assert len(df) == 1 and df.iloc[0]["type"] == "share_sale" and df.iloc[0]["r1"] == pytest.approx(0.0)
    f2 = [{**f[0], "date": str(idx[41].date())}]
    df2 = impact.reactions(f2, {"X": stock, "QQQ": bench})
    t = impact.table(df2)
    assert t[0]["n"] == 1 and t[0]["enough"] is False
