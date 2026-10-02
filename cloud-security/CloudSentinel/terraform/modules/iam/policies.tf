data "aws_iam_policy_document" "security_analyst" {
  statement {
    sid    = "SecurityFindingsReadOnly"
    effect = "Allow"

    actions = [
      "securityhub:Get*",
      "securityhub:Describe*",
      "securityhub:BatchGet*",
      "guardduty:Get*",
      "guardduty:List*",
      "inspector2:Get*",
      "inspector2:List*",
      "macie2:Get*",
      "macie2:List*",
      "config:Describe*",
      "config:Get*"
    ]

    resources = ["*"]
  }

  statement {
    sid    = "CloudTrailReadOnly"
    effect = "Allow"

    actions = [
      "cloudtrail:Describe*",
      "cloudtrail:Get*",
      "cloudtrail:List*",
      "cloudtrail:LookupEvents"
    ]

    resources = ["*"]
  }

  statement {
    sid    = "IAMSecurityReadOnly"
    effect = "Allow"

    actions = [
      "iam:Get*",
      "iam:List*",
      "iam:GenerateCredentialReport",
      "iam:SimulatePrincipalPolicy"
    ]

    resources = ["*"]
  }
}


data "aws_iam_policy_document" "auditor" {
  statement {
    sid    = "SecurityAuditReadOnly"
    effect = "Allow"

    actions = [
      "securityhub:Get*",
      "securityhub:Describe*",
      "guardduty:Get*",
      "guardduty:List*",
      "inspector2:Get*",
      "inspector2:List*",
      "macie2:Get*",
      "macie2:List*",
      "config:Describe*",
      "config:Get*",
      "cloudtrail:Describe*",
      "cloudtrail:Get*",
      "cloudtrail:LookupEvents"
    ]

    resources = ["*"]
  }

  statement {
    sid    = "IAMAuditReadOnly"
    effect = "Allow"

    actions = [
      "iam:Get*",
      "iam:List*",
      "iam:GenerateCredentialReport"
    ]

    resources = ["*"]
  }
}


data "aws_iam_policy_document" "application_workload" {
  statement {
    sid    = "ReadApplicationSecrets"
    effect = "Allow"

    actions = [
      "secretsmanager:GetSecretValue",
      "secretsmanager:DescribeSecret"
    ]

    resources = [
      "arn:aws:secretsmanager:*:*:secret:${var.project_name}/${var.environment}/*"
    ]
  }

  statement {
    sid    = "DecryptApplicationData"
    effect = "Allow"

    actions = [
      "kms:Decrypt"
    ]

    resources = [
      var.security_kms_key_arn
    ]

    condition {
      test     = "StringEquals"
      variable = "kms:ViaService"

      values = [
        "secretsmanager.*.amazonaws.com"
      ]
    }
  }
}


data "aws_iam_policy_document" "cicd" {
  statement {
    sid    = "TerraformRead"
    effect = "Allow"

    actions = [
      "sts:GetCallerIdentity",
      "iam:Get*",
      "iam:List*",
      "s3:Get*",
      "s3:List*"
    ]

    resources = ["*"]
  }
}