# FinFlow — Technical Requirements

## Functional Technical Requirements
- API must support authenticated user operations.
- Imports must be retry-safe.
- Transaction processing must be observable.
- Categorization must support user correction.
- Dashboard calculations must use consistent source data.
- Product analytics must use canonical event names.
- Notification preferences must be enforced before sending eligible notifications.

## Non-Functional Requirements
- Secure by default
- Horizontally scalable stateless API layer
- Observable critical paths
- Graceful failure for non-critical dependencies
- Automated test coverage for critical business logic
- Versioned API contracts
- Auditable deployment process

## Performance Targets
Proposed targets should be validated with load testing. Examples include p95 API latency for common reads, import processing throughput, and dashboard query latency.
