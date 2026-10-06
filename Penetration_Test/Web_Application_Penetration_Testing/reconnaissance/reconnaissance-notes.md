# Reconnaissance Notes

## Target

- Application: OWASP Juice Shop
- Environment: Local Docker laboratory
- Base URL: http://localhost:3000
- Host: 127.0.0.1

## Service Discovery

Command: nmap -sV -Pn -p 3000 localhost

Observed: TCP/3000 open; Nmap reported service as ppp? and did not confidently identify the application version.

## Application Mapping

Burp HTTP history showed normal Juice Shop traffic including the root page, admin application-version and application-configuration endpoints, product search, languages, login, and basket API requests.

The application-version endpoint disclosed version 20.2.0.

## Recon Observations

- HTTP service available on local port 3000.
- API endpoints are exposed under /rest/.
- User-controlled parameters exist in login, search, and object-identifier requests.
- Administrative information endpoints were observed during mapping.
- Basket identifiers are exposed through the client/API flow and were tested for authorization.
- ZAP later expanded the endpoint inventory to 88 URLs.

## Evidence

- `evidence/scan-results/nmap-localhost.txt`
- `evidence/screenshots/02-burp-http-history.png`
- `evidence/screenshots/03-burp-repeater-baseline.png`
- `evidence/screenshots/25-zap-baseline-scan.png`

All reconnaissance remained inside the local laboratory scope.

---