# BI Data Model

## Core fact tables

### fact_booking
- booking_id
- appointment_id
- user_id_hash
- organization_id_hash
- provider_id_hash
- booking_started_at
- booking_submitted_at
- booking_completed_at
- status
- failure_reason_category
- booking_channel

### fact_appointment
- appointment_id
- organization_id_hash
- provider_id_hash
- scheduled_start
- status
- cancellation_reason_category
- reschedule_flag
- self_service_flag

### fact_notification
- notification_id
- appointment_id
- channel
- template_category
- scheduled_at
- sent_at
- delivered_at
- failed_at
- status
- failure_reason_category

### fact_exception
- exception_id
- organization_id_hash
- exception_type
- severity
- created_at
- assigned_at
- resolved_at
- status

### fact_product_event
- event_id
- event_name
- event_version
- occurred_at
- actor_type
- organization_id_hash
- session_id
- platform

## Dimensions

### dim_date
- date
- week
- month
- quarter

### dim_organization
- organization_id_hash
- organization_segment
- region_category

### dim_provider
- provider_id_hash
- provider_category
- organization_id_hash

### dim_platform
- platform
- app_version

## Modeling principles

- Use pseudonymous IDs.
- Keep sensitive clinical information out of BI.
- Preserve event versioning.
- Use source-of-truth transactional tables for operational reconciliation.
- Define cohort windows explicitly.
