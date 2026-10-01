from app.services.risk_engine import calculate_risk_score

def test_high_risk_finding():
    score = calculate_risk_score(
        severity_score=10,
        asset_criticality=10,
        exploitability=10,
        exposure=10,
        data_sensitivity=10,
    )

    assert score == 100

def test_low_risk_finding():
    score = calculate_risk_score(
        severity_score=1,
        asset_criticality=1,
        exploitability=1,
        exposure=1,
        data_sensitivity=1,
    )

    assert score == 10

def test_example_risk_score():
    score = calculate_risk_score(
        severity_score=8,
        asset_criticality=8,
        exploitability=7,
        exposure=6,
        data_sensitivity=7,
    )

    assert score == 73.5