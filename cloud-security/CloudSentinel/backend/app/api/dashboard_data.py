from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding

router = APIRouter(prefix="/api/v1/dashboard-data", tags=["Dashboard Analytics"])

@router.get("/vulnerabilities")
def vulnerabilities(
    severity: str | None = Query(None),
    status: str | None = Query(None),
    min_risk_score: float | None = Query(None, ge=0, le=100),
    db: Session = Depends(get_db),
):
    q = db.query(Finding).filter(Finding.finding_type == "vulnerability")
    if severity: q = q.filter(Finding.severity == severity)
    if status: q = q.filter(Finding.status == status)
    if min_risk_score is not None: q = q.filter(Finding.risk_score >= min_risk_score)
    rows = q.order_by(Finding.risk_score.desc()).all()
    return {"total": len(rows), "critical": sum(x.severity == "critical" for x in rows), "high": sum(x.severity == "high" for x in rows), "medium": sum(x.severity == "medium" for x in rows), "low": sum(x.severity == "low" for x in rows), "items": [{"finding_id":x.finding_id,"title":x.title,"severity":x.severity,"risk_score":x.risk_score,"source":x.source,"asset":x.asset,"status":x.status,"remediation":x.remediation} for x in rows]}

@router.get("/iam-risks")
def iam_risks(
    min_risk_score: float | None = Query(None, ge=0, le=100),
    db: Session = Depends(get_db),
):
    rows = db.query(Finding).filter(Finding.finding_type == "identity").order_by(Finding.risk_score.desc()).all()
    if min_risk_score is not None: rows = [x for x in rows if x.risk_score >= min_risk_score]
    return {"total": len(rows), "critical": sum(x.severity == "critical" for x in rows), "high": sum(x.severity == "high" for x in rows), "items": [{"finding_id":x.finding_id,"title":x.title,"severity":x.severity,"risk_score":x.risk_score,"source":x.source,"asset":x.asset,"status":x.status,"remediation":x.remediation} for x in rows]}
