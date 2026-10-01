output "security_admin_role_arn" {
  description = "Security administrator role ARN"
  value       = aws_iam_role.security_admin.arn
}

output "security_analyst_role_arn" {
  description = "Security analyst role ARN"
  value       = aws_iam_role.security_analyst.arn
}

output "auditor_role_arn" {
  description = "Auditor role ARN"
  value       = aws_iam_role.auditor.arn
}

output "application_workload_role_arn" {
  description = "Application workload role ARN"
  value       = aws_iam_role.application_workload.arn
}

output "cicd_role_arn" {
  description = "CI/CD role ARN"
  value       = aws_iam_role.cicd.arn
}