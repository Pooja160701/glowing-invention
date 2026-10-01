# BI Implementation Guide

## Power BI

Recommended model:
- Import fact and dimension tables.
- Build a star schema.
- Create reusable DAX measures from the metric dictionary.
- Add role-based access where sensitive operational views require restriction.

## Tableau

Recommended:
- Published data source.
- Certified metric definitions.
- Executive dashboard.
- Funnel worksheet.
- Operations workbook.
- Security/governance workbook.

## Looker

Recommended:
- Model facts and dimensions in the semantic layer.
- Define reusable measures.
- Govern joins centrally.
- Create explores for Booking, Operations, Communications, and Security.

## Metabase

Recommended:
- Curated models.
- Saved questions for canonical metrics.
- Executive dashboard.
- Operational dashboard.
- Scheduled delivery only after privacy/access review.

## Dashboard governance

Every dashboard should show:
- Data freshness.
- Reporting period.
- Metric definition link.
- Owner.
- Synthetic-data indicator when applicable.

## Synthetic data

synthetic-dashboard-data.csv is illustrative portfolio data. It must not be represented as real MediConnect production telemetry.
