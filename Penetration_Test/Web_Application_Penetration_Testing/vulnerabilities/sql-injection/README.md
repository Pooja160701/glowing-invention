## Validation

SQL injection was manually validated using Burp Suite against the local OWASP Juice Shop login endpoint.

Endpoint:

POST /rest/user/login

The application accepted a crafted email value and returned an authenticated administrator identity.

The finding was independently validated with SQLmap.

SQLmap identified the `email` JSON parameter as vulnerable to:

- Boolean-based blind SQL injection
- SQLite backend
- JSON POST parameter

SQLmap validation was performed only against the local Juice Shop laboratory environment.

## Evidence

- Burp Suite SQL injection request/response
- SQLmap validation output