data "aws_caller_identity" "current" {}

resource "aws_guardduty_detector" "security" {
  enable = true

  finding_publishing_frequency = "FIFTEEN_MINUTES"

  tags = {
    Name        = "${var.project_name}-${var.environment}-guardduty"
    Project     = var.project_name
    Environment = var.environment
    Purpose     = "ThreatDetection"
    ManagedBy   = "Terraform"
  }
}

resource "aws_securityhub_account" "security" {
  enable_default_standards = true

  auto_enable_controls = true

  control_finding_generator = "SECURITY_CONTROL"

  depends_on = [
    aws_guardduty_detector.security
  ]
}