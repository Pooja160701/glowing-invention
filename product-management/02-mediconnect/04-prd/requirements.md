# Requirements & Traceability

## Priority definitions

- **P0:** Required for MVP launch.
- **P1:** Important post-MVP capability.
- **P2:** Future enhancement.

| ID | User need | Requirement | Priority | Success signal |
|---|---|---|---|---|
| R-001 | Find care | Search providers/clinics | P0 | Search completion |
| R-002 | Know availability | Show valid appointment slots | P0 | Availability-to-book conversion |
| R-003 | Book independently | Create appointment | P0 | Booking completion |
| R-004 | Trust booking | Confirmation + status | P0 | Booking-state consistency |
| R-005 | Remember appointment | Configurable reminders | P0 | Delivery rate |
| R-006 | Change appointment | Self-service reschedule | P0 | Self-service change rate |
| R-007 | Cancel appointment | Self-service cancellation | P0 | Successful cancellations |
| R-008 | Manage preferences | Communication settings | P0 | Preference completion |
| R-009 | Operate schedules | Staff availability management | P0 | Schedule update success |
| R-010 | Handle exceptions | Exception queue | P0 | Resolution time |
| R-011 | Protect data | RBAC + audit | P0 | Unauthorized access rate |
| R-012 | Improve product | Event instrumentation | P0 | Event coverage |
| R-013 | Support complex workflows | Advanced scheduling | P1 | Workflow completion |
| R-014 | Connect systems | External scheduling integrations | P1 | Sync success |
| R-015 | Communicate securely | Secure messaging | P1 | Message completion |

## Traceability chain

**Research theme → user need → requirement → feature → event → metric**

Example:

Availability confidence  
→ Know whether a displayed slot is truly bookable  
→ R-002  
→ Availability service + atomic reservation  
→ `availability_viewed`, `booking_started`, `booking_completed`  
→ Booking success rate / slot mismatch rate

Self-service changes  
→ Change appointment without calling  
→ R-006/R-007  
→ Reschedule/cancel workflow  
→ `reschedule_started`, `reschedule_completed`, `appointment_cancelled`  
→ Self-service change rate / staff contact rate

Communication transparency  
→ Know whether reminders were delivered  
→ R-005  
→ Notification service + delivery state  
→ `reminder_sent`, `reminder_delivered`, `notification_failed`  
→ Delivery rate / failure rate

Privacy trust  
→ Understand and control communication/data use  
→ R-008/R-011  
→ Preferences + RBAC + audit  
→ Preference and security events  
→ Consent/preference completion / security incidents
