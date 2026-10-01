# MediConnect Product FAQ

## What problem does MediConnect solve?

MediConnect reduces friction in administrative healthcare appointment workflows for patients and provider organizations.

## Who is the primary patient user?

The initial patient persona is a time-constrained patient who values reliable availability, simple booking, reminders, and self-service appointment changes.

## Who uses the staff experience?

Clinic coordinators and authorized provider-organization staff use scheduling, appointment, communication, and exception-management workflows.

## Is MediConnect a clinical decision-support product?

No. Clinical diagnosis, treatment recommendations, prescribing, emergency triage, and clinical decision support are outside the MVP boundary.

## What is the North Star metric?

Completed Care Journey Rate (CCJR), an administrative journey-completion metric.

## Why is self-service rescheduling included?

It addresses routine appointment-change friction and can reduce unnecessary staff-mediated workflows.

## How does MediConnect handle privacy?

The product design uses data minimization, role-based access, organization isolation, audit logging, communication preferences, secure transport/storage, and privacy-safe analytics.

Specific legal/compliance requirements depend on deployment geography, organization, architecture, and applicable law.

## Does MediConnect integrate with EHRs?

Integrations are a post-MVP capability in the current roadmap. The architecture is designed to establish clear source-of-truth and synchronization boundaries before integrations are added.

## What happens when a booking fails?

The system must not show a false confirmation. Slot availability is revalidated and booking operations are designed for safe transactional behavior.

## What happens when rescheduling fails?

The original appointment remains active when replacement booking cannot be completed.

## How are notification failures handled?

Delivery state is recorded, and configured operational exceptions can surface failures for staff resolution.

## What data is used for product analytics?

Only approved event properties should be collected. Unnecessary sensitive information must not be placed in product analytics events.

## How should roadmap decisions be made?

Prioritize validated user problems, measurable outcomes, dependencies, privacy/security impact, operational feasibility, and evidence from research or product usage.
