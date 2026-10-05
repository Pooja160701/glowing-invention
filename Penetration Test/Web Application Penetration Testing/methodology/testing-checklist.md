# Penetration Testing Checklist

## Reconnaissance
- [ ] Confirm authorized target
- [ ] Confirm local lab is running
- [ ] Identify open services
- [ ] Fingerprint technologies
- [ ] Map routes
- [ ] Map API endpoints

## Authentication
- [ ] Login behavior
- [ ] Failed login handling
- [ ] Session cookies
- [ ] Logout invalidation
- [ ] Password reset
- [ ] Rate limiting

## Authorization
- [ ] Horizontal access control
- [ ] Vertical access control
- [ ] Object identifier manipulation
- [ ] API authorization
- [ ] Hidden functionality

## Input Validation
- [ ] SQL injection
- [ ] XSS
- [ ] Command injection indicators
- [ ] Path traversal indicators
- [ ] File upload validation

## Configuration
- [ ] Security headers
- [ ] Cookie flags
- [ ] Error disclosure
- [ ] Debug configuration
- [ ] Unnecessary services
- [ ] CORS

## Reporting
- [ ] Evidence captured
- [ ] Sensitive data redacted
- [ ] Severity justified
- [ ] CWE/OWASP mapping added
- [ ] Remediation documented
- [ ] Retest plan documented