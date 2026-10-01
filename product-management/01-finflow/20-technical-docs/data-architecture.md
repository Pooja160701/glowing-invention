# FinFlow — Data Architecture

## Data Domains

### Identity
- User
- Preferences
- Consent / privacy settings

### Financial Data
- Import
- Transaction
- Category
- Merchant metadata where permitted

### Planning
- Budget
- Budget category
- Savings goal
- Goal progress

### Insights
- Insight
- Evidence metadata
- User action

### Product Analytics
- Event
- Session/cohort metadata

## Data Flow

```text
Import File
   ↓
Validation
   ↓
Normalized Transactions
   ↓
Categorization
   ↓
Aggregations
   ↓
Dashboard / Budgets / Goals / Insights
   ↓
Privacy-safe Product Events
```

## Data Quality Controls
- Schema validation
- Required-field validation
- Duplicate detection
- Idempotent imports
- Referential integrity
- Processing reconciliation
- Error quarantine
- Data-quality monitoring
