# OWASP ZAP Evidence

OWASP ZAP was used against the local Juice Shop instance for controlled automated baseline analysis.

## Scan

Target:

```text
http://host.docker.internal:3000
```

The ZAP container reached the host application through Docker host networking.

The completed baseline scan reported:

- 88 URLs
- 59 PASS
- 8 WARN
- 0 FAIL
- 0 INFO

## Alerts Observed

Warnings included:

- Content Security Policy header not set
- Non-storable content
- Deprecated Feature-Policy header
- Unix timestamp disclosure
- Cross-domain misconfiguration
- Modern web application detection
- Dangerous JavaScript functions
- Cross-Origin-Embedder-Policy missing/invalid

These alerts are not all confirmed vulnerabilities. They require context and manual validation. In particular, the `Modern Web Application` alert is informational, while several header findings are security-hardening observations.

## Stored Evidence

- `zap-baseline-report.html`
- `zap-baseline-report.json`
- `zap.yaml`
- `25-zap-baseline-scan.png`
- `26-zap-baseline-report.png`
- `27-zap-ftp-directory.png`

The FTP screenshot shows a denied request and an error/technology disclosure; it does not by itself prove sensitive file exposure.

## Evidence Handling

Do not publish credentials, cookies, JWTs, or unrelated application data. Automated alerts must be manually classified before being promoted to confirmed findings.
