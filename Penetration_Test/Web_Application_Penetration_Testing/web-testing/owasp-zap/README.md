# OWASP ZAP Assessment

OWASP ZAP was used for automated baseline analysis of the local Juice Shop instance.

## Workflow
1. Start the local Docker target.
2. Run the ZAP baseline scan against the target reachable from the ZAP container.
3. Review the generated HTML and JSON reports.
4. Classify alerts by relevance.
5. Manually verify important observations before reporting them as findings.

## Completed Scan
Target: http://host.docker.internal:3000
Result: 88 URLs, 59 PASS, 8 WARN, 0 FAIL, 0 INFO.

Warnings included CSP, non-storable content, deprecated Feature-Policy, timestamp disclosure, cross-domain configuration, Modern Web Application detection, dangerous JavaScript functions, and COEP configuration.

## Interpretation
The ZAP result is supporting evidence rather than a final vulnerability list. Modern Web Application detection is informational. Header/configuration warnings are treated as hardening observations unless manual testing demonstrates a security impact.

## Stored Evidence
- evidence/zap/zap-baseline-report.html
- evidence/zap/zap-baseline-report.json
- evidence/zap/zap.yaml
- evidence/screenshots/25-zap-baseline-scan.png
- evidence/screenshots/26-zap-baseline-report.png

An automated alert is never automatically treated as a confirmed vulnerability.