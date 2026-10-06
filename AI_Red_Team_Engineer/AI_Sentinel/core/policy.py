from dataclasses import dataclass
from .audit import log_event
from .config import KILL_SWITCH
from .models import AgentAction, AuditEvent

@dataclass(frozen=True)
class ToolPolicy:
    permission: str
    risk: str
    requires_approval: bool

POLICIES = {
    "database": ToolPolicy("database.read", "medium", False),
    "files": ToolPolicy("files.read", "low", False),
    "shell": ToolPolicy("shell.execute", "high", True),
    "web": ToolPolicy("web.request", "medium", False),
    "api": ToolPolicy("api.execute", "high", True),
}
ALLOWLIST = frozenset(POLICIES)

def authorize(action: AgentAction) -> tuple[bool, str]:
    if KILL_SWITCH:
        reason = "Kill switch is enabled"
        log_event(AuditEvent(event="agent_action", actor=action.actor, tool=action.tool, action=action.action, decision="DENY", reason=reason))
        return False, reason
    if action.tool not in ALLOWLIST:
        reason = "Tool is not allowlisted"
        log_event(AuditEvent(event="agent_action", actor=action.actor, tool=action.tool, action=action.action, decision="DENY", reason=reason))
        return False, reason
    policy = POLICIES[action.tool]
    if policy.requires_approval and not action.approved:
        reason = f"Approval required for {policy.permission}"
        log_event(AuditEvent(event="agent_action", actor=action.actor, tool=action.tool, action=action.action, decision="APPROVAL_REQUIRED", reason=reason))
        return False, reason
    log_event(AuditEvent(event="agent_action", actor=action.actor, tool=action.tool, action=action.action, decision="ALLOW", reason="Policy checks passed"))
    return True, "Allowed"
