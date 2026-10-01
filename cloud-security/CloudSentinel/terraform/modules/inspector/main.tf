resource "aws_inspector2_enabler" "security" {
  account_ids    = [data.aws_caller_identity.current.account_id]
  resource_types = ["EC2", "ECR", "LAMBDA"]

  depends_on = [
    data.aws_caller_identity.current
  ]
}

data "aws_caller_identity" "current" {}