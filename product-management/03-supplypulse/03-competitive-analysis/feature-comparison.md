# SupplyPulse Feature Comparison

Legend: D = publicly documented capability; H = hypothesis / category capability requiring validation; S = SupplyPulse MVP hypothesis.

| Capability | SAP IBP | Oracle NetSuite | Manhattan Active SCP | SupplyPulse |
|---|---|---|---|---|
| Inventory planning | D | D | D | S |
| Demand planning / forecasting | D | D | D | S |
| Replenishment | D | D | D | S |
| Allocation | D | D/H | D | Later |
| Scenario / what-if analysis | D | H | D | Later |
| Supply-chain alerts | D | H | D | S |
| Supplier / PO risk workflow | H | D/H | H | S |
| Exception prioritization | H | H | D/H | S / core |
| Data freshness visibility | H | H | H | S / core |
| Data lineage at decision point | H | H | H | S / core |
| Explainable recommendation | H | H | D | S / core |
| Human approval workflow | H | D/H | D/H | S / core |
| Exception ownership | H | H | H | S / core |
| Audit trail for decision | H | D/H | H | S / core |
| ERP/WMS integration | D | D | D | S / core |
| Autonomous replenishment | H | H | D | Later |
| Multi-echelon optimization | D/H | H | D | Later |
| Executive inventory/service view | D | D/H | D | S |

## Interpretation
The matrix is not a feature-scorecard. It is a scope and positioning tool.

Established platforms already cover many planning fundamentals. Manhattan explicitly documents demand forecasting, replenishment, allocation, execution integration, and explanation of decisions. Oracle documents demand planning, supply planning, and current inventory workflows. SAP documents planning, inventory, replenishment, simulations, analytics, and alerts. citeturn0search4turn0search9turn0search7turn0search15turn0search16

SupplyPulse should therefore concentrate MVP depth on the workflow that connects those capabilities:
exception → context → recommendation → approval → action → resolution evidence.
