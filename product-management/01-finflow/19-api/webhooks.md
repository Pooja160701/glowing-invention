# FinFlow — Webhook Specification

> Proposed contract; not connected to a live webhook provider.

## Events
- `import.completed`
- `import.failed`
- `budget.threshold_reached`
- `goal.progress_updated`

## Example

```json
{
  "id": "evt_123",
  "type": "import.completed",
  "created_at": "2026-08-31T10:30:00Z",
  "data": {
    "import_id": "imp_123",
    "status": "completed"
  }
}
```

## Reliability
- Sign webhook payloads.
- Include event IDs.
- Allow retries with exponential backoff.
- Consumers must be idempotent.
- Provide delivery logs.
- Never include unnecessary financial data in webhook payloads.
