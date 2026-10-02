from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class AlertStatus(str, Enum):
    NEW = "new"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    SUPPRESSED = "suppressed"


class AlertResponse(BaseModel):
    alert_id: str
    finding_id: str
    rule_id: str
    rule_name: str
    title: str
    message: str
    severity: str
    priority: str
    risk_score: float = Field(ge=0, le=100)
    status: AlertStatus
    source: str
    finding_type: str
    asset: dict
    remediation: str | None = None
    tags: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
    acknowledged_at: datetime | None = None
    resolved_at: datetime | None = None


class AlertStatusUpdate(BaseModel):
    status: AlertStatus
