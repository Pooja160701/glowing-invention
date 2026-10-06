# SQL Injection — Authentication Bypass

## Target
POST /rest/user/login
Local target: http://localhost:3000

## Manual Validation
Burp Suite was used to capture the login request and test a crafted SQL expression in the JSON email parameter.

The vulnerable request returned HTTP 200 and an authenticated administrator identity, demonstrating an authentication bypass condition.

## Independent Validation
SQLmap independently identified the JSON email parameter as injectable and reported boolean-based blind SQL injection against a SQLite backend. It also indicated UNION injection with 13 columns.

SQLmap validation was performed only against the local Juice Shop laboratory. No database extraction or dumping was performed.

## Severity
High

## Evidence
- evidence/screenshots/09-sqli-login-success.png
- evidence/screenshots/28-sqlmap-validation.png
- evidence/scan-results/sqlmap/

## Remediation
Use parameterized/prepared statements for database access, validate input server-side, and add regression tests for authentication-bypass SQL injection cases.