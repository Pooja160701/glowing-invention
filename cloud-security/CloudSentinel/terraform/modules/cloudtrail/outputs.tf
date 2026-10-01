output "trail_id" {
  description = "CloudSentinel CloudTrail ID"
  value       = aws_cloudtrail.security.id
}

output "trail_arn" {
  description = "CloudSentinel CloudTrail ARN"
  value       = aws_cloudtrail.security.arn
}

output "trail_name" {
  description = "CloudSentinel CloudTrail name"
  value       = aws_cloudtrail.security.name
}

output "trail_home_region" {
  description = "CloudTrail home region"
  value       = aws_cloudtrail.security.home_region
}