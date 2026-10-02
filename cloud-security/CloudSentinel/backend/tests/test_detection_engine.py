from pathlib import Path
from datetime import datetime, timezone
from app.models.finding import (
    AssetType,
    FindingAsset,
    FindingRisk,
    FindingSeverity,
    FindingSource,
    FindingStatus,
    FindingType,
    NormalizedFinding,
)
from app.services.detection_engine import DetectionEngine

def build_finding(
    title: str,
    description: str,
    finding_type: FindingType,
    source: FindingSource,
    asset_type: AssetType,
) -> NormalizedFinding:
    now = datetime.now(timezone.utc)

    return NormalizedFinding(
        finding_id="CS-TEST001",
        source_finding_id="test-001",
        source=source,
        finding_type=finding_type,
        title=title,
        description=description,
        severity=FindingSeverity.HIGH,
        status=FindingStatus.NEW,
        asset=FindingAsset(
            asset_type=asset_type,
            asset_id="test-resource",
            name="test-resource",
        ),
        risk=FindingRisk(
            risk_score=80,
            severity_score=8,
            asset_criticality=8,
            exploitability=7,
            exposure=7,
            data_sensitivity=7,
        ),
        remediation="Fix the issue.",
        tags=[],
        metadata={},
        first_seen=now,
        last_seen=now,
    )

def test_public_s3_rule_matches():
    rules_path = (
        Path(__file__).resolve().parents[2] / "detection-rules"
    )

    engine = DetectionEngine(rules_path)

    finding = build_finding(
        title="Public S3 bucket detected",
        description="The bucket allows public read access.",
        finding_type=FindingType.MISCONFIGURATION,
        source=FindingSource.CONFIG,
        asset_type=AssetType.S3,
    )

    matches = engine.evaluate(finding)

    rule_ids = {rule.rule_id for rule in matches}

    assert "CS-S3-001" in rule_ids

def test_unrelated_rule_does_not_match():
    rules_path = (
        Path(__file__).resolve().parents[2] / "detection-rules"
    )

    engine = DetectionEngine(rules_path)

    finding = build_finding(
        title="Normal EC2 configuration",
        description="No security issue detected.",
        finding_type=FindingType.COMPLIANCE,
        source=FindingSource.CONFIG,
        asset_type=AssetType.EC2,
    )

    matches = engine.evaluate(finding)

    assert matches == []