from fastapi import FastAPI

app = FastAPI(
    title="CloudSentinel API",
    description="AWS Cloud Security Posture and Threat Detection Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "cloudsentinel-api",
        "version": "0.1.0",
    }