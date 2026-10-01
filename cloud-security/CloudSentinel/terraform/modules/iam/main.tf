data "aws_caller_identity" "current" {}

data "aws_partition" "current" {}

data "aws_iam_policy_document" "trusted_principal" {
  statement {
    sid    = "AllowCurrentAccount"
    effect = "Allow"

    principals {
      type = "AWS"

      identifiers = [
        data.aws_caller_identity.current.account_id
      ]
    }

    actions = [
      "sts:AssumeRole"
    ]
  }
}

resource "aws_iam_role" "security_admin" {
  name = "${var.project_name}-${var.environment}-security-admin"

  assume_role_policy = data.aws_iam_policy_document.trusted_principal.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-security-admin"
    RoleType    = "SecurityAdmin"
    ManagedBy   = "Terraform"
    Environment = var.environment
  }
}

resource "aws_iam_role" "security_analyst" {
  name = "${var.project_name}-${var.environment}-security-analyst"

  assume_role_policy = data.aws_iam_policy_document.trusted_principal.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-security-analyst"
    RoleType    = "SecurityAnalyst"
    ManagedBy   = "Terraform"
    Environment = var.environment
  }
}

resource "aws_iam_role" "auditor" {
  name = "${var.project_name}-${var.environment}-auditor"

  assume_role_policy = data.aws_iam_policy_document.trusted_principal.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-auditor"
    RoleType    = "Auditor"
    ManagedBy   = "Terraform"
    Environment = var.environment
  }
}

resource "aws_iam_role" "application_workload" {
  name = "${var.project_name}-${var.environment}-application-workload"

  assume_role_policy = data.aws_iam_policy_document.trusted_principal.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-application-workload"
    RoleType    = "ApplicationWorkload"
    ManagedBy   = "Terraform"
    Environment = var.environment
  }
}

resource "aws_iam_role" "cicd" {
  name = "${var.project_name}-${var.environment}-cicd"

  assume_role_policy = data.aws_iam_policy_document.trusted_principal.json

  tags = {
    Name        = "${var.project_name}-${var.environment}-cicd"
    RoleType    = "CICD"
    ManagedBy   = "Terraform"
    Environment = var.environment
  }
}

resource "aws_iam_role_policy" "security_analyst" {
  name = "${var.project_name}-${var.environment}-security-analyst-policy"
  role = aws_iam_role.security_analyst.id

  policy = data.aws_iam_policy_document.security_analyst.json
}

resource "aws_iam_role_policy" "auditor" {
  name = "${var.project_name}-${var.environment}-auditor-policy"
  role = aws_iam_role.auditor.id

  policy = data.aws_iam_policy_document.auditor.json
}

resource "aws_iam_role_policy" "application_workload" {
  name = "${var.project_name}-${var.environment}-application-workload-policy"
  role = aws_iam_role.application_workload.id

  policy = data.aws_iam_policy_document.application_workload.json
}

resource "aws_iam_role_policy" "cicd" {
  name = "${var.project_name}-${var.environment}-cicd-policy"
  role = aws_iam_role.cicd.id

  policy = data.aws_iam_policy_document.cicd.json
}

resource "aws_iam_role_policy_attachment" "security_admin" {
  role       = aws_iam_role.security_admin.name
  policy_arn = "arn:aws:iam::aws:policy/SecurityAudit"
}