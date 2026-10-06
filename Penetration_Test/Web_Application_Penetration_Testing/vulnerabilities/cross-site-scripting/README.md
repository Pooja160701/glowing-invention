# Cross-Site Scripting Assessment

## Result

A controlled XSS proof of concept was executed in the local Juice Shop application through the search/input flow. The evidence set contains the baseline, executed alert, resulting page, and Burp request.

## Validation

1. Establish the normal search behavior.
2. Submit a controlled XSS payload in the local lab.
3. Observe browser-side script execution.
4. Capture the request and resulting page.

## Evidence

- `evidence/screenshots/11-xss-search-baseline.png`
- `evidence/screenshots/12-xss-alert.png`
- `evidence/screenshots/13-xss-executed-page.png`
- `evidence/screenshots/14-xss-burp-request.png`

## Severity

Medium

## Remediation

Apply context-aware output encoding, safe DOM APIs, secure templating, strict input handling, and Content Security Policy as defense in depth.

Mapping: CWE-79 / OWASP Cross-Site Scripting.

---