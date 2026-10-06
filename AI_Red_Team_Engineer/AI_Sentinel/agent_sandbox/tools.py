from pathlib import Path
import subprocess
from core.config import SANDBOX_ROOT

def database_tool(action: str) -> dict:
    return {"status":"ok","rows":[{"id":1,"name":"demo"}],"action":action}

def files_tool(action: str) -> dict:
    root=SANDBOX_ROOT.resolve()
    target=(root/action).resolve()
    if root not in target.parents and target != root:
        raise PermissionError("Path escapes filesystem sandbox")
    return {"status":"ok","path":str(target.relative_to(root)) if target != root else ".","exists":target.exists()}

def shell_tool(action: str) -> dict:
    if not action.startswith(("echo ","python -c ")):
        raise PermissionError("Shell command is outside the demo-safe command set")
    completed=subprocess.run(action,shell=True,capture_output=True,text=True,timeout=3,check=False)
    return {"status":"ok","returncode":completed.returncode,"stdout":completed.stdout[:2000],"stderr":completed.stderr[:2000]}

def web_tool(action: str) -> dict:
    return {"status":"ok","url":action,"note":"External network execution is simulated in the demo sandbox"}

def api_tool(action: str) -> dict:
    return {"status":"ok","request":action,"note":"External API execution is simulated in the demo sandbox"}
