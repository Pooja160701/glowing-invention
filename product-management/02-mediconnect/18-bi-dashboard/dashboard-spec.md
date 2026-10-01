# Dashboard Specification

## 1. Executive Product Dashboard

### KPI cards
- CCJR
- Booking success rate
- Search-to-book conversion
- Self-service change completion
- Notification delivery rate
- Exception resolution time
- Core scheduling availability

### Trend charts
- CCJR by week.
- Booking success by week.
- Search-to-book conversion by week.
- Notification delivery by week.

### Segment views
- Patient platform.
- Provider/clinic organization.
- Appointment type category where non-sensitive.
- New vs returning users.

Avoid displaying small cohorts where re-identification risk could increase.

---

## 2. Patient Booking Funnel

### Funnel
Search started
→ Results viewed
→ Availability viewed
→ Slot selected
→ Booking started
→ Booking submitted
→ Booking succeeded

### Breakdown
- Platform.
- Organization.
- Date/week.
- Search context.
- Provider category.

### Diagnostics
- Failure reasons.
- Latency.
- Availability coverage.
- Slot mismatch rate.

---

## 3. Scheduling & Operations

### KPIs
- Available slots.
- Booked slots.
- Cancellation rate.
- Reschedule completion.
- Exception volume.
- Median exception resolution time.
- Critical unresolved exceptions.

### Visuals
- Exception volume trend.
- Exception aging distribution.
- Resolution time by exception category.
- Staff workload trend.

---

## 4. Communications Reliability

### KPIs
- Reminder scheduled.
- Reminder sent.
- Reminder delivered.
- Reminder failed.
- Delivery rate.
- Failure rate.
- Retry rate.

### Visuals
- Delivery funnel.
- Failure reason distribution.
- Delivery latency.
- Trend by channel.

---

## 5. Security & Governance

### KPIs
- Authorization denials.
- Audit event coverage.
- Privacy request completion.
- Analytics schema violations.
- Security incidents.

Sensitive operational details should be access-controlled.
