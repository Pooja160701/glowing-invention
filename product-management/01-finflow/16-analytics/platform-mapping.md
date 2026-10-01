# FinFlow — Analytics Platform Mapping

## GA4
Track acquisition and high-level product events. Recommended dimensions include platform, acquisition source, campaign, and product version.

## Mixpanel
Use for user-level funnels, cohorts, behavioral segmentation, and retention.

## Amplitude
Use for journey analysis, behavioral cohorts, path exploration, and product decision support.

## PostHog
Use for product analytics plus feature flags and experiment instrumentation. Session replay should exclude sensitive financial fields.

## Hotjar
Use heatmaps, recordings, and qualitative feedback to identify UX friction. Financial screens require aggressive masking/exclusion.

## FullStory
Use session replay and interaction analysis for debugging UX friction. Sensitive financial fields must be excluded or masked.

## Implementation Rule
No platform should receive raw bank credentials, account numbers, raw transaction descriptions, exact balances, exact budget values, or other unnecessary sensitive financial data.
