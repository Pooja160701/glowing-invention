# MediConnect Acceptance Criteria

## US-001 — Create patient account

**AC-001**
- **Given** a patient provides valid required registration information
- **When** they submit registration
- **Then** the account is created and the patient receives a successful registration state.

**AC-002**
- **Given** required registration information is invalid or incomplete
- **When** registration is submitted
- **Then** the account is not created and actionable validation feedback is shown.

**AC-003**
- **Given** the identifier is already registered
- **When** registration is submitted
- **Then** the system does not create a duplicate account.

## US-002 — Secure sign in

**AC-004**
- **Given** valid credentials
- **When** the patient signs in
- **Then** an authenticated session is established.

**AC-005**
- **Given** invalid credentials
- **When** sign-in is attempted
- **Then** access is denied without exposing unnecessary account information.

## US-003 — Communication preferences

**AC-006**
- **Given** a signed-in patient
- **When** they change supported communication preferences
- **Then** the new preferences are persisted and applied to future eligible communications.

**AC-007**
- **Given** a patient has disabled an optional supported channel
- **When** a reminder is scheduled
- **Then** the disabled channel is not selected for that reminder.

## US-004 — Search providers

**AC-008**
- **Given** supported search criteria
- **When** a patient searches
- **Then** matching providers/clinics are returned.

**AC-009**
- **Given** no matching results
- **When** the search completes
- **Then** an empty state explains that no matching options were found.

## US-005 — Filter results

**AC-010**
- **Given** a set of provider results
- **When** a patient applies supported filters
- **Then** only matching results remain.

**AC-011**
- **Given** multiple filters
- **When** they are applied together
- **Then** the result set satisfies all applicable filter conditions.

## US-006 — Provider details

**AC-012**
- **Given** a provider/clinic result
- **When** the patient opens it
- **Then** supported profile, service, location, and appointment information is displayed.

## US-007 — View available slots

**AC-013**
- **Given** valid provider availability
- **When** the patient opens availability
- **Then** currently bookable slots are displayed.

**AC-014**
- **Given** a slot has become unavailable
- **When** the patient attempts to select it
- **Then** the system prevents booking and requests a refreshed selection.

## US-008 — Show time zone

**AC-015**
- **Given** an appointment slot
- **When** it is displayed
- **Then** the applicable time zone is unambiguous.

## US-009 — Prevent stale slot booking

**AC-016**
- **Given** a slot was available during search
- **When** another transaction claims it before confirmation
- **Then** the second booking attempt fails safely and does not create a false confirmation.

## US-010 — Book appointment

**AC-017**
- **Given** a valid patient and available slot
- **When** booking is confirmed
- **Then** an appointment is created with the expected provider, patient, date, time, and status.

**AC-018**
- **Given** booking validation fails
- **When** the patient submits the booking
- **Then** no confirmed appointment is created.

## US-011 — Confirm appointment

**AC-019**
- **Given** an appointment is successfully created
- **When** confirmation processing completes
- **Then** the patient can view a confirmed appointment state.

## US-012 — Prevent duplicate booking

**AC-020**
- **Given** the same booking request is submitted more than once with the same idempotency key
- **When** requests are processed
- **Then** the operation produces one booking outcome rather than duplicate appointments.

## US-013 — View appointment

**AC-021**
- **Given** an authenticated patient with an upcoming appointment
- **When** they open appointment details
- **Then** permitted appointment information is displayed.

## US-014 — Cancel appointment

**AC-022**
- **Given** an eligible appointment
- **When** the patient confirms cancellation
- **Then** the appointment changes to the defined cancelled state.

**AC-023**
- **Given** cancellation is outside the permitted policy
- **When** the patient attempts cancellation
- **Then** the system blocks or routes the request according to configured policy.

## US-015 — Reschedule appointment

**AC-024**
- **Given** an eligible appointment and available replacement slot
- **When** the patient confirms rescheduling
- **Then** the replacement appointment is created and the original appointment is updated according to the defined transaction.

## US-016 — Preserve original on failed reschedule

**AC-025**
- **Given** the replacement slot cannot be booked
- **When** rescheduling fails
- **Then** the original appointment remains active.

## US-017 — Appointment history

**AC-026**
- **Given** an authenticated patient
- **When** they open appointment history
- **Then** only appointments authorized for that patient are returned.

## US-018 — Booking confirmation

**AC-027**
- **Given** a booking succeeds
- **When** confirmation is triggered
- **Then** the supported confirmation workflow is initiated and status is recorded.

## US-019 — Reminders

**AC-028**
- **Given** an eligible appointment and configured reminder policy
- **When** the reminder time is reached
- **Then** the system attempts delivery through an allowed channel.

**AC-029**
- **Given** reminder delivery fails
- **When** the provider returns a failure
- **Then** delivery status is recorded and an operational exception is created when configured.

## US-020 — Communication status

**AC-030**
- **Given** authorized staff
- **When** they inspect notification status
- **Then** they can see the permitted delivery state without exposing unnecessary message content.

## US-021 — Manage provider availability

**AC-031**
- **Given** authorized staff
- **When** they create valid availability
- **Then** the schedule reflects the new availability.

**AC-032**
- **Given** unauthorized staff
- **When** they attempt to modify availability
- **Then** the operation is rejected.

## US-022 — View appointment schedule

**AC-033**
- **Given** authorized clinic staff
- **When** they open the schedule
- **Then** appointments within their permitted organization/scope are displayed.

## US-023 — Update provider availability

**AC-034**
- **Given** authorized staff
- **When** they block provider availability
- **Then** affected future slots are no longer presented as bookable.

## US-024 — Manage appointment administratively

**AC-035**
- **Given** an authorized staff member and an eligible appointment
- **When** they perform an allowed administrative update
- **Then** the appointment state changes and the action is audited.

## US-025 — Create scheduling exception

**AC-036**
- **Given** a configured scheduling failure occurs
- **When** the failure is classified as actionable
- **Then** an exception record is created with type, severity, timestamp, and related resource.

## US-026 — Review exception queue

**AC-037**
- **Given** unresolved exceptions exist
- **When** authorized staff open the exception queue
- **Then** unresolved exceptions are displayed with status and ownership information.

## US-027 — Assign exception

**AC-038**
- **Given** an authorized staff member
- **When** they assign an exception to an authorized owner
- **Then** the owner is recorded and the assignment is audited.

## US-028 — Resolve exception

**AC-039**
- **Given** an assigned exception
- **When** staff complete the required resolution action
- **Then** the exception moves to resolved status with outcome and timestamp.

## US-029 — Track notification failure

**AC-040**
- **Given** a supported notification provider reports failure
- **When** the failure is received
- **Then** the notification state is updated and the configured recovery workflow is triggered.

## US-030 — Role-based access

**AC-041**
- **Given** a user with a defined role
- **When** they access a protected function
- **Then** authorization is evaluated server-side before access is granted.

**AC-042**
- **Given** a user lacks the required permission
- **When** they attempt access
- **Then** access is denied.

## US-031 — Organization isolation

**AC-043**
- **Given** staff from Organization A
- **When** they request records belonging to Organization B
- **Then** the request is denied.

## US-032 — Audit actions

**AC-044**
- **Given** a sensitive administrative action
- **When** it succeeds or fails
- **Then** an appropriate audit record is created with actor, action, resource, timestamp, and result.

## US-033 — Minimize analytics data

**AC-045**
- **Given** a product event is emitted
- **When** the event is validated against the analytics schema
- **Then** unnecessary sensitive information is rejected or removed before ingestion.

## US-034 — Booking funnel

**AC-046**
- **Given** a patient progresses through supported booking steps
- **When** each canonical event occurs
- **Then** the corresponding analytics event is emitted with approved properties.

## US-035 — Operational performance

**AC-047**
- **Given** exceptions and notifications are processed
- **When** their states change
- **Then** operational metrics can calculate volume, failure rate, and resolution time.

## US-036 — Reliability

**AC-048**
- **Given** a critical scheduling request
- **When** it succeeds or fails
- **Then** the service records latency and outcome telemetry.

## US-037 — Secure administrative messaging

**AC-049**
- **Given** two authorized participants
- **When** one sends an allowed administrative message
- **Then** the message is transmitted and stored according to security and retention policies.

## US-038 — Advanced scheduling

**AC-050**
- **Given** configured scheduling constraints
- **When** availability is generated
- **Then** incompatible slots are excluded.

## US-039 — External synchronization

**AC-051**
- **Given** an enabled external scheduling integration
- **When** supported schedule data changes
- **Then** the integration synchronizes according to the defined source-of-truth and conflict policy.

**AC-052**
- **Given** synchronization fails
- **When** the failure is detected
- **Then** the system records the failure and prevents silent divergence from being treated as successful synchronization.
