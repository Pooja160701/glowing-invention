# Looker Semantic Model Specification

## Explores

### `product_events`
Dimensions:
- event_date
- platform
- event_name
- product_version
- acquisition_source

Measures:
- unique_users
- event_count

### `activation`
Dimensions:
- signup_week
- platform
- cohort

Measures:
- eligible_users
- activated_users
- activation_rate
- median_time_to_first_action

### `retention`
Dimensions:
- cohort_week
- retention_week

Measures:
- cohort_users
- retained_users
- retention_rate

## Governance
Metric definitions should be centralized. Derived metrics should reference approved measures rather than rebuilding formulas independently in each dashboard.
