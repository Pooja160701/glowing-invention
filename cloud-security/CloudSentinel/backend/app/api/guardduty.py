from fastapi import APIRouter, HTTPException
from app.integrations.guardduty.client import GuardDutyClient

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