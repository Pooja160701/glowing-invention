# Functional Requirements

## FR-001 — Authentication

**P0**

Patients and staff must authenticate through supported secure mechanisms.

Acceptance-level behavior:
- Invalid credentials are rejected.
- Sessions expire according to security policy.
- Staff access requires appropriate role authorization.
- Account recovery must not reveal sensitive account information.

## FR-002 — Provider discovery

**P0**

Patients can search for providers or clinics using supported filters.

Minimum filters:
- Specialty/service.
- Location.
- Availability.
- Provider/clinic name.

## FR-003 — Availability

**P0**

The system displays bookable appointment slots based on current scheduling state.

Requirements:
- Slot status is server-authoritative.
- Expired or reserved slots cannot be booked.
- Time zones are explicit.
- Concurrent booking attempts are handled safely.

## FR-004 — Booking

**P0**

A patient can select a valid slot and create an appointment.

Flow:
1. Validate patient/session.
2. Revalidate slot.
3. Reserve slot.
4. Create appointment.
5. Commit booking.
6. Emit booking event.
7. Trigger confirmation.
8. Show final state.

## FR-005 — Confirmation

**P0**

The patient receives a confirmation containing:
- Provider/clinic.
- Appointment date/time.
- Location or supported access method.
- Change/cancellation instructions.
- Appointment identifier.

## FR-006 — Reminders

**P0**

The system schedules reminders according to configured policy and patient preferences.

Requirements:
- Reminder schedule is deterministic.
- Delivery status is recorded.
- Failed delivery is observable.
- Notification payload follows data-minimization rules.

## FR-007 — Appointment history

**P0**

Patients can view their appointments and status history permitted by policy.

## FR-008 — Cancellation

**P0**

Patients can cancel eligible appointments.

Requirements:
- Policy is displayed.
- Confirmation is required.
- Appointment state changes atomically.
- Slot release behavior is defined.
- Confirmation is generated.

## FR-009 — Rescheduling

**P0**

Patients can replace an eligible appointment with another valid slot.

Critical rule:
**Do not cancel the original appointment until replacement booking succeeds.**

## FR-010 — Communication preferences

**P0**

Patients can manage supported reminder channels and timing preferences.

The system must honor configured opt-outs where legally and operationally applicable.

## FR-011 — Staff availability management

**P0**

Authorized staff can:
- Create availability windows.
- Modify availability.
- Block time.
- View schedule.
- Review conflicts.

## FR-012 — Staff appointment management

**P0**

Authorized staff can search, filter, view, and manage appointment records within their permitted scope.

## FR-013 — Exception queue

**P0**

The system creates operational exceptions for:
- Provider unavailability.
- Booking failures.
- Notification failures requiring intervention.
- Scheduling conflicts.
- Other configured administrative failures.

Each exception has:
- Type.
- Severity.
- Created time.
- Related appointment.
- Owner.
- Status.
- Resolution timestamp.

## FR-014 — Notification status

**P0**

Authorized staff can inspect whether supported notifications are queued, sent, delivered, failed, or suppressed.

## FR-015 — RBAC

**P0**

Minimum roles:
- Patient.
- Clinic Staff.
- Provider.
- Organization Admin.
- Platform Admin.

Authorization must be enforced server-side.

## FR-016 — Audit logging

**P0**

Record security-sensitive and administrative actions with:
- Actor.
- Action.
- Resource type/identifier.
- Timestamp.
- Result.
- Correlation/request identifier where appropriate.

Do not store unnecessary sensitive payloads in audit records.

## FR-017 — Analytics

**P0**

Core user and operational events must be captured using the canonical event taxonomy.

## FR-018 — Secure messaging

**P1**

Authorized patients and provider/staff users can exchange supported administrative messages through a controlled channel.

## FR-019 — Advanced scheduling

**P1**

Support complex scheduling rules such as provider/resource constraints, configurable buffers, and multi-step appointment requirements.

## FR-020 — External integrations

**P1**

Synchronize supported scheduling data with external systems while preserving a defined source-of-truth model and conflict-resolution policy.
