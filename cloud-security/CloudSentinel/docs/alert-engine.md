# CloudSentinel Alert Engine

The Alert Engine converts normalized findings and YAML detection-rule matches into persistent security alerts.

## Flow

```
AWS / provider integration
        ↓
Normalized Finding
        ↓
Detection Engine
        ↓
Matched Rule(s)
        ↓
Alert Engine
        ↓
PostgreSQL alerts table
        ↓
Alert API / dashboard / notification adapters
```

## Alert fields

- `alert_id`: CloudSentinel alert identifier
- `finding_id`: originating finding
- `rule_id`: detection rule that matched
- `severity`: highest severity between finding and detection rule
- `priority`: P1 through P5
- `risk_score`: CloudSentinel risk score
- `status`: new, acknowledged, resolved, suppressed
- `source`, `finding_type`, `asset`, `remediation`, and tags

## Deduplication

An alert is unique for a `finding_id + rule_id` pair. Re-running alert generation updates an existing active alert rather than creating another alert.

Resolved and suppressed alerts are not overwritten with active-state updates during regeneration.

## API

- `POST /api/v1/alerts/generate/{finding_id}` — evaluate one finding and create/update matching alerts
- `POST /api/v1/alerts/generate` — evaluate all active findings
- `GET /api/v1/alerts` — list and filter alerts
- `GET /api/v1/alerts/{alert_id}` — retrieve one alert
- `PATCH /api/v1/alerts/{alert_id}/status` — change alert lifecycle status

## Priority mapping

| Severity | Priority |
|---|---|
| critical | P1 |
| high | P2 |
| medium | P3 |
| low | P4 |
| informational | P5 |

The Alert Engine does not send email, Slack, PagerDuty, or other notifications yet. Those integrations should consume persisted alerts after the alert lifecycle is stable.
