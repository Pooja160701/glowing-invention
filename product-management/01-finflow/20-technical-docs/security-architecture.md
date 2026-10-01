# FinFlow — Security Architecture

## Security Principles
- Least privilege
- Defense in depth
- Secure defaults
- Data minimization
- Strong authentication
- Explicit authorization
- Auditability

## Controls

### Identity
- Short-lived access tokens
- Refresh-token rotation
- MFA support where appropriate
- Session revocation

### Authorization
- Resource ownership checks
- Role-based access for internal tooling
- Service-to-service identity

### Data Protection
- TLS in transit
- Encryption at rest
- Key management
- Secret manager
- No credentials in source code

### Application Security
- Input validation
- Output encoding
- CSRF protection where applicable
- Rate limiting
- Dependency scanning
- SAST/DAST
- Container/image scanning

### Privacy
- Minimize collected data
- Mask sensitive fields in logs
- Restrict analytics payloads
- Define retention periods
- Support data export/deletion workflows

## Threat Areas
- Account takeover
- Unauthorized data access
- Malicious import files
- API abuse
- Sensitive-data leakage
- Dependency vulnerabilities
- Privilege escalation
