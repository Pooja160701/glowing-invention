from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class FindingSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"

class FindingStatus(str, Enum):
    NEW = "new"
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    SUPPRESSED = "suppressed"

class FindingSource(str, Enum):
    GUARDDUTY = "guardduty"
    SECURITY_HUB = "security_hub"
    INSPECTOR = "inspector"
    MACIE = "macie"
    CONFIG = "config"
    IAM = "iam"
    WIZ = "wiz"
    PRISMA = "prisma"
    CORTEX = "cortex"
    CROWDSTRIKE = "crowdstrike"

class FindingType(str, Enum):
    THREAT = "threat"
    VULNERABILITY = "vulnerability"
    MISCONFIGURATION = "misconfiguration"
    SENSITIVE_DATA = "sensitive_data"
    IDENTITY = "identity"
    COMPLIANCE = "compliance"

class AssetType(str, Enum):
    AWS_ACCOUNT = "aws_account"
    EC2 = "ec2"
    S3 = "s3"
    IAM_ROLE = "iam_role"
    IAM_USER = "iam_user"
    IAM_POLICY = "iam_policy"
    ECR = "ecr"
    LAMBDA = "lambda"
    SECURITY_GROUP = "security_group"
    KMS_KEY = "kms_key"
    UNKNOWN = "unknown"

class FindingAsset(BaseModel):
    asset_id: str
    asset_type: AssetType
    region: str | None = None
    account_id: str | None = None
    resource_arn: str | None = None
    asset_name: str | None = None

class FindingRisk(BaseModel):
    severity_score: float = Field(ge=0, le=10)
    asset_criticality: float = Field(ge=0, le=10)
    exploitability: float = Field(ge=0, le=10)
    exposure: float = Field(ge=0, le=10)
    data_sensitivity: float = Field(ge=0, le=10)
    risk_score: float = Field(ge=0, le=100)

class NormalizedFinding(BaseModel):
    finding_id: str
    source_finding_id: str | None = None

    source: FindingSource
    finding_type: FindingType

    title: str
    description: str

    severity: FindingSeverity
    status: FindingStatus = FindingStatus.NEW

    asset: FindingAsset

    risk: FindingRisk

    remediation: str | None = None

    first_seen: datetime
    last_seen: datetime

    tags: list[str] = Field(default_factory=list)

    metadata: dict[str, object] = Field(default_factory=dict)