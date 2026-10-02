from datetime import datetime, timezone
from app.db.models import Alert

def test_alert_status_lifecycle(client, db_session):
    now=datetime.now(timezone.utc)
    alert=Alert(alert_id="ALT-API-001",finding_id="CS-API-001",rule_id="CS-S3-001",
      rule_name="Public S3 Exposure",title="Public S3",message="Public access",severity="critical",priority="P1",
      risk_score=90,status="new",source="config",finding_type="misconfiguration",
      asset={"asset_type":"s3","asset_id":"bucket-1"},remediation="Block public access",tags=[],
      created_at=now,updated_at=now)
    db_session.add(alert); db_session.commit()
    r=client.patch("/api/v1/alerts/ALT-API-001/status",json={"status":"acknowledged"})
    assert r.status_code==200 and r.json()["acknowledged_at"] is not None
    r=client.patch("/api/v1/alerts/ALT-API-001/status",json={"status":"resolved"})
    assert r.status_code==200 and r.json()["resolved_at"] is not None

def test_alert_filtering(client, db_session):
    now=datetime.now(timezone.utc)
    db_session.add(Alert(alert_id="ALT-API-002",finding_id="CS-API-002",rule_id="CS-S3-001",
      rule_name="Public S3 Exposure",title="Public S3",message="Public access",severity="critical",priority="P1",
      risk_score=90,status="new",source="config",finding_type="misconfiguration",
      asset={"asset_type":"s3","asset_id":"bucket-1"},remediation="Block public access",tags=[],
      created_at=now,updated_at=now))
    db_session.commit()
    r=client.get("/api/v1/alerts?severity=critical&min_risk_score=80")
    assert r.status_code==200 and len(r.json())>=1
