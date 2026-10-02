from app.db.models import Finding

CONTROLS = [
    ("CIS-S3-1", "S3 public access protection", "AWS CIS", ("s3", "public", "bucket")),
    ("CIS-IAM-1", "IAM least privilege", "AWS CIS", ("iam", "privilege", "permission", "access key")),
    ("CIS-NET-1", "Restrict public SSH access", "AWS CIS", ("ssh", "security group", "0.0.0.0/0")),
    ("CIS-ENC-1", "Encryption at rest", "AWS CIS", ("unencrypted", "encryption", "encrypted")),
    ("CIS-LOG-1", "CloudTrail audit logging", "AWS CIS", ("cloudtrail", "logging")),
    ("CIS-DATA-1", "Sensitive data protection", "AWS Data Protection", ("sensitive", "macie", "pii")),
    ("CIS-SEC-1", "Secrets protection", "AWS Data Protection", ("secret", "credential", "password", "token")),
    ("CIS-VULN-1", "Vulnerability management", "AWS CIS", ("vulnerability", "cve", "package")),
    ("CIS-DET-1", "Threat detection", "AWS Security", ("guardduty", "malicious", "suspicious", "threat")),
    ("CIS-CFG-1", "Configuration compliance", "AWS CIS", ("config", "compliance", "non_compliant")),
]

def calculate_compliance(findings: list[Finding]) -> dict:
    controls = []
    for control_id, name, framework, keywords in CONTROLS:
        matches = []
        for finding in findings:
            text = " ".join([
                finding.title or "",
                finding.description or "",
                finding.finding_type or "",
                finding.source or "",
                " ".join(finding.tags or []),
            ]).lower()
            if any(keyword.lower() in text for keyword in keywords):
                matches.append(finding)
        open_findings = [
            f for f in matches
            if f.status not in {"resolved", "suppressed"}
        ]
        if not matches:
            status = "not_evaluated"
            rationale = "No matching finding evidence is available for this control."
        elif open_findings:
            status = "non_compliant"
            rationale = f"{len(open_findings)} active finding(s) indicate a control gap."
        else:
            status = "compliant"
            rationale = "Matching findings are resolved or suppressed."
        controls.append({
            "control_id": control_id,
            "name": name,
            "framework": framework,
            "status": status,
            "evidence_count": len(matches),
            "open_findings": len(open_findings),
            "rationale": rationale,
        })

    evaluated = [c for c in controls if c["status"] != "not_evaluated"]
    compliant = sum(c["status"] == "compliant" for c in controls)
    non_compliant = sum(c["status"] == "non_compliant" for c in controls)
    score = round((compliant / len(evaluated)) * 100, 2) if evaluated else 0.0
    return {
        "framework": "CloudSentinel AWS Security Baseline",
        "score": score,
        "compliant": compliant,
        "non_compliant": non_compliant,
        "not_evaluated": len(controls) - len(evaluated),
        "total_controls": len(controls),
        "controls": controls,
    }
