# FinFlow — Data Dictionary

| Entity | Field | Type | Description | Sensitive |
|---|---|---|---|---|
| User | user_id | string | Anonymous product identifier | No |
| User | signup_date | date | Account creation date | No |
| Transaction | transaction_id | string | Transaction identifier | Yes |
| Transaction | category | string | Product category | Potentially |
| Transaction | transaction_date | date | Transaction date | Yes |
| Import | import_id | string | Import job identifier | No |
| Import | status | string | Import processing state | No |
| Budget | budget_id | string | Budget identifier | No |
| Budget | period | string | Budget period | No |
| Goal | goal_id | string | Savings goal identifier | No |
| Goal | goal_type | string | Goal category | Potentially |
| Event | event_name | string | Product event | No |
| Event | event_date | timestamp | Event timestamp | No |
| Experiment | experiment_id | string | Experiment identifier | No |
| Experiment | variant | string | Assigned variant | No |

Exact balances, account numbers, credentials, and unnecessary raw financial values should not be copied into product analytics datasets.
