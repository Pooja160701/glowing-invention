# MediConnect — Analytics Instrumentation

**Status:** Portfolio-ready specification

This layer defines the canonical product analytics contract for MediConnect.

## Goals

- Measure the complete administrative care journey.
- Identify booking and scheduling friction.
- Measure self-service behavior.
- Monitor notification reliability.
- Measure operational exception handling.
- Support privacy-safe product decisions.
- Provide a stable event contract for Mixpanel, Amplitude, PostHog, GA4, and BI tools.

## North Star

**Completed Care Journey Rate (CCJR)**

The percentage of eligible booked appointments reaching the defined administrative completion state without avoidable scheduling or communication failure.

CCJR is an administrative product metric, not a clinical outcome.

## Analytics principles

1. Instrument behavior, not sensitive clinical content.
2. Prefer stable IDs and categorical properties.
3. Never place diagnosis, treatment, clinical notes, or message bodies into analytics events.
4. Keep event names canonical across tools.
5. Validate events before production rollout.
6. Document ownership for every critical event.
