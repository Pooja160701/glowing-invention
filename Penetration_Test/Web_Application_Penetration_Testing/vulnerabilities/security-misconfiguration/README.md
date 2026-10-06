# Security Misconfiguration / Information Disclosure

## Confirmed Observation
GET /rest/admin/application-version returned HTTP 200 without an authenticated session and disclosed the application version 20.2.0.

This is treated as a low-severity information-disclosure issue. It does not by itself demonstrate administrative access.

## ZAP Configuration Observations
The ZAP baseline scan reported warnings involving CSP, deprecated Feature-Policy, timestamp disclosure, cross-domain configuration, dangerous JavaScript functions, and Cross-Origin-Embedder-Policy.

These are documented as hardening observations unless independently shown to be exploitable.

## FTP Error Observation
A request for an FTP backup-style path returned HTTP 403 with an error message revealing application implementation details. Because access was denied, this is not treated as confirmed sensitive file exposure.

## Evidence
- evidence/screenshots/23-security-misconfiguration-unauthenticated.png
- evidence/screenshots/27-zap-ftp-file-access.png
- evidence/screenshots/25-zap-baseline-scan.png
- evidence/screenshots/26-zap-baseline-report.png

## Remediation
Restrict unnecessary administrative metadata, minimize verbose error details, add appropriate security headers, review cross-origin policy, and avoid exposing implementation details in production errors.