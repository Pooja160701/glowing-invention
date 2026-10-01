-- Duplicate event IDs
SELECT event_id, COUNT(*) AS record_count
FROM product_events
GROUP BY event_id
HAVING COUNT(*) > 1;

-- Invalid event names
SELECT DISTINCT event_name
FROM product_events
WHERE event_name NOT IN (
  'signup_completed', 'onboarding_completed',
  'transactions_import_started', 'transactions_import_completed',
  'transaction_categorized', 'transaction_category_corrected',
  'financial_dashboard_viewed', 'budget_created',
  'budget_progress_viewed', 'savings_goal_created',
  'goal_contribution_recorded', 'insight_viewed',
  'insight_actioned', 'notification_preference_updated',
  'feedback_submitted'
);

-- Orphan users
SELECT e.event_id, e.user_id
FROM product_events e
LEFT JOIN users u ON e.user_id = u.user_id
WHERE u.user_id IS NULL;
