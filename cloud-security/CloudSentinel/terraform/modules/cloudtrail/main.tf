data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

resource "aws_cloudtrail" "security" {
  name = "${var.project_name}-${var.environment}-security-trail"

  s3_bucket_name = var.security_logs_bucket_name

  s3_key_prefix = "cloudtrail"

  include_global_service_events = true

  is_multi_region_trail = true

  enable_log_file_validation = true

  enable_logging = true

  kms_key_id = var.kms_key_arn

  tags = {
    Name        = "${var.project_name}-${var.environment}-security-trail"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "SecurityAudit"
    ManagedBy   = "Terraform"
  }
}