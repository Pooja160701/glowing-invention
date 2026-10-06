from core.models import AgentAction
from core.policy import authorize
from .tools import api_tool, database_tool, files_tool, shell_tool, web_tool

TOOLS={"database":database_tool,"files":files_tool,"shell":shell_tool,"web":web_tool,"api":api_tool}

def execute(action: AgentAction) -> dict:
    allowed, reason = authorize(action)
    if not allowed:
        return {"executed":False,"decision":"BLOCKED","reason":reason}
    try:
        return {"executed":True,"decision":"ALLOWED","result":TOOLS[action.tool](action.action)}
    except Exception as exc:
        return {"executed":False,"decision":"ERROR","reason":str(exc)}
