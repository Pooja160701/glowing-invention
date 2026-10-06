from fastapi import FastAPI
from agent_sandbox.executor import execute
from core.audit import read_events
from core.models import AgentAction, Finding, RedTeamRequest, SupplyChainRequest
from core.risk import aggregate_findings
from red_team.runner import run_red_team
from supply_chain.scanner import scan_path

app=FastAPI(title="AI Sentinel",version="1.0.0",description="AI red teaming, agent security and supply-chain risk lab.")

@app.get("/")
def root():
    return {"name":"AI Sentinel","status":"ready","modules":["red-team","agent-sandbox","supply-chain"]}

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/redteam/run")
def redteam(req: RedTeamRequest):
    return run_red_team(req.categories)

@app.post("/agent/action")
def agent_action(req: AgentAction):
    return execute(req)

@app.get("/audit")
def audit(limit:int=200):
    return {"events":read_events(limit)}

@app.post("/supply-chain/scan")
def supply_chain(req: SupplyChainRequest):
    return scan_path(req.path)

@app.get("/summary")
def summary():
    rt=run_red_team()
    sc=scan_path(".")
    findings=[Finding(**x) for x in rt["findings"]+sc["findings"]]
    return {"risk":aggregate_findings(findings),"red_team":rt["summary"],"supply_chain":sc["summary"]}
