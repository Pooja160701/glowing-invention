# AI Sentinel

**AI Red Teaming, Agent Security & Supply-Chain Risk Platform**

One defensive AI security project combining:
- **Attack:** prompt injection, jailbreaks, data leakage, tool abuse, hallucination, insecure output evaluation.
- **Protect:** agent tool allowlists, least privilege, approval gates, filesystem sandboxing, constrained shell, audit logs, kill switch.
- **Verify:** supply-chain inventory and static checks for models, datasets, prompts, dependencies, agent tools and containers.

## Architecture
```
AI Sentinel
├── Red Team Lab
├── Agent Security Sandbox
└── AI Supply-Chain Scanner
        │
        ▼
 Policy + Risk Engine
        │
        ▼
 Audit Logs + Reports
        │
        ▼
 Dashboard / FastAPI
```

## Safety
Designed for local, authorized testing. Red-team prompts are synthetic. Web/API actions are simulated. Shell execution is restricted to safe demo commands.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Dashboard:
```powershell
streamlit run dashboard/app.py
```

Docker:
```bash
docker compose up --build
```

API: http://localhost:8000  
Swagger: http://localhost:8000/docs  
Dashboard: http://localhost:8501

## CLI
```bash
python -m scripts.run_redteam
python -m scripts.run_agent
python -m scripts.scan_supply_chain
python -m scripts.generate_report
```
