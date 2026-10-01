from app.models.finding import FindingRisk

def calculate_risk_score(
    severity_score: float,
    asset_criticality: float,
    exploitability: float,
    exposure: float,
    data_sensitivity: float,
) -> float:
    """
    Calculate a normalized CloudSentinel risk score from 0 to 100.

    Each input is expected to be between 0 and 10.
    """

    weights = {
        "severity": 0.30,
        "asset_criticality": 0.20,
        "exploitability": 0.20,
        "exposure": 0.15,
        "data_sensitivity": 0.15,
    }

    weighted_score = (
        severity_score * weights["severity"]
        + asset_criticality * weights["asset_criticality"]
        + exploitability * weights["exploitability"]
        + exposure * weights["exposure"]
        + data_sensitivity * weights["data_sensitivity"]
    )

    return round(weighted_score * 10, 2)

def calculate_risk(
    severity_score: float,
    asset_criticality: float,
    exploitability: float,
    exposure: float,
    data_sensitivity: float,
) -> FindingRisk:
    """
    Build the complete FindingRisk object.
    """

    risk_score = calculate_risk_score(
        severity_score=severity_score,
        asset_criticality=asset_criticality,
        exploitability=exploitability,
        exposure=exposure,
        data_sensitivity=data_sensitivity,
    )

    return FindingRisk(
        severity_score=severity_score,
        asset_criticality=asset_criticality,
        exploitability=exploitability,
        exposure=exposure,
        data_sensitivity=data_sensitivity,
        risk_score=risk_score,
    )