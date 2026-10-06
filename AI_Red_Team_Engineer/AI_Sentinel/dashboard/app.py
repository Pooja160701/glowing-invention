import os
import requests
import streamlit as st

API=os.getenv("AISENTINEL_API_URL","http://localhost:8000")
st.set_page_config(page_title="AI Sentinel",page_icon="🛡️",layout="wide")
st.title("🛡️ AI Sentinel")
st.caption("AI Red Teaming • Agent Security • Supply-Chain Risk")

try:
    summary=requests.get(f"{API}/summary",timeout=5).json()
    risk=summary["risk"]
    cols=st.columns(4)
    cols[0].metric("Overall Risk",risk["score"])
    cols[1].metric("Rating",risk["rating"])
    cols[2].metric("Total Findings",risk["total_findings"])
    cols[3].metric("Critical",risk["counts"].get("critical",0))
    st.subheader("Security Pillars")
    st.json({"Red Team":summary["red_team"],"Supply Chain":summary["supply_chain"]})
except Exception as exc:
    st.warning(f"API unavailable: {exc}")

st.subheader("Run Red-Team Evaluation")
if st.button("Run full suite"):
    st.json(requests.post(f"{API}/redteam/run",json={"target":"demo-model"},timeout=10).json())

st.subheader("Agent Security Test")
with st.form("agent"):
    tool=st.selectbox("Tool",["database","files","shell","web","api"])
    action=st.text_input("Action",value="demo")
    approved=st.checkbox("Human approval granted")
    if st.form_submit_button("Execute"):
        st.json(requests.post(f"{API}/agent/action",json={"tool":tool,"action":action,"approved":approved},timeout=10).json())

st.subheader("Audit Log")
if st.button("Refresh audit"):
    st.json(requests.get(f"{API}/audit",timeout=5).json())
