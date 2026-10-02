from fastapi import APIRouter, Depends

from app.core.auth import KEYCLOAK_CLIENT_ID, KEYCLOAK_ISSUER, current_user

router = APIRouter(prefix="/api/v1/auth", tags=["Identity"])


@router.get("/config")
def auth_config():
    return {
        "issuer": KEYCLOAK_ISSUER,
        "client_id": KEYCLOAK_CLIENT_ID,
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
