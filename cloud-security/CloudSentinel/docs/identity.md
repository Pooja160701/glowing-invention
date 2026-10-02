# CloudSentinel Identity Architecture

CloudSentinel implements centralized identity using Keycloak and OpenID Connect.

## Authentication flow

```
Browser
  |
  | Authorization Code + PKCE
  v
Keycloak
  |
  | signed access token
  v
React Dashboard
  |
  | Authorization: Bearer <JWT>
  v
FastAPI
  |
  +--> verify issuer
  +--> verify RS256 signature via JWKS
  +--> verify expiration
  +--> verify client association
  +--> extract realm roles
  v
RBAC decision
```

The browser uses the Keycloak JavaScript adapter. Access and refresh tokens remain in memory rather than browser local storage.

## JWT validation

The backend validates:

1. JWT signature against Keycloak JWKS.
2. `iss` against the configured Keycloak realm issuer.
3. `exp` using PyJWT validation.
4. `aud` or `azp` against `cloudsentinel-frontend`.
5. Realm roles from `realm_access.roles`.

## RBAC

### security_admin
Full administrative access.

### security_analyst
Can operate findings, alerts and incident-response workflows.

### auditor
Read-only security visibility.

### developer
Read-only access for engineering investigation.

## Environment

```text
KEYCLOAK_ISSUER_URL=http://localhost:8080/realms/cloudsentinel
KEYCLOAK_CLIENT_ID=cloudsentinel-frontend
```

For production, replace local HTTP URLs with HTTPS, use a managed/production Keycloak deployment, restrict redirect URIs to exact application origins, and keep administrative credentials outside source control.
