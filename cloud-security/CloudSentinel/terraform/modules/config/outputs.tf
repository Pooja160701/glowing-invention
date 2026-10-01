output "config_recorder_name" {
  description = "AWS Config configuration recorder name"
  value       = aws_config_configuration_recorder.security.name
}

output "config_delivery_channel_name" {
  description = "AWS Config delivery channel name"
  value       = aws_config_delivery_channel.security.name
}

output "config_role_arn" {
  description = "IAM role ARN used by AWS Config"
  value       = aws_iam_role.config.arn
}

output "config_rule_names" {
  description = "CloudSentinel AWS Config compliance rule names"

  value = [
    aws_config_config_rule.s3_public_read_prohibited.name,
    aws_config_config_rule.restricted_ssh.name,
    aws_config_config_rule.encrypted_volumes.name,
    aws_config_config_rule.cloudtrail_enabled.name
  ]
}