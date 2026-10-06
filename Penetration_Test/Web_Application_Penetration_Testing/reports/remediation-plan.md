# Remediation Plan

| Priority | Finding / Area | Recommended Action | Verification |
|---|---|---|---|
| 1 | WEB-001 SQL Injection | Replace dynamic SQL with parameterized/prepared statements and add injection regression tests | Repeat Burp and SQLmap validation |
| 2 | WEB-003 IDOR | Enforce server-side ownership/authorization checks for every basket/object request | Repeat cross-user object-ID tests |
| 3 | WEB-004 Authentication | Remove weak/default credentials; enforce strong credential policy and appropriate abuse controls | Repeat authentication and session tests |
| 4 | WEB-002 XSS | Use context-aware output encoding, safe DOM APIs, safe templating, and CSP defense in depth | Repeat controlled XSS cases |
| 5 | WEB-005 Information Disclosure | Restrict unnecessary application-version metadata and review administrative endpoint authorization | Repeat unauthenticated endpoint checks |

## ZAP / Configuration Hardening
- Add an appropriate Content-Security-Policy.
- Review Cross-Origin-Embedder-Policy and cross-domain configuration.
- Replace deprecated security headers with current equivalents.
- Review timestamp and server/application information disclosure.
- Review cookie security attributes where sessions are used.
- Treat automated scanner warnings as inputs for manual verification.

## Secure Development Follow-up
- Add security regression tests for all confirmed findings.
- Centralize authorization logic.
- Use parameterized database access throughout the application.
- Add dependency and container scanning to CI/CD.
- Review security headers and cookie attributes as deployment requirements.
- Retest high-risk changes before release.