output "guardduty_detector_id" {
  description = "GuardDuty detector ID"
  value       = aws_guardduty_detector.security.id
}

output "guardduty_status" {
  description = "GuardDuty detector status"
  value       = aws_guardduty_detector.security.enable
}

output "securityhub_enabled" {
  description = "Whether Security Hub is enabled"
  value       = aws_securityhub_account.security.enable_default_standards
}