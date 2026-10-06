from agent_sandbox.executor import execute
from core.models import AgentAction

def test_file_escape_is_blocked_by_tool_boundary():
    result=execute(AgentAction(tool="files",action="../outside.txt"))
    assert result["decision"]=="ERROR"
    assert "escapes filesystem sandbox" in result["reason"]
