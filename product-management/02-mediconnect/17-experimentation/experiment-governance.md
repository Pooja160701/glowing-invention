# Experiment Governance

## Experiment review gates

### Before launch
- Product question approved.
- Hypothesis documented.
- Primary metric defined.
- Guardrails defined.
- Population and exclusions documented.
- Randomization/exposure method documented.
- Analytics events validated.
- Privacy review completed where required.
- Rollback plan documented.

### During experiment
- Monitor exposure.
- Monitor data quality.
- Monitor critical guardrails.
- Stop early only under predefined safety conditions.

### After experiment
- Lock analysis definition.
- Review results.
- Record decision.
- Update roadmap/backlog.
- Document learnings.
- Archive experiment configuration.

## Healthcare-specific boundary

Experiments should optimize administrative access, communication, and operations. They must not manipulate clinical care, diagnosis, treatment, or emergency decision-making.

## Experiment naming

Use:
EX-### — Short descriptive name

Keep IDs stable across analytics, dashboards, product documentation, and delivery tools.
