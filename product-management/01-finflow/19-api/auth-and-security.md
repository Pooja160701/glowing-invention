# FinFlow — API Authentication & Security

## Authentication
Use short-lived bearer access tokens issued by the authentication service.

## Authorization
Every resource request must be scoped to the authenticated user's authorization context.

## Security Controls
- TLS in transit
- Encryption at rest
- Token expiration and rotation
- Rate limiting
- Input validation
- Output encoding
- Audit logging for sensitive actions
- Secret management outside source code
- Dependency vulnerability scanning

## Sensitive Data
Do not expose bank credentials, account numbers, authentication secrets, or unnecessary financial values through API responses or analytics payloads.

## Privacy Operations
Support authenticated flows for data export and deletion where required by the product's applicable privacy requirements.

## Abuse Prevention
Apply rate limits to authentication, imports, feedback, and mutation endpoints. Use request IDs for incident investigation.
