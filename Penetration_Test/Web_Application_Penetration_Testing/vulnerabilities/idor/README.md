# IDOR / Broken Access Control — View Another User's Basket

## Target

OWASP Juice Shop running locally.

```text
http://localhost:3000
```

## Endpoint

```text
GET /rest/basket/{basketId}
```

## Description

The application exposes shopping basket data through a client-controlled basket identifier.

During testing, the authenticated user's basket request was captured using Burp Suite. The basket identifier was then changed to another existing identifier.

The modified request returned basket data belonging to a different basket.

## Testing Method

1. Authenticated normally as a test user.
2. Added a product to the user's basket.
3. Captured the basket API request using Burp Suite.
4. Sent the request to Burp Repeater.
5. Established a baseline response using the authenticated user's basket ID.
6. Changed only the basket identifier.
7. Sent the modified request.
8. Compared the returned data with the baseline.

## Result

The application returned another basket's data without adequately verifying that the authenticated user owned the requested basket.

## Impact

An authenticated attacker may be able to access another user's shopping basket and obtain information about their shopping activity.

## Severity

Medium

## Evidence

- `evidence/screenshots/15-idor-basket-baseline.png`
- `evidence/screenshots/16-idor-other-basket.png`
- `evidence/screenshots/17-idor-challenge-solved.png`

## Remediation

Implement server-side authorization checks for every basket access.

The server should verify that the requested basket belongs to the currently authenticated user before returning its contents.

Do not rely on client-side identifiers or hidden UI controls for authorization.

## VULN-002 — IDOR / Broken Access Control

**Severity:** Medium

**Category:** Broken Access Control

**Endpoint:**

```text
GET /rest/basket/{basketId}
```

### Description

The basket API accepts a client-controlled basket identifier. Testing demonstrated that changing the identifier could expose another basket's information without sufficient server-side ownership validation.

### Impact

An authenticated attacker could potentially view another customer's shopping activity.

### Recommendation

Enforce server-side authorization checks ensuring that the requested basket belongs to the authenticated user.

### Evidence

- `evidence/screenshots/15-idor-basket-baseline.png`
- `evidence/screenshots/16-idor-other-basket.png`
- `evidence/screenshots/17-idor-challenge-solved.png`
```

---