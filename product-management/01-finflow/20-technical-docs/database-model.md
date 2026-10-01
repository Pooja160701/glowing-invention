# FinFlow — Database Model

## Core Tables

### users
- id
- created_at
- status
- locale

### user_preferences
- user_id
- notification_preferences
- privacy_preferences
- updated_at

### imports
- id
- user_id
- source_type
- status
- created_at
- completed_at
- idempotency_key

### transactions
- id
- user_id
- import_id
- transaction_date
- category_id
- categorization_status
- created_at
- updated_at

### categories
- id
- name
- parent_id
- active

### budgets
- id
- user_id
- period
- status
- created_at

### budget_categories
- budget_id
- category_id
- limit_definition

### savings_goals
- id
- user_id
- goal_type
- target_definition
- target_date
- status

### insights
- id
- user_id
- insight_type
- confidence_bucket
- explanation
- created_at

### insight_actions
- id
- insight_id
- user_id
- action_type
- created_at

## Indexing Priorities
- user_id on user-owned resources
- transaction_date for time-based queries
- import_id for processing reconciliation
- status fields for operational queues
- created_at for audit/event queries
