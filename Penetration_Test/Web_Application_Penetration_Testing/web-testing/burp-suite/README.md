# Burp Suite Assessment

Burp Suite is the primary manual testing proxy.

## Workflow
1. Start Burp Suite.
2. Use Burp's temporary browser or configure a test browser proxy.
3. Browse only http://localhost:3000.
4. Review HTTP history.
5. Identify parameters, cookies, API calls, and object identifiers.
6. Send interesting requests to Repeater.
7. Change one variable at a time.
8. Compare baseline and modified responses.
9. Save sanitized evidence for confirmed findings.

## High-Value Tests
- Injection: begin with harmless markers and compare behavior.
- Access control: use two laboratory identities and compare authorization.
- Authentication: review login, session, logout, reset, and rate limiting.
- Configuration: inspect headers, cookies, errors, CORS, and information disclosure.

Never commit live session cookies, passwords, or tokens.