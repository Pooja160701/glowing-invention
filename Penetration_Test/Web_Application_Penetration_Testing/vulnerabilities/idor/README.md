# IDOR / Broken Access Control — Basket Access

## Target

OWASP Juice Shop running locally at http://localhost:3000

## Endpoint

GET /rest/basket/{basketId}

## Description

The basket endpoint accepts a client-controlled basket identifier. During testing, the authenticated user's basket request was captured and the identifier was changed to another existing basket.

The modified request returned another basket's data without sufficient server-side ownership validation.

## Testing Method

1. Authenticate as a laboratory user.
2. Capture the basket request with Burp Suite.
3. Establish a baseline using the user's basket ID.
4. Send the request to Repeater.
5. Change only the basket identifier.
6. Compare the response with the baseline.

## Result

Another basket's data was returned, confirming an authorization control failure.

## Severity

Medium

## Evidence

- `evidence/screenshots/21-idor-basket-baseline.png`
- `evidence/screenshots/22-idor-other-basket.png`

Older duplicate screenshots should not be treated as the primary evidence set.

## Remediation

Enforce server-side authorization on every basket/object request and verify that the requested object belongs to the authenticated user.

---