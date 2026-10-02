import React, { useEffect, useMemo, useState } from "react";

const api = async (path) => {
  const response = await fetch(path);
  const text = await response.text();
  if (!response.ok) throw new Error(`${path} returned ${response.status}`);
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`${path} returned invalid JSON`);
  }
};

const asItems = (value) => {
  if (Array.isArray(value)) return value;
  if (value && Array.isArray(value.items)) return value.items;
  if (value && Array.isArray(value.results)) return value.results;
  return [];
};

const n = (value) => new Intl.NumberFormat("en-IN").format(Number(value || 0));

function ErrorBoundary({ children }) {
  const [error, setError] = useState(null);

  useEffect(() => {
    const handler = (event) => setError(event.error || new Error(event.message || "Frontend error"));
    window.addEventListener("error", handler);
    return () => window.removeEventListener("error", handler);
  }, []);

  if (error) {
    return (
      <div className="error" style={{ margin: 30, whiteSpace: "pre-wrap" }}>
        <strong>CloudSentinel frontend error</strong>
        <p>{error.message}</p>
        <small>Open the browser DevTools Console for the full error.</small>
      </div>
    );
  }

  return children;
}

function App() {
  const [summary, setSummary] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [findings, setFindings] = useState([]);
  const [page, setPage] = useState("Overview");
  const [query, setQuery] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const load = async () => {
    setLoading(true);
    try {
      const [dashboardData, alertData, findingData] = await Promise.all([
        api("/api/v1/dashboard/summary"),
        api("/api/v1/alerts"),
        api("/api/v1/findings"),
      ]);

      setSummary(dashboardData || {});
      setAlerts(asItems(alertData));
      setFindings(asItems(findingData));
      setError("");
    } catch (err) {
      console.error("CloudSentinel API error:", err);
      setError(err.message || "API unavailable");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, []);

  const filteredFindings = useMemo(
    () =>
      findings.filter((item) =>
        JSON.stringify(item).toLowerCase().includes(query.toLowerCase())
      ),
    [findings, query]
  );

  const filteredAlerts = useMemo(
    () =>
      alerts.filter((item) =>
        JSON.stringify(item).toLowerCase().includes(query.toLowerCase())
      ),
    [alerts, query]
  );

  const severity = summary?.findings?.by_severity || {};
  const sources = summary?.findings?.by_source || {};
  const averageRisk = Number(summary?.risk?.average_finding_risk || 0);
  const score = Math.max(0, Math.round(100 - averageRisk));

  return (
    <div className="app">
      <aside>
        <div className="logo">◆</div>
        <h2>CloudSentinel</h2>
        <small>Security Operations</small>

        <nav>
          {["Overview", "Findings", "Alerts", "Integrations"].map((item) => (
            <button
              key={item}
              className={page === item ? "active" : ""}
              onClick={() => setPage(item)}
            >
              {item}
            </button>
          ))}
        </nav>

        <footer>
          <span>● Platform healthy</span>
          <br />
          <span>AWS • ap-south-1</span>
        </footer>
      </aside>

      <main>
        <header>
          <div>
            Cloud Security / <b>{page}</b>
          </div>

          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search..."
          />

          <button onClick={load} title="Refresh">
            ↻
          </button>
        </header>

        {error && (
          <div className="error">
            <strong>Backend connection error</strong>
            <div>{error}</div>
            <small>
              Confirm FastAPI is running on http://127.0.0.1:8000
            </small>
          </div>
        )}

        {loading ? (
          <section>
            <p className="eyebrow">CLOUDSENTINEL</p>
            <h1>Loading security console...</h1>
            <p className="muted">Connecting to the CloudSentinel API.</p>
          </section>
        ) : page === "Overview" ? (
          <Overview
            summary={summary}
            score={score}
            severity={severity}
            sources={sources}
            alerts={alerts}
          />
        ) : page === "Findings" ? (
          <Listing title="Findings" rows={filteredFindings} finding />
        ) : page === "Alerts" ? (
          <Listing title="Alerts" rows={filteredAlerts} />
        ) : (
          <Integrations />
        )}
      </main>
    </div>
  );
}

function Overview({ summary, score, severity, sources, alerts }) {
  return (
    <section>
      <p className="eyebrow">SECURITY POSTURE</p>
      <h1>Cloud security overview</h1>
      <p className="muted">
        Live AWS security visibility from CloudSentinel.
      </p>

      <div className="cards">
        <Card title="Security Score" value={score} hint="out of 100" />
        <Card
          title="Critical Findings"
          value={summary?.findings?.critical}
          hint="current"
        />
        <Card
          title="High Findings"
          value={summary?.findings?.high}
          hint="current"
        />
        <Card
          title="Open Alerts"
          value={summary?.alerts?.open}
          hint="response queue"
        />
      </div>

      <div className="grid">
        <Panel title="Findings by severity">
          <Bars data={severity} />
        </Panel>

        <Panel title="Findings by source">
          <Bars data={sources} />
        </Panel>
      </div>

      <div className="grid">
        <Panel title="Risk profile">
          <div className="big">
            {average(summary?.risk?.average_finding_risk)}
            <small>/100 average risk</small>
          </div>

          <div className="track">
            <i
              style={{
                width: `${Math.min(100, Math.max(0, Number(summary?.risk?.average_finding_risk || 0)))}%`,
              }}
            />
          </div>

          <p className="muted">
            Maximum risk: <b>{summary?.risk?.max_finding_risk || 0}</b>
          </p>
        </Panel>

        <Panel title="Priority alerts">
          <Table rows={alerts.slice(0, 6)} />
        </Panel>
      </div>
    </section>
  );
}

function average(value) {
  return Number(value || 0).toFixed(1);
}

function Card({ title, value, hint }) {
  return (
    <div className="card">
      <small>{title}</small>
      <strong>{value == null ? "—" : value}</strong>
      <span>{hint}</span>
    </div>
  );
}

function Panel({ title, children }) {
  return (
    <div className="panel">
      <h3>{title}</h3>
      {children}
    </div>
  );
}

function Bars({ data }) {
  const entries = Object.entries(data || {});
  const maximum = Math.max(...entries.map(([, value]) => Number(value) || 0), 1);

  if (!entries.length) {
    return <p className="muted">No data available.</p>;
  }

  return (
    <div>
      {entries.map(([key, value]) => (
        <div className="bar" key={key}>
          <span>{key.replace(/_/g, " ")}</span>
          <b>{n(value)}</b>
          <i>
            <em style={{ width: `${((Number(value) || 0) / maximum) * 100}%` }} />
          </i>
        </div>
      ))}
    </div>
  );
}

function Table({ rows }) {
  if (!rows.length) {
    return <p className="muted">No records available.</p>;
  }

  return (
    <div className="table">
      <div className="thead">
        <span>Title</span>
        <span>Source</span>
        <span>Severity</span>
        <span>Risk</span>
      </div>

      {rows.map((item, index) => (
        <div className="tr" key={item.finding_id || item.alert_id || index}>
          <span>
            <b>{item.title || item.rule_name || "Untitled"}</b>
            <small>{item.finding_id || item.alert_id || "—"}</small>
          </span>
          <span>{item.source || "—"}</span>
          <span className={`sev ${item.severity || "low"}`}>
            {item.severity || "—"}
          </span>
          <span>{Number(item.risk_score || 0).toFixed(0)}</span>
        </div>
      ))}
    </div>
  );
}

function Listing({ title, rows, finding }) {
  return (
    <section>
      <p className="eyebrow">
        {finding ? "EXPOSURE INVENTORY" : "RESPONSE CENTER"}
      </p>
      <h1>{title}</h1>
      <p className="muted">Search and review CloudSentinel records.</p>

      <div className="panel">
        <Table rows={rows} />
      </div>
    </section>
  );
}

function Integrations() {
  const awsServices = [
    "GuardDuty",
    "Security Hub",
    "Inspector",
    "Macie",
    "AWS Config",
    "CloudTrail",
    "IAM",
  ];

  const commercialAdapters = [
    "Wiz",
    "Prisma Cloud / Cortex Cloud",
    "CrowdStrike Falcon Cloud",
  ];

  return (
    <section>
      <p className="eyebrow">CONNECTIVITY</p>
      <h1>Integrations</h1>
      <p className="muted">
        AWS service coverage and normalized finding intake.
      </p>

      <div className="integrations">
        {awsServices.map((name) => (
          <div className="integration" key={name}>
            <b>{name}</b>
            <span>● Connected</span>
          </div>
        ))}
      </div>

      <div className="panel" style={{ marginTop: 14 }}>
        <h3>Commercial adapters</h3>

        <div className="integrations">
          {commercialAdapters.map((name) => (
            <div className="integration" key={name}>
              <b>{name}</b>
              <small>Mock adapter • credential-safe</small>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function CloudSentinel() {
  return (
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  );
}
