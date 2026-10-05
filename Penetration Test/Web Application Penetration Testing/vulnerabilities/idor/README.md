# IDOR / Broken Access Control Assessment

## Objective
Determine whether a user can access another user's object by changing a user-controlled identifier.

## Method
1. Create or identify an object as User A.
2. Capture the request.
3. Authenticate as User B.
4. Repeat the request.
5. Change only the object identifier.
6. Compare authorization behavior.

Expected secure behavior:
```text
User B -> object owned by User A -> authorization denied
```

## Remediation
Authorization must be enforced server-side for every protected object. Client-side hiding and unpredictable identifiers are not substitutes for authorization checks.

Mapping: OWASP Broken Access Control; CWE-639.