# SQLmap Validation

Use SQLmap only after manual testing identifies a credible SQL injection candidate.

## Process
1. Verify the target is localhost.
2. Capture the exact request.
3. Identify the suspected parameter.
4. Run SQLmap with the smallest useful scope.
5. Review results manually.
6. Save sanitized output.
7. Stop when sufficient evidence exists.

Example:
```bash
sqlmap -u "http://localhost:3000/<endpoint>?<parameter>=1" --batch
```

Do not copy the example to a real website without explicit authorization.