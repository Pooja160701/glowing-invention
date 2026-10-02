output "application_secret_arn" {
  description = "ARN of the CloudSentinel application secret"
  value       = aws_secretsmanager_secret.application.arn
}

output "application_secret_name" {
  description = "Name of the CloudSentinel application secret"
  value       = aws_secretsmanager_secret.application.name
}

output "application_secret_kms_key_id" {
  description = "KMS key ID used by the application secret"
  value       = aws_secretsmanager_secret.application.kms_key_id
}