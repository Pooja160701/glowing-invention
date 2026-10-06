from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

class Finding(BaseModel):
    title: str
    category: str
    severity: Severity
    description: str
    evidence: str
    remediation: str
    score: int = Field(ge=0, le=100)

class AuditEvent(BaseModel):
    event: str
    actor: str
    tool: str | None = None
    action: str | None = None
    decision: str
    reason: str
    metadata: dict[str, Any] = Field(default_factory=dict)

class AgentAction(BaseModel):
    tool: str
    action: str
    approved: bool = False
    actor: str = "user"

class RedTeamRequest(BaseModel):
    target: str = "demo-model"
    categories: list[str] | None = None

class SupplyChainRequest(BaseModel):
    path: str = "."
