from typing import Any
import boto3

REGION = "ap-south-1"


def _safe_call(label: str, fn) -> dict[str, Any]:
    try:
        return {"status": "ok", "items": fn()}
    except Exception as exc:
        return {"status": "error", "error": str(exc), "items": []}


def inventory(region_name: str = REGION) -> dict[str, Any]:
    s3 = boto3.client("s3", region_name=region_name)
    ec2 = boto3.client("ec2", region_name=region_name)
    iam = boto3.client("iam", region_name=region_name)
    ecr = boto3.client("ecr", region_name=region_name)
    lam = boto3.client("lambda", region_name=region_name)
    sts = boto3.client("sts", region_name=region_name)

    account_id = None
    try:
        account_id = sts.get_caller_identity().get("Account")
    except Exception:
        pass

    assets = []

    def add(asset_type, asset_id, name=None, region=region_name, arn=None, status="active", metadata=None):
        assets.append({
            "asset_type": asset_type,
            "asset_id": str(asset_id),
            "name": name or str(asset_id),
            "region": region,
            "account_id": account_id,
            "arn": arn,
            "status": status,
            "metadata": metadata or {},
        })

    s3_result = _safe_call("s3", lambda: s3.list_buckets().get("Buckets", []))
    for b in s3_result["items"]:
        add("s3", b.get("Name"), b.get("Name"), region=None, metadata={"creation_date": str(b.get("CreationDate"))})
    ec2_result = _safe_call("ec2", lambda: ec2.describe_instances().get("Reservations", []))
    for reservation in ec2_result["items"]:
        for i in reservation.get("Instances", []):
            add("ec2", i.get("InstanceId"), i.get("InstanceId"), metadata={"state": (i.get("State") or {}).get("Name"), "instance_type": i.get("InstanceType")})
    iam_roles = _safe_call("iam_roles", lambda: iam.list_roles(MaxItems=100).get("Roles", []))
    for r in iam_roles["items"]:
        add("iam_role", r.get("RoleName"), r.get("RoleName"), region=None, arn=r.get("Arn"))
    iam_users = _safe_call("iam_users", lambda: iam.list_users(MaxItems=100).get("Users", []))
    for u in iam_users["items"]:
        add("iam_user", u.get("UserName"), u.get("UserName"), region=None, arn=u.get("Arn"))
    ecr_result = _safe_call("ecr", lambda: ecr.describe_repositories(maxResults=100).get("repositories", []))
    for r in ecr_result["items"]:
        add("ecr", r.get("repositoryName"), r.get("repositoryName"), arn=r.get("repositoryArn"))
    lambda_result = _safe_call("lambda", lambda: lam.list_functions(MaxItems=100).get("Functions", []))
    for f in lambda_result["items"]:
        add("lambda", f.get("FunctionName"), f.get("FunctionName"), arn=f.get("FunctionArn"), metadata={"runtime": f.get("Runtime"), "last_modified": f.get("LastModified")})
    sg_result = _safe_call("security_group", lambda: ec2.describe_security_groups().get("SecurityGroups", []))
    for sg in sg_result["items"]:
        add("security_group", sg.get("GroupId"), sg.get("GroupName"), metadata={"vpc_id": sg.get("VpcId")})

    services = {
        "s3": s3_result["status"],
        "ec2": ec2_result["status"],
        "iam_roles": iam_roles["status"],
        "iam_users": iam_users["status"],
        "ecr": ecr_result["status"],
        "lambda": lambda_result["status"],
        "security_groups": sg_result["status"],
    }
    return {"account_id": account_id, "region": region_name, "asset_count": len(assets), "assets": assets, "services": services}
