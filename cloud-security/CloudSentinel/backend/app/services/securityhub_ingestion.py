from datetime import datetime, timezone
from typing import Any
from sqlalchemy.orm import Session
from app.db.models import Finding
from app.integrations.securityhub.client import SecurityHubClient
from app.models.finding import (
    AssetType,
    FindingAsset,
    FindingSeverity,
    FindingType,
)
from app.schemas.finding import FindingCreate
from app.services.finding_normalizer import normalize_finding

def _json_safe(value: Any) -> Any:
    """Convert values into JSON-compatible structures."""

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
    finding: dict,
) -> FindingSeverity:
    """
    Map Security Hub Severity.Label / Normalized
    into the CloudSentinel severity model.
    """

    severity = finding.get("Severity") or {}

    label = str(
        severity.get("Label") or ""
    ).upper()

    mapping = {
        "CRITICAL": FindingSeverity.CRITICAL,
        "HIGH": FindingSeverity.HIGH,
        "MEDIUM": FindingSeverity.MEDIUM,
        "LOW": FindingSeverity.LOW,
        "INFORMATIONAL": FindingSeverity.INFORMATIONAL,
    }

    if label in mapping:
        return mapping[label]

    normalized = severity.get("Normalized")

    if normalized is not None:
        try:
            value = float(normalized)

            if value >= 90:
                return FindingSeverity.CRITICAL

            if value >= 70:
                return FindingSeverity.HIGH

            if value >= 40:
                return FindingSeverity.MEDIUM

            if value > 0:
                return FindingSeverity.LOW

        except (TypeError, ValueError):
            pass

    return FindingSeverity.INFORMATIONAL

def _severity_score(
    finding: dict,
) -> float:
    severity = finding.get("Severity") or {}

    normalized = severity.get("Normalized")

    if normalized is not None:
        try:
            return round(
                min(
                    max(float(normalized) / 10.0, 0.0),
                    10.0,
                ),
                2,
            )
        except (TypeError, ValueError):
            pass

    severity_map = {
        FindingSeverity.CRITICAL: 10.0,
        FindingSeverity.HIGH: 8.0,
        FindingSeverity.MEDIUM: 5.0,
        FindingSeverity.LOW: 2.0,
        FindingSeverity.INFORMATIONAL: 0.0,
    }

    return severity_map[_map_severity(finding)]

def _extract_asset(
    finding: dict,
) -> FindingAsset:
    """
    Extract the primary resource from a Security Hub finding.
    """

    resources = finding.get("Resources") or []

    resource = resources[0] if resources else {}

    resource_type = resource.get(
        "Type",
        "Unknown",
    )

    resource_id = resource.get(
        "Id",
    )

    type_map = {
        "AwsEc2Instance": AssetType.EC2,
        "AwsS3Bucket": AssetType.S3,
        "AwsIamUser": AssetType.IAM_USER,
        "AwsIamRole": AssetType.IAM_ROLE,
        "AwsIamPolicy": AssetType.IAM_POLICY,
        "AwsEcrContainerImage": AssetType.ECR,
        "AwsLambdaFunction": AssetType.LAMBDA,
        "AwsEc2SecurityGroup": AssetType.SECURITY_GROUP,
        "AwsKmsKey": AssetType.KMS_KEY,
    }

    asset_type = type_map.get(
        resource_type,
        AssetType.UNKNOWN,
    )

    asset_id = (
        resource_id
        or finding.get("Id")
        or "unknown"
    )

    region = (
        resource.get("Region")
        or finding.get("Region")
    )

    return FindingAsset(
        asset_id=str(asset_id),
        asset_type=asset_type,
        region=region,
        account_id=finding.get("AwsAccountId"),
        resource_arn=(
            resource_id
            if isinstance(resource_id, str)
            and resource_id.startswith("arn:")
            else None
        ),
        asset_name=str(asset_id),
    )

def _parse_timestamp(
    value: Any,
) -> datetime:
    """
    Convert AWS timestamp strings into timezone-aware datetimes.
    """

    if isinstance(value, datetime):
        return (
            value
            if value.tzinfo
            else value.replace(tzinfo=timezone.utc)
        )

    if isinstance(value, str):
        try:
            return datetime.fromisoformat(
                value.replace("Z", "+00:00")
            )
        except ValueError:
            pass

    return datetime.now(timezone.utc)

def _build_finding_create(
    raw_finding: dict,
) -> FindingCreate:

    finding_id = raw_finding.get(
        "Id",
        "unknown",
    )

    title = (
        raw_finding.get("Title")
        or raw_finding.get("GeneratorId")
        or "Security Hub Finding"
    )

    description = (
        raw_finding.get("Description")
        or "AWS Security Hub reported a security finding."
    )

    severity = _map_severity(
        raw_finding
    )

    score = _severity_score(
        raw_finding
    )

    created_at = _parse_timestamp(
        raw_finding.get("CreatedAt")
    )

    updated_at = _parse_timestamp(
        raw_finding.get("UpdatedAt")
    )

    safe_metadata = _json_safe(
        {
            "securityhub_product_arn": raw_finding.get(
                "ProductArn"
            ),
            "securityhub_product_name": raw_finding.get(
                "ProductName"
            ),
            "generator_id": raw_finding.get(
                "GeneratorId"
            ),
            "record_state": raw_finding.get(
                "RecordState"
            ),
            "workflow": raw_finding.get(
                "Workflow"
            ),
            "compliance": raw_finding.get(
                "Compliance"
            ),
            "types": raw_finding.get(
                "Types"
            ),
            "remediation": raw_finding.get(
                "Remediation"
            ),
            "resources": raw_finding.get(
                "Resources"
            ),
            "raw_finding": raw_finding,
        }
    )

    return FindingCreate(
        source_finding_id=finding_id,
        source="security_hub",
        finding_type=FindingType.COMPLIANCE,
        title=title,
        description=description,
        severity=severity,
        asset=_extract_asset(
            raw_finding
        ),
        risk={
            "severity_score": score,
            "asset_criticality": 7.0,
            "exploitability": 6.0,
            "exposure": 6.0,
            "data_sensitivity": 5.0,
        },
        remediation=(
            "Review the Security Hub finding, "
            "validate the affected resource, "
            "and apply the recommended remediation."
        ),
        first_seen=created_at,
        last_seen=updated_at,
        tags=[
            "aws",
            "security-hub",
            "compliance",
        ],
        metadata=safe_metadata,
    )

def ingest_securityhub_findings(
    db: Session,
    region_name: str = "ap-south-1",
) -> dict:

    client = SecurityHubClient(
        region_name=region_name
    )

    standards = client.get_enabled_standards()

    raw_findings = client.get_findings(
        max_results=100
    )

    findings_ingested = 0
    findings_skipped = 0

    for raw_finding in raw_findings:

        source_finding_id = raw_finding.get(
            "Id"
        )

        if not source_finding_id:
            continue

        existing = (
            db.query(Finding)
            .filter(
                Finding.source == "security_hub",
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
        "service": "security_hub",
        "connected": True,
        "standards_enabled": len(standards),
        "findings_received": len(raw_findings),
        "findings_ingested": findings_ingested,
        "findings_skipped": findings_skipped,
    }