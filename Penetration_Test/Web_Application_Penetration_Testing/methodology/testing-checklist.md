# Penetration Testing Checklist

## Scope and Reconnaissance
- [x] Confirm authorized local target
- [x] Confirm Docker lab is running
- [x] Identify exposed service with Nmap
- [x] Review application/API traffic
- [x] Identify technology/application version where exposed

## Burp Suite
- [x] HTTP history reviewed
- [x] Baseline request captured
- [x] Repeater used for controlled comparisons
- [x] SQL injection request validated
- [x] IDOR authorization comparison performed
- [x] Authentication behavior reviewed

## SQL Injection
- [x] Login baseline captured
- [x] Crafted SQLi input tested
- [x] Administrative identity returned by vulnerable login flow
- [x] SQLmap independent validation completed
- [x] No database extraction performed

## Cross-Site Scripting
- [x] Search/input behavior tested
- [x] Controlled XSS proof of concept executed
- [x] Request and execution evidence captured

## Authorization / IDOR
- [x] Basket endpoint identified
- [x] Baseline basket request captured
- [x] Basket identifier changed
- [x] Another basket's data observed

## Authentication
- [x] Failed login behavior observed
- [x] Laboratory admin authentication verified
- [x] Authenticated admin state verified
- [ ] Full password-reset/rate-limit/session-lifecycle assessment not completed

## Configuration
- [x] Nmap service review
- [x] Unauthenticated application-version response reviewed
- [x] ZAP baseline scan completed
- [x] ZAP alerts manually classified
- [ ] All header/cookie hardening areas exhaustively validated

## Metasploit
- [x] Framework initialized
- [x] Juice Shop module search performed
- [x] Generic Express/Node/JavaScript searches reviewed
- [x] No unrelated exploit executed

## Evidence and Reporting
- [x] Screenshots collected
- [ ] Sensitive tokens/cookies must be redacted before publication
- [x] Automated findings manually reviewed
- [x] Remediation documented
- [x] Retest guidance documented
