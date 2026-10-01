data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

resource "aws_s3_bucket" "security_logs" {
  bucket = "${var.project_name}-${var.environment}-security-logs-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "${var.project_name}-${var.environment}-security-logs"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "CentralizedSecurityLogging"
    ManagedBy   = "Terraform"
  }
}


resource "aws_s3_bucket_versioning" "security_logs" {
  bucket = aws_s3_bucket.security_logs.id

  versioning_configuration {
    status = "Enabled"
  }
}


resource "aws_s3_bucket_server_side_encryption_configuration" "security_logs" {
  bucket = aws_s3_bucket.security_logs.id

  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_arn
      sse_algorithm     = "aws:kms"
    }

    bucket_key_enabled = true
  }
}


resource "aws_s3_bucket_public_access_block" "security_logs" {
  bucket = aws_s3_bucket.security_logs.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}


resource "aws_s3_bucket_ownership_controls" "security_logs" {
  bucket = aws_s3_bucket.security_logs.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}


resource "aws_s3_bucket_policy" "security_logs" {
  bucket = aws_s3_bucket.security_logs.id

  policy = data.aws_iam_policy_document.security_logs.json
}


data "aws_iam_policy_document" "security_logs" {
  statement {
    sid    = "DenyInsecureTransport"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = ["s3:*"]

    resources = [
      aws_s3_bucket.security_logs.arn,
      "${aws_s3_bucket.security_logs.arn}/*"
    ]

    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"

      values = ["false"]
    }
  }

  statement {
    sid    = "DenyUnencryptedObjectUploads"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = ["s3:PutObject"]

    resources = [
      "${aws_s3_bucket.security_logs.arn}/*"
    ]

    condition {
      test     = "StringNotEquals"
      variable = "s3:x-amz-server-side-encryption"

      values = ["aws:kms"]
    }
  }
}