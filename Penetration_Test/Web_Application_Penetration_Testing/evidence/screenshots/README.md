# Screenshot Evidence

## Final Evidence Set

The numbered screenshots document the assessment from target startup through manual and automated validation.

### Core Evidence

- 01 — Juice Shop running locally
- 02 — Burp HTTP history
- 03 — Burp Repeater baseline
- 04–07 — SQL injection exploratory requests/responses
- 08–10 — SQL injection login validation
- 11–14 — XSS validation
- 18–20 — authentication validation
- 21–22 — final IDOR baseline and unauthorized basket access
- 23 — unauthenticated application-version disclosure
- 24 — application-configuration response retained as a supplementary observation
- 25–27 — ZAP scan and FTP/error observation
- 28 — SQLmap validation
- 29 — Metasploit module applicability review

### Evidence Policy

Only evidence that supports an actual tested result is included in the final set. Earlier duplicate IDOR screenshots were removed in favor of the clearer 21–22 pair.

## Publication Rules

Before public publication:
- Redact JWTs and session cookies.
- Redact passwords and authorization headers.
- Remove unrelated personal/application data.
- Keep enough request/response context to reproduce the finding.

Evidence must reflect actual testing; screenshots must never be fabricated or edited in a way that changes the underlying result.

---