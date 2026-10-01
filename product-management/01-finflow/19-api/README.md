# FinFlow — API Documentation

> **Status:** API contract/specification. No production API was deployed by this portfolio artifact.

## API Goals
Provide stable, secure interfaces for onboarding, transaction import, categorization, dashboards, budgets, savings goals, insights, notifications, and feedback.

## Base Convention
`/api/v1`

## Core Resources
- users
- transactions
- imports
- budgets
- goals
- insights
- notifications
- feedback

## API Principles
- Resource-oriented endpoints
- Explicit versioning
- Consistent error schema
- Idempotent mutation where retry risk exists
- Least-privilege authorization
- Sensitive data minimization
- Auditability for security-relevant actions
