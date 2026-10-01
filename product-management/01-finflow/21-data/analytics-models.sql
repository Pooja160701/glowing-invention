-- Weekly activation model
WITH onboarding AS (
  SELECT user_id, MIN(event_time) AS onboarding_time
  FROM product_events
  WHERE event_name = 'onboarding_completed'
  GROUP BY user_id
), actions AS (
  SELECT user_id, MIN(event_time) AS first_action_time
  FROM product_events
  WHERE event_name IN (
    'budget_created',
    'savings_goal_created',
    'goal_contribution_recorded',
    'insight_actioned',
    'transaction_category_corrected'
  )
  GROUP BY user_id
)
SELECT
  DATE_TRUNC('week', o.onboarding_time) AS cohort_week,
  COUNT(*) AS onboarded_users,
  COUNT(a.user_id) AS activated_users,
  COUNT(a.user_id)::DECIMAL / COUNT(*) AS activation_rate
FROM onboarding o
LEFT JOIN actions a ON o.user_id = a.user_id
GROUP BY 1
ORDER BY 1;

-- Experiment activation summary
SELECT
  variant,
  COUNT(*) AS users,
  SUM(activated) AS activated_users,
  SUM(activated)::DECIMAL / COUNT(*) AS activation_rate,
  AVG(first_action_minutes) AS avg_first_action_minutes
FROM experiment_assignments
GROUP BY variant;
