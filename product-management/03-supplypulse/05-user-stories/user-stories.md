# SupplyPulse User Stories

## EP-01 — Inventory Visibility

### US-001 — View inventory by SKU and location
**As an Inventory Planner, I want to view inventory by SKU and location, so that I can understand current stock exposure.**
- Priority: P0
- PRD: FR-001, FR-002

### US-002 — See inventory position components
**As an Inventory Planner, I want to see on-hand, reserved, available, and in-transit quantities, so that I can understand the true inventory position.**
- Priority: P0
- PRD: FR-002

### US-003 — See inventory value and aging
**As an Inventory Planner, I want to see inventory value and aging, so that I can identify working-capital exposure.**
- Priority: P0
- PRD: FR-001

### US-004 — See source and freshness
**As an Operations Manager, I want to see the source and freshness of inventory data, so that I can judge whether it is safe to act on.**
- Priority: P0
- PRD: FR-003, FR-024

## EP-02 — Demand & Supply Intelligence

### US-005 — Review demand history
**As an Inventory Planner, I want to review historical demand by SKU/location, so that I can understand demand behavior before making a replenishment decision.**
- Priority: P0
- PRD: FR-012

### US-006 — View forecast input
**As an Inventory Planner, I want to see the current forecast input and version, so that I can understand the demand assumption behind a recommendation.**
- Priority: P0
- PRD: FR-012, FR-015

### US-007 — View open purchase orders
**As a Procurement Manager, I want to view open POs and expected receipts, so that I can understand incoming supply.**
- Priority: P0
- PRD: FR-012, FR-017

### US-008 — Compare demand and supply
**As an Inventory Planner, I want to compare projected demand with expected supply, so that I can identify potential service gaps.**
- Priority: P0
- PRD: FR-012

## EP-03 — Exception Management

### US-009 — Detect stockout risk
**As an Inventory Planner, I want the system to identify projected stockout risk, so that I can intervene before availability is affected.**
- Priority: P0
- PRD: FR-004

### US-010 — Detect excess inventory
**As an Inventory Planner, I want the system to identify excess or aging inventory, so that I can investigate working-capital exposure.**
- Priority: P0
- PRD: FR-005

### US-011 — Detect late purchase orders
**As a Procurement Manager, I want late POs to become exceptions, so that supplier issues are visible before they affect service.**
- Priority: P0
- PRD: FR-006

### US-012 — Detect lead-time deviation
**As a Procurement Manager, I want deviations from expected lead time to be detected, so that supplier risk becomes visible earlier.**
- Priority: P0
- PRD: FR-007

### US-013 — Prioritize exceptions
**As an Operations Manager, I want exceptions prioritized by severity and business impact, so that I can focus on the most important issues first.**
- Priority: P0
- PRD: FR-009

### US-014 — Filter exception queue
**As an Inventory Planner, I want to filter exceptions by type, SKU, location, severity, and owner, so that I can focus my work.**
- Priority: P0
- PRD: FR-009

### US-015 — Assign an exception owner
**As an Operations Manager, I want to assign an owner and due date to an exception, so that responsibility is explicit.**
- Priority: P0
- PRD: FR-010

### US-016 — Track exception status
**As an Inventory Planner, I want to track exception status and resolution reason, so that unresolved issues do not disappear.**
- Priority: P0
- PRD: FR-011, FR-025

### US-017 — View exception context
**As a Planner, I want one exception view to show inventory, demand, supply, supplier, and data-quality context, so that I do not have to reconcile multiple reports manually.**
- Priority: P0
- PRD: FR-012, FR-017, FR-024

## EP-04 — Replenishment Decision Support

### US-018 — Receive reorder recommendation
**As an Inventory Planner, I want a suggested reorder quantity, so that I can evaluate a replenishment action efficiently.**
- Priority: P0
- PRD: FR-013

### US-019 — Understand recommendation rationale
**As an Inventory Planner, I want to see why a reorder quantity was suggested, so that I can make a confident decision.**
- Priority: P0
- PRD: FR-013, FR-015

### US-020 — Review recommendation inputs
**As a Procurement Manager, I want to see demand, inventory, lead-time, safety-stock, and open-supply inputs, so that I can validate the recommendation.**
- Priority: P0
- PRD: FR-015

### US-021 — Approve recommendation
**As an authorized Planner, I want to approve a recommendation, so that an accepted decision is recorded for downstream action.**
- Priority: P0
- PRD: FR-014

### US-022 — Edit recommendation
**As an authorized Planner, I want to edit a suggested quantity before approval, so that I can incorporate operational context not represented by the model.**
- Priority: P0
- PRD: FR-014

### US-023 — Reject recommendation
**As an authorized Planner, I want to reject a recommendation with a reason, so that the decision remains explainable and auditable.**
- Priority: P0
- PRD: FR-014, FR-020

### US-024 — Preserve decision history
**As an Auditor, I want to see recommendation decisions and changes, so that material actions can be traced.**
- Priority: P0
- PRD: FR-020

## EP-05 — Supplier Risk

### US-025 — View supplier performance
**As a Procurement Manager, I want to view supplier on-time delivery and lead-time performance, so that I can identify supplier risk.**
- Priority: P1
- PRD: FR-016

### US-026 — Link supplier risk to inventory
**As a Procurement Manager, I want to see which inventory positions are affected by a supplier issue, so that I can prioritize supplier actions by business impact.**
- Priority: P0
- PRD: FR-017

### US-027 — See expected receipt changes
**As a Procurement Manager, I want to see changes to expected receipt dates, so that I can identify emerging supply risk.**
- Priority: P0
- PRD: FR-006, FR-017

### US-028 — Track supplier exception action
**As a Procurement Manager, I want to record supplier follow-up and resolution status, so that supplier exceptions have a closed-loop workflow.**
- Priority: P1
- PRD: FR-011, FR-025

## EP-06 — Data Quality & Lineage

### US-029 — Detect data-quality exceptions
**As an Operations Manager, I want missing, stale, duplicate, or conflicting records flagged, so that bad data does not silently drive decisions.**
- Priority: P0
- PRD: FR-008, FR-024

### US-030 — Trace decision data
**As an Auditor, I want decision-critical data linked to its source and refresh time, so that I can investigate discrepancies.**
- Priority: P0
- PRD: FR-003, FR-020

### US-031 — View degraded-data state
**As a Planner, I want the system to warn me when critical data is stale or unavailable, so that I do not treat degraded information as current.**
- Priority: P0
- PRD: FR-024

### US-032 — Resolve data-quality issue
**As an Operations Manager, I want to record the resolution of a data-quality exception, so that data problems have ownership and evidence of closure.**
- Priority: P0
- PRD: FR-025

## EP-07 — Governance & Audit

### US-033 — Enforce role-based access
**As an Administrator, I want role-based permissions, so that users only access actions appropriate to their responsibilities.**
- Priority: P0
- PRD: FR-020

### US-034 — Audit material actions
**As an Auditor, I want material changes to record actor, timestamp, object, and state change, so that decisions are traceable.**
- Priority: P0
- PRD: FR-020

### US-035 — Configure approval boundaries
**As an Administrator, I want configurable approval policies, so that high-impact actions require appropriate human authorization.**
- Priority: P1
- PRD: FR-022

## EP-08 — Analytics & Reporting

### US-036 — View inventory health KPIs
**As a Supply Chain Leader, I want inventory health KPIs, so that I can understand service and working-capital exposure.**
- Priority: P1
- PRD: FR-018

### US-037 — Drill from KPI to exceptions
**As a Supply Chain Leader, I want to drill from an aggregate risk metric to underlying exceptions, so that I can understand what is driving the result.**
- Priority: P1
- PRD: FR-018

## EP-09 — Integrations

### US-038 — Ingest source data idempotently
**As a Data Engineer, I want source records ingested idempotently, so that retries do not create duplicate operational data.**
- Priority: P0
- PRD: INT-002, INT-004

### US-039 — Monitor integration health
**As an Administrator, I want source freshness, failures, and reconciliation status visible, so that integration issues are detected before they affect decisions.**
- Priority: P0
- PRD: INT-005, INT-006, INT-009, INT-010

## EP-10 — Administration

### US-040 — Configure exception thresholds
**As an Administrator, I want configurable exception thresholds, so that business rules can adapt to different organizations and operating models.**
- Priority: P1
- PRD: FR-021

## Story quality checklist
Every story should eventually have:
- acceptance criteria,
- testable outcome,
- owner,
- priority,
- dependency,
- analytics events where relevant,
- security/privacy implications where relevant.
