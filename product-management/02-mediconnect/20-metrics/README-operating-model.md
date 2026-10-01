# Metrics Operating Model

## Source of truth

Metric definitions live in:
- analytics instrumentation
- metric definitions
- KPI scorecard

BI dashboards should reference these definitions rather than create competing formulas.

## Change control

A metric definition change requires:
1. Change description.
2. Reason.
3. Owner approval.
4. Effective date.
5. Historical reporting treatment.
6. Linked product decision if material.

## Synthetic data

synthetic-weekly-scorecard.csv contains illustrative portfolio data only. It is not production telemetry.

## Success

The metrics system is successful when teams can answer:
- Are patients completing the administrative journey?
- Where does the journey fail?
- Are failures safe and recoverable?
- Is operational burden improving?
- Are experiments producing trustworthy evidence?
- What product decision should happen next?
