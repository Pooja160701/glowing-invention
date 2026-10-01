data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

resource "aws_iam_role" "config" {
  name = "${var.project_name}-${var.environment}-config-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "config.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })

  tags = {
    Name        = "${var.project_name}-${var.environment}-config-role"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "ConfigurationCompliance"
    ManagedBy   = "Terraform"
  }
}

resource "aws_iam_role_policy_attachment" "config" {
  role       = aws_iam_role.config.name
  policy_arn = "arn:${data.aws_partition.current.partition}:iam::aws:policy/service-role/AWS_ConfigRole"
}

resource "aws_config_configuration_recorder" "security" {
  name     = "${var.project_name}-${var.environment}-config-recorder"
  role_arn = aws_iam_role.config.arn

  recording_group {
    all_supported                 = true
    include_global_resource_types = true
  }
}

resource "aws_config_delivery_channel" "security" {
  name           = "${var.project_name}-${var.environment}-config-channel"
  s3_bucket_name = var.security_logs_bucket_name

  s3_key_prefix = "config"

  s3_kms_key_arn = var.kms_key_arn

  depends_on = [
    aws_config_configuration_recorder.security
  ]
}

resource "aws_config_configuration_recorder_status" "security" {
  name       = aws_config_configuration_recorder.security.name
  is_enabled = true

  depends_on = [
    aws_config_delivery_channel.security
  ]
}