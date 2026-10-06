# Assessment Scope

## Authorized Target

- Application: OWASP Juice Shop
- Environment: Local Docker laboratory
- Base URL: http://localhost:3000
- Service: TCP/3000 on localhost

## In Scope

- Local HTTP application behavior.
- Routes, API endpoints, parameters, forms, cookies, sessions, and access-control boundaries.
- Nmap service enumeration.
- Burp Suite interception and manual validation.
- OWASP ZAP baseline analysis.
- SQL injection validation with SQLmap.
- Controlled Metasploit module applicability review.
- Security-header, error, and information-disclosure review.
- Evidence collection and remediation analysis.

## Out of Scope

- Public websites or third-party infrastructure.
- Production systems.
- Real credentials or personal information.
- Denial-of-service or destructive testing.
- Persistence, malware, or lateral movement outside the lab.
- Password spraying or credential attacks against real accounts.
- Database dumping or unnecessary data extraction.

## Assessment Goals

1. Identify reproducible security weaknesses.
2. Validate findings with manual evidence and, where useful, an independent tool.
3. Avoid false positives from automated scanners.
4. Produce actionable remediation guidance.
5. Maintain an auditable record of the assessment.

All testing remained within the local laboratory scope.

---