import React, { useEffect, useMemo, useState } from "react";

const api = async (path, options = {}) => {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  const text = await response.text();
  if (!response.ok) throw new Error(path + " returned " + response.status);
  try { return text ? JSON.parse(text) : {}; }
  catch { throw new Error(path + " returned invalid JSON"); }
};

const asItems = (value) => Array.isArray(value) ? value : (value?.items || value?.results || []);
const n = (value) => new Intl.NumberFormat("en-IN").format(Number(value || 0));

function App() {
  const [data, setData] = useState({ summary: null, alerts: [], findings: [], compliance: null, remediations: [], incidents: [] });
  const [page, setPage] = useState("Overview");
  const [query, setQuery] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const load = async () => {
    setLoading(true);
    try {
      const [summary, alerts, findings, compliance, remediations, incidents] = await Promise.all([
        api("/api/v1/dashboard/summary"),
        api("/api/v1/alerts"),
        api("/api/v1/findings"),
        api("/api/v1/compliance/summary"),
        api("/api/v1/remediation/open"),
        api("/api/v1/incidents"),
      ]);
      setData({ summary, alerts: asItems(alerts), findings: asItems(findings), compliance, remediations: asItems(remediations), incidents: asItems(incidents) });
      setError("");
    } catch (err) {
      console.error(err);
      setError(err.message || "API unavailable");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { load(); }, []);

  const filteredFindings = useMemo(() => data.findings.filter(x => JSON.stringify(x).toLowerCase().includes(query.toLowerCase())), [data.findings, query]);
  const filteredAlerts = useMemo(() => data.alerts.filter(x => JSON.stringify(x).toLowerCase().includes(query.toLowerCase())), [data.alerts, query]);
  const filteredIncidents = useMemo(() => data.incidents.filter(x => JSON.stringify(x).toLowerCase().includes(query.toLowerCase())), [data.incidents, query]);

  const avgRisk = Number(data.summary?.risk?.average_finding_risk || 0);
  const score = Math.max(0, Math.round(100 - avgRisk));

  return (
    <div className="app">
      <aside>
        <div className="logo">◆</div>
        <h2>CloudSentinel</h2>
        <small>Security Operations</small>
        <nav>
          {["Overview", "Findings", "Alerts", "Compliance", "Incidents", "Integrations"].map(item =>
            <button key={item} className={page === item ? "active" : ""} onClick={() => setPage(item)}>{item}</button>
          )}
        </nav>
        <footer><span>● Platform healthy</span><br/><span>AWS • ap-south-1</span></footer>
      </aside>

      <main>
        <header>
          <div>Cloud Security / <b>{page}</b></div>
          <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search..." />
          <button onClick={load} title="Refresh">↻</button>
        </header>

        {error && <div className="error"><strong>Backend error</strong><div>{error}</div></div>}

        {loading ? (
          <section><p className="eyebrow">CLOUDSENTINEL</p><h1>Loading security console...</h1></section>
        ) : page === "Overview" ? (
          <Overview data={data} score={score} />
        ) : page === "Findings" ? (
          <Findings rows={filteredFindings} remediations={data.remediations} />
        ) : page === "Alerts" ? (
          <Listing title="Alerts" rows={filteredAlerts} />
        ) : page === "Compliance" ? (
          <Compliance data={data.compliance} />
        ) : page === "Incidents" ? (
          <Incidents rows={filteredIncidents} reload={load} />
        ) : (
          <Integrations />
        )}
      </main>
    </div>
  );
}

function Overview({ data, score }) {
  const s = data.summary || {};
  const severity = s.findings?.by_severity || {};
  const sources = s.findings?.by_source || {};
  const c = s.compliance || {};
  const i = s.incidents || {};

  return <section>
    <p className="eyebrow">SECURITY POSTURE</p>
    <h1>Cloud security overview</h1>
    <p className="muted">Live AWS security visibility, compliance and incident response.</p>

    <div className="cards">
      <Card title="Security Score" value={score} hint="out of 100" />
      <Card title="Critical Findings" value={s.findings?.critical} hint="current" />
      <Card title="Compliance" value={c.score == null ? "—" : c.score + "%"} hint="AWS baseline" />
      <Card title="Open Incidents" value={i.open || 0} hint="response workflow" />
    </div>

    <div className="grid">
      <Panel title="Findings by severity"><Bars data={severity}/></Panel>
      <Panel title="Findings by source"><Bars data={sources}/></Panel>
    </div>

    <div className="grid">
      <Panel title="Risk profile">
        <div className="big">{Number(s.risk?.average_finding_risk || 0).toFixed(1)}<small>/100 average risk</small></div>
        <div className="track"><i style={{width: Math.min(100, Number(s.risk?.average_finding_risk || 0)) + "%"}}/></div>
        <p className="muted">Maximum risk: <b>{s.risk?.max_finding_risk || 0}</b></p>
      </Panel>
      <Panel title="Compliance posture">
        <div className="big">{c.score || 0}<small>/100 baseline score</small></div>
        <p className="muted">Compliant: <b>{c.compliant || 0}</b> · Non-compliant: <b>{c.non_compliant || 0}</b> · Not evaluated: <b>{c.not_evaluated || 0}</b></p>
      </Panel>
    </div>

    <Panel title="Priority alerts"><Table rows={data.alerts.slice(0, 5)}/></Panel>
  </section>;
}

function Findings({ rows, remediations }) {
  const recommendations = Object.fromEntries(remediations.map(x => [x.finding_id, x.action]));
  return <section>
    <p className="eyebrow">EXPOSURE INVENTORY</p><h1>Findings & remediation</h1>
    <p className="muted">Normalized findings with actionable remediation guidance.</p>
    <div className="panel"><div className="table">
      <div className="thead finding-head"><span>Finding</span><span>Source</span><span>Severity</span><span>Risk</span><span>Recommended action</span></div>
      {rows.map((x, idx) => <div className="tr finding-row" key={x.finding_id || idx}>
        <span><b>{x.title || "Untitled"}</b><small>{x.finding_id}</small></span>
        <span>{x.source}</span><span className={"sev " + x.severity}>{x.severity}</span>
        <span>{Number(x.risk_score || 0).toFixed(0)}</span>
        <span className="recommendation">{recommendations[x.finding_id] || "Review finding and apply least-privilege remediation."}</span>
      </div>)}
    </div></div>
  </section>;
}

function Compliance({ data }) {
  if (!data) return <section><h1>Compliance</h1><p className="muted">No compliance data.</p></section>;
  return <section>
    <p className="eyebrow">CONTROL ASSURANCE</p><h1>Compliance posture</h1>
    <p className="muted">CloudSentinel AWS Security Baseline control evaluation from normalized finding evidence.</p>
    <div className="cards">
      <Card title="Score" value={data.score + "%"} hint="evaluated controls" />
      <Card title="Compliant" value={data.compliant} hint="controls" />
      <Card title="Non-compliant" value={data.non_compliant} hint="controls" />
      <Card title="Not evaluated" value={data.not_evaluated} hint="controls" />
    </div>
    <div className="panel"><div className="table">
      <div className="thead"><span>Control</span><span>Framework</span><span>Status</span><span>Evidence</span></div>
      {data.controls.map(c => <div className="tr" key={c.control_id}>
        <span><b>{c.name}</b><small>{c.control_id}</small></span><span>{c.framework}</span>
        <span className={"sev " + (c.status === "compliant" ? "low" : c.status === "non_compliant" ? "critical" : "medium")}>{c.status.replace("_"," ")}</span>
        <span>{c.evidence_count}</span>
      </div>)}
    </div></div>
  </section>;
}

function Incidents({ rows, reload }) {
  const advance = async (incident, target) => {
    try {
      await api("/api/v1/incidents/" + incident.incident_id + "/status", {
        method: "PATCH",
        body: JSON.stringify({status: target, actor: "analyst", note: "Moved incident to " + target + "."})
      });
      await reload();
    } catch (e) { alert(e.message); }
  };

  return <section>
    <p className="eyebrow">INCIDENT RESPONSE</p><h1>Incident lifecycle</h1>
    <p className="muted">Track incidents from open → investigation → containment → resolution → closure.</p>
    {!rows.length ? <div className="panel"><p className="muted">No incidents yet. Create one from a critical alert through the API.</p></div> :
      rows.map(i => <div className="panel incident" key={i.incident_id}>
        <div className="incident-top"><div><h3>{i.title}</h3><small>{i.incident_id} · {i.priority} · {i.severity}</small></div><span className={"sev " + (i.status === "closed" || i.status === "resolved" ? "low" : "high")}>{i.status}</span></div>
        <p className="muted">{i.description}</p>
        <div className="lifecycle">{["open","investigating","contained","resolved","closed"].map(s =>
          <span className={i.status === s ? "current" : ""} key={s}>{s}</span>
        )}</div>
        <div className="incident-actions">
          {i.status === "open" && <button onClick={() => advance(i,"investigating")}>Start investigation</button>}
          {i.status === "investigating" && <button onClick={() => advance(i,"contained")}>Mark contained</button>}
          {i.status === "contained" && <button onClick={() => advance(i,"resolved")}>Resolve</button>}
          {i.status === "resolved" && <button onClick={() => advance(i,"closed")}>Close incident</button>}
        </div>
        <small className="muted">Timeline events: {i.events?.length || 0}</small>
      </div>)}
  </section>;
}

function Card({title,value,hint}) { return <div className="card"><small>{title}</small><strong>{value == null ? "—" : value}</strong><span>{hint}</span></div>; }
function Panel({title,children}) { return <div className="panel"><h3>{title}</h3>{children}</div>; }
function Bars({data}) {
  const entries=Object.entries(data||{}); const max=Math.max(...entries.map(([,v])=>Number(v)||0),1);
  if(!entries.length) return <p className="muted">No data available.</p>;
  return <div>{entries.map(([k,v])=><div className="bar" key={k}><span>{k.replace(/_/g," ")}</span><b>{n(v)}</b><i><em style={{width: Number(v)/max*100 + "%"}}/></i></div>)}</div>;
}
function Table({rows}) {
  if(!rows.length) return <p className="muted">No records available.</p>;
  return <div className="table"><div className="thead"><span>Title</span><span>Source</span><span>Severity</span><span>Risk</span></div>
    {rows.map((x,i)=><div className="tr" key={x.finding_id||x.alert_id||i}><span><b>{x.title||x.rule_name||"Untitled"}</b><small>{x.finding_id||x.alert_id}</small></span><span>{x.source||"—"}</span><span className={"sev " + (x.severity||"low")}>{x.severity||"—"}</span><span>{Number(x.risk_score||0).toFixed(0)}</span></div>)}
  </div>;
}
function Listing({title,rows}) { return <section><p className="eyebrow">RESPONSE CENTER</p><h1>{title}</h1><p className="muted">Search and review CloudSentinel records.</p><div className="panel"><Table rows={rows}/></div></section>; }
function Integrations() {
  const aws=["GuardDuty","Security Hub","Inspector","Macie","AWS Config","CloudTrail","IAM"];
  return <section><p className="eyebrow">CONNECTIVITY</p><h1>Integrations</h1><p className="muted">AWS service coverage and normalized finding intake.</p>
    <div className="integrations">{aws.map(x=><div className="integration" key={x}><b>{x}</b><span>● Connected</span></div>)}</div>
    <div className="panel" style={{marginTop:14}}><h3>Commercial adapters</h3><div className="integrations">{["Wiz","Prisma Cloud / Cortex Cloud","CrowdStrike Falcon Cloud"].map(x=><div className="integration" key={x}><b>{x}</b><small>Mock adapter • credential-safe</small></div>)}</div></div>
  </section>;
}
export default App;
