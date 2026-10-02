from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding
from app.models.finding import NormalizedFinding
from app.schemas.finding import (
    FindingCreate,
    FindingStatusUpdate,
)
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
    source: str | None = Query(default=None),
    severity: str | None = Query(default=None),
    status: str | None = Query(default=None),
    finding_type: str | None = Query(default=None),
    min_risk_score: float | None = Query(
        default=None,
        ge=0,
        le=100,
    ),
    db: Session = Depends(get_db),
) -> list[dict]:

    query = db.query(Finding)

    if source:
        query = query.filter(Finding.source == source)

    if severity:
        query = query.filter(Finding.severity == severity)

    if status:
        query = query.filter(Finding.status == status)

    if finding_type:
        query = query.filter(Finding.finding_type == finding_type)

    if min_risk_score is not None:
        query = query.filter(
            Finding.risk_score >= min_risk_score
        )

    findings = (
        query
        .order_by(Finding.risk_score.desc())
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

@router.get("/{finding_id}")
def get_finding(
    finding_id: str,
    db: Session = Depends(get_db),
) -> dict:
    finding = (
        db.query(Finding)
        .filter(Finding.finding_id == finding_id)
        .first()
    )

    if finding is None:
        raise HTTPException(
            status_code=404,
            detail="Finding not found",
        )

    return {
        "finding_id": finding.finding_id,
        "source_finding_id": finding.source_finding_id,
        "source": finding.source,
        "finding_type": finding.finding_type,
        "title": finding.title,
        "description": finding.description,
        "severity": finding.severity,
        "status": finding.status,
        "asset": finding.asset,
        "risk": {
            "severity_score": finding.severity_score,
            "asset_criticality": finding.asset_criticality,
            "exploitability": finding.exploitability,
            "exposure": finding.exposure,
            "data_sensitivity": finding.data_sensitivity,
            "risk_score": finding.risk_score,
        },
        "remediation": finding.remediation,
        "first_seen": finding.first_seen,
        "last_seen": finding.last_seen,
        "tags": finding.tags,
        "metadata": finding.metadata_json,
        "created_at": finding.created_at,
        "updated_at": finding.updated_at,
    }


@router.patch("/{finding_id}/status")
def update_finding_status(
    finding_id: str,
    update: FindingStatusUpdate,
    db: Session = Depends(get_db),
) -> dict:
    allowed_statuses = {
        "new",
        "open",
        "acknowledged",
        "resolved",
        "suppressed",
    }

    if update.status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Invalid status. Allowed values: "
                f"{sorted(allowed_statuses)}"
            ),
        )

    finding = (
        db.query(Finding)
        .filter(Finding.finding_id == finding_id)
        .first()
    )

    if finding is None:
        raise HTTPException(
            status_code=404,
            detail="Finding not found",
        )

    finding.status = update.status

    db.commit()
    db.refresh(finding)

    return {
        "finding_id": finding.finding_id,
        "status": finding.status,
        "updated_at": finding.updated_at,
    }