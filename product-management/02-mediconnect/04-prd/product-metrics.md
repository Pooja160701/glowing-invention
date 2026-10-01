# Product Metrics

## North Star

### Completed Care Journey Rate (CCJR)

**Definition:** Percentage of eligible booked appointments reaching the defined administrative completion state without avoidable scheduling or communication failure.

**Formula:**

`completed eligible appointments / eligible booked appointments × 100`

---

## Acquisition / discovery

| Metric | Definition |
|---|---|
| Search start rate | Users initiating provider/clinic search |
| Provider view rate | Searches leading to provider detail views |
| Availability view rate | Provider views leading to slot availability |
| Search-to-book conversion | Searches resulting in completed bookings |

## Activation

Suggested activation definition:

A new patient is activated after completing a valid appointment booking and reaching the confirmation state.

Track:
- Signup-to-book rate.
- Time to first booking.
- Booking failure rate.

## Engagement

- Appointment self-service change rate.
- Reminder interaction rate where measurable.
- Appointment history usage.
- Communication preference completion.

## Operational metrics

- Staff exception-resolution time.
- Exceptions per 100 appointments.
- Manual intervention rate.
- Availability update success rate.
- Notification delivery rate.
- Notification failure rate.
- Booking conflict rate.

## Quality / reliability

- Booking success rate.
- Duplicate booking rate.
- Slot mismatch rate.
- API error rate.
- P95 latency.
- Scheduling synchronization failure rate.

## Privacy/security guardrails

- Unauthorized access incidents.
- Privilege escalation attempts.
- Audit logging coverage.
- Sensitive analytics-event violation count.
- Data retention-policy exceptions.

## Suggested initial targets

These are **portfolio planning targets, not observed market benchmarks**.

| Metric | Initial target |
|---|---:|
| Booking success rate | ≥ 98% |
| Notification delivery rate | ≥ 98% |
| Slot mismatch rate | < 0.5% |
| Duplicate booking rate | < 0.1% |
| Core scheduling availability | ≥ 99.9% |
| P95 availability response | ≤ 1.5 sec |
| Critical audit-event coverage | 100% |
| Sensitive analytics-event violations | 0 |

Targets should be revised after baseline data is available.
