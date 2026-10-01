# Non-Functional Requirements

## Security

- Encrypt network traffic using current secure transport protocols.
- Encrypt sensitive stored data.
- Enforce least privilege.
- Separate authentication and authorization concerns.
- Apply rate limits to abuse-prone endpoints.
- Log security-relevant events.
- Protect secrets through managed secret storage.
- Perform dependency and vulnerability scanning in CI.

## Privacy

- Collect only data required for defined product purposes.
- Classify data before implementation.
- Do not place unnecessary sensitive information in analytics events.
- Provide communication preference controls.
- Define retention and deletion behavior.
- Restrict access by organization and role.
- Maintain auditable access to sensitive administrative records.

## Reliability

- Booking operations must be idempotent.
- Appointment state transitions must be transactional.
- Downstream notification failures must not silently change booking state.
- Failed asynchronous jobs require retry/dead-letter behavior.
- Critical scheduling data requires backup and recovery procedures.

## Performance

Initial targets:
- P95 search ≤ 2s.
- P95 availability query ≤ 1.5s.
- P95 booking API ≤ 3s excluding downstream notifications.
- Staff appointment list loads within 2s under agreed baseline conditions.

## Scalability

The architecture should support horizontal scaling of:
- API services.
- Availability queries.
- Notification workers.
- Analytics ingestion.

Scheduling state must remain consistent across horizontally scaled services.

## Availability

Target for mature production:
- 99.9% monthly availability for core scheduling services.

Planned maintenance and dependency outages must have defined operational procedures.

## Accessibility

Target WCAG 2.2 AA where applicable.

Must support:
- Keyboard navigation.
- Focus management.
- Screen-reader semantics.
- Accessible error handling.
- Responsive interfaces.
- Non-color-only status indicators.

## Observability

Every critical request should support:
- Structured logs.
- Metrics.
- Traces/correlation identifiers.
- Error classification.

Critical alerts:
- Booking failure spikes.
- Availability synchronization failure.
- Notification failure spikes.
- Authentication/authorization anomalies.
- Queue backlog.
- Data consistency incidents.

## Maintainability

- API contracts versioned.
- Schema changes reviewed.
- Automated tests required for critical state transitions.
- Architecture decisions documented.
- Feature flags used for risky launches where appropriate.
