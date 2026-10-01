# KMS and Centralized Security Logging

## Purpose

CloudSentinel uses a customer-managed AWS KMS key to encrypt centralized
security logs and other security-sensitive data.

## KMS Controls

- Customer-managed KMS key
- Automatic key rotation
- Dedicated CloudSentinel alias
- Explicit key policy
- AWS service access restricted by source account
- 30-day deletion protection window

## Security Logging

Security logs are stored in an S3 bucket with:

- SSE-KMS encryption
- S3 Bucket Keys
- Versioning
- Public access blocked
- Bucket owner enforced
- HTTPS-only access
- Explicit denial of unencrypted object uploads

## Planned Consumers

The bucket will be used by:

- AWS CloudTrail
- AWS Config
- Future security-event archival workflows

## Key Management

The application does not receive unrestricted KMS permissions.

Application workloads will receive only the minimum required permissions,
such as `kms:Decrypt`, against specific keys and through specific AWS services.

## Cost Considerations

AWS KMS customer-managed keys and S3 storage/requests may incur AWS charges.
CloudSentinel therefore keeps the security infrastructure modular so that
resources can be enabled deliberately.

## Future Enhancements

- Key grants
- Separate keys by data classification
- Cross-account security logging
- KMS key administrators
- Key usage monitoring
- CloudTrail monitoring of KMS API activity