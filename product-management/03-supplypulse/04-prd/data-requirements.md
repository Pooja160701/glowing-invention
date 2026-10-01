# SupplyPulse Data Requirements

## Core entities
- Organization
- User
- Role
- SKU
- Product
- Location
- Supplier
- Inventory Position
- Inventory Transaction
- Demand Observation
- Forecast Input
- Purchase Order
- Purchase Order Line
- Expected Receipt
- Lead Time Observation
- Exception
- Recommendation
- Decision
- Approval
- Data Quality Event
- Audit Event

## Required inventory fields
- SKU ID
- location ID
- on-hand quantity
- reserved quantity
- available quantity
- in-transit quantity
- inventory value
- inventory status
- timestamp
- source system
- freshness status

## Required supply fields
- supplier ID
- PO ID
- PO line
- ordered quantity
- expected receipt date
- actual receipt date when available
- lead-time value
- lead-time observation date
- PO status

## Required demand fields
- SKU/location
- observation date
- demand quantity
- forecast quantity where available
- forecast version
- source
- timestamp

## Data-quality rules
At minimum detect:
- missing required keys
- stale records
- duplicate records
- invalid dates
- negative quantities where not allowed
- orphaned supplier/SKU/location references
- inconsistent PO quantities
- impossible receipt dates

## Data lineage
Every decision-critical record should be traceable to:
source system → ingestion time → transformation/version → published record.

## Synthetic data policy
Portfolio datasets used for demos must be clearly labeled synthetic and must not resemble or expose real customer records.
