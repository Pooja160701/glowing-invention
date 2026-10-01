from datetime import datetime, timezone
from uuid import uuid4
from app.models.finding import NormalizedFinding
from app.schemas.finding import FindingCreate
from app.services.risk_engine import calculate_risk

def normalize_finding(finding: FindingCreate) -> NormalizedFinding:
    """
    Convert a provider finding into CloudSentinel's
    normalized finding representation.

    The risk score is calculated internally by CloudSentinel.
    """

    calculated_risk = calculate_risk(
        severity_score=finding.risk.severity_score,
        asset_criticality=finding.risk.asset_criticality,
        exploitability=finding.risk.exploitability,
        exposure=finding.risk.exposure,
        data_sensitivity=finding.risk.data_sensitivity,
    )

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
        risk=calculated_risk,
        remediation=finding.remediation,
        first_seen=finding.first_seen,
        last_seen=finding.last_seen,
        tags=finding.tags,
        metadata={
            **finding.metadata,
            "normalized_at": datetime.now(timezone.utc).isoformat(),
        },
    )