from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Finding
from app.services.asset_inventory import inventory

router = APIRouter(prefix="/api/v1/inventory", tags=["Asset Inventory"])

@router.get("/assets")
def assets(
    asset_type: str | None = Query(None),
    region: str | None = Query(None),
    db: Session = Depends(get_db),
):
    try:
        result = inventory()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"AWS asset inventory failed: {exc}") from exc
    rows = result["assets"]
    if asset_type:
        rows = [x for x in rows if x["asset_type"] == asset_type]
    if region:
        rows = [x for x in rows if x["region"] == region]
    finding_assets = {}
    for f in db.query(Finding).all():
        asset = f.asset or {}
        key = asset.get("asset_id")
        if key:
            finding_assets.setdefault(str(key), []).append({
                "finding_id": f.finding_id, "severity": f.severity, "risk_score": f.risk_score
            })
    for row in rows:
        row["findings"] = finding_assets.get(row["asset_id"], [])
        row["finding_count"] = len(row["findings"])
    return {**result, "assets": rows, "filtered_count": len(rows)}
