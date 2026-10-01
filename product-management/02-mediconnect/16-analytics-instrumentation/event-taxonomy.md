# Canonical Event Taxonomy

## Identity and account

| Event | Trigger | Primary owner |
|---|---|---|
| account_created | Patient or staff account successfully created | Identity |
| account_login | Successful authentication | Identity |
| account_logout | User explicitly logs out | Identity |
| communication_preferences_updated | Supported preference changed | Patient Experience |

## Discovery

| Event | Trigger | Primary owner |
|---|---|---|
| provider_search_started | User submits provider/clinic search | Discovery |
| provider_results_viewed | Search results rendered | Discovery |
| provider_selected | User selects provider/clinic | Discovery |
| availability_viewed | Availability successfully displayed | Scheduling |
| slot_selected | User selects an available slot | Scheduling |

## Booking

| Event | Trigger | Primary owner |
|---|---|---|
| booking_started | Booking flow begins | Booking |
| booking_submitted | Booking request submitted | Booking |
| booking_succeeded | Appointment transaction succeeds | Booking |
| booking_failed | Booking transaction fails | Booking |
| booking_confirmation_viewed | Confirmation state displayed | Booking |

## Appointment management

| Event | Trigger | Primary owner |
|---|---|---|
| appointment_viewed | Appointment details viewed | Management |
| cancellation_started | Cancellation flow starts | Management |
| appointment_cancelled | Cancellation succeeds | Management |
| reschedule_started | Reschedule flow starts | Management |
| appointment_rescheduled | Reschedule succeeds | Management |
| appointment_history_viewed | History is viewed | Management |

## Communications

| Event | Trigger | Primary owner |
|---|---|---|
| reminder_scheduled | Reminder scheduled | Communications |
| reminder_sent | Reminder accepted by delivery provider | Communications |
| reminder_delivered | Delivery confirmation received | Communications |
| reminder_failed | Delivery fails | Communications |
| communication_preferences_viewed | Preferences opened | Communications |

## Staff operations

| Event | Trigger | Primary owner |
|---|---|---|
| schedule_viewed | Staff schedule opened | Operations |
| availability_updated | Staff changes availability | Operations |
| appointment_updated_by_staff | Staff updates appointment | Operations |
| exception_created | Operational exception created | Operations |
| exception_resolved | Exception resolved | Operations |

## Security and governance

| Event | Trigger | Primary owner |
|---|---|---|
| authorization_denied | Authorized resource check fails | Security |
| audit_event_created | Auditable administrative action recorded | Security |
| privacy_request_started | Supported privacy request initiated | Privacy |
| privacy_request_completed | Privacy request completed | Privacy |

## Reliability

| Event | Trigger | Primary owner |
|---|---|---|
| api_error | User-facing API error | Platform |
| integration_failure | External integration fails | Platform |
| notification_provider_error | Notification provider error | Communications |
