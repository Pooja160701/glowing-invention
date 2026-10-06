from pathlib import Path
from supply_chain.scanner import scan_path

def test_scanner_detects_secret(tmp_path: Path):
    sample=tmp_path/"sample.py"
    sample.write_text('API_KEY = "sk-abcdefghijklmnopqrstuvwxyz0123456789"',encoding="utf-8")
    result=scan_path(str(tmp_path))
    assert any(f["severity"]=="critical" for f in result["findings"])

def test_scanner_builds_inventory(tmp_path: Path):
    sample=tmp_path/"model.safetensors"
    sample.write_bytes(b"demo")
    result=scan_path(str(tmp_path))
    assert result["inventory"][0]["class"]=="model"
