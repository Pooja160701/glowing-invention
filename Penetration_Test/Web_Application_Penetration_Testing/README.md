# Web Application Penetration Testing & Vulnerability Assessment

A controlled web application penetration-testing portfolio project using OWASP Juice Shop in a local Docker laboratory.

> Safety: use this project only against the intentionally vulnerable local laboratory. Never point the commands at systems you do not own or have explicit permission to test.

## Tech Stack
Kali Linux | Burp Suite | OWASP ZAP | Nmap | SQLmap | Metasploit | OWASP methodology | Docker

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
      +---- Metasploit where applicable
      |
      v
Evidence + Risk Assessment
      |
      v
Remediation + Retest
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
10. Retest fixes.

## Reporting Standard
Every confirmed finding should contain the finding title, severity, affected component, OWASP/CWE mapping, prerequisites, reproduction, evidence, impact, remediation, and retest status.

Final vulnerability counts are intentionally not fabricated. Findings become confirmed only after the local lab is actually tested.

## Resume Version
**Web Application Penetration Testing & Vulnerability Assessment**

**Tech Stack:** Kali Linux | Burp Suite | OWASP ZAP | Nmap | SQLmap | Metasploit

- Performed controlled penetration testing against a deliberately vulnerable web application, assessing SQL injection, XSS, IDOR, authentication weaknesses, and security misconfigurations using OWASP-aligned testing practices.
- Used Burp Suite, OWASP ZAP, Nmap, SQLmap, and Metasploit for reconnaissance, validation, evidence collection, and remediation-focused vulnerability reporting.