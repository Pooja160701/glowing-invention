from typing import Any
import boto3

class GuardDutyClient:
    """Read-only client for Amazon GuardDuty findings."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "guardduty",
            region_name=region_name,
        )

    def get_detector_ids(self) -> list[str]:
        response = self.client.list_detectors()

        return response.get("DetectorIds", [])

    def list_findings(
        self,
        detector_id: str,
        max_results: int = 50,
    ) -> list[str]:
        response = self.client.list_findings(
            DetectorId=detector_id,
            MaxResults=max_results,
        )

        return response.get("FindingIds", [])

    def get_findings(
        self,
        detector_id: str,
        finding_ids: list[str],
    ) -> list[dict[str, Any]]:
        if not finding_ids:
            return []

        response = self.client.get_findings(
            DetectorId=detector_id,
            FindingIds=finding_ids,
        )

        return response.get("Findings", [])