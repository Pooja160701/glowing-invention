from pathlib import Path
import re
from core.models import Finding, Severity
from core.risk import aggregate_findings

SECRET_PATTERNS=[
    (re.compile(r"(?i)(aws_secret_access_key|api[_-]?key|password)\s*[:=]\s*['\"][^'\"]+['\"]"),"Potential hard-coded secret"),
    (re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),"Potential API key"),
]
CONTAINER_FILES={"Dockerfile","docker-compose.yml"}
RISKY_WORDS={"privileged","chmod 777","curl | sh","rm -rf /"}
ARTIFACT_CLASSES={".safetensors":"model",".pt":"model",".pth":"model",".onnx":"model",".csv":"dataset",".parquet":"dataset",".jsonl":"dataset",".txt":"prompt_or_text"}

def classify_artifact(path: Path) -> str:
    name=path.name.lower()
    if name in {"requirements.txt","pyproject.toml","poetry.lock"}: return "dependency_manifest"
    if name in {"dockerfile","docker-compose.yml"}: return "container"
    return ARTIFACT_CLASSES.get(path.suffix.lower(),"source_or_config")

def scan_path(root: str) -> dict:
    base=Path(root)
    if not base.exists(): return {"inventory":[],"findings":[],"summary":aggregate_findings([])}
    findings=[]; inventory=[]
    for path in base.rglob("*"):
        if not path.is_file() or any(part.startswith(".git") for part in path.parts): continue
        rel=str(path.relative_to(base)); inventory.append({"path":rel,"class":classify_artifact(path)})
        try: text=path.read_text(encoding="utf-8",errors="ignore")[:200000]
        except OSError: continue
        for pattern,title in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(Finding(title=title,category="secret_detection",severity=Severity.CRITICAL,
                    description=f"Sensitive material pattern detected in {rel}.",evidence=rel,
                    remediation="Remove secrets, rotate exposed credentials, and use a secret manager.",score=95))
        if path.name in CONTAINER_FILES:
            for word in RISKY_WORDS:
                if word.lower() in text.lower():
                    findings.append(Finding(title=f"Risky container configuration: {word}",category="container",severity=Severity.HIGH,
                        description=f"Potentially dangerous container configuration detected in {rel}.",evidence=word,
                        remediation="Use least privilege, explicit permissions, non-root execution and minimal images.",score=80))
        if path.name == "pyproject.toml":
            for line in text.splitlines():
                stripped=line.strip()
                if stripped and not stripped.startswith("#") and ">=" in stripped and "==" not in stripped:
                    findings.append(Finding(title="Non-pinned dependency range",category="dependency",severity=Severity.LOW,
                        description=f"Dependency is expressed as a range in {rel}.",evidence=stripped,
                        remediation="Use a lockfile or exact production pins.",score=20))
    return {"inventory":inventory,"findings":[f.model_dump() for f in findings],"summary":aggregate_findings(findings)}
