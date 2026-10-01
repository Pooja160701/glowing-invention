# Event Properties

## Common properties

Every applicable event should include:

| Property | Type | Example |
|---|---|---|
| event_name | string | booking_succeeded |
| event_version | string | 1.0 |
| event_id | string | evt_123 |
| occurred_at | ISO timestamp | 2026-10-01T10:15:00Z |
| actor_type | enum | patient |
| session_id | string | sess_123 |
| organization_id | pseudonymous ID | org_123 |
| platform | enum | web |
| app_version | string | 1.0.0 |
| environment | enum | production |
| correlation_id | string | corr_123 |

## Discovery properties

- search_context
- provider_type
- location_region
- result_count
- availability_count

Do not collect precise location unless explicitly required and approved.

## Booking properties

- appointment_id (pseudonymous)
- provider_id (pseudonymous)
- slot_id (pseudonymous)
- booking_channel
- booking_attempt_number
- booking_failure_reason_category
- booking_duration_ms

## Appointment properties

- appointment_id (pseudonymous)
- appointment_status
- change_reason_category
- self_service_flag

## Communication properties

- channel
- template_category
- delivery_status
- failure_reason_category
- retry_count

Do not include message body, patient clinical content, or free-text communication content.

## Operational properties

- exception_type
- severity
- queue_age_seconds
- resolution_time_seconds
- staff_role

## Security properties

- authorization_scope
- resource_type
- action
- result

Do not include credentials, tokens, secrets, or sensitive payloads.

## Property governance

Every new property should document:
- Purpose.
- Data type.
- Allowed values.
- Owner.
- Privacy classification.
- Retention requirement.
