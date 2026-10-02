from collections import Counter

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Alert, Finding, Incident
from app.services.compliance_service import calculate_compliance

router = APIRouter(prefix="/api/v1/dashboard", tags=["Dashboard"])


def _distribution(rows, field):
    return dict(sorted(Counter(getattr(row, field) for row in rows).items()))


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    findings = db.query(Finding).all()
    alerts = db.query(Alert).all()
    incidents = db.query(Incident).all()
    risks = [x.risk_score for x in findings]
    compliance = calculate_compliance(findings)
    vulnerabilities = [x for x in findings if x.finding_type == "vulnerability"]
    iam_risks = [x for x in findings if x.finding_type == "identity"]
    assets = {str((x.asset or {}).get("asset_id")) for x in findings if (x.asset or {}).get("asset_id")}

    return {
        "findings": {
            "total": len(findings),
            "critical": sum(x.severity == "critical" for x in findings),
            "high": sum(x.severity == "high" for x in findings),
            "by_source": _distribution(findings, "source"),
            "by_type": _distribution(findings, "finding_type"),
            "by_severity": _distribution(findings, "severity"),
        },
        "alerts": {
            "total": len(alerts),
            "open": sum(x.status in {"new", "acknowledged"} for x in alerts),
            "critical": sum(x.severity == "critical" for x in alerts),
            "by_severity": _distribution(alerts, "severity"),
            "by_status": _distribution(alerts, "status"),
        },
        "assets": {"observed": len(assets), "with_findings": len(assets)},
        "vulnerabilities": {"total": len(vulnerabilities), "critical": sum(x.severity == "critical" for x in vulnerabilities), "high": sum(x.severity == "high" for x in vulnerabilities)},
        "iam_risks": {"total": len(iam_risks), "critical": sum(x.severity == "critical" for x in iam_risks), "high": sum(x.severity == "high" for x in iam_risks)},
        "risk": {
            "average_finding_risk": round(sum(risks) / len(risks), 2) if risks else 0.0,
            "max_finding_risk": max(risks) if risks else 0.0,
        },
        "compliance": {
            "score": compliance["score"],
            "compliant": compliance["compliant"],
            "non_compliant": compliance["non_compliant"],
            "not_evaluated": compliance["not_evaluated"],
            "total_controls": compliance["total_controls"],
        },
        "incidents": {
            "total": len(incidents),
            "open": sum(i.status in {"open", "investigating", "contained"} for i in incidents),
            "resolved": sum(i.status == "resolved" for i in incidents),
            "closed": sum(i.status == "closed" for i in incidents),
            "by_status": {
                status: sum(i.status == status for i in incidents)
                for status in ["open", "investigating", "contained", "resolved", "closed"]
            },
        },
    }


@router.get("/top-alerts")
def top_alerts(limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    rows = (
        db.query(Alert)
        .order_by(Alert.risk_score.desc(), Alert.created_at.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "alert_id": x.alert_id,
            "title": x.title,
            "severity": x.severity,
            "priority": x.priority,
            "risk_score": x.risk_score,
            "status": x.status,
            "source": x.source,
            "finding_type": x.finding_type,
            "rule_id": x.rule_id,
            "asset": x.asset,
        }
        for x in rows
    ]
