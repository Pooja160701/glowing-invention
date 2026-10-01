# MediConnect Tracking Plan

## Product questions

### Q1 — Can patients find viable appointment options?
Events:
- provider_search_started
- provider_results_viewed
- availability_viewed
- slot_selected

### Q2 — Can patients successfully book?
Events:
- booking_started
- booking_submitted
- booking_succeeded
- booking_failed

### Q3 — Can patients manage appointments without staff intervention?
Events:
- appointment_viewed
- cancellation_started
- appointment_cancelled
- reschedule_started
- appointment_rescheduled

### Q4 — Are communications reliable?
Events:
- reminder_scheduled
- reminder_sent
- reminder_delivered
- reminder_failed

### Q5 — Can staff recover operational exceptions?
Events:
- exception_created
- exception_resolved

### Q6 — Is access controlled correctly?
Events:
- authorization_denied
- audit_event_created

## Analytics tool mapping

### Mixpanel
Use for:
- Funnels.
- Retention-style behavioral analysis where appropriate.
- Cohorts.
- User journeys.

### Amplitude
Use for:
- Behavioral funnels.
- Path analysis.
- Cohort analysis.
- Product experimentation analysis.

### PostHog
Use for:
- Product analytics.
- Feature flags where approved.
- Session/product diagnostics where privacy review permits.

### GA4
Use for:
- High-level web acquisition and product interaction measurement where appropriate.
- Avoid sending sensitive healthcare content.

The tools are alternative/compatible implementation targets; the canonical event contract remains the source of truth.
