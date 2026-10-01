# MediConnect User Stories

## E01 — Patient Account & Access

### US-001 — Create patient account
**As a patient, I want to create an account so that I can manage appointments securely.**

**Priority:** P0  
**Requirement:** R-001

### US-002 — Sign in securely
**As a patient, I want to sign in securely so that only I can access my appointment information.**

**Priority:** P0  
**Requirement:** R-001

### US-003 — Manage communication preferences
**As a patient, I want to control supported appointment communication preferences so that reminders fit my needs.**

**Priority:** P0  
**Requirement:** R-008

---

## E02 — Provider Discovery

### US-004 — Search providers
**As a patient, I want to search for providers and clinics so that I can find an appropriate appointment option.**

**Priority:** P0  
**Requirement:** R-001

### US-005 — Filter search results
**As a patient, I want to filter providers by supported criteria so that I can narrow my options.**

**Priority:** P0  
**Requirement:** R-001

### US-006 — View provider details
**As a patient, I want to view provider and clinic details so that I can decide whether an available appointment is relevant.**

**Priority:** P0  
**Requirement:** R-001

---

## E03 — Availability & Scheduling

### US-007 — View available slots
**As a patient, I want to see currently bookable appointment slots so that I can choose a suitable time.**

**Priority:** P0  
**Requirement:** R-002

### US-008 — See appointment time zone
**As a patient, I want appointment times to clearly identify the applicable time zone so that I do not misunderstand my appointment time.**

**Priority:** P0  
**Requirement:** R-002

### US-009 — Prevent stale slot booking
**As a patient, I want the system to revalidate a slot before booking so that I do not receive a false confirmation.**

**Priority:** P0  
**Requirement:** R-002

---

## E04 — Appointment Booking

### US-010 — Book an appointment
**As a patient, I want to book an available appointment so that I can secure care access.**

**Priority:** P0  
**Requirement:** R-003

### US-011 — Confirm appointment
**As a patient, I want to receive clear booking confirmation so that I know my appointment was successfully created.**

**Priority:** P0  
**Requirement:** R-004

### US-012 — Prevent duplicate booking
**As a patient, I want repeated booking requests to be handled safely so that I do not accidentally create duplicate appointments.**

**Priority:** P0  
**Requirement:** R-004

---

## E05 — Appointment Management

### US-013 — View appointment
**As a patient, I want to view my upcoming appointment details so that I know when and where to attend.**

**Priority:** P0  
**Requirement:** R-004

### US-014 — Cancel appointment
**As a patient, I want to cancel an eligible appointment so that the slot can be released appropriately.**

**Priority:** P0  
**Requirement:** R-007

### US-015 — Reschedule appointment
**As a patient, I want to reschedule an eligible appointment so that I can change the time without starting over.**

**Priority:** P0  
**Requirement:** R-006

### US-016 — Preserve original appointment on failed reschedule
**As a patient, I want my existing appointment preserved if replacement booking fails so that I do not lose my appointment accidentally.**

**Priority:** P0  
**Requirement:** R-006

### US-017 — View appointment history
**As a patient, I want to view permitted appointment history so that I can understand my previous and upcoming administrative activity.**

**Priority:** P0  
**Requirement:** R-004

---

## E06 — Patient Communications

### US-018 — Receive booking confirmation
**As a patient, I want a booking confirmation through a supported channel so that I can verify the appointment details.**

**Priority:** P0  
**Requirement:** R-005

### US-019 — Receive reminders
**As a patient, I want reminders before my appointment so that I can prepare and attend on time.**

**Priority:** P0  
**Requirement:** R-005

### US-020 — View communication status
**As authorized staff, I want to see notification status so that I can identify delivery problems that require intervention.**

**Priority:** P0  
**Requirement:** R-005

---

## E07 — Staff Operations

### US-021 — Manage provider availability
**As authorized clinic staff, I want to create and modify provider availability so that patients see valid appointment options.**

**Priority:** P0  
**Requirement:** R-009

### US-022 — View appointment schedule
**As authorized clinic staff, I want to view appointments in a schedule/list so that I can manage daily operations.**

**Priority:** P0  
**Requirement:** R-009

### US-023 — Update provider availability
**As authorized clinic staff, I want to block or change provider availability so that schedule changes are reflected accurately.**

**Priority:** P0  
**Requirement:** R-009

### US-024 — Manage appointment administratively
**As authorized clinic staff, I want to update eligible appointment states so that exceptions can be resolved.**

**Priority:** P0  
**Requirement:** R-009

---

## E08 — Exception Management

### US-025 — Create scheduling exception
**As the system, I want to create an exception when a configured scheduling failure occurs so that staff can investigate it.**

**Priority:** P0  
**Requirement:** R-010

### US-026 — Review exception queue
**As clinic staff, I want to see unresolved appointment exceptions in one queue so that I can prioritize operational work.**

**Priority:** P0  
**Requirement:** R-010

### US-027 — Assign exception
**As clinic staff, I want to assign an exception to an authorized owner so that responsibility is clear.**

**Priority:** P0  
**Requirement:** R-010

### US-028 — Resolve exception
**As clinic staff, I want to resolve an exception with a recorded outcome so that the operational state is clear.**

**Priority:** P0  
**Requirement:** R-010

### US-029 — Track notification failure
**As clinic staff, I want notification failures to be visible so that communication problems can be addressed.**

**Priority:** P0  
**Requirement:** R-010

---

## E09 — Security, Privacy & Governance

### US-030 — Enforce role-based access
**As a system administrator, I want permissions to be enforced by role so that users only access authorized functions and data.**

**Priority:** P0  
**Requirement:** R-011

### US-031 — Restrict organization access
**As an organization administrator, I want staff access scoped to the appropriate organization so that one clinic cannot access another clinic's records.**

**Priority:** P0  
**Requirement:** R-011

### US-032 — Audit administrative actions
**As a security/operations stakeholder, I want sensitive administrative actions recorded so that activity can be investigated.**

**Priority:** P0  
**Requirement:** R-011

### US-033 — Minimize analytics data
**As a privacy stakeholder, I want product analytics to exclude unnecessary sensitive information so that measurement does not create avoidable privacy risk.**

**Priority:** P0  
**Requirement:** R-011

---

## E10 — Analytics & Product Operations

### US-034 — Track booking funnel
**As a product manager, I want the booking funnel instrumented so that I can identify where users abandon the journey.**

**Priority:** P0  
**Requirement:** R-012

### US-035 — Track operational performance
**As an operations stakeholder, I want exception and notification metrics so that I can identify process failures.**

**Priority:** P0  
**Requirement:** R-012

### US-036 — Track reliability
**As an engineering stakeholder, I want scheduling reliability metrics so that service degradation can be detected quickly.**

**Priority:** P0  
**Requirement:** R-012

### US-037 — Support secure messaging
**As an authorized patient or provider/staff user, I want to exchange permitted administrative messages securely so that routine coordination does not require unsupported channels.**

**Priority:** P1  
**Requirement:** R-015

### US-038 — Support advanced scheduling
**As authorized staff, I want configurable scheduling constraints so that more complex appointment workflows can be represented.**

**Priority:** P1  
**Requirement:** R-013

### US-039 — Synchronize external systems
**As a clinic administrator, I want supported scheduling systems synchronized so that staff do not maintain conflicting schedules in multiple places.**

**Priority:** P1  
**Requirement:** R-014
