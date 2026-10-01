# FinFlow — Productboard Prioritization

> **Status:** Portfolio prioritization model. Scores are illustrative, not measured customer or business values.

## Framework

Each feature receives a 1–5 score for:

- **Reach:** How broadly the feature could affect the target user base
- **Impact:** Potential effect on a key user outcome
- **Confidence:** Strength of available evidence
- **Strategic Fit:** Alignment with the FinFlow product strategy
- **Effort:** Relative implementation complexity

### Formula

**Opportunity Score = (Reach + Impact + Confidence + Strategic Fit) − Effort**

This is a prioritization aid, not an objective truth.

## Illustrative Scoring

| Feature | Reach | Impact | Confidence | Strategic Fit | Effort | Score |
|---|---:|---:|---:|---:|---:|---:|
| Transaction Import | 5 | 5 | 5 | 5 | 3 | 17 |
| Categorization | 5 | 5 | 4 | 5 | 4 | 15 |
| Financial Dashboard | 5 | 5 | 5 | 5 | 4 | 16 |
| Budget Monitoring | 4 | 5 | 4 | 5 | 3 | 15 |
| Savings Goals | 3 | 4 | 4 | 4 | 3 | 12 |
| Explainable Insights | 4 | 5 | 3 | 5 | 5 | 12 |
| Recurring Expenses | 3 | 3 | 3 | 4 | 4 | 9 |
| Notification Preferences | 3 | 3 | 4 | 3 | 2 | 11 |
| Advanced Forecasting | 2 | 4 | 2 | 3 | 5 | 6 |
| Household Finance | 2 | 3 | 2 | 2 | 5 | 4 |

## Interpretation

The scores are designed to demonstrate a transparent decision framework. They should be replaced with validated product analytics, customer evidence, and engineering estimates once available.

## Prioritization Guardrails

A high score does not automatically override:
- Security requirements
- Privacy requirements
- Regulatory review
- Critical reliability work
- Known technical dependencies
