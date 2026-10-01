output "security_logs_bucket_id" {
  description = "Security logging S3 bucket name"
  value       = aws_s3_bucket.security_logs.id
}

output "security_logs_bucket_arn" {
  description = "Security logging S3 bucket ARN"
  value       = aws_s3_bucket.security_logs.arn
}