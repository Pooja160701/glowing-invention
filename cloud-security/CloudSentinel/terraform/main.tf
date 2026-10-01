data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "aws_partition" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
  region     = var.aws_region
  partition  = data.aws_partition.current.partition
}

module "iam" {
  source = "./modules/iam"

  project_name = var.project_name
  environment  = var.environment
}

module "kms" {
  source = "./modules/kms"

  project_name = var.project_name
  environment  = var.environment
  aws_region   = var.aws_region
}

module "security_logging" {
  source = "./modules/security-logging"

  project_name    = var.project_name
  environment     = var.environment
  aws_region      = var.aws_region
  kms_key_arn     = module.kms.security_key_arn
  cloudtrail_name = "${var.project_name}-${var.environment}-security-trail"
}

module "cloudtrail" {
  source = "./modules/cloudtrail"

  project_name              = var.project_name
  environment               = var.environment
  aws_region                = var.aws_region
  security_logs_bucket_name = module.security_logging.security_logs_bucket_id
  security_logs_bucket_arn  = module.security_logging.security_logs_bucket_arn
  kms_key_arn               = module.kms.security_key_arn
}

module "security_services" {
  source = "./modules/security-services"

  project_name = var.project_name
  environment  = var.environment
  aws_region   = var.aws_region
}

module "config" {
  source = "./modules/config"

  project_name = var.project_name
  environment  = var.environment
  aws_region   = var.aws_region

  security_logs_bucket_name = module.security_logging.security_logs_bucket_id
  kms_key_arn               = module.kms.security_key_arn
}

module "inspector" {
  source = "./modules/inspector"

  project_name = var.project_name
  environment  = var.environment
  aws_region   = var.aws_region
}