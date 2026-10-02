from typing import Any
import boto3

class SecurityHubClient:
    """Read-only client for AWS Security Hub findings."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "securityhub",
            region_name=region_name,
        )

    def get_enabled_standards(self) -> list[dict[str, Any]]:
        response = self.client.get_enabled_standards()

        return response.get(
            "StandardsSubscriptions",
            [],
        )

    def get_findings(
        self,
        max_results: int = 100,
    ) -> list[dict[str, Any]]:
        response = self.client.get_findings(
            MaxResults=max_results,
        )

        return response.get(
            "Findings",
            [],
        )