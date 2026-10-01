from fastapi import APIRouter
from app.models.finding import NormalizedFinding
from app.schemas.finding import FindingCreate
from app.services.finding_normalizer import normalize_finding

router = APIRouter(prefix="/api/v1/findings", tags=["Findings"])

@router.post("", response_model=NormalizedFinding)
def create_finding(finding: FindingCreate) -> NormalizedFinding:
    return normalize_finding(finding)