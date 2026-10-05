# Cross-Site Scripting Assessment

## Objective
Determine whether attacker-controlled data is rendered as executable browser content.

## Test Areas
- Reflected input
- Stored input
- DOM-based input
- Search fields
- Profile fields
- Reviews/feedback
- URL parameters and fragments

## Safe Validation
Start with a unique non-executing marker:
```text
PENTEST-XSS-MARKER-001
```

If reflected, identify the output context and encoding behavior before performing a controlled proof of concept inside the local lab.

## Remediation
- Context-aware output encoding.
- Safe templating.
- Secure DOM APIs.
- Strict input handling.
- Content Security Policy as defense in depth.

Mapping: OWASP XSS; CWE-79.