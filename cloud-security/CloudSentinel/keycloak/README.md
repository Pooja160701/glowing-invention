# CloudSentinel Keycloak

CloudSentinel uses Keycloak as the local identity provider.

## Components

- Realm: `cloudsentinel`
- Frontend client: `cloudsentinel-frontend`
- Protocol: OpenID Connect
- Flow: Authorization Code + PKCE
- Roles: `security_admin`, `security_analyst`, `auditor`, `developer`

The realm definition is imported automatically by the Docker Compose service. Keycloak's container import directory is used with `--import-realm`.

## Start

From the CloudSentinel directory:

```bash
docker compose up -d keycloak
```

Open the Keycloak Admin Console:

`http://localhost:8080/admin`

The development admin credentials come from:

- `KEYCLOAK_ADMIN_USERNAME`
- `KEYCLOAK_ADMIN_PASSWORD`

Set these in a local `.env` file. Never commit production credentials.

## Create a user

In the `cloudsentinel` realm:

1. Create a user.
2. Set a strong password and disable temporary password if desired.
3. Open Role mapping.
4. Assign exactly one application role:
   - Security Admin: `security_admin`
   - Security Analyst: `security_analyst`
   - Auditor: `auditor`
   - Developer: `developer`

The backend trusts only signed JWTs issued by this realm and checks the issuer, expiration, signing key and client association before using the role claim.

## Role model

| Role | Read security data | Modify findings/alerts/incidents | Administrative |
|---|---|---|---|
| security_admin | Yes | Yes | Yes |
| security_analyst | Yes | Yes | No |
| auditor | Yes | No | No |
| developer | Yes | No | No |

The current project keeps read-only GET endpoints available for service discovery and dashboard rendering. Mutation endpoints enforce RBAC.
