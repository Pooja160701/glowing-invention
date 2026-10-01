# SupplyPulse Functional Requirements

| ID | Requirement | Priority | Primary user | Acceptance target |
|---|---|---|---|---|
| FR-001 | Display inventory by SKU/location | P0 | Planner | User can filter and open inventory records |
| FR-002 | Display on-hand/available/reserved/in-transit | P0 | Planner | Values reconcile to defined source fields |
| FR-003 | Display inventory freshness/source | P0 | All | Timestamp and source are visible |
| FR-004 | Detect stockout-risk exceptions | P0 | Planner | Rule creates actionable exception |
| FR-005 | Detect excess/aging exceptions | P0 | Planner | Configurable threshold creates exception |
| FR-006 | Detect late-PO exceptions | P0 | Procurement | Late PO appears with affected receipt |
| FR-007 | Detect lead-time deviation | P0 | Procurement | Deviation threshold is configurable |
| FR-008 | Detect data-quality exceptions | P0 | Operations | Missing/stale/conflicting data is flagged |
| FR-009 | Prioritize exception queue | P0 | All | User can sort/filter by severity and impact |
| FR-010 | Assign exception owner | P0 | All | Owner and due date are persisted |
| FR-011 | Record exception status | P0 | All | Open/in-progress/resolved states are auditable |
| FR-012 | Show demand/supply context | P0 | Planner | Exception displays relevant signals |
| FR-013 | Show replenishment recommendation | P0 | Planner | Recommendation contains quantity and rationale |
| FR-014 | Approve/reject/edit recommendation | P0 | Planner/Procurement | Decision is persisted with actor/time |
| FR-015 | Show recommendation inputs | P0 | Planner | Key inputs and assumptions are visible |
| FR-016 | Track supplier performance | P1 | Procurement | Supplier metrics available by period |
| FR-017 | Link supplier risk to inventory | P0 | Procurement | Affected SKU/location is discoverable |
| FR-018 | Provide executive inventory-risk view | P1 | Leader | KPIs and drill-down available |
| FR-019 | Export operational data | P1 | All | Authorized users can export allowed fields |
| FR-020 | Maintain audit history | P0 | Admin/Auditor | Material changes are traceable |
| FR-021 | Configure exception thresholds | P1 | Admin | Authorized users can change rules |
| FR-022 | Configure approval policies | P1 | Admin | Policies support risk/value boundaries |
| FR-023 | Support role-based dashboards | P1 | All | Users see relevant workflows |
| FR-024 | Show data-quality status | P0 | All | Critical quality issues visible in context |
| FR-025 | Capture resolution reason | P0 | All | Resolved exceptions require reason |

## Priority
P0 = required for controlled MVP pilot.
P1 = important but can follow the initial pilot.
P2 = later roadmap consideration.
