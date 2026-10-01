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