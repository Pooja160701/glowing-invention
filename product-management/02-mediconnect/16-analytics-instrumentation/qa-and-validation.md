# Analytics QA and Validation

## Event contract testing

For each P0 event verify:
- Event name matches canonical taxonomy.
- Version is present.
- Required properties are present.
- Property types are correct.
- Allowed values are enforced.
- No sensitive free text is transmitted.
- Event is emitted once for the intended state transition.

## Reconciliation tests

Compare analytics events against source-of-truth records.

Examples:
- booking_succeeded count vs successful booking transactions.
- appointment_cancelled count vs appointment state transitions.
- reminder_delivered count vs delivery provider confirmations.
- exception_resolved count vs resolved exception records.

## Duplicate-event testing

Generate:
- Browser retries.
- API retries.
- Network reconnects.
- Page refreshes.

Verify downstream metrics remain idempotent or duplicates are detectable.

## Missing-event testing

Exercise:
- Failed API requests.
- Partial UI loads.
- Notification provider outage.
- Offline/reconnect scenarios.

Verify instrumentation does not silently disappear.

## Privacy QA

Search event payloads for prohibited fields before release.

Examples:
- diagnosis
- treatment
- clinical notes
- message body
- credentials
- access tokens
- unnecessary precise location

## Release gate

Analytics is production-ready only when:
- P0 event tests pass.
- Reconciliation variance is within the agreed tolerance.
- Privacy review passes.
- Dashboard queries return expected results.
- Event documentation is versioned.
