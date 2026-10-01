# SupplyPulse Figma-Ready Specification

> No external Figma workspace is created by this repository. This specification is intended to be directly translated into a Figma file.

## Pages
1. Cover
2. Foundations
3. Components
4. App Shell
5. Home
6. Exceptions
7. Inventory
8. Supply
9. Replenishment
10. Analytics
11. Administration
12. Prototype Flows

## Frames
Desktop baseline: 1440 × 1024
Responsive reference: 1024 × 768

## Prototype flows
### Flow A
Home → Exception Queue → Exception Detail → Replenishment Recommendation → Approve → Confirmation

### Flow B
Home → Late PO → Supplier Context → Affected Inventory → Action → Resolution

### Flow C
Home → Data Quality → Source Detail → Lineage → Resolution

### Flow D
Home → KPI → Exception Cluster → Exception Detail

## Component variants
- severity: critical/high/medium/low/info
- status: new/in-progress/blocked/resolved
- freshness: fresh/stale/unavailable/conflicting
- recommendation: pending/approved/edited/rejected/blocked

## Prototype interaction rules
- Clicking an exception opens detail.
- Clicking a KPI drills into the related population.
- Recommendation approval opens confirmation.
- Editing a recommendation shows original and edited quantity.
- Rejecting requires a reason.
- Stale data displays warning before high-impact action.
- Unauthorized controls are hidden or disabled according to the permission model.

## Design QA checklist
- desktop and responsive layouts reviewed
- keyboard navigation
- empty/loading/error states
- long SKU names
- large numbers
- missing data
- permission states
- stale-data warnings
- approval confirmation
- audit visibility
