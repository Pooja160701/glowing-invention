from collections import Counter
from .models import Finding, Severity

WEIGHTS = {Severity.CRITICAL:10, Severity.HIGH:7, Severity.MEDIUM:4, Severity.LOW:2, Severity.INFO:0}

def aggregate_findings(findings: list[Finding]) -> dict:
    raw = sum(WEIGHTS[f.severity] for f in findings)
    score = min(100, raw * 3)
    counts = Counter(f.severity.value for f in findings)
    rating = "LOW" if score < 25 else "MEDIUM" if score < 50 else "HIGH" if score < 75 else "CRITICAL"
    return {"score":score, "rating":rating, "counts":dict(counts), "total_findings":len(findings)}
