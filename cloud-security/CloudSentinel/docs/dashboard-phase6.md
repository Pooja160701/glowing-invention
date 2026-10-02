# CloudSentinel Phase 6 — Security Dashboard

Phase 6 expands the dashboard from normalized findings into operational cloud visibility.

## 33. Asset inventory

GET /api/v1/inventory/assets performs read-only AWS discovery for S3 buckets, EC2 instances, IAM roles, IAM users, ECR repositories, Lambda functions, and EC2 security groups. Each asset is enriched with matching CloudSentinel finding evidence when the asset identifier is available.

## 34. Security score

The existing security score remains the primary posture metric. The dashboard also exposes average and maximum finding risk through GET /api/v1/dashboard/summary.

## 35. Findings

Existing normalized findings remain available through GET /api/v1/findings. Filtering supports source, severity, status, finding type, and minimum risk score.

## 36. Vulnerabilities

GET /api/v1/dashboard-data/vulnerabilities groups normalized findings using finding_type=vulnerability. The API returns total, severity counts, source, asset, risk, status, and remediation.

## 37. IAM risks

GET /api/v1/dashboard-data/iam-risks combines persisted identity findings with live read-only IAM analysis. The live analyzer checks roles for AdministratorAccess or broad FullAccess managed policies, wildcard action/resource permissions, and inline policies. This is a portfolio security heuristic, not a replacement for IAM Access Analyzer or enterprise identity governance.

## 38. Config compliance

The existing GET /api/v1/compliance/summary endpoint remains the compliance view. AWS Config non-compliant evaluations are normalized into compliance findings and contribute to the baseline posture.

## 39. CloudTrail activity

GET /api/v1/cloudtrail/events?hours=24&max_results=50 provides sanitized CloudTrail activity. The API removes credential/session-sensitive fields before returning events to the UI.

## 40. Filtering/search

The dashboard search bar filters findings, alerts, and incidents client-side. Findings also support server-side filters through the findings API.

## Dashboard navigation

The UI now contains Overview, Assets, Findings, Vulnerabilities, IAM Risks, CloudTrail, Alerts, Compliance, Incidents, and Integrations.

Dashboard data views are read-only unless an existing RBAC-protected response action is explicitly invoked.

## AWS permissions

For local development, the backend needs read access appropriate to the services being displayed. Use least privilege in production. Never hardcode AWS credentials in the repository.
