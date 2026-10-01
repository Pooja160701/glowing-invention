variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "security_logs_bucket_name" {
  description = "S3 bucket used for centralized security logs"
  type        = string
}

variable "kms_key_arn" {
  description = "KMS key used for AWS Config encryption"
  type        = string
}