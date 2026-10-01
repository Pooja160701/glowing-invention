# Workflow Comparison

## Workflow A — Find and book care

| Step | Zocdoc | Practo | Doctolib | Epic/MyChart | MediConnect design hypothesis |
|---|---|---|---|---|---|
| Search provider/care | Provider + need/location filters | Doctor/clinic discovery | Practitioner/care access | Health-system entry points | Provider, specialty, location |
| View availability | Real-time availability | Available slots | Availability-aware access | Integrated scheduling | Explicit slot freshness |
| Select slot | Yes | Yes | Yes | Yes | Yes |
| Confirm | Online booking | Confirmed booking workflow | Booking workflow | Patient self-scheduling | Confirmation + audit event |
| Remind | Yes | Yes | Yes | Yes | Preference-aware reminders |
| Change appointment | Supported workflows | Supported workflows | Supported workflows | Supported | Self-service change + exception queue |

## Workflow B — Staff operations

MediConnect should treat staff workflows as a first-class product surface:

1. Configure provider availability.
2. View daily/weekly appointment queue.
3. Detect scheduling conflicts.
4. Resolve cancellation/reschedule exceptions.
5. Track notification delivery status.
6. Review operational metrics.
7. Audit sensitive administrative actions.

## Workflow C — Exception handling

### Patient-side exception
**Scenario:** A patient needs to reschedule.

Expected flow:
1. Open appointment.
2. Select reschedule.
3. Show valid replacement slots.
4. Confirm replacement.
5. Release original slot.
6. Notify patient and staff.
7. Write audit event.

### Provider-side exception
**Scenario:** Provider becomes unavailable.

Expected flow:
1. Staff marks unavailable period.
2. System identifies impacted appointments.
3. Staff sees exception queue.
4. Patients receive approved communication.
5. Replacement slots are offered where available.
6. Resolution state is tracked.

## Product insight

The differentiating workflow opportunity is not just initial booking. It is **making exceptions visible and recoverable without forcing every change through a phone call or manual back-office process**.

This should be validated with additional research before becoming a final positioning claim.
