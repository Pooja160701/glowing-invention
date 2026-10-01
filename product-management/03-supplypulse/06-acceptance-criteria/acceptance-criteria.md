# SupplyPulse Acceptance Criteria

## EP-01 — Inventory Visibility

### AC-US-001 — View inventory by SKU and location
**Given** the user has inventory-view permission  
**When** they select a SKU and location filter  
**Then** matching inventory records are displayed.

**Given** no records match  
**When** the filter is applied  
**Then** the interface shows an explicit empty state rather than an incorrect zero.

**Given** the user lacks permission  
**When** they attempt to access restricted inventory  
**Then** access is denied and the event is logged where required.

### AC-US-002 — Inventory position components
**Given** an inventory record exists  
**When** the record is opened  
**Then** on-hand, reserved, available, and in-transit quantities are shown with units and timestamp.

**Given** a component is unavailable from the source  
**Then** it is shown as unavailable/unknown rather than silently treated as zero.

### AC-US-003 — Inventory value and aging
**Given** inventory valuation and receipt/aging data are available  
**When** the user opens an inventory record  
**Then** value and aging are displayed using the configured business rules.

**Given** valuation inputs are missing  
**Then** the UI identifies the value as unavailable and explains the data-quality condition.

### AC-US-004 — Source and freshness
**Given** an inventory record has source metadata  
**When** the user views it  
**Then** source system, last refresh time, and freshness state are visible.

**Given** the freshness threshold is exceeded  
**Then** the record is marked stale and affected workflows show a degraded-data warning.

## EP-02 — Demand & Supply Intelligence

### AC-US-005 — Demand history
**Given** historical demand exists  
**When** a user selects SKU/location and date range  
**Then** demand observations are displayed in the selected period.

**Given** data is incomplete  
**Then** missing periods are distinguishable from true zero demand.

### AC-US-006 — Forecast input
**Given** a forecast input exists  
**When** the user views demand context  
**Then** forecast quantity, version, source, and timestamp are visible.

**Given** no forecast is available  
**Then** the system does not fabricate a forecast and clearly indicates the missing input.

### AC-US-007 — Open purchase orders
**Given** the user has procurement visibility  
**When** they open supply context  
**Then** open POs, quantities, status, and expected receipt dates are shown.

**Given** a PO has changed since the previous source update  
**Then** the latest state and update timestamp are displayed.

### AC-US-008 — Demand vs supply
**Given** demand and expected supply data exist  
**When** the user views projected exposure  
**Then** the system shows the relevant demand/supply comparison.

**Given** critical supply data is stale  
**Then** the comparison is marked degraded and cannot be represented as fully current.

## EP-03 — Exception Management

### AC-US-009 — Stockout risk
**Given** configured stockout rules and valid demand/supply inputs  
**When** projected availability crosses the configured risk condition  
**Then** a stockout-risk exception is created or updated.

**Given** required inputs are stale  
**Then** the exception is marked data-degraded rather than presenting the result as fully reliable.

### AC-US-010 — Excess inventory
**Given** an excess/aging threshold is configured  
**When** inventory exceeds the threshold  
**Then** an excess exception is created with affected SKU/location and value context.

### AC-US-011 — Late PO
**Given** a PO has an expected receipt date  
**When** the configured lateness condition is met  
**Then** a late-PO exception is created or updated.

**Given** the PO is cancelled  
**Then** the system updates or closes the exception according to the configured rule.

### AC-US-012 — Lead-time deviation
**Given** historical/expected lead-time data exists  
**When** observed or projected lead time exceeds the configured deviation threshold  
**Then** a lead-time exception is generated.

### AC-US-013 — Prioritize exceptions
**Given** multiple open exceptions exist  
**When** the user opens the queue  
**Then** exceptions can be ordered by configured severity and business impact.

**Given** two exceptions have equal priority  
**Then** the tie-breaking rule is deterministic and documented.

### AC-US-014 — Filter exception queue
**Given** exceptions exist  
**When** the user selects filters  
**Then** only matching exceptions are displayed.

**Given** filters produce no results  
**Then** an empty state identifies the active filters and provides a clear reset action.

### AC-US-015 — Assign owner
**Given** the user has assignment permission  
**When** they assign an owner and due date  
**Then** the exception records both values and the change is auditable.

### AC-US-016 — Track status
**Given** an exception is open  
**When** the owner changes status  
**Then** the new state and timestamp are recorded.

**Given** a user attempts to resolve without required resolution information  
**Then** the system blocks completion and identifies the missing information.

### AC-US-017 — Exception context
**Given** an exception has related inventory, demand, supply, or supplier data  
**When** the exception is opened  
**Then** relevant linked context is available from one workflow.

**Given** a related source is unavailable  
**Then** the unavailable dependency is clearly identified.

## EP-04 — Replenishment Decision Support

### AC-US-018 — Reorder recommendation
**Given** required inputs are valid  
**When** a replenishment trigger occurs  
**Then** a recommendation contains SKU/location, suggested quantity, and timestamp.

### AC-US-019 — Recommendation rationale
**Given** a recommendation exists  
**When** the user opens it  
**Then** the system explains the key drivers behind the quantity.

**Given** a required driver is unavailable  
**Then** the recommendation identifies the missing input and follows the configured safe-fallback behavior.

### AC-US-020 — Recommendation inputs
**Given** the user is authorized to review a recommendation  
**When** they open the details  
**Then** relevant inventory, demand, lead-time, safety-stock, and open-supply inputs are visible.

### AC-US-021 — Approve recommendation
**Given** the user has approval permission and recommendation data is valid  
**When** they approve  
**Then** approval is recorded with actor, timestamp, recommendation version, and decision state.

### AC-US-022 — Edit recommendation
**Given** editing is permitted  
**When** the user changes the suggested quantity  
**Then** the edited quantity and original quantity are both retained in decision history.

### AC-US-023 — Reject recommendation
**Given** a recommendation is pending  
**When** the user rejects it  
**Then** a rejection reason is required and recorded.

### AC-US-024 — Decision history
**Given** a material recommendation decision exists  
**When** an authorized auditor views history  
**Then** prior recommendation, edits, approvals/rejections, actors, and timestamps are traceable.

## EP-05 — Supplier Risk

### AC-US-025 — Supplier performance
**Given** supplier performance data exists  
**When** the user selects a supplier and period  
**Then** configured supplier metrics are displayed with definitions and time period.

### AC-US-026 — Supplier risk to inventory
**Given** a supplier exception affects an open PO  
**When** the user opens the exception  
**Then** affected SKU/location inventory exposure is discoverable.

### AC-US-027 — Expected receipt changes
**Given** a source update changes an expected receipt  
**When** the change is processed  
**Then** the latest date and change state are visible.

### AC-US-028 — Supplier exception action
**Given** a supplier exception is assigned  
**When** the user records a follow-up action  
**Then** action, owner, timestamp, and resulting status are stored.

## EP-06 — Data Quality & Lineage

### AC-US-029 — Data-quality exceptions
**Given** a configured quality rule detects missing, stale, duplicate, or conflicting data  
**When** validation runs  
**Then** a data-quality exception identifies the affected object and rule.

### AC-US-030 — Decision data lineage
**Given** a decision depends on source data  
**When** an authorized user views lineage  
**Then** source, ingestion time, transformation/version, and published record reference are available.

### AC-US-031 — Degraded-data state
**Given** a critical source becomes stale or unavailable  
**When** a user opens an affected workflow  
**Then** the system shows a degraded-data warning and prevents unsafe automated actions.

### AC-US-032 — Resolve data-quality issue
**Given** a data-quality exception is open  
**When** an authorized owner records resolution  
**Then** resolution reason, actor, timestamp, and resulting quality state are recorded.

## EP-07 — Governance & Audit

### AC-US-033 — Role-based access
**Given** a user has a defined role  
**When** they access the platform  
**Then** only permitted views and actions are available.

**Given** an unauthorized API action is attempted  
**Then** the server rejects the action regardless of client UI state.

### AC-US-034 — Audit material actions
**Given** a material state change occurs  
**When** the action completes  
**Then** an immutable audit event contains actor, timestamp, object, previous state where applicable, and new state.

### AC-US-035 — Approval boundaries
**Given** an approval policy is configured  
**When** an action crosses the configured boundary  
**Then** required approval is enforced before downstream execution.

## EP-08 — Analytics & Reporting

### AC-US-036 — Inventory health KPIs
**Given** metric data is available  
**When** a leader opens the dashboard  
**Then** inventory and service-risk KPIs are displayed with period and definition.

### AC-US-037 — KPI drill-down
**Given** a KPI has underlying exception records  
**When** the leader selects the KPI  
**Then** the user can drill to the relevant exception population.

## EP-09 — Integrations

### AC-US-038 — Idempotent ingestion
**Given** the same source record is delivered more than once  
**When** ingestion processes the records  
**Then** the operational dataset contains one logical record and duplicate delivery is recorded as expected behavior.

**Given** ingestion fails transiently  
**Then** retry does not corrupt or duplicate successful records.

### AC-US-039 — Integration health
**Given** a configured source is active  
**When** the administrator opens integration health  
**Then** freshness, recent failures, and reconciliation status are visible.

## EP-10 — Administration

### AC-US-040 — Exception thresholds
**Given** the administrator has rule-configuration permission  
**When** a threshold is changed and published  
**Then** future exception evaluations use the new version while prior decisions retain historical context.

## Global negative cases
- Unauthorized users cannot bypass permissions through direct API calls.
- Missing required data never becomes an invented default without an explicit business rule.
- Stale data is not presented as current.
- Material decisions cannot be silently overwritten.
- Failed integrations cannot silently appear healthy.
- Audit events cannot be edited by ordinary operational users.
