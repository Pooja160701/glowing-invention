from typing import Any
import json
import boto3

REGION = "ap-south-1"


def _statement_is_wildcard(statement: dict[str, Any]) -> bool:
    actions = statement.get("Action", statement.get("NotAction"))
    resources = statement.get("Resource", statement.get("NotResource"))
    if isinstance(actions, str):
        actions = [actions]
    if isinstance(resources, str):
        resources = [resources]
    return actions == ["*"] and resources == ["*"]


def analyze_iam_risks(region_name: str = REGION) -> dict[str, Any]:
    iam = boto3.client("iam", region_name=region_name)
    risks: list[dict[str, Any]] = []
    checked_roles = 0

    roles = iam.list_roles(MaxItems=100).get("Roles", [])
    for role in roles:
        checked_roles += 1
        role_name = role.get("RoleName")
        arn = role.get("Arn")
        findings = []

        attached = iam.list_attached_role_policies(RoleName=role_name).get("AttachedPolicies", [])
        for policy in attached:
            name = policy.get("PolicyName", "")
            arn_policy = policy.get("PolicyArn", "")
            if name == "AdministratorAccess" or name.endswith("FullAccess"):
                findings.append({
                    "title": f"Broad managed policy attached: {name}",
                    "severity": "high",
                    "reason": "Managed policy grants broad administrative or full-service access.",
                    "policy": name,
                })
            if arn_policy.startswith("arn:aws:iam::aws:policy/"):
                try:
                    meta = iam.get_policy(PolicyArn=arn_policy).get("Policy", {})
                    version_id = meta.get("DefaultVersionId")
                    if version_id:
                        doc = iam.get_policy_version(PolicyArn=arn_policy, VersionId=version_id).get("PolicyVersion", {}).get("Document", {})
                        if isinstance(doc, str):
                            doc = json.loads(doc)
                        statements = doc.get("Statement", []) if isinstance(doc, dict) else []
                        if isinstance(statements, dict):
                            statements = [statements]
                        if any(_statement_is_wildcard(s) for s in statements if isinstance(s, dict)):
                            findings.append({
                                "title": f"Wildcard permissions in {name}",
                                "severity": "critical",
                                "reason": "Policy statement allows all actions on all resources.",
                                "policy": name,
                            })
                except Exception:
                    pass

        inline = iam.list_role_policies(RoleName=role_name).get("PolicyNames", [])
        if inline:
            findings.append({
                "title": f"Inline policies present on {role_name}",
                "severity": "medium",
                "reason": "Inline policies increase policy-management and review complexity.",
                "policy": ", ".join(inline[:5]),
            })

        for finding in findings:
            risk = 90 if finding["severity"] == "critical" else 75 if finding["severity"] == "high" else 55
            risks.append({
                "finding_id": f"IAM-LIVE-{role_name}-{len(risks)+1}",
                "title": finding["title"],
                "severity": finding["severity"],
                "risk_score": risk,
                "source": "iam",
                "asset": {"asset_id": role_name, "asset_type": "iam_role", "resource_arn": arn},
                "status": "new",
                "remediation": "Apply least privilege, remove broad permissions, and review role trust and policy scope.",
                "reason": finding["reason"],
            })

    return {
        "service": "iam",
        "connected": True,
        "roles_checked": checked_roles,
        "total": len(risks),
        "critical": sum(x["severity"] == "critical" for x in risks),
        "high": sum(x["severity"] == "high" for x in risks),
        "items": risks,
    }
