from typing import Any
import boto3

class MacieClient:
    """Read-only client for Amazon Macie findings."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "macie2",
            region_name=region_name,
        )

    def get_findings(
        self,
        max_results: int = 50,
    ) -> list[dict[str, Any]]:

        max_results = min(
            max(max_results, 1),
            50,
        )

        finding_ids: list[str] = []
        next_token: str | None = None

        while True:
            request: dict[str, Any] = {
                "maxResults": max_results,
            }

            if next_token:
                request["nextToken"] = next_token

            response = self.client.list_findings(
                **request
            )

            finding_ids.extend(
                response.get(
                    "findingIds",
                    [],
                )
            )

            next_token = response.get(
                "nextToken"
            )

            if not next_token:
                break

        if not finding_ids:
            return []

        findings: list[dict[str, Any]] = []

        # Macie GetFindings accepts at most 50 IDs.
        for start in range(
            0,
            len(finding_ids),
            50,
        ):
            batch = finding_ids[
                start:start + 50
            ]

            response = self.client.get_findings(
                ids=batch,
            )

            findings.extend(
                response.get(
                    "findings",
                    [],
                )
            )

        return findings

    def get_status(
        self,
    ) -> dict[str, Any]:

        return self.client.get_macie_session()