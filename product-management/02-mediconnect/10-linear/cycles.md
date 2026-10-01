# MediConnect Linear Cycles

**Assumption:** 2-week cycles.

## Cycle 1 — Discovery Foundation

**Goal:** Build the patient discovery path.

Focus:
- Authentication.
- Search.
- Filters.
- Provider details.
- Availability UI.

## Cycle 2 — Availability Integrity

**Goal:** Make availability and booking state reliable.

Focus:
- Slot validation.
- Reservation model.
- Time zones.
- Concurrency tests.
- Booking APIs.

## Cycle 3 — Booking Completion

**Goal:** Complete the end-to-end booking journey.

Focus:
- Booking.
- Confirmation.
- Idempotency.
- Basic staff schedule controls.
- Funnel events.

## Cycle 4 — Self-Service

**Goal:** Enable appointment changes and reminders.

Focus:
- Appointment details.
- Cancellation.
- Rescheduling.
- Reminder scheduling.
- Preferences.
- Notification status.

## Cycle 5 — Operations

**Goal:** Make staff operations recoverable.

Focus:
- Staff calendar.
- Exception queue.
- Assignment.
- Resolution.
- Notification failure handling.

## Cycle 6 — Trust & Launch Readiness

**Goal:** Harden the product for controlled launch.

Focus:
- RBAC.
- Organization isolation.
- Audit logs.
- Privacy-safe analytics.
- Reliability metrics.
- Security/accessibility testing.

## Cycle planning rules

Before entering a cycle:
- Issue has acceptance criteria.
- Dependencies are known.
- Design requirements are available.
- Security/privacy impact is understood.
- Estimate is agreed.

During the cycle:
- Protect the cycle goal.
- Track blocked issues explicitly.
- Avoid unplanned scope unless a priority trade-off is documented.

At cycle end:
- Review outcome metrics.
- Demo completed work.
- Record retrospective actions.
