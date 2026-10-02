# CloudSentinel Frontend

React + Vite security operations dashboard for CloudSentinel.

## Run

```bash
cd cloud-security/CloudSentinel/frontend
npm install
npm run dev
```

Open http://localhost:5173 while the FastAPI backend is running on http://127.0.0.1:8000.

The Vite development server proxies `/api/*` to the backend.

## Views

- Overview: security score, severity/source breakdowns, risk profile and priority alerts
- Findings: searchable normalized finding inventory
- Alerts: searchable response queue
- Integrations: AWS security-service coverage plus credential-safe commercial adapter placeholders
