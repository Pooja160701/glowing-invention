# MediConnect Story Map

## Backbone

| Discover | Schedule | Book | Manage | Communicate | Operate | Measure |
|---|---|---|---|---|---|---|
| Search | View availability | Select slot | View appointment | Confirmation | Staff calendar | Funnel |
| Filter | Time zone | Confirm booking | Cancel | Reminders | Availability | Operations |
| Provider details | Slot validation | Duplicate protection | Reschedule | Delivery status | Exceptions | Reliability |
| Location/service | Scheduling rules | Booking state | History | Preferences | Audit | Privacy |

## Release slicing

### Release 1 — Core booking

Goal: prove that a patient can independently discover and book an appointment.

Include:
- US-001 to US-012.
- Basic staff availability.
- Basic confirmation.
- Core analytics.

### Release 2 — Self-service management

Goal: reduce avoidable staff involvement after booking.

Include:
- US-013 to US-020.
- Cancellation.
- Rescheduling.
- Reminder preferences.
- Notification visibility.

### Release 3 — Operational control

Goal: make clinic-side exceptions manageable.

Include:
- US-021 to US-033.
- Exception queue.
- RBAC.
- Audit logging.
- Privacy controls.

### Release 4 — Optimization

Goal: expand workflow depth after MVP validation.

Include:
- US-034 to US-039.
- Advanced analytics.
- Secure messaging.
- Advanced scheduling.
- External integrations.

## MVP cut

The MVP should establish the complete core loop:

**Discover → Availability → Book → Confirm → Remind → Change/Cancel → Staff exception resolution → Measure**
