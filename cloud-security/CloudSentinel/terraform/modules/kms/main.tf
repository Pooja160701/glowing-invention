data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

locals {
  cloudtrail_name = "${var.project_name}-${var.environment}-security-trail"

  cloudtrail_arn = "arn:${data.aws_partition.current.partition}:cloudtrail:${var.aws_region}:${data.aws_caller_identity.current.account_id}:trail/${local.cloudtrail_name}"
}


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

    actions = [
      "kms:*"
    ]

    resources = [
      "*"
    ]
  }


  statement {
    sid    = "AllowCloudTrailToEncrypt"
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

    resources = [
      "*"
    ]

    condition {
      test     = "StringEquals"
      variable = "aws:SourceArn"

      values = [
        local.cloudtrail_arn
      ]
    }
  }


  statement {
    sid    = "AllowCloudTrailToDecrypt"
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

    resources = [
      "*"
    ]

    condition {
      test     = "StringEquals"
      variable = "aws:SourceArn"

      values = [
        local.cloudtrail_arn
      ]
    }
  }
}