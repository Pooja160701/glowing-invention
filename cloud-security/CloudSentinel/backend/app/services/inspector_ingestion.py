from datetime import datetime, timezone
from typing import Any
from sqlalchemy.orm import Session
from app.db.models import Finding
from app.integrations.inspector.client import InspectorClient
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
        return [_json_safe(item) for item in value]

    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]

    if isinstance(value, (str, int, float, bool)) or value is None:
        return value

    return str(value)

def _map_severity(
    severity: Any,
) -> FindingSeverity:

    value = str(
        severity or ""
    ).upper()

    mapping = {
        "CRITICAL": FindingSeverity.CRITICAL,
        "HIGH": FindingSeverity.HIGH,
        "MEDIUM": FindingSeverity.MEDIUM,
        "LOW": FindingSeverity.LOW,
        "INFORMATIONAL": FindingSeverity.INFORMATIONAL,
    }

    return mapping.get(
        value,
        FindingSeverity.INFORMATIONAL,
    )

def _severity_score(
    finding: dict,
) -> float:

    score = finding.get(
        "inspectorScore"
    )

    if score is not None:
        try:
            return min(
                max(float(score), 0.0),
                10.0,
            )
        except (TypeError, ValueError):
            pass

    severity = _map_severity(
        finding.get("severity")
    )

    return {
        FindingSeverity.CRITICAL: 10.0,
        FindingSeverity.HIGH: 8.0,
        FindingSeverity.MEDIUM: 5.0,
        FindingSeverity.LOW: 2.0,
        FindingSeverity.INFORMATIONAL: 0.0,
    }[severity]

def _extract_asset(
    finding: dict,
) -> FindingAsset:

    resources = finding.get(
        "resources"
    ) or []

    resource = (
        resources[0]
        if resources
        else {}
    )

    resource_type = str(
        resource.get("type", "")
    )

    type_map = {
        "AWS_EC2_INSTANCE": AssetType.EC2,
        "AWS_ECR_CONTAINER_IMAGE": AssetType.ECR,
        "AWS_LAMBDA_FUNCTION": AssetType.LAMBDA,
    }

    asset_type = type_map.get(
        resource_type,
        AssetType.UNKNOWN,
    )

    resource_id = (
        resource.get("id")
        or finding.get("findingArn")
        or "unknown"
    )

    return FindingAsset(
        asset_id=str(resource_id),
        asset_type=asset_type,
        region=finding.get("awsAccountId")
        and finding.get("region"),
        account_id=finding.get(
            "awsAccountId"
        ),
        resource_arn=(
            resource.get("id")
            if isinstance(
                resource.get("id"),
                str,
            )
            and resource.get("id").startswith("arn:")
            else None
        ),
        asset_name=str(resource_id),
    )

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

def _build_finding_create(
    raw_finding: dict,
) -> FindingCreate:

    finding_arn = raw_finding.get(
        "findingArn",
        "unknown",
    )

    severity = _map_severity(
        raw_finding.get("severity")
    )

    score = _severity_score(
        raw_finding
    )

    title = (
        raw_finding.get("title")
        or "Amazon Inspector vulnerability"
    )

    description = (
        raw_finding.get("description")
        or "Amazon Inspector detected a vulnerability."
    )

    created_at = _parse_timestamp(
        raw_finding.get("firstObservedAt")
    )

    updated_at = _parse_timestamp(
        raw_finding.get("lastObservedAt")
    )

    safe_metadata = _json_safe(
        {
            "inspector_score": raw_finding.get(
                "inspectorScore"
            ),
            "inspector_score_details": raw_finding.get(
                "inspectorScoreDetails"
            ),
            "package_vulnerability_details": raw_finding.get(
                "packageVulnerabilityDetails"
            ),
            "finding_arn": finding_arn,
            "status": raw_finding.get(
                "status"
            ),
            "fix_available": raw_finding.get(
                "fixAvailable"
            ),
            "exploit_available": raw_finding.get(
                "exploitAvailable"
            ),
            "resources": raw_finding.get(
                "resources"
            ),
            "raw_finding": raw_finding,
        }
    )

    return FindingCreate(
        source_finding_id=finding_arn,
        source="inspector",
        finding_type=FindingType.VULNERABILITY,
        title=title,
        description=description,
        severity=severity,
        asset=_extract_asset(
            raw_finding
        ),
        risk={
            "severity_score": score,
            "asset_criticality": 7.0,
            "exploitability": 8.0,
            "exposure": 6.0,
            "data_sensitivity": 4.0,
        },
        remediation=(
            "Review the vulnerable package or resource, "
            "apply the available security update, and "
            "redeploy the affected workload."
        ),
        first_seen=created_at,
        last_seen=updated_at,
        tags=[
            "aws",
            "inspector",
            "vulnerability",
        ],
        metadata=safe_metadata,
    )

def ingest_inspector_findings(
    db: Session,
    region_name: str = "ap-south-1",
) -> dict:

    client = InspectorClient(
        region_name=region_name
    )

    raw_findings = client.get_findings(
        max_results=100
    )

    findings_ingested = 0
    findings_skipped = 0

    for raw_finding in raw_findings:

        source_finding_id = raw_finding.get(
            "findingArn"
        )

        if not source_finding_id:
            continue

        existing = (
            db.query(Finding)
            .filter(
                Finding.source == "inspector",
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

        finding_create = _build_finding_create(
            raw_finding
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
        "service": "inspector",
        "connected": True,
        "findings_received": len(raw_findings),
        "findings_ingested": findings_ingested,
        "findings_skipped": findings_skipped,
    }