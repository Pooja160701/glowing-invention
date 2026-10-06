# SQLmap Validation

SQLmap was used only to independently validate the manually identified SQL injection in the local Juice Shop login endpoint.

## Target

POST /rest/user/login

JSON parameter: email

Environment: http://localhost:3000

## Validation Command

The scan was executed from the official Parrot SQLmap container against host.docker.internal:3000 with the JSON content type and a controlled invalid password. The HTTP 401 response was explicitly ignored so SQLmap could continue parameter analysis.

## Result

SQLmap v1.10.4 identified the email JSON parameter as injectable and reported:
- Boolean-based blind SQL injection
- SQLite backend
- JSON POST parameter
- UNION injection indication with 13 columns
- 411 HTTP requests during validation

The result independently supports the manual Burp finding. No database extraction or dumping was performed.

## Evidence

- `evidence/screenshots/28-sqlmap-validation.png`
- `evidence/scan-results/sqlmap/`

## Safety

Testing was limited to the local deliberately vulnerable Juice Shop laboratory.

---