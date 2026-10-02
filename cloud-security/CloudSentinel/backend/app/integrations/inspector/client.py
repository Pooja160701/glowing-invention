from typing import Any
import boto3

class InspectorClient:
    """Read-only client for Amazon Inspector findings."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "inspector2",
            region_name=region_name,
        )

    def get_findings(
        self,
        max_results: int = 100,
    ) -> list[dict[str, Any]]:
        response = self.client.list_findings(
            maxResults=max_results,
        )

        finding_arns = response.get(
            "findings",
            [],
        )

        if not finding_arns:
            return []

        return self.client.batch_get_findings(
            findingArns=finding_arns,
        ).get("findings", [])

    def get_status(self) -> dict[str, Any]:
        response = self.client.batch_get_account_status(
            accountIds=[]
        )

        return response