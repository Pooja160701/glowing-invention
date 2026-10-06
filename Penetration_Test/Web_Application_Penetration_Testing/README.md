# Web Application Penetration Testing & Vulnerability Assessment

A controlled web application penetration-testing portfolio project using OWASP Juice Shop in a local Docker laboratory.

> Safety: use this project only against the intentionally vulnerable local laboratory. Never point the commands at systems you do not own or have explicit permission to test.

## Tech Stack
Docker | Burp Suite | OWASP ZAP | Nmap | SQLmap | Metasploit | OWASP methodology

## Assessment Architecture
```text
Local Docker Lab
      |
      v
Scope + Rules of Engagement
      |
      v
Reconnaissance
      +---- Nmap
      +---- Application discovery
      |
      v
Burp Suite / OWASP ZAP
      +---- SQL Injection
      +---- XSS
      +---- IDOR / Broken Access Control
      +---- Authentication
      +---- Security Misconfiguration
      |
      v
Controlled Validation
      +---- SQLmap
      +---- Metasploit applicability review
      |
      v
Evidence + Risk Assessment
      |
      v
Remediation Recommendations
      |
      v
Final Report
```

## Laboratory
Target: OWASP Juice Shop running locally at http://localhost:3000.

Start the lab:
```bash
docker compose up -d
```

Stop the lab:
```bash
docker compose down
```

## Confirmed Findings
| ID | Finding | Severity | Primary Validation |
|---|---|---|---|
| WEB-001 | SQL Injection / Authentication Bypass | High | Burp Suite + SQLmap |
| WEB-002 | Cross-Site Scripting | Medium | Manual browser validation + Burp evidence |
| WEB-003 | IDOR / Broken Access Control | Medium | Burp baseline vs modified basket ID |
| WEB-004 | Authentication Weakness | High | Laboratory credential authentication |
| WEB-005 | Unauthenticated Application Version Disclosure | Low | Unauthenticated endpoint review |

## Automated Assessment
OWASP ZAP baseline scanning covered 88 URLs and reported 59 PASS, 8 WARN, 0 FAIL, and 0 INFO. The warnings were reviewed as a mixture of hardening observations, informational detections, and items requiring context; they were not blindly promoted to confirmed vulnerabilities.

Metasploit Framework was evaluated for applicability. No Juice Shop-specific exploit module was identified, so no unrelated module was executed.

SQLmap independently validated the login SQL injection as boolean-based blind injection against the SQLite backend. No database extraction or dumping was performed.

## Repository Structure
```text
Penetration Test/
└── Web Application Penetration Testing/
    ├── README.md
    ├── docker-compose.yml
    ├── scope/
    ├── reconnaissance/
    ├── web-testing/
    ├── vulnerabilities/
    ├── validation/
    ├── evidence/
    ├── reports/
    └── methodology/
```

## Assessment Lifecycle
1. Confirm authorization and target.
2. Discover exposed services.
3. Map routes, parameters, APIs, and trust boundaries.
4. Perform manual vulnerability testing.
5. Use scanners to supplement manual testing.
6. Validate credible findings.
7. Capture sanitized evidence.
8. Rate risk from evidence and impact.
9. Recommend remediation.
10. Document retest requirements.

## Evidence Integrity
Findings are based on actual testing against the local deliberately vulnerable lab. Evidence was organized around the confirmed findings and supporting tool output.

Before public publication, screenshots containing JWTs, session cookies, passwords, authorization headers, or unrelated personal/application data must be sanitized. No production or third-party systems were tested.

## Reports
- `reports/executive-summary.md`
- `reports/vulnerability-report.md`
- `reports/remediation-plan.md`

## Resume Version
**Web Application Penetration Testing & Vulnerability Assessment**

**Tech Stack:** Docker | Burp Suite | OWASP ZAP | Nmap | SQLmap | Metasploit

- Performed controlled penetration testing against a deliberately vulnerable web application, identifying and validating SQL injection, XSS, IDOR/broken access control, authentication weaknesses, and information disclosure using OWASP-aligned testing practices.
- Used Burp Suite, OWASP ZAP, Nmap, SQLmap, and Metasploit for reconnaissance, manual validation, automated analysis, evidence collection, and remediation-focused reporting.
