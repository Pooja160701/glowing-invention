# Scan Results

This directory contains sanitized reconnaissance and automated-validation output produced during the local Juice Shop assessment.

## Nmap

`nmap-localhost.txt` records service discovery for:

```text
127.0.0.1:3000
3000/tcp open
Service/version identification: ppp? (Nmap could not confidently identify the application service)
```

The scan was performed with:

```bash
nmap -sV -Pn -p 3000 localhost
```

## OWASP ZAP

The ZAP baseline report is stored under `evidence/zap/`.

The completed scan reported 88 URLs, 59 PASS, 8 WARN, 0 FAIL, and 0 INFO. Warnings were reviewed as hardening or information findings rather than automatically treated as exploitable vulnerabilities.

## SQLmap

SQLmap output is stored under:

```text
evidence/scan-results/sqlmap/
```

The local login endpoint was independently validated as injectable through the JSON `email` parameter. SQLmap identified boolean-based blind SQL injection with SQLite as the backend.

## Metasploit

Metasploit Framework was initialized successfully. Searches for Juice Shop, Express, Node, and JavaScript did not identify an applicable Juice Shop exploit module. No unrelated exploit module was executed.

## Evidence Rule

Automated scanner output is supporting evidence. Every security finding must be manually reviewed before being included in the final vulnerability report.
