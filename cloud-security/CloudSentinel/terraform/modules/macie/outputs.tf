output "macie_status" {
  description = "Amazon Macie account status"
  value       = aws_macie2_account.security.status
}

output "macie_finding_publishing_frequency" {
  description = "Amazon Macie finding publishing frequency"
  value       = aws_macie2_account.security.finding_publishing_frequency
}