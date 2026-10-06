# Rules of Engagement

1. Test only the local deliberately vulnerable Juice Shop target.
2. Verify the target before active scanning.
3. Prefer controlled and non-destructive validation.
4. Do not test unrelated hosts discovered during reconnaissance.
5. Use only laboratory accounts and data.
6. Stop if testing causes instability.
7. Do not perform denial-of-service, persistence, malware deployment, or lateral movement.
8. Do not dump or unnecessarily extract application data.
9. Sanitize tokens, passwords, cookies, and personal data before committing evidence.
10. Record enough information for another tester to reproduce each finding.
11. Remove the lab container when the assessment is complete.

## Evidence Policy
Screenshots and HTTP captures must contain no live secrets. Replace JWTs, cookies, passwords, authorization headers, and other sensitive values with [REDACTED] before publication.

## Validation Policy
An automated scanner result is treated as a lead, not a confirmed vulnerability. Manual review is required before inclusion in the final finding register.