from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.findings import router as findings_router
from app.api.security import router as security_router
from app.api.guardduty import router as guardduty_router
from app.api.cloudtrail import router as cloudtrail_router
from app.api.detections import router as detections_router
from app.api.alerts import router as alerts_router
from app.api.dashboard import router as dashboard_router
from app.api.compliance import router as compliance_router
from app.api.remediation import router as remediation_router
from app.api.incidents import router as incidents_router
from app.api.inventory import router as inventory_router
from app.api.dashboard_data import router as dashboard_data_router
from app.db.database import Base, engine
from app.db import models as db_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="CloudSentinel API",
    description="AWS Cloud Security Posture and Threat Detection Platform",
    version="0.6.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(findings_router)
app.include_router(security_router)
app.include_router(guardduty_router)
app.include_router(cloudtrail_router)
app.include_router(detections_router)
app.include_router(alerts_router)
app.include_router(dashboard_router)
app.include_router(compliance_router)
app.include_router(remediation_router)
app.include_router(incidents_router)
app.include_router(inventory_router)
app.include_router(dashboard_data_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "cloudsentinel-api",
        "version": "0.6.0",
    }
