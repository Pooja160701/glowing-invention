# BI Dashboard QA

## Metric QA
- [ ] Metric formula matches metric dictionary.
- [ ] Date filters behave correctly.
- [ ] Time zones are documented.
- [ ] Null handling is defined.
- [ ] Duplicate records are controlled.

## Reconciliation
- [ ] Booking counts reconcile with source-of-truth booking data.
- [ ] Notification counts reconcile with delivery records.
- [ ] Exception counts reconcile with operational queue.
- [ ] Security events reconcile with audit logs.

## Privacy QA
- [ ] No clinical content appears in dashboards.
- [ ] Pseudonymous identifiers are used where required.
- [ ] Small cohorts are handled safely.
- [ ] Access restrictions are tested.

## Release gate
A dashboard is production-ready only after metric, data-quality, reconciliation, privacy, and access checks pass.
