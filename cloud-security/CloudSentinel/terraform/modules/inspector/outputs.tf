output "inspector_account_id" {
  description = "AWS account monitored by Amazon Inspector"
  value       = data.aws_caller_identity.current.account_id
}

output "inspector_resource_types" {
  description = "Resource types monitored by Amazon Inspector"
  value       = aws_inspector2_enabler.security.resource_types
}