# OWASP ZAP Assessment

ZAP supplements manual testing with passive analysis and controlled automated scanning.

## Workflow
1. Configure the local target.
2. Browse through ZAP.
3. Review Sites and History.
4. Review passive scanner alerts.
5. Run a baseline scan against the local target.
6. Manually verify important alerts.
7. Record false positives separately.

Example:
```bash
zap-baseline.py -t http://localhost:3000 -r zap-report.html
```

An automated alert is not automatically a confirmed vulnerability.