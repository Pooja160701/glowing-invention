# CloudSentinel

CloudSentinel is a production-style AWS Cloud Security Posture Management
(CSPM), Cloud Detection and Response, and Compliance platform.

## Project Status

🚧 Under active development

## Objectives

CloudSentinel provides a centralized security platform for:

- AWS security posture monitoring
- Cloud security findings aggregation
- Threat detection
- Vulnerability management
- IAM security analysis
- Configuration compliance
- Sensitive data discovery
- Risk scoring
- Security alerting
- Security operations dashboards
- Cloud security platform integrations

## Technology Stack

### AWS

- IAM
- CloudTrail
- GuardDuty
- Security Hub
- Inspector
- Macie
- KMS
- Secrets Manager
- AWS Config

### Infrastructure

- Terraform
- Docker
- GitHub Actions

### Identity

- Keycloak
- OAuth2
- OpenID Connect
- SAML

### Application

- Python
- FastAPI
- PostgreSQL
- React

### Cloud Security Integrations

- Wiz
- Prisma Cloud / Cortex Cloud
- CrowdStrike Falcon Cloud

Commercial cloud-security integrations will use adapter interfaces and
mock implementations unless real enterprise credentials are configured.

## Architecture

```text
AWS Accounts / Resources
          |
          v
CloudTrail + AWS Config
          |
     +----+----+
     |         |
 GuardDuty   Inspector
     |         |
     +----+----+
          |
        Macie
          |
          v
    Security Hub
          |
          v
Security Event Normalization
          |
     +----+----+
     |         |
 Risk Engine Alert Engine
     |         |
     +----+----+
          |
          v
     Dashboard/API
          |
          v
   Security Operations