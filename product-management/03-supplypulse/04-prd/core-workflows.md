# SupplyPulse Core Workflows

## Workflow 1 — Start-of-day exception review
1. User opens role dashboard.
2. System loads current exception queue.
3. Exceptions are ranked by severity and business impact.
4. User filters by location, SKU, category, or owner.
5. User opens highest-priority exception.
6. System displays inventory, demand, supply, supplier, freshness, and data-quality context.
7. User assigns or accepts ownership.
8. User records action or opens related workflow.

Success: user reaches an actionable high-impact exception without manually combining reports.

## Workflow 2 — Replenishment decision
1. Trigger identifies replenishment need.
2. System assembles current inventory, demand, lead time, safety stock, open supply, and relevant exceptions.
3. Recommendation engine calculates or retrieves suggested quantity.
4. User reviews rationale and inputs.
5. User approves, edits, or rejects.
6. System records actor, timestamp, decision, and rationale.
7. Downstream order workflow remains governed by configured integration and approval policy.

## Workflow 3 — Late supplier PO
1. Source update changes expected receipt.
2. System detects lateness or lead-time deviation.
3. Exception is created or updated.
4. Affected SKU/location inventory exposure is calculated.
5. Procurement owner is notified through configured channel.
6. User records supplier action.
7. Exception closes after defined resolution condition.

## Workflow 4 — Data-quality exception
1. Ingestion detects missing, stale, or conflicting record.
2. Data-quality exception is created.
3. Source and affected objects are shown.
4. Owner investigates.
5. Correction/reconciliation occurs in source system where appropriate.
6. SupplyPulse records resolution and refresh state.

## Workflow 5 — Executive risk review
1. Leader opens KPI view.
2. System shows inventory exposure, service risk, exception aging, supplier risk, and trend.
3. Leader drills from KPI to exception cluster.
4. Leader identifies owner and action status.
5. Review outcome is recorded through the configured workflow.

## Workflow principle
signal → context → decision → owner → action → resolution evidence
