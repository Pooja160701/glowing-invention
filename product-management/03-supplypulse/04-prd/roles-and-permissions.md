# SupplyPulse Roles & Permissions

| Capability | Planner | Procurement | Warehouse/Ops | Leader | Admin | Auditor |
|---|---|---|---|---|---|---|
| View inventory | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| View exceptions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Assign exceptions | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| Resolve exceptions | ✓ | ✓ | ✓ | - | ✓ | - |
| View supplier data | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Approve replenishment | ✓ | ✓ | - | Optional | Configurable | - |
| Edit recommendation | ✓ | ✓ | - | - | Configurable | - |
| Configure rules | - | - | - | - | ✓ | - |
| Configure approval policies | - | - | - | - | ✓ | - |
| Export data | ✓ | ✓ | ✓ | ✓ | ✓ | Configurable |
| View audit trail | Limited | Limited | Limited | ✓ | ✓ | ✓ |
| Manage users/roles | - | - | - | - | ✓ | - |

## Permission principles
1. Default deny.
2. Separate read, write, approve, configure, and administer permissions.
3. Approval permissions should be configurable by organization.
4. High-impact actions should require stronger authorization where policy demands it.
5. Every material action records actor, timestamp, object, previous state, and new state.
