# SupplyPulse Wireframe Specifications

## UX-001 — Home / Priority Dashboard
Header: organization, location, date/time context, global search, profile.
Summary row: high-impact exceptions, at-risk inventory value, pending approvals, data-quality warnings.
Main area: priority exception queue plus risk summary/trend.
Bottom area: inventory risk trend, supplier risk, recent decisions.
Primary CTA: Open highest-priority exception.

## UX-002 — Exception Queue
Include page title, filters, saved-view control, sort control, and table/list.
Required columns: severity, exception type, SKU/location, business impact, owner, due date, status, data freshness.
Row action: Open exception.
Empty state: explain why there are no matches and offer reset filters.

## UX-003 — Exception Detail
Header: exception type, severity, status, owner, due date.
Impact panel: inventory exposure, service-risk indicator, affected location, affected SKU, supplier where relevant.
Context tabs: Inventory, Demand, Supply, Supplier, Data quality, History.
Action panel: assign, change status, inspect recommendation, add resolution note.
Trust panel: source, last refresh, quality state.

## UX-004 — Inventory Overview
Summary: total inventory value, at-risk value, excess value, stockout-risk value.
Main table filters: SKU, location, category, status, aging.
Secondary panel: inventory trend and risk distribution.

## UX-005 — SKU Inventory Detail
Header: SKU, description, location, status.
Position card: on-hand, reserved, available, in-transit.
Timeline: demand history, forecast, expected receipts, projected availability.
Risk: stockout, excess, supplier risk.
Actions: view exceptions, view recommendation.

## UX-006 — Purchase Order Detail
Header: PO, supplier, status, expected receipt.
Details: ordered quantity, received quantity, remaining quantity, original vs current expected receipt.
Risk: late status, lead-time deviation, affected inventory.
Actions: open supplier, open affected exceptions, record follow-up.

## UX-008 — Replenishment Recommendation
Recommendation header: suggested quantity, urgency, recommendation timestamp.
Explainability: why now, projected depletion, demand change, lead-time change; why this quantity, reorder point, safety stock, expected supply.
Decision controls: Approve, Edit quantity, Reject.
Confirmation: decision, actor, timestamp, downstream state.

## UX-010 — Data Quality Center
Summary: critical issues, stale sources, duplicate records, schema errors.
Main table: source, issue type, affected object, age, owner, status.
Detail: source lineage and validation rule.

## UX-011 — Analytics Overview
KPI cards: inventory health, service-risk exposure, exception resolution time, supplier risk, data-quality rate.
Every KPI should support drill-down to the underlying population where feasible.
