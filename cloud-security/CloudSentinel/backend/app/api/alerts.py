from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Alert, Finding
from app.models.finding import (
    FindingAsset,
    FindingRisk,
    FindingSeverity,
    FindingSource,
    FindingStatus,
    FindingType,
    NormalizedFinding,
)
from app.schemas.alert import AlertResponse, AlertStatus, AlertStatusUpdate
from app.services.alert_engine import AlertEngine
from app.services.alert_notifications import AlertNotificationService

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts"])
alert_engine = AlertEngine()
notification_service = AlertNotificationService()

def _to_normalized_finding(row: Finding) -> NormalizedFinding:
    return NormalizedFinding(
        finding_id=row.finding_id,
        source_finding_id=row.source_finding_id,
        source=FindingSource(row.source),
        finding_type=FindingType(row.finding_type),
        title=row.title,
        description=row.description,
        severity=FindingSeverity(row.severity),
        status=FindingStatus(row.status),
        asset=FindingAsset.model_validate({**row.asset, "asset_name": row.asset.get("asset_name") or row.asset.get("name")}),
        risk=FindingRisk(
            severity_score=row.severity_score,
            asset_criticality=row.asset_criticality,
            exploitability=row.exploitability,
            exposure=row.exposure,
            data_sensitivity=row.data_sensitivity,
            risk_score=row.risk_score,
        ),
        remediation=row.remediation,
        first_seen=row.first_seen,
        last_seen=row.last_seen,
        tags=row.tags or [],
        metadata=row.metadata_json or {},
    )

def _alert_response(alert: Alert) -> AlertResponse:
    return AlertResponse(
        alert_id=alert.alert_id,
        finding_id=alert.finding_id,
        rule_id=alert.rule_id,
        rule_name=alert.rule_name,
        title=alert.title,
        message=alert.message,
        severity=alert.severity,
        priority=alert.priority,
        risk_score=alert.risk_score,
        status=AlertStatus(alert.status),
        source=alert.source,
        finding_type=alert.finding_type,
        asset=alert.asset,
        remediation=alert.remediation,
        tags=alert.tags or [],
        created_at=alert.created_at,
        updated_at=alert.updated_at,
        acknowledged_at=alert.acknowledged_at,
        resolved_at=alert.resolved_at,
    )

def _persist_alerts(db: Session, payloads) -> list[Alert]:
    alerts: list[Alert] = []
    for payload in payloads:
        existing = (
            db.query(Alert)
            .filter(
                Alert.finding_id == payload.finding_id,
                Alert.rule_id == payload.rule_id,
            )
            .first()
        )
        if existing:
            if existing.status not in {"resolved", "suppressed"}:
                existing.risk_score = payload.risk_score
                existing.severity = payload.severity
                existing.priority = payload.priority
                existing.message = payload.message
                existing.updated_at = datetime.now(timezone.utc)
            alerts.append(existing)
            continue

        alert = Alert(
            alert_id=payload.alert_id,
            finding_id=payload.finding_id,
            rule_id=payload.rule_id,
            rule_name=payload.rule_name,
            title=payload.title,
            message=payload.message,
            severity=payload.severity,
            priority=payload.priority,
            risk_score=payload.risk_score,
            status="new",
            source=payload.source,
            finding_type=payload.finding_type,
            asset=payload.asset,
            remediation=payload.remediation,
            tags=payload.tags,
        )
        db.add(alert)
        alerts.append(alert)
    return alerts

@router.post("/generate/{finding_id}", response_model=list[AlertResponse])
def generate_alerts(finding_id: str, db: Session = Depends(get_db)) -> list[AlertResponse]:
    finding = db.query(Finding).filter(Finding.finding_id == finding_id).first()
    if finding is None:
        raise HTTPException(status_code=404, detail="Finding not found")

    payloads = alert_engine.evaluate(_to_normalized_finding(finding))
    alerts = _persist_alerts(db, payloads)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        existing = (
            db.query(Alert)
            .filter(Alert.finding_id == finding_id)
            .order_by(Alert.created_at.desc())
            .all()
        )
        return [_alert_response(alert) for alert in existing]

    for alert in alerts:
        db.refresh(alert)
    return [_alert_response(alert) for alert in alerts]

@router.post("/generate", response_model=dict)
def generate_alerts_for_findings(
    db: Session = Depends(get_db),
) -> dict:
    findings = (
        db.query(Finding)
        .filter(Finding.status.notin_(["resolved", "suppressed"]))
        .all()
    )
    generated = 0
    matched_findings = 0
    for finding in findings:
        payloads = alert_engine.evaluate(_to_normalized_finding(finding))
        if payloads:
            matched_findings += 1
        _persist_alerts(db, payloads)
        generated += len(payloads)
    db.commit()
    return {
        "findings_evaluated": len(findings),
        "findings_with_matches": matched_findings,
        "alerts_generated_or_updated": generated,
    }


@router.post("/notify/{alert_id}")
def notify_alert(alert_id: str, db: Session = Depends(get_db)) -> dict:
    alert = db.query(Alert).filter(Alert.alert_id == alert_id).first()
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"alert_id": alert.alert_id, "results": [
        {"channel": r.channel, "delivered": r.delivered, "detail": r.detail}
        for r in notification_service.notify(alert)
    ]}

@router.post("/notify/open")
def notify_open_alerts(db: Session = Depends(get_db)) -> dict:
    alerts = db.query(Alert).filter(Alert.status.in_([AlertStatus.NEW.value, AlertStatus.ACKNOWLEDGED.value])).order_by(Alert.risk_score.desc()).all()
    results=[]
    for alert in alerts:
        for r in notification_service.notify(alert):
            results.append({"alert_id":alert.alert_id,"channel":r.channel,"delivered":r.delivered,"detail":r.detail})
    return {"alerts_evaluated":len(alerts),"notifications_attempted":len(results),"results":results}

@router.get("", response_model=list[AlertResponse])
def list_alerts(
    severity: str | None = Query(default=None),
    status: AlertStatus | None = Query(default=None),
    priority: str | None = Query(default=None),
    source: str | None = Query(default=None),
    rule_id: str | None = Query(default=None),
    min_risk_score: float | None = Query(default=None, ge=0, le=100),
    db: Session = Depends(get_db),
) -> list[AlertResponse]:
    query = db.query(Alert)
    if severity:
        query = query.filter(Alert.severity == severity)
    if status:
        query = query.filter(Alert.status == status.value)
    if priority:
        query = query.filter(Alert.priority == priority)
    if source:
        query = query.filter(Alert.source == source)
    if rule_id:
        query = query.filter(Alert.rule_id == rule_id)
    if min_risk_score is not None:
        query = query.filter(Alert.risk_score >= min_risk_score)
    alerts = query.order_by(Alert.risk_score.desc(), Alert.created_at.desc()).all()
    return [_alert_response(alert) for alert in alerts]

@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: str, db: Session = Depends(get_db)) -> AlertResponse:
    alert = db.query(Alert).filter(Alert.alert_id == alert_id).first()
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return _alert_response(alert)

@router.patch("/{alert_id}/status", response_model=AlertResponse)
def update_alert_status(
    alert_id: str,
    update: AlertStatusUpdate,
    db: Session = Depends(get_db),
) -> AlertResponse:
    alert = db.query(Alert).filter(Alert.alert_id == alert_id).first()
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    now = datetime.now(timezone.utc)
    new_status = update.status.value
    if new_status == "acknowledged":
        alert.acknowledged_at = alert.acknowledged_at or now
        alert.resolved_at = None
    elif new_status == "resolved":
        alert.acknowledged_at = alert.acknowledged_at or now
        alert.resolved_at = alert.resolved_at or now
    elif new_status == "new":
        alert.acknowledged_at = None
        alert.resolved_at = None
    elif new_status == "suppressed":
        alert.resolved_at = None

    alert.status = new_status
    alert.updated_at = now
    db.commit()
    db.refresh(alert)
    return _alert_response(alert)
