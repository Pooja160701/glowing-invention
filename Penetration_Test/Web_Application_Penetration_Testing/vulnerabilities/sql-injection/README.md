# SQL Injection Assessment

## Objective
Determine whether user-controlled input can alter a backend database query.

## Method
1. Identify database-backed parameters.
2. Establish a normal response.
3. Introduce harmless syntax markers.
4. Compare status, content, timing, and errors.
5. Confirm manually.
6. Use SQLmap only against the local lab after identifying a credible candidate.

Example lab structure:
```bash
sqlmap -u "http://localhost:3000/<authorized-endpoint>?id=1" --batch
```

## Evidence
Capture the baseline request, modified request, relevant response, tool output, and impact.

## Remediation
- Use parameterized queries/prepared statements.
- Avoid dynamic SQL from user input.
- Apply database least privilege.
- Add regression tests.

Mapping: OWASP Injection; CWE-89.