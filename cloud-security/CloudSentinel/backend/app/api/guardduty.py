from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.integrations.guardduty.client import GuardDutyClient
from app.services.guardduty_ingestion import ingest_guardduty_findings

router = APIRouter(
    prefix="/api/v1/integrations/guardduty",
    tags=["GuardDuty"],
)

@router.get("/status")
def guardduty_status() -> dict:
    try:
        client = GuardDutyClient()

        detector_ids = client.get_detector_ids()

        return {
            "service": "guardduty",
            "connected": True,
            "detector_count": len(detector_ids),
            "detector_ids": detector_ids,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Unable to connect to GuardDuty: {exc}",
        ) from exc

@router.post("/ingest")
def ingest_guardduty(
    db: Session = Depends(get_db),
) -> dict:
    try:
        return ingest_guardduty_findings(
            db=db,
            region_name="ap-south-1",
        )

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"GuardDuty ingestion failed: {exc}",
        ) from exc