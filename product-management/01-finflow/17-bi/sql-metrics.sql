-- FinFlow BI metric examples

-- Weekly active financial action users
SELECT
  DATE_TRUNC('week', event_date) AS week,
  COUNT(DISTINCT user_id) AS wafau
FROM product_events
WHERE event_name IN (
  'budget_created',
  'goal_contribution_recorded',
  'insight_actioned',
  'transaction_category_corrected',
  'financial_dashboard_viewed'
)
GROUP BY 1
ORDER BY 1;

-- Import completion rate
SELECT
  DATE_TRUNC('week', event_date) AS week,
  SUM(CASE WHEN event_name = 'transactions_import_completed' THEN 1 ELSE 0 END)::DECIMAL /
  NULLIF(SUM(CASE WHEN event_name = 'transactions_import_started' THEN 1 ELSE 0 END), 0) AS import_completion_rate
FROM product_events
GROUP BY 1
ORDER BY 1;

-- Categorization correction rate
SELECT
  DATE_TRUNC('week', event_date) AS week,
  SUM(CASE WHEN event_name = 'transaction_category_corrected' THEN 1 ELSE 0 END)::DECIMAL /
  NULLIF(SUM(CASE WHEN event_name = 'transaction_categorized' THEN 1 ELSE 0 END), 0) AS correction_rate
FROM product_events
GROUP BY 1
ORDER BY 1;
