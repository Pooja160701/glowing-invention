from pydantic import BaseModel, Field

class ComplianceControl(BaseModel):
    control_id: str
    name: str
    framework: str
    status: str
    evidence_count: int = Field(ge=0)
    open_findings: int = Field(ge=0)
    rationale: str

class ComplianceSummary(BaseModel):
    framework: str
    score: float = Field(ge=0, le=100)
    compliant: int
    non_compliant: int
    not_evaluated: int
    total_controls: int
    controls: list[ComplianceControl]
