from fastapi import APIRouter, Depends

from app.core.auth import current_user

router = APIRouter(prefix="/api/v1/auth", tags=["Identity"])


@router.get("/config")
def auth_config():
    return {
        "issuer": "http://localhost:8080/realms/cloudsentinel",
        "client_id": "cloudsentinel-frontend",
        "protocol": "OpenID Connect",
        "flow": "Authorization Code + PKCE",
        "roles": [
            "security_admin",
            "security_analyst",
            "auditor",
            "developer",
        ],
    }


@router.get("/me")
def me(user: dict = Depends(current_user)):
    return {
        "subject": user["sub"],
        "username": user["username"],
        "email": user["email"],
        "roles": user["roles"],
    }
