# ADR-001 — Use Asynchronous Processing for Imports

## Status
Accepted

## Context
Financial imports can involve many records and may exceed a comfortable synchronous request duration.

## Decision
Accept imports through the API and process them asynchronously using durable queue-backed workers.

## Consequences
### Positive
- Better user responsiveness
- Retryable processing
- Scalable worker capacity
- Clear operational monitoring

### Trade-offs
- More infrastructure
- Eventual completion
- Additional status management

## Rejected Alternative
Process the entire file synchronously inside the API request.
