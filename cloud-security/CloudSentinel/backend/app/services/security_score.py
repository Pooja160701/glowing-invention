from sqlalchemy.orm import Session
from app.db.models import Finding

def calculate_security_score(db: Session) -> dict:
    findings = db.query(Finding).all()

    total_findings = len(findings)

    if total_findings == 0:
        return {
            "security_score": 100.0,
            "total_findings": 0,
            "critical_findings": 0,
            "high_findings": 0,
            "medium_findings": 0,
            "low_findings": 0,
            "open_findings": 0,
            "resolved_findings": 0,
            "average_risk_score": 0.0,
        }

    active_findings = [
        finding
        for finding in findings
        if finding.status not in {"resolved", "suppressed"}
    ]

    total_risk = sum(
        finding.risk_score
        for finding in active_findings
    )

    average_risk_score = (
        total_risk / len(active_findings)
        if active_findings
        else 0.0
    )

    critical_findings = sum(
        1 for finding in active_findings
        if finding.severity == "critical"
    )

    high_findings = sum(
        1 for finding in active_findings
        if finding.severity == "high"
    )

    medium_findings = sum(
        1 for finding in active_findings
        if finding.severity == "medium"
    )

    low_findings = sum(
        1 for finding in active_findings
        if finding.severity == "low"
    )

    open_findings = sum(
        1 for finding in findings
        if finding.status in {"new", "open", "acknowledged"}
    )

    resolved_findings = sum(
        1 for finding in findings
        if finding.status == "resolved"
    )

    critical_penalty = critical_findings * 10
    high_penalty = high_findings * 5
    medium_penalty = medium_findings * 2
    low_penalty = low_findings * 0.5

    penalty = (
        critical_penalty
        + high_penalty
        + medium_penalty
        + low_penalty
    )

    security_score = max(
        0.0,
        min(100.0, 100.0 - penalty),
    )

    return {
        "security_score": round(security_score, 2),
        "total_findings": total_findings,
        "critical_findings": critical_findings,
        "high_findings": high_findings,
        "medium_findings": medium_findings,
        "low_findings": low_findings,
        "open_findings": open_findings,
        "resolved_findings": resolved_findings,
        "average_risk_score": round(average_risk_score, 2),
    }