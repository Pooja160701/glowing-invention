from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.security_score import calculate_security_score
from app.services.securityhub_ingestion import (
    ingest_securityhub_findings,
)

router = APIRouter(
    prefix="/api/v1/security",
    tags=["Security Posture"],
)

@router.get("/score")
def get_security_score(
    db: Session = Depends(get_db),
) -> dict:
    return calculate_security_score(db)

@router.post("/security-hub/ingest")
def ingest_security_hub(
    db: Session = Depends(get_db),
) -> dict:

    try:
        return ingest_securityhub_findings(
            db=db,
            region_name="ap-south-1",
        )

    except Exception as exc:
        db.rollback()

        raise HTTPException(
            status_code=502,
            detail=(
                f"Security Hub ingestion failed: {exc}"
            ),
        ) from exc