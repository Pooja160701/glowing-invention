from typing import Any
import boto3

class ConfigClient:
    """Read-only client for AWS Config compliance data."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "config",
            region_name=region_name,
        )

    def get_rules(self) -> list[dict[str, Any]]:
        response = self.client.describe_config_rules()

        return response.get(
            "ConfigRules",
            [],
        )

    def get_compliance_details(
        self,
        rule_name: str,
        max_results: int = 100,
    ) -> list[dict[str, Any]]:
        response = (
            self.client.get_compliance_details_by_config_rule(
                ConfigRuleName=rule_name,
                Limit=max_results,
            )
        )

        return response.get(
            "EvaluationResults",
            [],
        )