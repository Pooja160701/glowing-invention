# FinFlow — Developer Handoff

## Handoff Package
- User flow
- Screen specification
- Component states
- Responsive behavior
- Accessibility notes
- Interaction rules
- Analytics events
- Error states

## Required States
Every core component should document:
- Default
- Loading
- Empty
- Success
- Error
- Disabled
- Validation

## Analytics Handoff
Designers should annotate relevant interaction points with canonical event names from `16-analytics/event-taxonomy.csv`.

## Engineering Questions
Before implementation:
- What data is required?
- What happens if data is unavailable?
- What is the loading behavior?
- What is the failure recovery path?
- Which actions require confirmation?
- Which information must be masked?
