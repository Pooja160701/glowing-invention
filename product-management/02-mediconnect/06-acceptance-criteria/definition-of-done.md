# Definition of Done

A MediConnect story is complete only when applicable criteria below are satisfied.

## Product

- Requirement is linked to a product objective.
- Acceptance criteria are satisfied.
- Scope is consistent with the current release.

## Design

- UX flow reviewed.
- Empty, loading, success, and error states defined.
- Accessibility considerations addressed.
- Privacy-sensitive UI copy reviewed.

## Engineering

- Implementation complete.
- Code reviewed.
- API/schema changes documented.
- Error handling implemented.
- Idempotency/transaction behavior addressed for critical scheduling operations.
- Feature flags used where appropriate.

## QA

- Unit tests pass.
- Integration tests pass.
- Acceptance criteria tested.
- Negative and authorization scenarios tested.
- Regression suite passes.
- Critical booking state transitions tested for concurrency.

## Security & Privacy

- Authorization tested server-side.
- Sensitive data exposure reviewed.
- Audit events verified where required.
- Analytics payload reviewed for unnecessary sensitive data.
- Secrets are not committed.
- Dependency/security checks pass.

## Analytics

- Required events implemented.
- Event properties validated.
- Metric definitions updated if needed.
- No duplicate or ambiguous canonical events.

## Operations

- Logging and monitoring available.
- Critical errors observable.
- Runbook updated when operational behavior changes.
- Rollback strategy known for risky changes.

## Documentation

- User-facing behavior documented.
- API documentation updated where applicable.
- Decision/architecture records updated where relevant.

## Release readiness

- Product owner accepts the story.
- QA sign-off complete.
- No unresolved P0 defects.
- Known risks documented.
