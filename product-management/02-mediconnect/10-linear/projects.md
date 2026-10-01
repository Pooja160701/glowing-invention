# MediConnect Linear Projects

## INIT-01 / Project P01 — Patient Discovery

**Goal:** Enable patients to find relevant providers and inspect available care options.

Scope:
- Account access.
- Provider search.
- Filters.
- Provider details.
- Availability display.

Success:
- Discovery funnel instrumented.
- Availability can be reached from search.
- Accessibility checks pass.

---

## INIT-01 / Project P02 — Availability & Booking

**Goal:** Establish reliable appointment booking.

Scope:
- Slot validation.
- Atomic reservation.
- Booking.
- Confirmation.
- Idempotency.
- Concurrency testing.

Success:
- No false confirmations in tested concurrency scenarios.
- Booking reliability target met.

---

## INIT-02 / Project P03 — Appointment Management

**Goal:** Enable patient self-service changes.

Scope:
- Appointment details.
- History.
- Cancellation.
- Rescheduling.
- Failed-reschedule recovery.

Success:
- Eligible changes complete without staff intervention.
- Original appointment preserved when replacement fails.

---

## INIT-02 / Project P04 — Patient Communications

**Goal:** Deliver useful appointment communications.

Scope:
- Confirmations.
- Reminders.
- Communication preferences.
- Delivery tracking.

Success:
- Delivery status observable.
- Preference rules honored.

---

## INIT-03 / Project P05 — Staff Scheduling

**Goal:** Give clinic teams control over provider schedules and appointments.

Scope:
- Availability management.
- Appointment schedule.
- Administrative updates.
- Organization scoping.

Success:
- Staff can manage valid schedule changes.
- Cross-organization access is prevented.

---

## INIT-03 / Project P06 — Exception Operations

**Goal:** Make scheduling and notification failures visible and recoverable.

Scope:
- Exception creation.
- Queue.
- Assignment.
- Resolution.
- Notification failures.

Success:
- Exceptions are created consistently.
- Resolution time is measurable.

---

## INIT-04 / Project P07 — Security & Governance

**Goal:** Protect administrative healthcare data and enforce controlled access.

Scope:
- RBAC.
- Organization isolation.
- Audit logging.
- Privacy-safe analytics.
- Security monitoring.

Success:
- Authorization tests pass.
- Required sensitive actions are audited.
- Analytics schema passes privacy review.

---

## INIT-04 / Project P08 — Analytics & Observability

**Goal:** Make product and service behavior measurable.

Scope:
- Event taxonomy.
- Booking funnel.
- Operational metrics.
- Reliability telemetry.
- Dashboards.

Success:
- Canonical events cover core journey.
- Product and operational KPIs are reproducible.

---

## INIT-05 / Project P09 — Advanced Scheduling

**Goal:** Support validated complex scheduling requirements.

Scope:
- Configurable constraints.
- Resource/provider rules.
- Buffers.
- Complex appointment structures.

Status: Candidate / post-MVP.

---

## INIT-05 / Project P10 — External Integrations

**Goal:** Reduce duplicate schedule maintenance.

Scope:
- Integration contracts.
- Synchronization.
- Conflict handling.
- Monitoring.

Status: Candidate / post-MVP.
