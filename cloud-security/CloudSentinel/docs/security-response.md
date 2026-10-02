# Compliance, Remediation & Incident Response

CloudSentinel now provides three response capabilities.

## Compliance scoring

Endpoint: `GET /api/v1/compliance/summary`

The service evaluates a 10-control AWS security baseline using normalized finding evidence:

- S3 public access protection
- IAM least privilege
- Public SSH restriction
- Encryption at rest
- CloudTrail audit logging
- Sensitive data protection
- Secrets protection
- Vulnerability management
- Threat detection
- Configuration compliance

A control is **non-compliant** when active finding evidence matches it, **compliant** when matching evidence exists but is resolved/suppressed, and **not evaluated** when no matching evidence exists. The score is the percentage of evaluated controls that are compliant.

## Remediation recommendations

Endpoint: `GET /api/v1/remediation/finding/{finding_id}`

CloudSentinel maps finding context to practical AWS remediation steps. Recommendations cover S3 exposure, SSH/network exposure, IAM privilege, encryption, secrets, vulnerabilities, sensitive data, CloudTrail and generic investigation.

Recommendations are guidance, not automatic changes. The platform does not modify AWS resources automatically.

## Incident lifecycle

Endpoints:

- `POST /api/v1/incidents`
- `POST /api/v1/incidents/from-alert/{alert_id}`
- `GET /api/v1/incidents`
- `GET /api/v1/incidents/{incident_id}`
- `PATCH /api/v1/incidents/{incident_id}/status`
- `POST /api/v1/incidents/{incident_id}/events`

Lifecycle:

`open -> investigating -> contained -> resolved -> closed`

Every transition is recorded as an incident event with actor, timestamp and note. Containment, root-cause and resolution notes are retained on the incident.

The dashboard exposes compliance posture, open incidents and remediation guidance. Alerts can be converted into incidents directly from the React dashboard.
