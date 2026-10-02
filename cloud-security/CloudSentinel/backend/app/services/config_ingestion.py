from datetime import datetime, timezone
from typing import Any
from sqlalchemy.orm import Session
from app.db.models import Finding
from app.integrations.config.client import ConfigClient
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

    if (
        isinstance(value, (str, int, float, bool))
        or value is None
    ):
        return value

    return str(value)

def _extract_asset(
    evaluation: dict,
) -> FindingAsset:

    qualifier = (
        evaluation.get(
            "EvaluationResultIdentifier"
        )
        or {}
    )

    qualifier = (
        qualifier.get(
            "EvaluationResultQualifier"
        )
        or {}
    )

    resource_id = (
        qualifier.get(
            "ResourceId"
        )
        or evaluation.get(
            "EvaluationResultIdentifier",
            {}
        ).get("EvaluationResultQualifier", {})
        .get("ResourceId")
        or "unknown"
    )

    resource_type = qualifier.get(
        "ResourceType"
    ) or "Unknown"

    asset_type_map = {
        "AWS::S3::Bucket": AssetType.S3,
        "AWS::EC2::Instance": AssetType.EC2,
        "AWS::IAM::Role": AssetType.IAM_ROLE,
        "AWS::IAM::User": AssetType.IAM_USER,
        "AWS::IAM::Policy": AssetType.IAM_POLICY,
        "AWS::ECR::Repository": AssetType.ECR,
        "AWS::Lambda::Function": AssetType.LAMBDA,
        "AWS::EC2::SecurityGroup": AssetType.SECURITY_GROUP,
        "AWS::KMS::Key": AssetType.KMS_KEY,
    }

    asset_type = asset_type_map.get(
        resource_type,
        AssetType.UNKNOWN,
    )

    return FindingAsset(
        asset_id=str(resource_id),
        asset_type=asset_type,
        region=None,
        account_id=None,
        resource_arn=(
            resource_id
            if isinstance(
                resource_id,
                str,
            )
            and resource_id.startswith("arn:")
            else None
        ),
        asset_name=str(resource_id),
    )

def _build_finding_create(
    rule: dict,
    evaluation: dict,
) -> FindingCreate:

    rule_name = rule.get(
        "ConfigRuleName",
        "unknown-rule",
    )

    rule_identifier = rule.get(
        "Source",
        {}
    ).get(
        "SourceIdentifier",
        rule_name,
    )

    resource_id = (
        evaluation.get(
            "EvaluationResultIdentifier",
            {}
        )
        .get(
            "EvaluationResultQualifier",
            {}
        )
        .get(
            "ResourceId",
            "unknown",
        )
    )

    source_finding_id = (
        f"{rule_name}:{resource_id}"
    )

    title = (
        f"AWS Config non-compliance: "
        f"{rule_name}"
    )

    description = (
        evaluation.get(
            "Annotation"
        )
        or (
            f"Resource {resource_id} "
            f"failed AWS Config rule "
            f"{rule_identifier}."
        )
    )

    evaluation_time = (
        evaluation.get(
            "ResultRecordedTime"
        )
        or evaluation.get(
            "ConfigRuleInvokedTime"
        )
    )

    if isinstance(
        evaluation_time,
        datetime,
    ):
        timestamp = (
            evaluation_time
            if evaluation_time.tzinfo
            else evaluation_time.replace(
                tzinfo=timezone.utc
            )
        )
    else:
        timestamp = datetime.now(
            timezone.utc
        )

    safe_metadata = _json_safe(
        {
            "config_rule_name": rule_name,
            "source_identifier": rule_identifier,
            "compliance_type": evaluation.get(
                "ComplianceType"
            ),
            "annotation": evaluation.get(
                "Annotation"
            ),
            "raw_evaluation": evaluation,
        }
    )

    return FindingCreate(
        source_finding_id=source_finding_id,
        source="config",
        finding_type=FindingType.COMPLIANCE,
        title=title,
        description=description,
        severity=FindingSeverity.HIGH,
        asset=_extract_asset(
            evaluation
        ),
        risk={
            "severity_score": 8.0,
            "asset_criticality": 7.0,
            "exploitability": 6.0,
            "exposure": 7.0,
            "data_sensitivity": 6.0,
        },
        remediation=(
            f"Remediate the resource so it satisfies "
            f"AWS Config rule {rule_name}."
        ),
        first_seen=timestamp,
        last_seen=timestamp,
        tags=[
            "aws",
            "config",
            "compliance",
            rule_name,
        ],
        metadata=safe_metadata,
    )

def ingest_config_findings(
    db: Session,
    region_name: str = "ap-south-1",
) -> dict:

    client = ConfigClient(
        region_name=region_name
    )

    rules = client.get_rules()

    evaluations_received = 0
    findings_ingested = 0
    findings_skipped = 0

    for rule in rules:

        rule_name = rule.get(
            "ConfigRuleName"
        )

        if not rule_name:
            continue

        evaluations = (
            client.get_compliance_details(
                rule_name=rule_name
            )
        )

        evaluations_received += len(
            evaluations
        )

        for evaluation in evaluations:

            compliance_type = (
                evaluation.get(
                    "ComplianceType"
                )
            )

            if compliance_type != "NON_COMPLIANT":
                continue

            finding_create = (
                _build_finding_create(
                    rule,
                    evaluation,
                )
            )

            source_finding_id = (
                finding_create.source_finding_id
            )

            existing = (
                db.query(Finding)
                .filter(
                    Finding.source == "config",
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
        "service": "config",
        "connected": True,
        "rules_checked": len(rules),
        "evaluations_received": evaluations_received,
        "findings_ingested": findings_ingested,
        "findings_skipped": findings_skipped,
    }