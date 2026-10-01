# FinFlow — Deployment & CI/CD

## Pipeline

```text
Pull Request
   ↓
Lint / Format
   ↓
Unit Tests
   ↓
Integration Tests
   ↓
Security Scans
   ↓
Build Artifact
   ↓
Deploy Staging
   ↓
Smoke Tests
   ↓
Approval / Release Gate
   ↓
Production
   ↓
Post-Deploy Verification
```

## Branching
- `main`: releasable
- feature branches: short-lived
- pull requests required before merge

## Deployment Principles
- Immutable artifacts
- Environment-specific configuration
- Secrets outside source control
- Automated rollback capability
- Database migration safety

## Release Strategy
Prefer small, reversible releases. Feature flags can separate deployment from user exposure for higher-risk changes.
