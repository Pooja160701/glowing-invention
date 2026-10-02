from datetime import datetime, timezone
from typing import Any
from sqlalchemy.orm import Session
from app.db.models import Finding
from app.integrations.guardduty.client import GuardDutyClient
from app.models.finding import (
    AssetType,
    FindingAsset,
    FindingSeverity,
    FindingType,
)
from app.schemas.finding import FindingCreate
from app.services.finding_normalizer import normalize_finding

def _json_safe(value: Any) -> Any:
    """
    Convert AWS/boto3 response values into JSON-serializable values.
    """
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

def _map_severity(severity_value: Any) -> FindingSeverity:
    """
    Map GuardDuty numeric severity to CloudSentinel severity.
    """
    if severity_value is None:
        return FindingSeverity.INFORMATIONAL

    try:
        severity = float(severity_value)
    except (TypeError, ValueError):
        return FindingSeverity.INFORMATIONAL

    if severity >= 7:
        return FindingSeverity.HIGH

    if severity >= 4:
        return FindingSeverity.MEDIUM

    return FindingSeverity.LOW

def _extract_asset(finding: dict) -> FindingAsset:
    """
    Extract a normalized asset from a GuardDuty finding.
    Handles different GuardDuty resource shapes safely.
    """
    resource = finding.get("Resource") or {}

    resource_type = resource.get("ResourceType", "Unknown")

    asset_type_map = {
        "Instance": AssetType.EC2,
        "S3Bucket": AssetType.S3,
        "AccessKey": AssetType.IAM_USER,
        "Lambda": AssetType.LAMBDA,
    }

    asset_type = asset_type_map.get(
        resource_type,
        AssetType.UNKNOWN,
    )

    instance_details = resource.get("InstanceDetails") or {}
    access_key_details = resource.get("AccessKeyDetails") or {}

    s3_details = resource.get("S3BucketDetails") or []

    s3_name = None

    if isinstance(s3_details, list) and s3_details:
        first_bucket = s3_details[0] or {}

        if isinstance(first_bucket, dict):
            s3_name = first_bucket.get("Name")

    asset_id = (
        instance_details.get("InstanceId")
        or access_key_details.get("UserName")
        or s3_name
        or finding.get("Id")
        or "unknown"
    )

    return FindingAsset(
        asset_id=str(asset_id),
        asset_type=asset_type,
        region=finding.get("Region"),
        account_id=finding.get("AccountId"),
        resource_arn=None,
        asset_name=str(asset_id),
    )

def _build_finding_create(raw_finding: dict) -> FindingCreate:
    """
    Convert a raw GuardDuty finding into the common CloudSentinel
    FindingCreate schema.
    """

    severity_value = raw_finding.get("Severity")

    severity = _map_severity(severity_value)

    try:
        numeric_severity = float(severity_value or 0)
    except (TypeError, ValueError):
        numeric_severity = 0.0

    numeric_severity = min(max(numeric_severity, 0.0), 10.0)

    finding_id = raw_finding.get("Id", "unknown")

    title = (
        raw_finding.get("Title")
        or raw_finding.get("Type")
        or "GuardDuty Finding"
    )

    description = (
        raw_finding.get("Description")
        or "GuardDuty detected a security-related event."
    )

    safe_metadata = _json_safe(
        {
            "guardduty_type": raw_finding.get("Type"),
            "guardduty_schema_version": raw_finding.get("SchemaVersion"),
            "region": raw_finding.get("Region"),
            "account_id": raw_finding.get("AccountId"),
            "service": raw_finding.get("Service"),
            "resource": raw_finding.get("Resource"),
            "severity": raw_finding.get("Severity"),
            "created_at": raw_finding.get("CreatedAt"),
            "updated_at": raw_finding.get("UpdatedAt"),
            "raw_finding": raw_finding,
        }
    )

    return FindingCreate(
        source_finding_id=finding_id,
        source="guardduty",
        finding_type=FindingType.THREAT,
        title=title,
        description=description,
        severity=severity,
        asset=_extract_asset(raw_finding),
        risk={
            "severity_score": numeric_severity,
            "asset_criticality": 7.0,
            "exploitability": 7.0,
            "exposure": 6.0,
            "data_sensitivity": 5.0,
        },
        remediation=(
            "Investigate the GuardDuty finding, validate the affected "
            "resource, contain suspicious activity if necessary, and "
            "apply the recommended remediation."
        ),
        first_seen=datetime.now(timezone.utc),
        last_seen=datetime.now(timezone.utc),
        tags=[
            "aws",
            "guardduty",
            "threat-detection",
        ],
        metadata=safe_metadata,
    )

def ingest_guardduty_findings(
    db: Session,
    region_name: str = "ap-south-1",
) -> dict:
    """
    Pull GuardDuty findings and persist normalized findings.

    The ingestion is idempotent:
    - New source finding -> insert
    - Existing source finding -> update last_seen
    """

    client = GuardDutyClient(region_name=region_name)

    detector_ids = client.get_detector_ids()

    if not detector_ids:
        return {
            "service": "guardduty",
            "connected": True,
            "detectors": 0,
            "findings_received": 0,
            "findings_ingested": 0,
            "findings_skipped": 0,
        }

    findings_received = 0
    findings_ingested = 0
    findings_skipped = 0

    for detector_id in detector_ids:

        finding_ids = client.list_findings(
            detector_id=detector_id,
            max_results=50,
        )

        raw_findings = client.get_findings(
            detector_id=detector_id,
            finding_ids=finding_ids,
        )

        findings_received += len(raw_findings)

        for raw_finding in raw_findings:

            source_finding_id = raw_finding.get("Id")

            if not source_finding_id:
                continue

            existing = (
                db.query(Finding)
                .filter(
                    Finding.source == "guardduty",
                    Finding.source_finding_id == source_finding_id,
                )
                .first()
            )

            if existing:
                existing.last_seen = datetime.now(timezone.utc)
                findings_skipped += 1
                continue

            finding_create = _build_finding_create(raw_finding)

            normalized = normalize_finding(finding_create)

            db_finding = Finding(
                finding_id=normalized.finding_id,
                source_finding_id=normalized.source_finding_id,
                source=normalized.source.value,
                finding_type=normalized.finding_type.value,
                title=normalized.title,
                description=normalized.description,
                severity=normalized.severity.value,
                status=normalized.status.value,
                asset=normalized.asset.model_dump(mode="json"),
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
                metadata_json=_json_safe(normalized.metadata),
            )

            db.add(db_finding)
            findings_ingested += 1

    db.commit()

    return {
        "service": "guardduty",
        "connected": True,
        "detectors": len(detector_ids),
        "findings_received": findings_received,
        "findings_ingested": findings_ingested,
        "findings_skipped": findings_skipped,
    }