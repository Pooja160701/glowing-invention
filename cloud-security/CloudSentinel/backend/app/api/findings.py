from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding
from app.models.finding import NormalizedFinding
from app.schemas.finding import FindingCreate
from app.services.finding_normalizer import normalize_finding

router = APIRouter(
    prefix="/api/v1/findings",
    tags=["Findings"],
)

@router.post("", response_model=NormalizedFinding)
def create_finding(
    finding: FindingCreate,
    db: Session = Depends(get_db),
) -> NormalizedFinding:
    normalized = normalize_finding(finding)

    db_finding = Finding(
        finding_id=normalized.finding_id,
        source_finding_id=normalized.source_finding_id,
        source=normalized.source.value,
        finding_type=normalized.finding_type.value,
        title=normalized.title,
        description=normalized.description,
        severity=normalized.severity.value,
        status=normalized.status.value,
        asset=normalized.asset.model_dump(),
        severity_score=normalized.risk.severity_score,
        asset_criticality=normalized.risk.asset_criticality,
        exploitability=normalized.risk.exploitability,
        exposure=normalized.risk.exposure,
        data_sensitivity=normalized.risk.data_sensitivity,
        risk_score=normalized.risk.risk_score,
        remediation=normalized.remediation,
        first_seen=normalized.first_seen,
        last_seen=normalized.last_seen,
        tags=normalized.tags,
        metadata_json=normalized.metadata,
    )

    db.add(db_finding)
    db.commit()
    db.refresh(db_finding)

    return normalized

@router.get("")
def list_findings(
    db: Session = Depends(get_db),
) -> list[dict]:
    findings = (
        db.query(Finding)
        .order_by(Finding.created_at.desc())
        .all()
    )

    return [
        {
            "finding_id": finding.finding_id,
            "source": finding.source,
            "finding_type": finding.finding_type,
            "title": finding.title,
            "severity": finding.severity,
            "status": finding.status,
            "risk_score": finding.risk_score,
            "created_at": finding.created_at,
        }
        for finding in findings
    ]