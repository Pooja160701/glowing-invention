# ADR-002 — Minimize Sensitive Data Exposure

## Status
Accepted

## Context
Financial information is highly sensitive and product analytics do not require raw financial values for most questions.

## Decision
Separate transactional financial data from product analytics and avoid sending raw sensitive values to analytics/replay tools.

## Consequences
- Reduced exposure surface
- Safer analytics
- More explicit data contracts
- Additional engineering effort for masking and aggregation
