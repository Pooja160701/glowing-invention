# SupplyPulse Non-Functional Requirements

## Performance
| ID | Requirement | Target |
|---|---|---|
| NFR-001 | Standard dashboard load | p95 ≤ 3 seconds under agreed pilot load |
| NFR-002 | Exception search/filter | p95 ≤ 2 seconds |
| NFR-003 | Recommendation calculation | p95 ≤ 5 seconds for synchronous request |
| NFR-004 | API availability | ≥ 99.9% monthly for production pilot |
| NFR-005 | Critical event processing | 95% processed within 2 minutes of source availability |

## Reliability
- Idempotent ingestion for supported source feeds.
- Retry policy for transient integration failures.
- Dead-letter/error queue for failed records.
- No silent data loss.
- Reconciliation reports for critical feeds.
- Recovery runbooks for integration failures.

## Security
- TLS in transit.
- Encryption at rest.
- Least-privilege service identities.
- RBAC.
- Secret management outside source code.
- Audit logging for privileged and material actions.
- Environment separation.

## Privacy and governance
- Collect only required business data.
- Avoid unnecessary personal data.
- Mask sensitive fields in non-production environments.
- Define retention by data class.
- Record data-source ownership.
- Support deletion/retention policies where applicable.

## Accessibility
Target WCAG 2.2 AA for user-facing workflows where technically applicable.

## Observability
- application logs
- structured integration logs
- metrics
- traces for critical workflows
- data freshness monitoring
- exception processing monitoring
- alerting with ownership

## Scalability
Architecture should allow horizontal scaling of API and event-processing services and partition large operational datasets by organization, location, and time.

## AI/ML governance
If forecasting or recommendation models are introduced:
- version model outputs
- retain input snapshot/reference
- expose key drivers
- monitor drift
- log recommendation decisions
- provide fallback behavior when model confidence/data quality is insufficient
