# FinFlow — Data Layer

> **Status:** Data architecture and synthetic datasets. No production financial data is included.

## Objectives
- Provide trustworthy product and financial-domain data models.
- Separate sensitive transactional data from product analytics.
- Support product metrics, BI, experimentation, and operational monitoring.
- Make data quality measurable and auditable.

## Data Layers

```text
Raw
 ↓
Validated
 ↓
Normalized
 ↓
Analytics Models
 ↓
Metrics / BI / Experiments
```

## Synthetic Data Rule
Every dataset in this folder is synthetic and must not be interpreted as real customer financial data.
