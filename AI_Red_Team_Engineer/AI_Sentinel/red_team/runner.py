import json
from pathlib import Path
from core.models import Finding, Severity
from core.risk import aggregate_findings
from .attacks import ATTACKS, LocalMockModel, evaluate

SEV = {s.value: s for s in Severity}

def run_red_team(categories=None, output_path=None):
    selected = [c for c in ATTACKS if not categories or c.category in categories]
    model = LocalMockModel()
    findings, results = [], []
    for case in selected:
        response = model.respond(case.prompt)
        verdict = evaluate(case, response)
        results.append({"case":case.name,"category":case.category,**verdict})
        if not verdict["passed"]:
            findings.append(Finding(title=f"{case.name} vulnerability",category=case.category,severity=SEV[case.severity],
                description=f"The target model failed the {case.category} security control.",
                evidence=response,remediation=case.expected_control,
                score={"critical":90,"high":75,"medium":50,"low":25,"info":0}[case.severity]))
    result={"target":"LocalMockModel","results":results,"findings":[f.model_dump() for f in findings],"summary":aggregate_findings(findings)}
    if output_path:
        path=Path(output_path); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(result,indent=2),encoding="utf-8")
    return result
