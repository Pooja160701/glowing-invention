# Funnels and Product Metrics

## Funnel 1 — Discovery to booking

provider_search_started
→ provider_results_viewed
→ provider_selected
→ availability_viewed
→ slot_selected
→ booking_started
→ booking_submitted
→ booking_succeeded

Primary metrics:
- Search-to-book conversion.
- Availability view rate.
- Slot selection rate.
- Booking success rate.
- Booking failure rate.
- Median booking duration.

## Funnel 2 — Self-service change

appointment_viewed
→ cancellation_started
→ appointment_cancelled

or

appointment_viewed
→ reschedule_started
→ appointment_rescheduled

Primary metrics:
- Self-service completion rate.
- Self-service abandonment.
- Change success rate.
- Change failure rate.

## Funnel 3 — Communication reliability

reminder_scheduled
→ reminder_sent
→ reminder_delivered

Monitor:
- Delivery success.
- Failure rate.
- Retry rate.
- Delivery latency.

## Funnel 4 — Operational exception

exception_created
→ exception_assigned
→ exception_resolved

Monitor:
- Exception volume.
- Time to assignment.
- Time to resolution.
- Reopened exceptions.

## North Star calculation

CCJR should use a documented cohort definition.

Illustrative definition:

**CCJR = eligible booked appointments reaching the administrative completion state without an avoidable scheduling or communication failure / all eligible booked appointments in the cohort**

The exact completion state and exclusion rules must be versioned before reporting.

## Guardrail metrics

- Duplicate booking rate.
- Slot mismatch rate.
- Authorization failure rate.
- Notification failure rate.
- Core scheduling availability.
- Analytics privacy violations.
