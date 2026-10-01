# Metric Alerting

## Alert levels

### Critical
Immediate investigation required.

Examples:
- Slot mismatch above approved safety threshold.
- Duplicate booking above approved threshold.
- Core scheduling outage.
- Cross-organization authorization anomaly.
- Analytics privacy violation.

### High
Prompt owner review required.

Examples:
- Booking success degradation.
- Notification delivery degradation.
- Exception resolution time spike.

### Medium
Review during regular product operations.

Examples:
- Funnel conversion decline.
- Support volume increase.
- Non-critical usability metric movement.

## Alert design

Every alert should specify:
- Metric.
- Threshold.
- Evaluation window.
- Cohort.
- Owner.
- Notification channel.
- Runbook.
- Escalation path.

## Avoid alert fatigue

Do not alert on every small movement.

Use:
- Minimum volume thresholds.
- Sustained breach windows.
- Severity-specific routing.
- Deduplication.
- Maintenance windows.

## Example

**Condition:** Booking success <98% for two consecutive 15-minute windows with sufficient volume.

**Action:** Notify Engineering + Product Operations and open an investigation task.

The exact threshold should be approved against the actual production baseline before activation.
