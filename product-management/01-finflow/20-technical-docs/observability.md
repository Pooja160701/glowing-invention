# FinFlow — Observability

## Golden Signals
- Latency
- Traffic
- Errors
- Saturation

## Service Metrics
- API request latency
- API error rate
- Import processing duration
- Import failure rate
- Queue depth
- Categorization processing time
- Database connection utilization
- Notification delivery failures

## Logs
Structured logs should include:
- timestamp
- service
- environment
- request_id
- operation
- outcome

Never log authentication secrets, bank credentials, raw account identifiers, or unnecessary financial values.

## Traces
Trace the import path across API → queue → worker → categorization → persistence.

## Alerts
Alert on sustained error-rate increases, queue backlog, failed imports, database saturation, and security events.
