resource "aws_secretsmanager_secret" "application" {
  name        = "${var.project_name}/${var.environment}/application"
  description = "CloudSentinel application secrets for the ${var.environment} environment"

  kms_key_id = var.kms_key_arn

  recovery_window_in_days = 7

  tags = {
    Name        = "${var.project_name}-${var.environment}-application-secret"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "ApplicationSecrets"
    ManagedBy   = "Terraform"
  }
}