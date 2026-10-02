from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class IncidentStatus(str, Enum):
    OPEN = "open"
    INVESTIGATING = "investigating"
    CONTAINED = "contained"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=500)
    description: str = Field(min_length=3)
    severity: str = "high"
    priority: str = "P2"
    owner: str | None = None
    finding_ids: list[str] = Field(default_factory=list)
    alert_ids: list[str] = Field(default_factory=list)

class IncidentStatusUpdate(BaseModel):
    status: IncidentStatus
    note: str | None = None
    actor: str = "analyst"
    containment_notes: str | None = None
    root_cause: str | None = None
    resolution_notes: str | None = None

class IncidentEventCreate(BaseModel):
    event_type: str = Field(min_length=2, max_length=50)
    note: str = Field(min_length=2)
    actor: str = "analyst"

class IncidentEventResponse(BaseModel):
    event_id: str
    incident_id: str
    event_type: str
    actor: str
    note: str
    created_at: datetime

class IncidentResponse(BaseModel):
    incident_id: str
    title: str
    description: str
    severity: str
    priority: str
    status: IncidentStatus
    owner: str | None
    finding_ids: list[str]
    alert_ids: list[str]
    containment_notes: str | None
    root_cause: str | None
    resolution_notes: str | None
    created_at: datetime
    updated_at: datetime
    contained_at: datetime | None
    resolved_at: datetime | None
    closed_at: datetime | None
    events: list[IncidentEventResponse] = Field(default_factory=list)
