import json
from datetime import datetime, timezone
from .config import AUDIT_PATH
from .models import AuditEvent

def log_event(event: AuditEvent) -> None:
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), **event.model_dump()}
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")

def read_events(limit: int = 200) -> list[dict]:
    if not AUDIT_PATH.exists():
        return []
    lines = AUDIT_PATH.read_text(encoding="utf-8").splitlines()[-limit:]
    return [json.loads(line) for line in lines if line.strip()]
