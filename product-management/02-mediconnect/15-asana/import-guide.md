# Asana Import Guide

## Recommended implementation

Create the workspace:
**MediConnect Product Delivery**

Create the four projects defined in workspace-structure.md.

Use task-catalog.csv as the initial task source.

Map:
- Task → Task name
- Project → Project
- Section → Section
- Priority → Priority custom field
- Workstream → Product Area
- Release → Release custom field
- Owner → Assignee
- Points → Effort field
- Dependency → Dependency relationship
- Metric → Description or Metric field

Create milestones:
- M1 Discovery Ready
- M2 Booking MVP Ready
- M3 Self-Service Ready
- M4 Operations & Trust Ready
- M5 Controlled MVP Launch

## Important

This repository does not claim an external Asana workspace was created. It provides an implementation-ready portfolio specification.
