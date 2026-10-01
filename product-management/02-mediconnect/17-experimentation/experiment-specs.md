# Experiment Specifications

## EXP-001 — Booking Progress Indicator

**Question:** Does clearer progress reduce booking abandonment?

**Hypothesis:** If the booking flow communicates clear progress, then booking completion will increase because users have better visibility into remaining steps.

**Control:** Existing booking flow.

**Treatment:** Add step indicator such as Select slot → Confirm details → Complete.

**Primary metric:** Booking completion rate.

**Guardrails:**
- Booking failure rate.
- Page/API error rate.
- Booking duration.
- Duplicate booking rate.

**Decision rule:** Continue only if the primary metric improves by the predefined practical threshold without guardrail deterioration.

---

## EXP-002 — Availability Confidence Message

**Question:** Does communicating slot freshness increase confidence?

**Hypothesis:** If the interface explains when availability was last refreshed, then availability-to-book conversion will improve.

**Primary metric:** Availability-to-book conversion.

**Guardrails:**
- Slot mismatch rate.
- Availability latency.
- Support contacts.

**Risk:** A message can create false confidence if the underlying availability data is stale.

---

## EXP-003 — Self-Service Reschedule Entry Point

**Question:** Can clearer access to rescheduling reduce avoidable staff intervention?

**Hypothesis:** If rescheduling is visible from appointment details, then successful self-service rescheduling will increase.

**Primary metric:** Reschedule completion rate.

**Guardrails:**
- Reschedule failure rate.
- Staff escalation rate.
- Invalid slot selection rate.

---

## EXP-004 — Reminder Preference Presentation

**Question:** Can clearer preference controls improve communication preference completion?

**Primary metric:** Preference completion rate.

**Guardrails:**
- Notification failure.
- Incorrect preference application.
- Opt-out errors.

---

## EXP-005 — Exception Queue Prioritization

**Question:** Can structured exception prioritization improve operational recovery?

**Hypothesis:** If exceptions are sorted using severity and age, then median resolution time will decrease.

**Primary metric:** Median exception resolution time.

**Guardrails:**
- Critical exceptions unresolved beyond threshold.
- Staff workload.
- Reopened exceptions.

---

## EXP-006 — Booking Confirmation Clarity

**Question:** Does a clearer confirmation reduce repeated booking attempts?

**Primary metric:** Repeat booking attempt rate.

**Guardrails:**
- Duplicate booking rate.
- Support contacts.
- Confirmation delivery failures.
