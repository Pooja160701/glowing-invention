from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Alert, Incident, IncidentEvent
from app.schemas.incident import (
    IncidentCreate,
    IncidentEventCreate,
    IncidentEventResponse,
    IncidentResponse,
    IncidentStatus,
    IncidentStatusUpdate,
)

router = APIRouter(prefix="/api/v1/incidents", tags=["Incidents"])

_ALLOWED_TRANSITIONS = {
    "open": {"investigating", "contained", "resolved", "closed"},
    "investigating": {"contained", "resolved", "closed"},
    "contained": {"investigating", "resolved"},
    "resolved": {"closed", "investigating"},
    "closed": set(),
}

def _event_response(event: IncidentEvent) -> IncidentEventResponse:
    return IncidentEventResponse(
        event_id=event.event_id,
        incident_id=event.incident_id,
        event_type=event.event_type,
        actor=event.actor,
        note=event.note,
        created_at=event.created_at,
    )

def _response(db: Session, incident: Incident) -> IncidentResponse:
    events = (
        db.query(IncidentEvent)
        .filter(IncidentEvent.incident_id == incident.incident_id)
        .order_by(IncidentEvent.created_at.asc())
        .all()
    )
    return IncidentResponse(
        incident_id=incident.incident_id,
        title=incident.title,
        description=incident.description,
        severity=incident.severity,
        priority=incident.priority,
        status=IncidentStatus(incident.status),
        owner=incident.owner,
        finding_ids=incident.finding_ids or [],
        alert_ids=incident.alert_ids or [],
        containment_notes=incident.containment_notes,
        root_cause=incident.root_cause,
        resolution_notes=incident.resolution_notes,
        created_at=incident.created_at,
        updated_at=incident.updated_at,
        contained_at=incident.contained_at,
        resolved_at=incident.resolved_at,
        closed_at=incident.closed_at,
        events=[_event_response(e) for e in events],
    )

def _add_event(db: Session, incident_id: str, event_type: str, note: str, actor: str) -> IncidentEvent:
    event = IncidentEvent(
        event_id=f"IEV-{uuid4().hex[:12].upper()}",
        incident_id=incident_id,
        event_type=event_type,
        actor=actor,
        note=note,
    )
    db.add(event)
    return event

@router.post("", response_model=IncidentResponse)
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    incident = Incident(
        incident_id=f"INC-{uuid4().hex[:12].upper()}",
        title=payload.title,
        description=payload.description,
        severity=payload.severity,
        priority=payload.priority,
        status="open",
        owner=payload.owner,
        finding_ids=payload.finding_ids,
        alert_ids=payload.alert_ids,
    )
    db.add(incident)
    db.flush()
    _add_event(db, incident.incident_id, "created", "Incident created.", payload.owner or "analyst")
    db.commit()
    db.refresh(incident)
    return _response(db, incident)

@router.post("/from-alert/{alert_id}", response_model=IncidentResponse)
def create_incident_from_alert(alert_id: str, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.alert_id == alert_id).first()
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    existing = (
        db.query(Incident)
        .filter(Incident.alert_ids.contains([alert.alert_id]))
        .first()
    )
    if existing:
        return _response(db, existing)

    incident = Incident(
        incident_id=f"INC-{uuid4().hex[:12].upper()}",
        title=f"Incident: {alert.title}",
        description=alert.message,
        severity=alert.severity,
        priority=alert.priority,
        status="open",
        finding_ids=[alert.finding_id],
        alert_ids=[alert.alert_id],
    )
    db.add(incident)
    db.flush()
    _add_event(
        db,
        incident.incident_id,
        "created_from_alert",
        f"Incident created from alert {alert.alert_id}.",
        "system",
    )
    db.commit()
    db.refresh(incident)
    return _response(db, incident)

@router.get("", response_model=list[IncidentResponse])
def list_incidents(
    status: IncidentStatus | None = Query(default=None),
    severity: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Incident)
    if status:
        query = query.filter(Incident.status == status.value)
    if severity:
        query = query.filter(Incident.severity == severity)
    incidents = query.order_by(Incident.updated_at.desc()).all()
    return [_response(db, incident) for incident in incidents]

@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: str, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(Incident.incident_id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return _response(db, incident)

@router.patch("/{incident_id}/status", response_model=IncidentResponse)
def update_incident_status(
    incident_id: str,
    payload: IncidentStatusUpdate,
    db: Session = Depends(get_db),
):
    incident = db.query(Incident).filter(Incident.incident_id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    current = incident.status
    target = payload.status.value
    if target != current and target not in _ALLOWED_TRANSITIONS.get(current, set()):
        raise HTTPException(
            status_code=409,
            detail=f"Invalid incident transition: {current} -> {target}",
        )

    now = datetime.now(timezone.utc)
    incident.status = target
    incident.updated_at = now

    if payload.containment_notes is not None:
        incident.containment_notes = payload.containment_notes
    if payload.root_cause is not None:
        incident.root_cause = payload.root_cause
    if payload.resolution_notes is not None:
        incident.resolution_notes = payload.resolution_notes

    if target == "contained":
        incident.contained_at = incident.contained_at or now
    elif target == "resolved":
        incident.contained_at = incident.contained_at or now
        incident.resolved_at = incident.resolved_at or now
    elif target == "closed":
        incident.contained_at = incident.contained_at or now
        incident.resolved_at = incident.resolved_at or now
        incident.closed_at = incident.closed_at or now
    elif target == "investigating":
        incident.closed_at = None

    note = payload.note or f"Incident status changed from {current} to {target}."
    _add_event(db, incident.incident_id, f"status_{target}", note, payload.actor)
    db.commit()
    db.refresh(incident)
    return _response(db, incident)

@router.post("/{incident_id}/events", response_model=IncidentEventResponse)
def add_incident_event(
    incident_id: str,
    payload: IncidentEventCreate,
    db: Session = Depends(get_db),
):
    incident = db.query(Incident).filter(Incident.incident_id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    event = _add_event(db, incident_id, payload.event_type, payload.note, payload.actor)
    incident.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(event)
    return _event_response(event)

@router.get("/stats/summary")
def incident_stats(db: Session = Depends(get_db)):
    incidents = db.query(Incident).all()
    return {
        "total": len(incidents),
        "open": sum(i.status in {"open", "investigating", "contained"} for i in incidents),
        "resolved": sum(i.status == "resolved" for i in incidents),
        "closed": sum(i.status == "closed" for i in incidents),
        "by_status": {
            status: sum(i.status == status for i in incidents)
            for status in ["open", "investigating", "contained", "resolved", "closed"]
        },
    }
