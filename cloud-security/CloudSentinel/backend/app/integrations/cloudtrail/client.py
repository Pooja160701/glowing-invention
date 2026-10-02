from datetime import datetime, timedelta, timezone
from typing import Any
import boto3

class CloudTrailClient:
    """Read-only client for CloudTrail activity events."""

    def __init__(self, region_name: str | None = None):
        self.client = boto3.client(
            "cloudtrail",
            region_name=region_name,
        )

    def lookup_events(
        self,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        max_results: int = 50,
    ) -> list[dict[str, Any]]:

        if end_time is None:
            end_time = datetime.now(
                timezone.utc
            )

        if start_time is None:
            start_time = (
                end_time
                - timedelta(hours=24)
            )

        response = self.client.lookup_events(
            StartTime=start_time,
            EndTime=end_time,
            MaxResults=max_results,
        )

        return response.get(
            "Events",
            [],
        )