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