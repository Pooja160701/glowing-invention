# Reconnaissance Notes

## Target Verification
```bash
docker ps
curl -I http://localhost:3000
```

## Nmap
```bash
nmap -sV -Pn -p 3000 localhost
```

Record the actual port, service, version, and observations.

## Application Mapping
Browse the application normally through Burp Suite or OWASP ZAP and build an endpoint inventory.

Prioritize authentication, user/profile functions, search, product/catalog functions, basket/cart, checkout, APIs, and administrative functionality.

## Recon Questions
- What services are exposed?
- What technologies can be identified?
- Which inputs are user controlled?
- Which endpoints require authentication?
- Which endpoints return object identifiers?
- Which security headers are present?