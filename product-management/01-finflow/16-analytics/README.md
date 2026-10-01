# FinFlow — Product Analytics

> **Status:** Analytics specification with simulated sample data. No external analytics workspace was connected or modified.

## Analytics Stack

| Tool | Intended Role |
|---|---|
| GA4 | Acquisition, web/app traffic, campaign attribution |
| Mixpanel | Product funnels, cohorts, retention, user actions |
| Amplitude | Behavioral analysis, journeys, retention, experimentation analysis |
| PostHog | Product analytics, feature flags, experiments, session replay specification |
| Hotjar | Qualitative behavior: heatmaps and recordings specification |
| FullStory | Session replay and friction investigation specification |

## North Star Metric
**Weekly Active Financial Action Users (WAFAU)** — unique users who complete at least one meaningful financial action in a rolling seven-day period.

Meaningful actions include budget creation, category correction, goal contribution, insight action, or financial review action.

## Core Funnel
Landing / Install → Sign Up → Import → First Categorized Transactions → Dashboard View → First Financial Action → Week-4 Retention

## Data Principle
The same canonical event names and properties should be used across analytics systems where the platform supports them. Financially sensitive values should not be sent as raw event properties.
