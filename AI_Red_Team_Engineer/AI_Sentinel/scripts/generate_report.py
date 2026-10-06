import json
from pathlib import Path
from core.models import Finding
from core.risk import aggregate_findings
from red_team.runner import run_red_team
from supply_chain.scanner import scan_path

rt=run_red_team()
sc=scan_path(".")
findings=[Finding(**x) for x in rt["findings"]+sc["findings"]]
risk=aggregate_findings(findings)
report=f"""# AI Sentinel Security Report

## Executive Summary

Overall risk score: **{risk["score"]}/100**  
Overall rating: **{risk["rating"]}**

## Red-Team
Cases executed: **{len(rt["results"])}**  
Findings: **{rt["summary"]["total_findings"]}**

## Supply Chain
Inventory items: **{len(sc["inventory"])}**  
Findings: **{sc["summary"]["total_findings"]}**

## Severity Counts
```json
{json.dumps(risk["counts"],indent=2)}
```

## Findings
```json
{json.dumps([f.model_dump() for f in findings],indent=2)}
```
"""
Path("reports/AI_Sentinel_Security_Report.md").write_text(report,encoding="utf-8")
print("Report written to reports/AI_Sentinel_Security_Report.md")
