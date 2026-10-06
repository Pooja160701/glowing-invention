import os
def kill_switch_status() -> bool:
    return os.getenv("AISENTINEL_KILL_SWITCH", "false").lower() == "true"
