# FinFlow — Errors, Pagination & Idempotency

## Error Schema

```json
{
  "error": {
    "code": "INVALID_CATEGORY",
    "message": "The requested category is not supported.",
    "request_id": "req_123"
  }
}
```

## Status Codes
- `400` invalid request
- `401` unauthenticated
- `403` unauthorized
- `404` resource not found
- `409` conflict / duplicate operation
- `422` validation failure
- `429` rate limited
- `500` unexpected server error
- `503` temporary service unavailable

## Cursor Pagination

```text
GET /api/v1/transactions?limit=50&cursor=abc123
```

Response should provide a stable `next_cursor` when more records exist.

## Idempotency
Mutation endpoints that may be retried should accept an `Idempotency-Key` header. The same key and equivalent request should return the original operation result rather than create a duplicate.
