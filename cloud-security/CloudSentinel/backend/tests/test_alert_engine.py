from datetime import datetime, timezone
from pathlib import Path

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
from app.services.alert_engine import AlertEngine
from app.services.detection_engine import DetectionEngine

def build_finding(
    severity: FindingSeverity = FindingSeverity.HIGH,
    risk_score: float = 80,
) -> NormalizedFinding:
    now = datetime.now(timezone.utc)
    return NormalizedFinding(
        finding_id="CS-ALERTTEST001",
        source_finding_id="test-alert-001",
        source=FindingSource.CONFIG,
        finding_type=FindingType.MISCONFIGURATION,
        title="Public S3 bucket detected",
        description="The bucket allows public read access.",
        severity=severity,
        status=FindingStatus.NEW,
        asset=FindingAsset(
            asset_type=AssetType.S3,
            asset_id="bucket-1",
            asset_name="bucket-1",
        ),
        risk=FindingRisk(
            severity_score=8,
            asset_criticality=8,
            exploitability=7,
            exposure=8,
            data_sensitivity=7,
            risk_score=risk_score,
        ),
        remediation="Fix the public S3 exposure.",
        first_seen=now,
        last_seen=now,
        tags=["test"],
        metadata={},
    )

def test_critical_detection_creates_p1_alert():
    rules_path = Path(__file__).resolve().parents[2] / "detection-rules"
    detection_engine = DetectionEngine(rules_path)
    alert_engine = AlertEngine(rules_path)
    finding = build_finding()
    rule = next(rule for rule in detection_engine.evaluate(finding) if rule.rule_id == "CS-S3-001")
    alert = alert_engine.build_alert(finding, rule)
    assert alert.severity == "critical"
    assert alert.priority == "P1"
    assert alert.risk_score == 80
    assert alert.rule_id == "CS-S3-001"

def test_high_finding_uses_rule_severity_when_rule_is_critical():
    rules_path = Path(__file__).resolve().parents[2] / "detection-rules"
    detection_engine = DetectionEngine(rules_path)
    alert_engine = AlertEngine(rules_path)
    finding = build_finding(severity=FindingSeverity.HIGH, risk_score=73.5)
    rule = next(rule for rule in detection_engine.evaluate(finding) if rule.rule_id == "CS-S3-001")
    alert = alert_engine.build_alert(finding, rule)
    assert alert.severity == "critical"
    assert alert.priority == "P1"

def test_alert_tags_are_deduplicated():
    rules_path = Path(__file__).resolve().parents[2] / "detection-rules"
    detection_engine = DetectionEngine(rules_path)
    alert_engine = AlertEngine(rules_path)
    finding = build_finding()
    rule = next(rule for rule in detection_engine.evaluate(finding) if rule.rule_id == "CS-S3-001")
    alert = alert_engine.build_alert(finding, rule)
    assert alert.tags.count("test") == 1
    assert len(alert.tags) == len(set(alert.tags))


def test_alert_engine_default_rules_directory_loads_rules():
    alert_engine = AlertEngine()
    rule_ids = {rule.rule_id for rule in alert_engine.detection_engine.list_rules()}
    assert "CS-S3-001" in rule_ids
    assert len(rule_ids) >= 6
