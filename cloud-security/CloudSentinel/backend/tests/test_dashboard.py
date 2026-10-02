from datetime import datetime, timezone
from app.db.models import Alert, Finding

def test_dashboard_summary(client, db_session):
    now=datetime.now(timezone.utc)
    db_session.add(Finding(finding_id="CS-DASH-001",source_finding_id="dash-001",source="config",
      finding_type="misconfiguration",title="Public bucket",description="Bucket is public",severity="critical",
      status="new",asset={"asset_type":"s3","asset_id":"bucket-1"},severity_score=9,asset_criticality=8,
      exploitability=8,exposure=10,data_sensitivity=8,risk_score=89,remediation="Block public access",
      first_seen=now,last_seen=now,tags=[],metadata_json={}))
    db_session.add(Alert(alert_id="ALT-DASH-001",finding_id="CS-DASH-001",rule_id="CS-S3-001",
      rule_name="Public S3 Exposure",title="Public S3",message="Public access",severity="critical",priority="P1",
      risk_score=89,status="new",source="config",finding_type="misconfiguration",
      asset={"asset_type":"s3","asset_id":"bucket-1"},remediation="Block public access",tags=["aws"],
      created_at=now,updated_at=now))
    db_session.commit()
    response=client.get("/api/v1/dashboard/summary")
    assert response.status_code==200
    data=response.json()
    assert data["findings"]["critical"]>=1
    assert data["alerts"]["open"]>=1
    assert data["risk"]["max_finding_risk"]>=89
