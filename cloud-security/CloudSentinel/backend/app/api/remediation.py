from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding
from app.services.remediation_service import recommend_remediation

router = APIRouter(prefix="/api/v1/remediation", tags=["Remediation"])

@router.get("/finding/{finding_id}")
def finding_remediation(finding_id: str, db: Session = Depends(get_db)):
    finding = db.query(Finding).filter(Finding.finding_id == finding_id).first()
    if finding is None:
        raise HTTPException(status_code=404, detail="Finding not found")
    return recommend_remediation(finding)

@router.get("/open")
def open_remediation(db: Session = Depends(get_db)):
    findings = (
        db.query(Finding)
        .filter(Finding.status.notin_(["resolved", "suppressed"]))
        .order_by(Finding.risk_score.desc())
        .all()
    )
    return [recommend_remediation(f) for f in findings]
