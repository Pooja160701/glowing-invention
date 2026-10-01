# Trello Automation Rules

These are proposed Butler-style rules. They are specifications, not executed automations in an external Trello workspace.

## Rule 1 — P0 visibility
When a card receives the P0 label, keep it visibly prioritized in its current list.

## Rule 2 — Ready for QA
When a card moves to QA / Validation, add the QA label and create a QA checklist if needed.

## Rule 3 — Release readiness
When a card moves to Ready for Release, verify the Definition of Done checklist and add the release label.

## Rule 4 — Blocker visibility
When a card moves to Blocked / Needs Decision, add a Blocked label and assign the decision owner.

## Rule 5 — Release closure
When a card moves to Released, add the release date and request metric verification.

## Rule 6 — Aging work
When a card remains In Progress beyond the agreed sprint threshold, add an Aging label and surface it in the next product review.

## Rule 7 — Analytics dependency
When a card with an analytics requirement moves to QA, add an Analytics Verification checklist item.

## Governance
Automation should improve visibility, not make irreversible product decisions automatically.
