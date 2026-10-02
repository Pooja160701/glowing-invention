from app.db.models import Finding

def test_vulnerability_endpoint(client, db_session):
    db_session.add(Finding(
        finding_id="VULN-1", source_finding_id="src", source="inspector",
        finding_type="vulnerability", title="Critical package CVE", description="CVE",
        severity="critical", status="new", asset={"asset_id":"i-1","asset_type":"ec2"},
        severity_score=10, asset_criticality=8, exploitability=9, exposure=7,
        data_sensitivity=5, risk_score=90, remediation="Patch", first_seen="2026-01-01",
        last_seen="2026-01-01", tags=[], metadata_json={}
    ))
    db_session.commit()
    r=client.get("/api/v1/dashboard-data/vulnerabilities")
    assert r.status_code == 200 and r.json()["total"] == 1

def test_iam_risk_endpoint(client, db_session):
    db_session.add(Finding(
        finding_id="IAM-1", source_finding_id="src", source="iam",
        finding_type="identity", title="Wildcard IAM policy", description="Overly broad access",
        severity="high", status="new", asset={"asset_id":"role-1","asset_type":"iam_role"},
        severity_score=8, asset_criticality=8, exploitability=8, exposure=7,
        data_sensitivity=7, risk_score=80, remediation="Restrict policy", first_seen="2026-01-01",
        last_seen="2026-01-01", tags=[], metadata_json={}
    ))
    db_session.commit()
    r=client.get("/api/v1/dashboard-data/iam-risks")
    assert r.status_code == 200 and r.json()["total"] == 1
