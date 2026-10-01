# Roadmap Dependencies & Risks

## Critical dependencies

| Dependency | Needed for | Risk if delayed |
|---|---|---|
| Identity/authentication | All protected workflows | Blocks MVP |
| Canonical appointment model | Booking + integrations | High rework |
| Availability engine | Discovery + booking | Booking failure |
| Atomic reservation | Booking integrity | Duplicate/stale bookings |
| Notification provider | Reminders | Communication gaps |
| RBAC model | Staff operations | Security exposure |
| Audit infrastructure | Governance | Compliance/forensics gap |
| Analytics taxonomy | Measurement | Weak product learning |
| Observability | Production launch | Slow incident response |
| Integration contracts | Post-MVP | Schedule divergence |

## Risk register

### R1 — Stale availability
**Impact:** High  
**Mitigation:** Server-side revalidation, atomic reservation, freshness monitoring.

### R2 — Duplicate booking
**Impact:** Critical  
**Mitigation:** Idempotency keys, transactional state transitions, concurrency testing.

### R3 — Provider schedule changes
**Impact:** High  
**Mitigation:** Exception queue, controlled availability updates, patient communication workflow.

### R4 — Notification failure
**Impact:** Medium/High  
**Mitigation:** Delivery tracking, retries, failure state, operational escalation.

### R5 — Unauthorized access
**Impact:** Critical  
**Mitigation:** Server-side RBAC, organization scoping, negative authorization tests, audit logs.

### R6 — Privacy over-collection
**Impact:** High  
**Mitigation:** Data inventory, minimization review, analytics governance, retention policy.

### R7 — Integration complexity
**Impact:** High  
**Mitigation:** Defer integrations until source-of-truth and conflict policies are defined.

### R8 — Staff adoption
**Impact:** High  
**Mitigation:** Workflow observation, usability testing, gradual rollout, measure intervention time.

### R9 — Scope expansion into clinical functionality
**Impact:** High  
**Mitigation:** Explicit non-goals and product review gates.

## Launch dependency sequence

**Identity → Data model → Availability → Booking → Notifications → Staff operations → Security/governance → Analytics → Controlled launch**

This sequence can overlap where safe, but booking-state integrity and access control should not be bypassed.
