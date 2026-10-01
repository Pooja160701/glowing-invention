variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "security_log_bucket_arn" {
  description = "ARN of the security logging bucket"
  type        = string
  default     = ""
}