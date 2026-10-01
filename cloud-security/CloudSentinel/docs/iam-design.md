# CloudSentinel IAM Design

## Objective

CloudSentinel follows least-privilege IAM principles and separates security
administration, security analysis, auditing, application workloads, and CI/CD.

## Roles

| Role | Purpose |
|---|---|
| Security Admin | Manage CloudSentinel security infrastructure |
| Security Analyst | Investigate security findings |
| Auditor | Read-only compliance and security review |
| Application Workload | Access only application resources |
| CI/CD | Deploy infrastructure through controlled automation |

## Principles

1. Least privilege
2. Role separation
3. No long-lived access keys
4. Temporary credentials where possible
5. Resource-scoped permissions
6. Explicit permissions
7. Auditable access
8. No wildcard administrative policies in production

## Prohibited Pattern

```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}