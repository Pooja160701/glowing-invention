from app.db.models import Finding

def recommend_remediation(finding: Finding) -> dict:
    text = f"{finding.title} {finding.description}".lower()
    ftype = (finding.finding_type or "").lower()
    asset = finding.asset or {}
    asset_id = asset.get("asset_id") or asset.get("resource_arn") or "affected resource"

    if "s3" in text or asset.get("asset_type") == "s3":
        action = "Remove unintended public access and enable S3 Block Public Access."
        steps = [
            "Review the bucket policy and ACL for public principals.",
            "Enable S3 Block Public Access unless public exposure is explicitly required.",
            "Review bucket encryption and logging configuration.",
            "Re-test access and verify the finding is resolved.",
        ]
    elif "ssh" in text or "security group" in text:
        action = "Restrict administrative network access to trusted sources."
        steps = [
            "Remove 0.0.0.0/0 access to TCP/22.",
            "Use a private subnet, VPN, bastion, or SSM Session Manager.",
            "Restrict security-group ingress to approved CIDRs.",
            "Re-run AWS Config and verify the control is compliant.",
        ]
    elif "iam" in text or "privilege" in text or ftype == "identity":
        action = "Reduce permissions to the minimum required by the workload."
        steps = [
            "Review the identity policy and last-accessed information.",
            "Remove wildcard actions or resources that are not required.",
            "Use separate roles for distinct workloads and duties.",
            "Validate the replacement policy with IAM Access Analyzer.",
        ]
    elif "unencrypt" in text or "encryption" in text:
        action = "Enable encryption at rest using an approved KMS key."
        steps = [
            "Identify the affected resource and its data classification.",
            "Enable service-native encryption or customer-managed KMS encryption.",
            "Verify key policy and least-privilege access.",
            "Confirm the compliance control becomes compliant.",
        ]
    elif "secret" in text or "credential" in text or "password" in text or "token" in text:
        action = "Rotate exposed credentials and remove secrets from unsafe locations."
        steps = [
            "Revoke or rotate the affected credential immediately.",
            "Move secrets into AWS Secrets Manager or another approved vault.",
            "Remove credentials from code, logs, images, and configuration files.",
            "Review CloudTrail for unauthorized use and re-test detection.",
        ]
    elif "vulnerab" in text or "cve" in text or "package" in text:
        action = "Patch or replace the vulnerable dependency or image."
        steps = [
            "Confirm the affected package, image, or runtime version.",
            "Apply the vendor security update or rebuild from a patched base image.",
            "Run vulnerability scanning again.",
            "Promote the fixed artifact only after validation.",
        ]
    elif "sensitive" in text or "macie" in text:
        action = "Protect sensitive data with appropriate access controls and encryption."
        steps = [
            "Classify the discovered data and confirm business need.",
            "Restrict bucket and object access using least privilege.",
            "Enable encryption and logging.",
            "Remove unnecessary sensitive data and verify the finding.",
        ]
    elif "cloudtrail" in text or "logging" in text:
        action = "Restore centralized audit logging and validate log delivery."
        steps = [
            "Verify CloudTrail is enabled across required regions.",
            "Confirm log delivery to the protected security bucket.",
            "Enable log file validation and encryption.",
            "Generate a test management event and verify ingestion.",
        ]
    else:
        action = "Investigate the finding, contain exposure, and validate the fix."
        steps = [
            "Confirm the finding and affected resource.",
            "Assess business impact and exposure.",
            "Apply the least-privilege remediation available.",
            "Re-run the relevant AWS security control.",
        ]

    return {
        "finding_id": finding.finding_id,
        "risk_score": finding.risk_score,
        "severity": finding.severity,
        "asset": asset_id,
        "action": action,
        "steps": steps,
        "existing_remediation": finding.remediation,
    }
