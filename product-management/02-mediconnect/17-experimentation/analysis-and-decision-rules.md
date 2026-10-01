# Experiment Analysis and Decision Rules

## Required analysis

For every experiment report:
1. Eligible population.
2. Exposed population.
3. Exposure quality.
4. Primary metric by variant.
5. Absolute difference.
6. Relative difference where useful.
7. Statistical uncertainty.
8. Guardrail results.
9. Segment observations.
10. Data-quality issues.

## Decision framework

### Continue treatment
Use when:
- Primary metric meets the predefined practical threshold.
- Guardrails remain within acceptable limits.
- Instrumentation quality is sufficient.
- No material privacy/security issue is introduced.

### Stop treatment
Use when:
- Primary metric materially deteriorates.
- A critical guardrail fails.
- Security/privacy risk is identified.
- Data quality invalidates safe rollout.

### Iterate and retest
Use when:
- Direction is promising but effect is below the practical threshold.
- A meaningful usability issue is identified.
- Segment behavior suggests a revised treatment.

### Inconclusive
Use when:
- Evidence is insufficient.
- Exposure was compromised.
- Instrumentation is incomplete.
- Results are too uncertain for the predefined decision rule.

## Important statistical note

Do not use a fixed p-value as the sole product decision rule. Practical effect size, uncertainty, guardrails, experiment quality, and product risk should all be considered.

## Synthetic-data warning

The results in synthetic-results.csv are illustrative only. They are not claims about MediConnect users or real-world performance.
