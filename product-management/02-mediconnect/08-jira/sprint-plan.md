# MediConnect Jira Sprint Plan

**Planning assumption:** 2-week Scrum sprints. Estimates are illustrative planning values.

## Sprint 0 — Foundation

**Goal:** Prepare the product for implementation.

Focus:
- Architecture.
- Data model.
- API contracts.
- Design system.
- Authentication foundation.
- Analytics taxonomy.
- CI/CD.
- Observability.

## Sprint 1 — Discovery

**Goal:** Enable patients to find providers and availability.

Stories:
- MED-101
- MED-104
- MED-105
- MED-106
- MED-107
- MED-108

## Sprint 2 — Booking

**Goal:** Establish reliable booking-state transitions.

Stories:
- MED-109
- MED-110
- MED-111
- MED-112
- MED-121

Critical QA:
- Concurrent booking.
- Stale slot.
- Idempotency.
- Schedule changes.

## Sprint 3 — Self-Service

**Goal:** Enable patients to manage appointments.

Stories:
- MED-103
- MED-113
- MED-114
- MED-115
- MED-116
- MED-117
- MED-118
- MED-119
- MED-120
- MED-122
- MED-123
- MED-124

## Sprint 4 — Operations & Security

**Goal:** Make exception handling and governance production-ready.

Stories:
- MED-125
- MED-126
- MED-127
- MED-128
- MED-129
- MED-130
- MED-131
- MED-132
- MED-133

Critical QA:
- Cross-organization access.
- Role authorization.
- Audit coverage.
- Sensitive analytics payloads.

## Sprint 5 — Measurement & Hardening

**Goal:** Establish product measurement and production readiness.

Stories:
- MED-134
- MED-135
- MED-136

Tasks:
- Load testing.
- Security testing.
- Accessibility validation.
- Incident runbook.
- Rollback rehearsal.
- Dashboard validation.

## Post-MVP backlog

- MED-137 — Secure administrative messaging.
- MED-138 — Advanced scheduling constraints.
- MED-139 — External schedule synchronization.

## Scrum ceremonies

- Sprint planning.
- Daily stand-up.
- Backlog refinement.
- Sprint review.
- Retrospective.

## Definition of Ready

A story should not enter a sprint until:
- Problem/user value is understood.
- Acceptance criteria exist.
- Dependencies identified.
- UX requirements available.
- Security/privacy impact understood.
- Estimate agreed.

## Definition of Done

Use `06-acceptance-criteria/definition-of-done.md`.
