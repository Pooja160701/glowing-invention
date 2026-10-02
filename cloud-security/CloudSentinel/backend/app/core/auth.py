import os
from functools import lru_cache
from typing import Any

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWKClient

KEYCLOAK_ISSUER = os.getenv(
    "KEYCLOAK_ISSUER_URL",
    "http://localhost:8080/realms/cloudsentinel",
)
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "cloudsentinel-frontend")
JWKS_URL = f"{KEYCLOAK_ISSUER.rstrip('/')}/protocol/openid-connect/certs"

bearer_scheme = HTTPBearer(auto_error=False)


@lru_cache(maxsize=1)
def _jwks_client() -> PyJWKClient:
    return PyJWKClient(JWKS_URL, cache_jwk_set=True, lifespan=300)


def decode_token(token: str) -> dict[str, Any]:
    try:
        signing_key = _jwks_client().get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            issuer=KEYCLOAK_ISSUER,
            options={"verify_aud": False},
        )
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    audience = claims.get("aud", [])
    if isinstance(audience, str):
        audience = [audience]
    authorized_party = claims.get("azp")
    if KEYCLOAK_CLIENT_ID not in audience and authorized_party != KEYCLOAK_CLIENT_ID:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token was not issued for CloudSentinel",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return claims


def current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> dict[str, Any]:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    claims = decode_token(credentials.credentials)
    realm_roles = claims.get("realm_access", {}).get("roles", [])
    return {
        "sub": claims.get("sub"),
        "username": claims.get("preferred_username") or claims.get("email") or claims.get("sub"),
        "email": claims.get("email"),
        "roles": sorted(set(realm_roles)),
        "claims": claims,
    }


def require_roles(*allowed_roles: str):
    allowed = set(allowed_roles) | {"security_admin"}

    def dependency(user: dict[str, Any] = Depends(current_user)) -> dict[str, Any]:
        user_roles = set(user.get("roles", []))
        if not user_roles.intersection(allowed):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "message": "Insufficient role",
                    "required_roles": sorted(allowed),
                    "user_roles": sorted(user_roles),
                },
            )
        return user

    return dependency
