# FinFlow — API Data Schemas

## Transaction

```json
{
  "id": "txn_123",
  "date": "2026-08-31",
  "category": "groceries",
  "direction": "expense",
  "status": "categorized"
}
```

Exact financial amounts and raw account identifiers are intentionally omitted from public analytics examples.

## Budget

```json
{
  "id": "budget_123",
  "period": "2026-08",
  "status": "active",
  "category_count": 6
}
```

## Goal

```json
{
  "id": "goal_123",
  "type": "emergency_fund",
  "status": "active",
  "progress_bucket": "25_50_percent"
}
```

## Insight

```json
{
  "id": "insight_123",
  "type": "spending_change",
  "confidence_bucket": "high",
  "explanation": "Your recent spending pattern changed compared with your recent baseline.",
  "action_types": ["review_category"]
}
```
