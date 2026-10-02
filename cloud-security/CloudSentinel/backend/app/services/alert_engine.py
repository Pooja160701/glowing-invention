from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from app.models.finding import NormalizedFinding
from app.services.detection_engine import DetectionEngine, DetectionRule

_SEVERITY_RANK = {
    "critical": 5,
    "high": 4,
    "medium": 3,
    "low": 2,
    "informational": 1,
}

_PRIORITY = {
    "critical": "P1",
    "high": "P2",
    "medium": "P3",
    "low": "P4",
    "informational": "P5",
}

@dataclass(frozen=True)
class AlertPayload:
    alert_id: str
    finding_id: str
    rule_id: str
    rule_name: str
    title: str
    message: str
    severity: str
    priority: str
    risk_score: float
    source: str
    finding_type: str
    asset: dict
    remediation: str | None
    tags: list[str]

class AlertEngine:
    """Convert detection-rule matches into actionable security alerts."""

    def __init__(self, rules_directory: str | Path | None = None):
        self.rules_directory = Path(
            rules_directory
            or Path(__file__).resolve().parents[3] / "detection-rules"
        )
        self.detection_engine = DetectionEngine(self.rules_directory)

    def build_alert(self, finding: NormalizedFinding, rule: DetectionRule) -> AlertPayload:
        finding_severity = finding.severity.value
        rule_severity = rule.severity.value
        severity = (
            finding_severity
            if _SEVERITY_RANK[finding_severity] >= _SEVERITY_RANK[rule_severity]
            else rule_severity
        )
        return AlertPayload(
            alert_id=f"ALT-{uuid4().hex[:12].upper()}",
            finding_id=finding.finding_id,
            rule_id=rule.rule_id,
            rule_name=rule.name,
            title=f"{rule.name}: {finding.title}",
            message=(
                f"{rule.description} Source: {finding.source.value}. "
                f"Risk score: {finding.risk.risk_score:.1f}."
            ),
            severity=severity,
            priority=_PRIORITY[severity],
            risk_score=finding.risk.risk_score,
            source=finding.source.value,
            finding_type=finding.finding_type.value,
            asset=finding.asset.model_dump(mode="json"),
            remediation=rule.remediation or finding.remediation,
            tags=sorted(set([*finding.tags, *rule.tags])),
        )

    def evaluate(self, finding: NormalizedFinding) -> list[AlertPayload]:
        return [
            self.build_alert(finding, rule)
            for rule in self.detection_engine.evaluate(finding)
        ]
