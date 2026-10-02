from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import yaml
from app.models.finding import FindingSeverity, NormalizedFinding

@dataclass(frozen=True)
class DetectionRule:
    rule_id: str
    name: str
    description: str
    severity: FindingSeverity
    finding_types: list[str]
    sources: list[str]
    conditions: dict[str, Any]
    remediation: str
    tags: list[str]

class DetectionEngine:
    def __init__(self, rules_directory: str | Path):
        self.rules_directory = Path(rules_directory)
        self.rules = self._load_rules()

    def _load_rules(self) -> list[DetectionRule]:
        rules: list[DetectionRule] = []

        if not self.rules_directory.exists():
            return rules

        for rule_file in sorted(self.rules_directory.rglob("*.yaml")):
            with rule_file.open("r", encoding="utf-8") as file:
                document = yaml.safe_load(file) or {}

            for rule_data in document.get("rules", []):
                rules.append(
                    DetectionRule(
                        rule_id=rule_data["id"],
                        name=rule_data["name"],
                        description=rule_data["description"],
                        severity=FindingSeverity(rule_data["severity"]),
                        finding_types=rule_data.get("finding_types", []),
                        sources=rule_data.get("sources", []),
                        conditions=rule_data.get("conditions", {}),
                        remediation=rule_data.get("remediation", ""),
                        tags=rule_data.get("tags", []),
                    )
                )

        return rules

    def list_rules(self) -> list[DetectionRule]:
        return self.rules

    def evaluate(
        self,
        finding: NormalizedFinding,
    ) -> list[DetectionRule]:
        matches: list[DetectionRule] = []

        for rule in self.rules:
            if self._matches_rule(rule, finding):
                matches.append(rule)

        return matches

    def _matches_rule(
        self,
        rule: DetectionRule,
        finding: NormalizedFinding,
    ) -> bool:
        if rule.finding_types:
            if finding.finding_type.value not in rule.finding_types:
                return False

        if rule.sources:
            if finding.source.value not in rule.sources:
                return False

        return self._matches_conditions(rule.conditions, finding)

    def _matches_conditions(
        self,
        conditions: dict[str, Any],
        finding: NormalizedFinding,
    ) -> bool:
        if not conditions:
            return True

        title = finding.title.lower()
        description = finding.description.lower()

        searchable_text = f"{title} {description}"

        keywords = conditions.get("keywords", [])
        if keywords:
            if not any(
                str(keyword).lower() in searchable_text
                for keyword in keywords
            ):
                return False

        asset_types = conditions.get("asset_types", [])
        if asset_types:
            if finding.asset.asset_type.value not in asset_types:
                return False

        min_risk_score = conditions.get("min_risk_score")
        if min_risk_score is not None:
            if finding.risk.risk_score < float(min_risk_score):
                return False

        return True