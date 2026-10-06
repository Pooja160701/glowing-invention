# Executive Summary

## Assessment

Web Application Penetration Testing & Vulnerability Assessment

Target: OWASP Juice Shop running in a local Docker laboratory at http://localhost:3000.

## Objective

Assess the deliberately vulnerable application through reconnaissance, manual HTTP testing, automated analysis, controlled validation, evidence collection, and remediation review.

## Confirmed Security Findings

| ID | Finding | Severity | Validation |
|---|---|---|---|
| WEB-001 | SQL Injection / Authentication Bypass | High | Burp Suite + SQLmap |
| WEB-002 | Cross-Site Scripting | Medium | Manual browser validation + Burp evidence |
| WEB-003 | IDOR / Broken Access Control | Medium | Burp baseline vs modified basket ID |
| WEB-004 | Authentication Weakness | High | Laboratory credential authentication |
| WEB-005 | Unauthenticated Application Version Disclosure | Low | Unauthenticated endpoint review |

## Automated Assessment

OWASP ZAP baseline scanning covered 88 URLs and reported 8 WARN, 0 FAIL, and 0 INFO results. The warnings were reviewed as a mixture of hardening observations, informational detections, and items requiring context; they were not blindly promoted to vulnerabilities.

Metasploit Framework was evaluated for applicability. No Juice Shop-specific exploit module was identified, so no unrelated module was executed.

## Highest Priorities

1. Fix SQL injection in the login flow using parameterized queries.
2. Enforce server-side authorization for object/basket access.
3. Strengthen authentication and remove weak/default laboratory credentials before deployment.
4. Apply context-aware output encoding and suitable CSP protections.
5. Minimize unauthenticated information disclosure and harden security headers/configuration.

## Evidence Integrity

Findings are based on testing against the local deliberately vulnerable lab. No production or third-party systems were tested. Screenshots containing tokens or cookies must be sanitized before public GitHub publication.

---