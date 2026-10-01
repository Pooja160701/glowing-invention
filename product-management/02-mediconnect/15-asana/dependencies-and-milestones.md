# Asana Dependencies and Milestones

## Milestones

### M1 — Discovery Ready
Entry:
- Provider and availability requirements agreed.
- UX booking flow defined.
- Research evidence synthesized.

### M2 — Booking MVP Ready
Entry:
- Availability search works.
- Slot validation is implemented.
- Atomic booking passes concurrency testing.
- Confirmation state is reliable.

### M3 — Self-Service Ready
Entry:
- Cancellation and rescheduling work.
- Reminder and preference flows are validated.

### M4 — Operations & Trust Ready
Entry:
- Staff scheduling is available.
- Exception queue is operational.
- RBAC, organization isolation, and audit logging pass validation.

### M5 — Controlled MVP Launch
Entry:
- Critical acceptance criteria pass.
- Production monitoring is active.
- Analytics are validated.
- Support and incident procedures are ready.

## Dependency chain

Provider discovery
→ Availability search
→ Slot validation
→ Atomic booking
→ Booking confirmation
→ Self-service changes

Identity model
→ RBAC
→ Organization isolation
→ Audit logging

Event taxonomy
→ Instrumentation
→ BI dashboard
→ Product review

MVP completion
→ Launch readiness
→ Controlled launch
→ Post-launch feedback
→ Roadmap iteration

## Blocker policy

A dependency that threatens a milestone should be surfaced during the weekly product review rather than hidden inside individual task comments.
