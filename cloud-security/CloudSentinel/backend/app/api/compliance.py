from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding
from app.schemas.compliance import ComplianceSummary
from app.services.compliance_service import calculate_compliance

router = APIRouter(prefix="/api/v1/compliance", tags=["Compliance"])

@router.get("/summary", response_model=ComplianceSummary)
def compliance_summary(db: Session = Depends(get_db)):
    return calculate_compliance(db.query(Finding).all())

@router.get("/controls")
def compliance_controls(db: Session = Depends(get_db)):
    return calculate_compliance(db.query(Finding).all())["controls"]
