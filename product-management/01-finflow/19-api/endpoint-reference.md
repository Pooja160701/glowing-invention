# FinFlow — Endpoint Reference

## User
`GET /me`

Returns the authenticated user's profile and product preferences. Never return secrets or authentication credentials.

## Imports
`POST /imports`

Starts a transaction import. Use an idempotency key to make retries safe.

Response status: `202 Accepted` when processing asynchronously.

## Transactions
`GET /transactions`

Returns a paginated list. Use cursor pagination for stable traversal.

`PATCH /transactions/{transactionId}`

Updates permitted transaction metadata such as category.

## Budgets
`GET /budgets`

Returns budgets visible to the authenticated user.

`POST /budgets`

Creates a budget after validating period, categories, and permitted limits.

## Goals
`GET /goals`

Returns the user's goals.

`POST /goals`

Creates a savings goal using non-sensitive target representations where possible.

## Insights
`GET /insights`

Returns explainable insights with evidence metadata appropriate for the user.

`POST /insights/{insightId}/actions`

Records an action taken on an insight.

## Notifications
`GET /notifications/preferences`

`PUT /notifications/preferences`

Allows users to control supported notification channels.

## Feedback
`POST /feedback`

Accepts structured product feedback. Free-form text should be treated as potentially sensitive and protected accordingly.
