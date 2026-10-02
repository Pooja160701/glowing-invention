from datetime import datetime, timezone
from typing import Any
from sqlalchemy.orm import Session
from app.db.models import Finding
from app.integrations.macie.client import MacieClient
from app.models.finding import (
    AssetType,
    FindingAsset,
    FindingSeverity,
    FindingType,
)
from app.schemas.finding import FindingCreate
from app.services.finding_normalizer import normalize_finding

def _json_safe(value: Any) -> Any:

    if isinstance(value, datetime):
        return value.isoformat()

    if isinstance(value, dict):
        return {
            str(key): _json_safe(item)
            for key, item in value.items()
        }

    if isinstance(value, list):
        return [
            _json_safe(item)
            for item in value
        ]

    if isinstance(value, tuple):
        return [
            _json_safe(item)
            for item in value
        ]

    if (
        isinstance(value, (str, int, float, bool))
        or value is None
    ):
        return value

    return str(value)

def _map_severity(
    finding: dict,
) -> FindingSeverity:

    severity = str(
        finding.get("severity")
        or ""
    ).upper()

    return {
        "CRITICAL": FindingSeverity.CRITICAL,
        "HIGH": FindingSeverity.HIGH,
        "MEDIUM": FindingSeverity.MEDIUM,
        "LOW": FindingSeverity.LOW,
    }.get(
        severity,
        FindingSeverity.INFORMATIONAL,
    )

def _severity_score(
    finding: dict,
) -> float:

    severity = _map_severity(
        finding
    )

    return {
        FindingSeverity.CRITICAL: 10.0,
        FindingSeverity.HIGH: 8.0,
        FindingSeverity.MEDIUM: 5.0,
        FindingSeverity.LOW: 2.0,
        FindingSeverity.INFORMATIONAL: 0.0,
    }[severity]

def _parse_timestamp(
    value: Any,
) -> datetime:

    if isinstance(value, datetime):
        return (
            value
            if value.tzinfo
            else value.replace(
                tzinfo=timezone.utc
            )
        )

    if isinstance(value, str):
        try:
            return datetime.fromisoformat(
                value.replace(
                    "Z",
                    "+00:00",
                )
            )
        except ValueError:
            pass

    return datetime.now(
        timezone.utc
    )

def _extract_asset(
    finding: dict,
) -> FindingAsset:

    resource = finding.get(
        "resource",
    ) or {}

    s3_bucket = (
        resource.get("s3Bucket")
        or {}
    )

    bucket_name = s3_bucket.get(
        "name"
    )

    if bucket_name:
        asset_id = bucket_name
        asset_type = AssetType.S3
        resource_arn = (
            s3_bucket.get("arn")
        )
    else:
        asset_id = (
            finding.get("id")
            or "unknown"
        )
        asset_type = AssetType.UNKNOWN
        resource_arn = None

    return FindingAsset(
        asset_id=str(asset_id),
        asset_type=asset_type,
        region=finding.get(
            "region"
        ),
        account_id=finding.get(
            "accountId"
        ),
        resource_arn=resource_arn,
        asset_name=str(asset_id),
    )

def _build_finding_create(
    raw_finding: dict,
) -> FindingCreate:

    finding_id = raw_finding.get(
        "id",
        "unknown",
    )

    title = (
        raw_finding.get("title")
        or "Macie sensitive-data finding"
    )

    description = (
        raw_finding.get("description")
        or "Amazon Macie detected sensitive data or a related security condition."
    )

    severity = _map_severity(
        raw_finding
    )

    score = _severity_score(
        raw_finding
    )

    created_at = _parse_timestamp(
        raw_finding.get(
            "createdAt"
        )
    )

    updated_at = _parse_timestamp(
        raw_finding.get(
            "updatedAt"
        )
    )

    safe_metadata = _json_safe(
        {
            "macie_finding_type": raw_finding.get(
                "type"
            ),
            "category": raw_finding.get(
                "category"
            ),
            "classification_details": raw_finding.get(
                "classificationDetails"
            ),
            "sample": raw_finding.get(
                "sample"
            ),
            "resource": raw_finding.get(
                "resource"
            ),
            "raw_finding": raw_finding,
        }
    )

    return FindingCreate(
        source_finding_id=finding_id,
        source="macie",
        finding_type=FindingType.SENSITIVE_DATA,
        title=title,
        description=description,
        severity=severity,
        asset=_extract_asset(
            raw_finding
        ),
        risk={
            "severity_score": score,
            "asset_criticality": 7.0,
            "exploitability": 5.0,
            "exposure": 7.0,
            "data_sensitivity": 10.0,
        },
        remediation=(
            "Investigate the affected S3 resource, "
            "identify the sensitive data involved, "
            "restrict unnecessary access, and apply "
            "appropriate data protection controls."
        ),
        first_seen=created_at,
        last_seen=updated_at,
        tags=[
            "aws",
            "macie",
            "sensitive-data",
        ],
        metadata=safe_metadata,
    )

def ingest_macie_findings(
    db: Session,
    region_name: str = "ap-south-1",
) -> dict:

    client = MacieClient(
        region_name=region_name
    )

    raw_findings = client.get_findings(
        max_results=100
    )

    findings_ingested = 0
    findings_skipped = 0

    for raw_finding in raw_findings:

        source_finding_id = raw_finding.get(
            "id"
        )

        if not source_finding_id:
            continue

        existing = (
            db.query(Finding)
            .filter(
                Finding.source == "macie",
                Finding.source_finding_id
                == source_finding_id,
            )
            .first()
        )

        if existing:
            existing.last_seen = datetime.now(
                timezone.utc
            )

            findings_skipped += 1
            continue

        finding_create = (
            _build_finding_create(
                raw_finding
            )
        )

        normalized = normalize_finding(
            finding_create
        )

        db_finding = Finding(
            finding_id=normalized.finding_id,
            source_finding_id=normalized.source_finding_id,
            source=normalized.source.value,
            finding_type=normalized.finding_type.value,
            title=normalized.title,
            description=normalized.description,
            severity=normalized.severity.value,
            status=normalized.status.value,
            asset=normalized.asset.model_dump(
                mode="json"
            ),
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
            metadata_json=_json_safe(
                normalized.metadata
            ),
        )

        db.add(db_finding)
        findings_ingested += 1

    db.commit()

    return {
        "service": "macie",
        "connected": True,
        "findings_received": len(
            raw_findings
        ),
        "findings_ingested": findings_ingested,
        "findings_skipped": findings_skipped,
    }