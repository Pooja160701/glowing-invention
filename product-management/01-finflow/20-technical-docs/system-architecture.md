# FinFlow — System Architecture

## Logical Architecture

```text
Client
  |
  v
API Gateway / Edge
  |
  +--> Authentication
  +--> User/Profile Service
  +--> Transaction Service
  +--> Budget Service
  +--> Goal Service
  +--> Insight Service
  +--> Notification Service
  |
  v
Transactional Database

Import Upload --> Object Storage --> Import Queue --> Import Worker
                                      |
                                      v
                               Categorization
                                      |
                                      v
                               Transaction DB

Product Events --> Analytics Pipeline --> BI / Product Analytics

All services --> Logs / Metrics / Traces --> Observability Platform
```

## Architectural Boundaries

### Synchronous
Used for user-facing reads and small mutations where immediate feedback is appropriate.

### Asynchronous
Used for file imports, bulk processing, categorization jobs, notifications, and analytics pipelines.

## Design Principle
The product should remain usable if a non-critical asynchronous subsystem is temporarily unavailable.
