# Metric Definitions

## CCJR

**Definition:** Eligible booked appointments reaching the defined administrative completion state without avoidable scheduling or communication failure.

**Formula:**

Completed eligible appointments without qualifying avoidable failure
÷
Eligible booked appointments

**Owner:** Product

**Cadence:** Weekly

The cohort definition and qualifying failure rules must be versioned.

---

## Booking success rate

**Formula:**

Successful booking transactions ÷ booking submissions

**Owner:** Product + Engineering

**Cadence:** Daily

---

## Search-to-book conversion

**Formula:**

Successful bookings ÷ qualifying search sessions

**Owner:** Product

**Cadence:** Weekly

---

## Self-service change completion

**Formula:**

Successful cancellation/reschedule actions ÷ started self-service change flows

**Owner:** Product

**Cadence:** Weekly

---

## Notification delivery rate

**Formula:**

Delivered notifications ÷ notifications sent

**Owner:** Operations

**Cadence:** Daily

---

## Slot mismatch rate

**Formula:**

Booking attempts using unavailable/stale selected slots ÷ booking attempts

**Owner:** Engineering

**Cadence:** Daily

---

## Duplicate booking rate

**Formula:**

Duplicate booking incidents ÷ successful booking transactions

**Owner:** Engineering

**Cadence:** Daily

---

## Exception resolution time

**Formula:**

Resolution timestamp − creation timestamp

Report median and relevant percentiles.

**Owner:** Operations

**Cadence:** Daily

---

## Core scheduling availability

**Formula:**

Available service time ÷ observed service time

**Owner:** Engineering

**Cadence:** Daily
