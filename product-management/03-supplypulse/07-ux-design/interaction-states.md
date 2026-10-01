# SupplyPulse Interaction & State Specification

## Global states
Every data-driven screen should support:
1. Loading
2. Loaded
3. Empty
4. Partial/degraded
5. Error
6. Unauthorized

## Data states
- Fresh: normal presentation.
- Stale: show freshness warning and last-known timestamp.
- Unavailable: show unavailable state; never substitute fabricated values.
- Conflicting: show data-quality warning and source/lineage context.

## Exception states
New, Acknowledged, In progress, Blocked, Resolved, Reopened.

## Recommendation states
Generated, Needs review, Approved, Edited, Rejected, Expired, Blocked by data quality.

## Approval interaction
Before approval:
- show decision impact
- show rationale
- show critical inputs

After approval:
- confirmation state
- actor
- timestamp
- downstream status

## High-impact actions
Use confirmation when the consequence is material. Confirmation should summarize what will change rather than rely on generic confirmation copy.

## Notifications
Notifications should be actionable, deduplicated, severity-aware, linked to the underlying object, and dismissible where appropriate.
