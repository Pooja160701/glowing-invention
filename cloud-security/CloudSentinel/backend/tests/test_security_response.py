from datetime import datetime, timezone

from app.db.models import Finding
from app.services.compliance_service import calculate_compliance
from app.services.remediation_service import recommend_remediation


def _finding(**overrides):
    values = dict(
        finding_id="TEST-001",
        source_finding_id="src-1",
        source="security_hub",
        finding_type="misconfiguration",
        title="S3 Public Access",
        description="S3 bucket is public",
        severity="high",
        status="new",
        asset={"asset_id": "bucket-1", "asset_type": "s3"},
        severity_score=8,
        asset_criticality=7,
        exploitability=8,
        exposure=9,
        data_sensitivity=6,
        risk_score=80,
        remediation=None,
        first_seen=datetime.now(timezone.utc),
        last_seen=datetime.now(timezone.utc),
        tags=["aws", "s3"],
        metadata_json={},
    )
    values.update(overrides)
    return Finding(**values)


def test_compliance_detects_non_compliant_control():
    result = calculate_compliance([_finding()])
    s3 = next(x for x in result["controls"] if x["control_id"] == "CIS-S3-1")
    assert s3["status"] == "non_compliant"
    assert result["non_compliant"] >= 1
    assert 0 <= result["score"] <= 100


def test_remediation_recommends_s3_hardening():
    result = recommend_remediation(_finding())
    assert "Block Public Access" in result["action"]
    assert len(result["steps"]) >= 3


def test_incident_lifecycle(client):
    created = client.post(
        "/api/v1/incidents",
        json={
            "title": "S3 exposure incident",
            "description": "Public bucket requires investigation",
            "severity": "critical",
            "priority": "P1",
        },
    )
    assert created.status_code == 200
    incident = created.json()
    incident_id = incident["incident_id"]

    for status in ["investigating", "contained", "resolved", "closed"]:
        response = client.patch(
            f"/api/v1/incidents/{incident_id}/status",
            json={"status": status, "actor": "test"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == status

    events = client.get(f"/api/v1/incidents/{incident_id}").json()["events"]
    assert len(events) >= 5
