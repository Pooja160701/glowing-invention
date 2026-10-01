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
}


module "security_logging" {
  source = "./modules/security-logging"

  project_name = var.project_name
  environment  = var.environment
  kms_key_arn  = module.kms.security_key_arn
}