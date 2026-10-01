# Identity, Privacy & Data Governance

## Identity model

Use pseudonymous identifiers for analytics.

Recommended identifiers:
- anonymous_id
- user_id_hash
- organization_id_hash
- session_id
- appointment_id_hash

Avoid exposing direct identifiers in product analytics systems where they are not required.

## Sensitive data boundary

Do not send to product analytics:
- Diagnosis.
- Treatment details.
- Clinical notes.
- Prescription information.
- Medical record content.
- Message bodies.
- Authentication credentials.
- Access tokens.
- Payment credentials.
- Unnecessary precise location.

## Role-aware tracking

Track actor type and organizational scope where useful:
- patient
- clinic_staff
- provider
- organization_admin
- support_admin

## Retention

Retention periods should be defined with the organization's privacy and legal requirements before production.

## Data minimization

Collect the minimum properties required to answer a documented product question.

## Access control

Analytics access should follow least privilege.

## Privacy review gate

A new event or property should not reach production until:
1. Product purpose is documented.
2. Data classification is recorded.
3. Sensitive-data review is complete.
4. Retention is understood.
5. Access requirements are approved.
