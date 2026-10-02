variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "kms_key_arn" {
  description = "KMS key used to encrypt Secrets Manager secrets"
  type        = string
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}