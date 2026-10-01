# Experiment Framework

## 1. Question

What user or operational problem are we trying to understand?

## 2. Hypothesis

Format:

**If** [change], **then** [metric] will change because [reason].

## 3. Population

Define:
- Eligible users.
- Exclusions.
- Platform.
- Organization scope.
- Experiment duration.

## 4. Variants

- Control: existing experience.
- Treatment: proposed experience.

Additional variants require a clear research reason.

## 5. Primary metric

Choose one primary decision metric whenever possible.

## 6. Secondary metrics

Use supporting metrics to explain behavior.

## 7. Guardrails

Protect:
- Booking reliability.
- Slot integrity.
- Notification delivery.
- Authorization/security.
- Privacy.
- Support burden.

## 8. Decision rule

Predefine the rule before looking at results.

## 9. Analysis

Report:
- Sample size.
- Exposure.
- Conversion.
- Absolute change.
- Relative change.
- Uncertainty interval or statistical test where appropriate.
- Guardrail movement.
- Segment observations.

## 10. Decision

Possible outcomes:
- Continue treatment.
- Stop treatment.
- Iterate and retest.
- Inconclusive; collect more evidence.

Do not declare success solely because a secondary metric improves.
