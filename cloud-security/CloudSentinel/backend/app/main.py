from fastapi import FastAPI
from app.api.findings import router as findings_router

app = FastAPI(
    title="CloudSentinel API",
    description="AWS Cloud Security Posture and Threat Detection Platform",
    version="0.2.0",
)

app.include_router(findings_router)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "cloudsentinel-api",
        "version": "0.2.0",
    }