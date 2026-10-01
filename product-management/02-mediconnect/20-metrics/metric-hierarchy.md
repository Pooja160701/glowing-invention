# Metric Hierarchy

## Level 1 — Strategic outcome

### North Star
**Completed Care Journey Rate (CCJR)**

Measures the percentage of eligible booked appointments reaching the defined administrative completion state without avoidable scheduling or communication failure.

## Level 2 — Product outcomes

- Booking success.
- Search-to-book conversion.
- Self-service change completion.
- Notification delivery.
- Operational exception recovery.

## Level 3 — Guardrails

- Slot mismatch rate.
- Duplicate booking rate.
- Authorization failure rate.
- Critical unresolved exceptions.
- Core scheduling availability.
- Analytics privacy violations.

## Level 4 — Diagnostic metrics

- Search latency.
- Availability latency.
- Booking duration.
- Funnel step abandonment.
- Notification latency.
- Exception aging.
- Support volume.
- Error categories.

## Metric tree

CCJR
├── Reliable booking
│   ├── Booking success
│   ├── Slot validity
│   └── Duplicate booking protection
├── Patient self-service
│   ├── Cancellation completion
│   └── Reschedule completion
├── Communication reliability
│   ├── Delivery rate
│   └── Failure recovery
└── Operational recovery
    ├── Exception resolution
    └── Critical exception closure
