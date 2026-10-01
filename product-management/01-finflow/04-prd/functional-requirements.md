# FinFlow — Functional Requirements

## FR-001 Transaction Import

The system shall allow a user to upload a supported transaction file.

The system shall:
- Validate required fields.
- Reject malformed records.
- Report import errors clearly.
- Prevent duplicate records where an identifier is available.
- Show import completion status.

## FR-002 Transaction Categorization

The system shall assign a category to eligible transactions.

The user shall be able to:
- View the assigned category.
- Change the category.
- Save the correction.
- See the updated category in subsequent views.

## FR-003 Dashboard

The dashboard shall display:
- Total income
- Total expenses
- Net cash flow
- Spending by category
- Budget status
- Goal progress
- Relevant financial insights

Users shall be able to select a time period.

## FR-004 Budgeting

Users shall be able to:
- Create a category budget.
- Edit a budget.
- View actual versus planned spending.
- View remaining budget.
- Receive a budget event when a configured threshold is reached.

## FR-005 Savings Goals

Users shall be able to:
- Create a goal.
- Define target amount.
- Define target date.
- Record contributions.
- View progress.
- Edit or archive a goal.

## FR-006 Explainable Insights

Each insight shall include:
- Insight title
- Supporting context
- Explanation
- Optional suggested action
- Dismiss/feedback control

The product shall not present automated insights as guaranteed financial outcomes.

## FR-007 Notifications

Users shall be able to:
- Enable/disable notification categories.
- Control notification frequency where supported.
- Dismiss notifications.

## FR-008 Recurring Expenses

The system shall identify candidate recurring transactions based on repeated patterns.

Candidates must be presented as suggestions and remain user-reviewable.
