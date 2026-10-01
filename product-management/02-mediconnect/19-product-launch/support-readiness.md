# Support & Operations Readiness

## Support tiers

### Tier 1 — Operational support
Handles:
- Appointment status questions.
- Scheduling workflow questions.
- Reminder delivery questions.
- Basic account navigation.

### Tier 2 — Product/Engineering
Handles:
- Booking failures.
- Availability inconsistencies.
- Integration failures.
- Reproducible product defects.

### Tier 3 — Security/Privacy
Handles:
- Suspected unauthorized access.
- Privacy incidents.
- Audit anomalies.
- Security events.

## Support intake fields

- Case ID.
- Organization.
- Workflow.
- Timestamp.
- Severity.
- User role.
- Error category.
- Correlation ID where available.
- Resolution status.

Do not collect unnecessary clinical content in support tickets.

## Incident severity

### Critical
Potential booking-integrity failure, unauthorized access, major service outage, or material privacy/security incident.

### High
Major workflow degradation with meaningful operational impact.

### Medium
Localized product issue with workaround.

### Low
Minor defect or usability issue.

## Runbooks

Prepare runbooks for:
- Booking failure.
- Stale availability.
- Notification provider outage.
- Duplicate booking investigation.
- Authorization failure.
- Analytics event failure.
- Rollback.
