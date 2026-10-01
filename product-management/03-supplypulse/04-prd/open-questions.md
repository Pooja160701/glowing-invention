# SupplyPulse Open Product Questions

These questions should be resolved through customer discovery, technical discovery, prototype testing, or controlled pilots.

## User and workflow
1. Which exceptions have the highest financial or service impact?
2. How should severity be calculated?
3. What ownership model exists today?
4. Which decisions require formal approval?
5. How much explanation is enough for approval?

## Data
6. Which ERP/WMS systems are most common in the target segment?
7. What is the acceptable data latency by workflow?
8. Which fields are authoritative for inventory?
9. How should conflicting source values be handled?
10. How should inventory value be calculated?

## Recommendation
11. Should reorder-point calculations be native or initially ingested from existing planning systems?
12. Which recommendation inputs must always be visible?
13. What confidence or quality threshold should block a recommendation?

## Business
14. Which buyer owns budget?
15. Which ROI metric is easiest to validate?
16. Is pricing best based on locations, SKUs, transactions, users, or modules?
17. What implementation time is acceptable?

## Governance
18. Which actions require approval by value or risk?
19. What audit retention period is required?
20. Which downstream systems may receive writes?

## Pilot decision gate
Do not expand scope until the team has evidence for:
- data availability
- user workflow fit
- recommendation trust
- integration feasibility
- measurable operational value
