output "security_key_id" {
  description = "CloudSentinel security KMS key ID"
  value       = aws_kms_key.security.key_id
}

output "security_key_arn" {
  description = "CloudSentinel security KMS key ARN"
  value       = aws_kms_key.security.arn
}

output "security_key_alias" {
  description = "CloudSentinel security KMS key alias"
  value       = aws_kms_alias.security.name
}