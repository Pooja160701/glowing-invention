variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "aws_region" {
  description = "AWS region where CloudTrail is managed"
  type        = string
}

variable "security_logs_bucket_name" {
  description = "S3 bucket receiving CloudTrail logs"
  type        = string
}

variable "security_logs_bucket_arn" {
  description = "ARN of the security logging bucket"
  type        = string
}

variable "kms_key_arn" {
  description = "KMS key used for CloudTrail encryption"
  type        = string
}