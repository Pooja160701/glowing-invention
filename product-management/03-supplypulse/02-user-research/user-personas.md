# SupplyPulse User Personas

> Personas are **synthetic archetypes** derived from the synthetic research dataset. They are not real customer profiles.

## Persona 1 — Maya, Inventory Planner
**Primary goal:** keep inventory available without creating unnecessary excess.

**Typical responsibilities**
- monitor SKU/location inventory,
- review demand and forecast inputs,
- identify stockout/excess risk,
- prepare replenishment recommendations,
- coordinate with procurement and operations.

**Pain points**
- conflicting inventory numbers,
- alert overload,
- spreadsheet reconciliation,
- unclear recommendation rationale,
- limited visibility into lead-time variability.

**Needs**
- trusted inventory state,
- prioritized exceptions,
- demand + supply context,
- explainable reorder recommendations,
- clear data freshness.

**Success looks like**
- fewer manual reconciliation steps,
- earlier identification of service risk,
- faster replenishment decisions,
- confidence that recommendations can be audited.

## Persona 2 — Arjun, Procurement Manager
**Primary goal:** keep suppliers and purchase orders aligned with operational demand.

**Typical responsibilities**
- monitor open POs,
- manage supplier performance,
- investigate late receipts,
- negotiate/coordinate supplier actions,
- support purchasing decisions.

**Pain points**
- supplier information scattered across systems,
- late-risk discovered too late,
- averages hide lead-time volatility,
- reactive expediting.

**Needs**
- supplier risk visibility,
- current PO status,
- expected receipt changes,
- lead-time trend/variability,
- shared context for approvals.

**Success looks like**
- earlier supplier-risk detection,
- fewer avoidable escalations,
- faster exception ownership.

## Persona 3 — Ravi, Warehouse / Operations Manager
**Primary goal:** keep physical inventory and operational execution aligned with system expectations.

**Typical responsibilities**
- inbound/outbound operations,
- inventory accuracy,
- discrepancy resolution,
- receiving,
- shift-level exception management.

**Pain points**
- system vs physical discrepancies,
- stale expected receipts,
- too many unprioritized issues,
- unclear ownership of aging stock.

**Needs**
- current inbound visibility,
- inventory discrepancy queue,
- role-specific priorities,
- clear owners and next actions.

**Success looks like**
- fewer surprises at receiving,
- faster discrepancy resolution,
- less manual shift reporting.

## Persona 4 — Elena, Supply Chain Leader
**Primary goal:** balance service, inventory, working capital, and operational risk.

**Typical responsibilities**
- set supply-chain priorities,
- review service and inventory performance,
- manage cross-functional trade-offs,
- communicate risk to leadership.

**Pain points**
- fragmented reporting,
- inconsistent metrics,
- delayed root-cause visibility,
- separate views of service and inventory trade-offs.

**Needs**
- consistent KPI definitions,
- risk narrative,
- network-level trends,
- drill-down to actionable exceptions.

**Success looks like**
- faster management decisions,
- fewer surprises,
- clear linkage between exceptions and business impact.

## Cross-persona design implication
The platform should provide a **shared data foundation** with role-specific workflows rather than four disconnected dashboards.
