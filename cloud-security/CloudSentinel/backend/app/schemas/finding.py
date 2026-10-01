from datetime import datetime
from pydantic import BaseModel
from app.models.finding import (
    AssetType,
    FindingAsset,
    FindingRisk,
    FindingSeverity,
    FindingSource,
    FindingStatus,
    FindingType,
    NormalizedFinding,
)

class FindingCreate(BaseModel):
    source: FindingSource
    source_finding_id: str | None = None

    finding_type: FindingType

    title: str
    description: str

    severity: FindingSeverity

    asset: FindingAsset

    risk: FindingRisk

    remediation: str | None = None

    first_seen: datetime
    last_seen: datetime

    tags: list[str] = []
    metadata: dict[str, object] = {}

class FindingResponse(NormalizedFinding):
    pass