# FinFlow — Data Governance

## Ownership
- Product: metric definitions and business meaning
- Data: pipelines, models, quality controls
- Engineering: source-system correctness
- Security: access controls and privacy requirements
- Analytics: reporting and interpretation

## Access Levels
1. Public portfolio artifacts
2. Internal product analytics
3. Restricted operational data
4. Highly sensitive financial data

## Retention
Define retention by data class and applicable legal/product requirements. Do not retain data indefinitely by default.

## Change Management
Changes to event names, metric formulas, or core schemas require versioned documentation and downstream impact review.

## Experiment Integrity
Assignment, exposure, and outcome data must be separated enough to detect implementation errors and support reproducible analysis.
