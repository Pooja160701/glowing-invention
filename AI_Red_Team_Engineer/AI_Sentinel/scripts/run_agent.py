import json
from agent_sandbox.executor import execute
from core.models import AgentAction
if __name__=="__main__":
    actions=[AgentAction(tool="database",action="SELECT demo rows"),AgentAction(tool="shell",action="echo hello"),AgentAction(tool="shell",action="echo approved",approved=True),AgentAction(tool="files",action="README.txt")]
    for action in actions: print(json.dumps(execute(action),indent=2))
