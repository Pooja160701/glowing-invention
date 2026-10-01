variable "aws_region" {
  description = "AWS region used by CloudSentinel"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "CloudSentinel project name"
  type        = string
  default     = "cloudsentinel"
}

variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "Environment must be one of: dev, test, prod."
  }

  default = "dev"
}

variable "owner" {
  description = "Project owner/team"
  type        = string
  default     = "cloudsentinel-security"
}