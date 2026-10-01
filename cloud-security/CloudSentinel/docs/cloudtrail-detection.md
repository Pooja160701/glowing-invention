# CloudTrail Detection

## Purpose

CloudSentinel uses AWS CloudTrail as the audit source for AWS management-plane
activity.

## Current Coverage

The first detection rules focus on security-sensitive API operations including:

- IAM policy changes
- Access key creation
- Login profile creation
- CloudTrail modification
- CloudTrail shutdown
- KMS key changes

## Detection Pipeline

```text
CloudTrail
    |
    v
Raw Event
    |
    v
Event Parser
    |
    v
Normalized Event
    |
    v
Detection Rules
    |
    v
Risk Engine
    |
    v
Finding
    |
    v
Alert / Dashboard
```

## Suspicious Activity

A security-sensitive API operation is not automatically malicious.

## CloudSentinel evaluates:

- identity
- API operation
- resource
- source IP
- region
- MFA context
- temporal behavior
- asset criticality
- exposure
- data sensitivity

before assigning a final risk score.

## Integrity

CloudTrail log file validation is enabled.

AWS provides log-file validation to determine whether delivered log files were modified, deleted, or unchanged after delivery.

AWS documents log-file validation as the mechanism for checking delivered log integrity. 