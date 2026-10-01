# MediConnect Decision Log

## Decision template

| Field | Description |
|---|---|
| ID | Unique decision identifier |
| Date | Decision date |
| Status | Proposed / Accepted / Superseded |
| Decision | What was decided |
| Context | Why a decision was needed |
| Options | Considered alternatives |
| Rationale | Evidence and trade-offs |
| Impact | Product/technical/operational impact |
| Owner | Decision owner |
| Review date | When to revisit |

---

## ADR/DEC-001 — Administrative product boundary

**Status:** Accepted

**Decision:** MVP focuses on appointment access and administrative engagement, not clinical diagnosis or treatment.

**Rationale:** Keeps the initial product problem measurable and avoids unnecessary clinical scope.

**Impact:** Clinical decision support and medical advice are explicit non-goals.

---

## DEC-002 — North Star metric

**Status:** Accepted

**Decision:** Use Completed Care Journey Rate (CCJR) as the primary outcome metric.

**Rationale:** Booking volume alone does not show whether the administrative journey completed successfully.

**Impact:** Product analytics must connect booking, communication, and appointment-state events.

---

## DEC-003 — Atomic booking

**Status:** Accepted

**Decision:** Appointment creation must use server-authoritative slot validation and an atomic reservation/booking flow.

**Rationale:** Prevent stale-slot confirmations and duplicate appointments.

**Impact:** Engineering, API, database, and QA designs must support concurrency safety.

---

## DEC-004 — Self-service changes

**Status:** Accepted

**Decision:** Eligible cancellation and rescheduling are MVP capabilities.

**Rationale:** Research identified appointment-change friction as a meaningful administrative problem.

**Impact:** Policy rules, replacement-slot handling, notifications, and exception workflows are required.

---

## DEC-005 — Privacy-safe analytics

**Status:** Accepted

**Decision:** Product analytics use a canonical event taxonomy and exclude unnecessary sensitive information.

**Rationale:** Product measurement should not create avoidable privacy risk.

**Impact:** Analytics schemas require privacy review before implementation.

---

## DEC-006 — Integrations deferred

**Status:** Accepted

**Decision:** External scheduling/EHR integrations remain post-MVP.

**Rationale:** Integration architecture depends on a stable canonical scheduling model and explicit source-of-truth/conflict rules.

**Impact:** MVP uses a defined internal scheduling model with integration-ready boundaries.
