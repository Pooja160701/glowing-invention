# Burp Suite Assessment

Burp Suite was the primary manual HTTP testing proxy for the local Juice Shop assessment.

## Workflow
1. Start Burp Suite and use the temporary browser or configured test browser.
2. Browse only http://localhost:3000.
3. Review HTTP history.
4. Identify parameters, cookies, API calls, and object identifiers.
5. Send relevant requests to Repeater.
6. Establish a baseline.
7. Change one variable at a time.
8. Compare modified responses with the baseline.
9. Save sanitized evidence for confirmed findings.

## Tests Actually Performed
- HTTP history and endpoint mapping.
- Login request inspection.
- SQL injection validation against POST /rest/user/login.
- IDOR testing against GET /rest/basket/{basketId}.
- Authentication behavior review.
- Application-version/configuration endpoint review.

## Evidence
Primary screenshots are stored under evidence/screenshots/.
Key captures include 02-burp-http-history.png, 03-burp-repeater-baseline.png, 09-sqli-login-success.png, 21-idor-basket-baseline.png, and 22-idor-other-basket.png.

## Security
Never commit live session cookies, JWTs, passwords, authorization headers, or Burp project files containing sensitive session state.