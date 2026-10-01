# FinFlow — Acceptance Criteria

> Acceptance criteria are proposed product requirements for the portfolio MVP. They are not evidence of completed implementation.

## US-001 — Create Profile

### AC-001
**Given** a new user provides valid required profile information  
**When** they submit the form  
**Then** the profile is created and the user is taken to the next onboarding step.

### AC-002
**Given** a required field is missing or invalid  
**When** the user submits  
**Then** the system identifies the field and explains what must be corrected.

### Edge Cases
- Duplicate account identifier
- Invalid input format
- Interrupted submission

---

## US-002 — Understand Data Use

### AC-003
**Given** the user is entering the financial-data setup flow  
**When** data-use information is displayed  
**Then** the user can understand what data is collected, why it is used, and what relevant controls are available.

### AC-004
**Given** the user does not provide required consent  
**When** they attempt to continue to a consent-dependent step  
**Then** the product does not proceed and explains the consequence.

---

## US-003 — Import Transactions

### AC-005
**Given** the user selects a supported file  
**When** the file passes validation  
**Then** the system imports valid transaction records and shows an import summary.

### AC-006
**Given** the uploaded file contains invalid records  
**When** the import is processed  
**Then** valid records are handled according to the import policy and invalid records are reported.

### AC-007
**Given** a duplicate transaction can be identified  
**When** the user imports it again  
**Then** the system prevents unintended duplication.

### Edge Cases
- Empty file
- Unsupported format
- Missing required columns
- Malformed dates
- Invalid amount
- Duplicate file
- Very large file

---

## US-004 — Review Import Errors

### AC-008
**Given** an import contains validation failures  
**When** processing finishes  
**Then** the user can identify failed records and the reason for each failure.

### AC-009
**Given** some records failed  
**When** the user views the import result  
**Then** the product clearly distinguishes successful, failed, and skipped records.

---

## US-005 — View Categorized Transactions

### AC-010
**Given** imported transactions have categories  
**When** the user opens the transaction list  
**Then** each eligible transaction displays its category.

### AC-011
**Given** a category cannot be confidently assigned  
**When** the transaction is displayed  
**Then** it is presented for user review rather than being represented as certain.

---

## US-006 — Correct a Category

### AC-012
**Given** a user opens a transaction  
**When** they select a different category and save  
**Then** the transaction displays the new category.

### AC-013
**Given** a category update succeeds  
**When** the user returns to the transaction list  
**Then** the corrected category is persisted.

---

## US-007 — View Financial Summary

### AC-014
**Given** the user has valid transaction data  
**When** the dashboard loads  
**Then** income, expenses, and net cash flow are displayed for the selected period.

### AC-015
**Given** no transaction data exists  
**When** the user opens the dashboard  
**Then** the product shows an informative empty state rather than misleading zero-value conclusions.

---

## US-008 — Explore Spending Categories

### AC-016
**Given** categorized transactions exist  
**When** the user selects a time period  
**Then** spending by category is recalculated for that period.

### AC-017
**Given** the user selects a category  
**When** category details open  
**Then** the user can identify the underlying transactions contributing to the amount.

---

## US-009 — Create Budget

### AC-018
**Given** the user enters a valid category and budget amount  
**When** they save the budget  
**Then** the budget is created and visible in the budget view.

### AC-019
**Given** the amount is invalid  
**When** the user attempts to save  
**Then** the system prevents submission and explains the validation error.

---

## US-010 — Monitor Budget

### AC-020
**Given** a budget exists and transactions are available  
**When** the user opens budget status  
**Then** actual spending, planned amount, and remaining amount are displayed.

### AC-021
**Given** spending reaches a configured threshold  
**When** budget status is recalculated  
**Then** the corresponding budget event becomes eligible for notification.

---

## US-011 — Edit Budget

### AC-022
**Given** an existing budget  
**When** the user changes its amount and saves  
**Then** the updated amount is applied to subsequent budget calculations.

---

## US-012 — Create Savings Goal

### AC-023
**Given** the user enters a valid goal name, target amount, and target date  
**When** they save  
**Then** the goal is created with zero or existing contribution state.

### AC-024
**Given** the target amount or date is invalid  
**When** the user submits  
**Then** the system explains the validation problem.

---

## US-013 — View Goal Progress

### AC-025
**Given** a savings goal exists  
**When** the user opens the goal  
**Then** current progress, remaining amount, and target date are displayed.

### AC-026
**Given** a contribution is recorded  
**When** goal progress recalculates  
**Then** the progress display reflects the new amount.

---

## US-014 — View Insight

### AC-027
**Given** sufficient financial data exists for an eligible insight  
**When** the dashboard is generated  
**Then** the insight is displayed with relevant context.

### AC-028
**Given** insufficient data exists  
**When** the insight engine evaluates the user  
**Then** the product does not fabricate a financial insight.

---

## US-015 — Understand Insight

### AC-029
**Given** an insight is displayed  
**When** the user opens its explanation  
**Then** the product shows the relevant data signal or rule behind the insight.

### AC-030
**Given** an insight contains an automated recommendation  
**When** the user views it  
**Then** the product clearly distinguishes observed information from a suggested action.

---

## US-016 — Act on Insight

### AC-031
**Given** an insight has a supported action  
**When** the user selects the action  
**Then** the corresponding workflow opens with relevant context prefilled where appropriate.

### AC-032
**Given** no supported action exists  
**When** the user views the insight  
**Then** the product does not present a misleading action control.

---

## US-017 — Configure Notifications

### AC-033
**Given** the user opens notification settings  
**When** they change a supported notification preference  
**Then** the preference is saved and applied to future notifications.

---

## US-018 — Receive Budget Event

### AC-034
**Given** a user has enabled budget notifications  
**When** the configured threshold is reached  
**Then** an eligible notification is generated according to the notification policy.

### AC-035
**Given** the user has disabled the relevant notification  
**When** the threshold is reached  
**Then** no user notification is sent for that category.

---

## US-019 — Track Product Events

### AC-036
**Given** a tracked product action occurs  
**When** the action completes  
**Then** the corresponding analytics event is recorded with required event properties.

### AC-037
**Given** analytics collection is unavailable  
**When** a core product action completes  
**Then** the user-facing workflow remains functional.

---

## US-020 — Track Insight Feedback

### AC-038
**Given** an insight is displayed  
**When** the user interacts with it or dismisses it  
**Then** the relevant event is captured for product analysis.

---

## US-021 — Review Data Controls

### AC-039
**Given** the user opens privacy/data controls  
**When** the page loads  
**Then** relevant permissions and controls are visible.

---

## US-022 — Delete Financial Data

### AC-040
**Given** the user requests financial-data deletion  
**When** they complete the required confirmation flow  
**Then** the deletion request is recorded and processed according to the defined data-lifecycle policy.

### AC-041
**Given** deletion is irreversible for a data category  
**When** the user reaches the final confirmation  
**Then** the product clearly communicates the consequence before confirmation.
