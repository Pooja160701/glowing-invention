resource "aws_macie2_account" "security" {
  status = "ENABLED"

  finding_publishing_frequency = "FIFTEEN_MINUTES"
}