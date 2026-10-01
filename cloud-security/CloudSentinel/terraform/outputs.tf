output "aws_account_id" {
  description = "AWS account ID used by CloudSentinel"
  value       = local.account_id
}

output "aws_region" {
  description = "AWS region used by CloudSentinel"
  value       = local.region
}

output "aws_partition" {
  description = "AWS partition"
  value       = local.partition
}

output "project_name" {
  description = "CloudSentinel project name"
  value       = var.project_name
}

output "environment" {
  description = "CloudSentinel environment"
  value       = var.environment
}

output "security_kms_key_id" {
  description = "CloudSentinel security KMS key ID"
  value       = module.kms.security_key_id
}

output "security_kms_key_arn" {
  description = "CloudSentinel security KMS key ARN"
  value       = module.kms.security_key_arn
}

output "security_kms_key_alias" {
  description = "CloudSentinel security KMS key alias"
  value       = module.kms.security_key_alias
}

output "security_logs_bucket" {
  description = "CloudSentinel centralized security logging bucket"
  value       = module.security_logging.security_logs_bucket_id
}

output "security_logs_bucket_arn" {
  description = "CloudSentinel centralized security logging bucket ARN"
  value       = module.security_logging.security_logs_bucket_arn
}

output "cloudtrail_id" {
  description = "CloudSentinel CloudTrail ID"
  value       = module.cloudtrail.trail_id
}

output "cloudtrail_arn" {
  description = "CloudSentinel CloudTrail ARN"
  value       = module.cloudtrail.trail_arn
}

output "cloudtrail_name" {
  description = "CloudSentinel CloudTrail name"
  value       = module.cloudtrail.trail_name
}