from datetime import datetime, timezone
from uuid import uuid4
from app.models.finding import NormalizedFinding
from app.schemas.finding import FindingCreate

def normalize_finding(finding: FindingCreate) -> NormalizedFinding:
    """
    Convert a provider finding into CloudSentinel's
    normalized finding representation.
    """

    return NormalizedFinding(
        finding_id=f"CS-{uuid4().hex[:12].upper()}",
        source_finding_id=finding.source_finding_id,
        source=finding.source,
        finding_type=finding.finding_type,
        title=finding.title,
        description=finding.description,
        severity=finding.severity,
        status="new",
        asset=finding.asset,
        risk=finding.risk,
        remediation=finding.remediation,
        first_seen=finding.first_seen,
        last_seen=finding.last_seen,
        tags=finding.tags,
        metadata={
            **finding.metadata,
            "normalized_at": datetime.now(timezone.utc).isoformat(),
        },
    )