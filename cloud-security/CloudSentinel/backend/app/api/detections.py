from pathlib import Path
from fastapi import APIRouter
from app.services.detection_engine import DetectionEngine

router = APIRouter(
    prefix="/api/v1/detections",
    tags=["Detections"],
)

RULES_DIRECTORY = (
    Path(__file__).resolve().parents[3] / "detection-rules"
)

engine = DetectionEngine(RULES_DIRECTORY)

@router.get("/rules")
def list_detection_rules() -> dict:
    rules = engine.list_rules()

    return {
        "rules_count": len(rules),
        "rules": [
            {
                "id": rule.rule_id,
                "name": rule.name,
                "description": rule.description,
                "severity": rule.severity.value,
                "finding_types": rule.finding_types,
                "sources": rule.sources,
                "remediation": rule.remediation,
                "tags": rule.tags,
            }
            for rule in rules
        ],
    }