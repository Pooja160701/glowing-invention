# Trello Labels & Automation Specification

## Labels
P0 = release-critical; P1 = high-value; P2 = later; Discovery; Product; Design; Engineering; Data; Analytics; Security; QA.

## Suggested Automations

### Completion
When a card moves to Released: add release date and release-review marker.

### Blocker
When a card moves to Blocked: add Blocked label, require blocker description, and notify the owner.

### QA
When a card moves to QA / Validation: add QA checklist and require acceptance-criteria review.

> These are workflow specifications, not claims that Trello automation was configured in an external workspace.
