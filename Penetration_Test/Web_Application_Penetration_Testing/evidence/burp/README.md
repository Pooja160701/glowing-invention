# Burp Suite Evidence

Burp Suite was used for manual interception, request inspection, Repeater testing, and controlled validation against the local OWASP Juice Shop target.

## Confirmed Evidence

- `02-burp-http-history.png` — HTTP history showing application/API traffic to `localhost:3000`.
- `03-burp-repeater-baseline.png` — baseline Repeater request/response.
- `09-sqli-login-success.png` — SQL injection validation against `POST /rest/user/login`.
- `21-idor-basket-baseline.png` — baseline basket authorization request.
- `22-idor-other-basket.png` — modified basket identifier returning another basket's data.
- Authentication evidence is stored under the numbered screenshots in `evidence/screenshots/`.

## Testing Pattern

For manual validation, establish a baseline, change one relevant variable, send the request again, and compare the response. This was used for SQL injection and IDOR testing.

## Evidence Handling

Only sanitized screenshots and captures should be committed. Redact JWTs, cookies, passwords, authorization headers, and other secrets before publication. Burp project files containing live session state are not committed.

## Scope

All Burp testing was limited to the local Docker Juice Shop laboratory at `http://localhost:3000`.
