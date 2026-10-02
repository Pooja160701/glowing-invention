from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, Query
from app.integrations.cloudtrail.client import (
    CloudTrailClient,
)

router = APIRouter(
    prefix="/api/v1/cloudtrail",
    tags=["CloudTrail"],
)

def _sanitize_event(
    event: dict,
) -> dict:

    cloudtrail_event = {}

    raw_event = event.get(
        "CloudTrailEvent"
    )

    if isinstance(raw_event, str):
        try:
            import json

            cloudtrail_event = json.loads(
                raw_event
            )
        except (json.JSONDecodeError, TypeError):
            cloudtrail_event = {}

    user_identity = (
        cloudtrail_event.get(
            "userIdentity"
        )
        or {}
    )

    session_context = (
        user_identity.get(
            "sessionContext"
        )
        or {}
    )

    session_issuer = (
        session_context.get(
            "sessionIssuer"
        )
        or {}
    )

    return {
        "event_id": event.get(
            "EventId"
        ),
        "event_name": event.get(
            "EventName"
        ),
        "event_time": event.get(
            "EventTime"
        ),
        "event_source": event.get(
            "EventSource"
        ),
        "username": (
            event.get("Username")
            or user_identity.get(
                "userName"
            )
        ),
        "identity_type": user_identity.get(
            "type"
        ),
        "role_name": session_issuer.get(
            "userName"
        ),
        "read_only": event.get(
            "ReadOnly"
        ),
        "source_ip": cloudtrail_event.get(
            "sourceIPAddress"
        ),
        "region": cloudtrail_event.get(
            "awsRegion"
        ),
        "event_type": cloudtrail_event.get(
            "eventType"
        ),
        "management_event": cloudtrail_event.get(
            "managementEvent"
        ),
        "resources": [
            {
                "type": resource.get(
                    "ResourceType"
                ),
                "name": resource.get(
                    "ResourceName"
                ),
            }
            for resource in (
                event.get("Resources")
                or []
            )
        ],
    }

@router.get("/events")
def get_cloudtrail_events(
    hours: int = Query(
        default=24,
        ge=1,
        le=168,
    ),
    max_results: int = Query(
        default=50,
        ge=1,
        le=50,
    ),
) -> dict:

    try:
        end_time = datetime.now(
            timezone.utc
        )

        start_time = (
            end_time
            - timedelta(hours=hours)
        )

        client = CloudTrailClient(
            region_name="ap-south-1"
        )

        events = client.lookup_events(
            start_time=start_time,
            end_time=end_time,
            max_results=max_results,
        )

        sanitized_events = [
            _sanitize_event(event)
            for event in events
        ]

        return {
            "service": "cloudtrail",
            "connected": True,
            "hours": hours,
            "events_received": len(
                sanitized_events
            ),
            "events": sanitized_events,
        }

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=(
                f"CloudTrail lookup failed: {exc}"
            ),
        ) from exc