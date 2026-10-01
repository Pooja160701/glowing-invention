# SupplyPulse Research Synthesis

> **Evidence note:** All participant evidence in this portfolio layer is synthetic. The synthesis demonstrates how real research could be analyzed; it is not proof of customer demand.

## Executive summary
The synthetic research points to a common pattern across planning, procurement, operations, and leadership: users do not primarily lack dashboards; they lack a trusted, prioritized path from **data → risk → explanation → action**.

The recurring workflow begins with reconciling data, moves into identifying exceptions, then requires cross-functional investigation before a decision can be approved. This suggests that SupplyPulse should treat data trust and workflow context as first-class product concerns.

## Theme 1 — Trust precedes action
Participants repeatedly describe checking timestamps, reconciling systems, or comparing spreadsheets before acting.

**Hypothesis:** showing source, freshness, and data-quality status could increase confidence in operational decisions.

**Potential PRD implication:** every material inventory or recommendation view should expose relevant provenance and freshness.

## Theme 2 — Exceptions need prioritization
Users report that large volumes of alerts can create noise. Operational teams want a smaller list of issues that require attention.

**Hypothesis:** severity should combine operational impact, time sensitivity, and affected inventory/service exposure.

**Potential PRD implication:** create an exception queue with severity, owner, due date, business impact, and recommended next action.

## Theme 3 — Recommendations need explanations
A suggested reorder quantity is not enough for a human approver.

**Hypothesis:** users will trust decision support more when demand, inventory position, lead time, safety stock, and relevant changes are visible.

**Potential PRD implication:** recommendation cards should expose inputs, assumptions, rationale, and approval history.

## Theme 4 — Supplier risk is connected to inventory risk
Procurement and planning decisions are intertwined. A late PO matters most when it affects a service-risk SKU.

**Hypothesis:** supplier events should be connected to impacted inventory and expected service outcomes.

**Potential PRD implication:** supplier exceptions should show affected SKUs/locations and inventory exposure.

## Theme 5 — Manual reconciliation is a workflow problem
Spreadsheet use is not simply a tooling preference. It often acts as a local control mechanism for reconciling data, calculating risk, or recording decisions.

**Hypothesis:** replacing spreadsheets without replacing their control functions will not solve the underlying problem.

**Potential PRD implication:** provide auditability, exports, calculation transparency, and decision history.

## Theme 6 — Human control matters
Users appear comfortable with decision assistance but want control over material actions.

**Hypothesis:** human approval should remain mandatory for high-impact replenishment actions in the initial product.

**Potential PRD implication:** design recommendation workflows around approve/reject/edit rather than autonomous execution.

## Contradictions to validate
1. High-maturity planners may want deeper automation while lower-maturity teams may need better visibility first.
2. Some users may prefer aggregated risk scores; others may distrust opaque scores.
3. Leaders want simple summaries while operators need detailed evidence.
4. Near-real-time data may be valuable for some workflows but unnecessary for slower-moving categories.
5. Automation tolerance may differ by SKU criticality and business risk.

## Research-derived product hypotheses
| Hypothesis | Confidence from synthetic exercise | Next validation |
|---|---|---|
| Data freshness/source improves trust | Medium | Usability test |
| Prioritized exceptions reduce triage effort | Medium | Workflow prototype |
| Explainable recommendations improve approval confidence | Medium | Concept test |
| Supplier risk should connect to inventory impact | Medium | Journey walkthrough |
| Human approval is preferred for material actions | Medium | Interview + prototype |
| Data-quality visibility is a product feature | Medium | Shadow reconciliation work |

Confidence here refers only to the strength of the **synthetic portfolio exercise**, not statistical confidence.

## Key opportunity statement
> Supply-chain teams need a trusted and explainable way to identify the few inventory and supply exceptions that matter most, understand why they are happening, and coordinate a human-approved response.

## Research → product translation
**Research theme:** fragmented data  
→ **Need:** trusted inventory state  
→ **Requirement hypothesis:** source/freshness/quality metadata

**Research theme:** alert overload  
→ **Need:** prioritized exceptions  
→ **Requirement hypothesis:** severity and business-impact scoring

**Research theme:** unclear recommendations  
→ **Need:** explainable decisions  
→ **Requirement hypothesis:** recommendation rationale + approval workflow

**Research theme:** supplier variability  
→ **Need:** connected risk  
→ **Requirement hypothesis:** supplier event → impacted inventory mapping

## Next research round
Before locking the PRD, validate:
- actual ERP/WMS/source-system patterns,
- exact exception definitions,
- acceptable data latency,
- preferred severity logic,
- recommendation approval behavior,
- measurable value from reduced decision time and avoided exceptions.
