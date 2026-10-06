# OWASP-Aligned Testing Methodology

The assessment uses an OWASP-oriented workflow and adapts it to the deliberately vulnerable Juice Shop laboratory.

## Method

1. Confirm scope and local target.
2. Perform reconnaissance and service enumeration.
3. Map application routes and API requests.
4. Establish normal/baseline behavior.
5. Test authentication and authorization controls.
6. Test input-handling weaknesses.
7. Review security configuration and information disclosure.
8. Use automated tools to support, not replace, manual testing.
9. Independently validate credible findings.
10. Capture sanitized evidence.
11. Document impact, remediation, and retest guidance.

## Tools Used

- Nmap — local service reconnaissance.
- Burp Suite — HTTP interception, Repeater, and manual validation.
- OWASP ZAP — automated baseline/passive analysis.
- SQLmap — independent SQL injection validation.
- Metasploit Framework — module applicability assessment.

## Actual Validation Outcomes

- SQL injection: manually confirmed at `POST /rest/user/login`; independently validated with SQLmap.
- XSS: controlled proof of concept executed in the local Juice Shop application.
- IDOR/broken access control: changing `/rest/basket/{id}` exposed another basket's data.
- Authentication weakness: laboratory admin credentials allowed successful authentication.
- Security configuration: unauthenticated application-version information was exposed; additional ZAP header/configuration observations were reviewed as hardening findings.

## Important Principle

A scanner warning or interesting response is not automatically a vulnerability. Findings are reported only when the observed behavior is supported by evidence and can be explained and reproduced within the authorized lab.
