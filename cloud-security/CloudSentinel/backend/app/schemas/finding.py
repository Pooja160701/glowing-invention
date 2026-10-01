from datetime import datetime
from pydantic import BaseModel, Field
from app.models.finding import (
    FindingAsset,
    FindingRisk,
    FindingSeverity,
    FindingSource,
    FindingType,
    NormalizedFinding,
)

class FindingRiskInput(BaseModel):
    severity_score: float = Field(ge=0, le=10)
    asset_criticality: float = Field(ge=0, le=10)
    exploitability: float = Field(ge=0, le=10)
    exposure: float = Field(ge=0, le=10)
    data_sensitivity: float = Field(ge=0, le=10)

class FindingCreate(BaseModel):
    source: FindingSource
    source_finding_id: str | None = None

    finding_type: FindingType

    title: str
    description: str

    severity: FindingSeverity

    asset: FindingAsset

    risk: FindingRiskInput

    remediation: str | None = None

    first_seen: datetime
    last_seen: datetime

    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, object] = Field(default_factory=dict)

class FindingResponse(NormalizedFinding):
    pass