from agent_sandbox.executor import execute
from core.models import AgentAction

def test_shell_requires_approval():
    result=execute(AgentAction(tool="shell",action="echo safe"))
    assert result["decision"]=="BLOCKED"

def test_shell_works_after_approval():
    result=execute(AgentAction(tool="shell",action="echo safe",approved=True))
    assert result["executed"] is True

def test_unknown_tool_is_blocked():
    result=execute(AgentAction(tool="unknown",action="x",approved=True))
    assert result["decision"]=="BLOCKED"
