from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]
KILL_SWITCH = os.getenv("AISENTINEL_KILL_SWITCH", "false").lower() == "true"
AUDIT_PATH = Path(os.getenv("AISENTINEL_AUDIT_PATH", str(BASE_DIR / "reports" / "audit.jsonl")))
SANDBOX_ROOT = Path(os.getenv("AISENTINEL_SANDBOX_ROOT", str(BASE_DIR / "sample_targets" / "sandbox")))
AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
