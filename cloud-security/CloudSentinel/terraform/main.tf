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