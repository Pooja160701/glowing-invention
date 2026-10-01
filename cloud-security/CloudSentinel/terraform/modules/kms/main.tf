data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

resource "aws_kms_key" "security" {
  description             = "CloudSentinel security encryption key"
  enable_key_rotation     = true
  deletion_window_in_days = 30

  policy = data.aws_iam_policy_document.security_key.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-security-key"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "CloudSecurity"
    ManagedBy   = "Terraform"
  }
}

resource "aws_kms_alias" "security" {
  name          = "alias/${var.project_name}-${var.environment}-security"
  target_key_id = aws_kms_key.security.key_id
}


data "aws_iam_policy_document" "security_key" {
  statement {
    sid    = "EnableAccountRootPermissions"
    effect = "Allow"

    principals {
      type = "AWS"

      identifiers = [
        "arn:${data.aws_partition.current.partition}:iam::${data.aws_caller_identity.current.account_id}:root"
      ]
    }

    actions   = ["kms:*"]
    resources = ["*"]
  }

  statement {
    sid    = "AllowSecurityServicesToEncrypt"
    effect = "Allow"

    principals {
      type = "Service"

      identifiers = [
        "cloudtrail.amazonaws.com"
      ]
    }

    actions = [
      "kms:GenerateDataKey*",
      "kms:DescribeKey"
    ]

    resources = ["*"]

    condition {
      test     = "StringEquals"
      variable = "aws:SourceAccount"

      values = [
        data.aws_caller_identity.current.account_id
      ]
    }
  }

  statement {
    sid    = "AllowSecurityServicesToDecrypt"
    effect = "Allow"

    principals {
      type = "Service"

      identifiers = [
        "cloudtrail.amazonaws.com"
      ]
    }

    actions = [
      "kms:Decrypt",
      "kms:DescribeKey"
    ]

    resources = ["*"]

    condition {
      test     = "StringEquals"
      variable = "aws:SourceAccount"

      values = [
        data.aws_caller_identity.current.account_id
      ]
    }
  }
}