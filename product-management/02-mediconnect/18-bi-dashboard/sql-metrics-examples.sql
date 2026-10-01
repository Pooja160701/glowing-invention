-- Illustrative SQL. Adapt table and SQL dialect to the chosen BI warehouse.

-- Booking success rate
SELECT
  COUNT(CASE WHEN status = 'succeeded' THEN 1 END) * 1.0
    / NULLIF(COUNT(*), 0) AS booking_success_rate
FROM fact_booking
WHERE booking_submitted_at >= :start_date
  AND booking_submitted_at < :end_date;

-- Notification delivery rate
SELECT
  COUNT(CASE WHEN status = 'delivered' THEN 1 END) * 1.0
    / NULLIF(COUNT(CASE WHEN status IN ('sent','delivered','failed') THEN 1 END), 0)
    AS notification_delivery_rate
FROM fact_notification
WHERE sent_at >= :start_date
  AND sent_at < :end_date;

-- Exception resolution time
SELECT
  AVG(EXTRACT(EPOCH FROM (resolved_at - created_at)) / 3600.0)
    AS avg_resolution_hours
FROM fact_exception
WHERE resolved_at IS NOT NULL
  AND created_at >= :start_date
  AND created_at < :end_date;

-- Critical unresolved exceptions
SELECT COUNT(*) AS critical_unresolved
FROM fact_exception
WHERE severity = 'critical'
  AND status <> 'resolved'
  AND created_at < :cutoff_time;

-- Search-to-book conversion
SELECT
  COUNT(DISTINCT CASE WHEN event_name = 'booking_succeeded' THEN session_id END) * 1.0
    / NULLIF(
        COUNT(DISTINCT CASE WHEN event_name = 'provider_search_started' THEN session_id END),
        0
      ) AS search_to_book_conversion
FROM fact_product_event
WHERE occurred_at >= :start_date
  AND occurred_at < :end_date;
