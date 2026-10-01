# FinFlow — Roadmap Dependencies & Risks

## Dependencies

| Dependency | Affects | Risk |
|---|---|---|
| Transaction schema | Import, categorization, dashboard | High |
| Categorization logic | Dashboard, budgets, insights | High |
| Identity/access | All authenticated workflows | High |
| Analytics schema | Product measurement | Medium |
| Notification service | Alerts | Medium |
| Privacy/data lifecycle | Data workflows | High |
| Design system | UX consistency | Medium |

## Key Risks

### R1 — Poor Categorization Quality
**Impact:** Incorrect dashboards and insights.

**Mitigation:** User correction, confidence handling, QA datasets.

### R2 — Low Activation
**Impact:** Users may not reach the value moment.

**Mitigation:** Reduce onboarding friction and instrument the activation funnel.

### R3 — Insight Fatigue
**Impact:** Users may dismiss or disable insights.

**Mitigation:** Relevance thresholds, frequency controls, feedback events.

### R4 — Trust Concerns
**Impact:** Users may avoid importing financial information.

**Mitigation:** Clear consent, data controls, transparent explanations.

### R5 — Scope Expansion
**Impact:** MVP delivery becomes diluted.

**Mitigation:** Enforce explicit non-goals and outcome-based prioritization.

## Decision Log

Roadmap decisions should record:
- Problem
- Evidence
- Decision
- Alternatives considered
- Expected outcome
- Owner
- Review date
