# app.py

import streamlit as st

from simulator import get_current_incident, get_system_state
from tools import (
    check_logs,
    check_metrics,
    check_database,
    restart_service,
    verify_health,
    get_action_history
)


st.set_page_config(
    page_title="AI Incident Response Agent",
    page_icon="🚨",
    layout="wide"
)


st.title("🚨 AI Incident Response & Learning Agent")

st.write(
    "Simulated incident-response environment"
)


# --------------------------------------------------
# INCIDENT INFORMATION
# --------------------------------------------------

incident = get_current_incident()
system_state = get_system_state()


st.header("Current Incident")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Incident", incident["incident_id"])

with col2:
    st.metric("Service", incident["service"])

with col3:
    st.metric("Status Code", incident["status_code"])

with col4:
    st.metric("Severity", incident["severity"])


st.write(
    f"**Description:** {incident['description']}"
)


# --------------------------------------------------
# SYSTEM STATE
# --------------------------------------------------

st.header("System State")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "API Status",
        system_state["api_status"]
    )

with col2:
    st.metric(
        "DB Connections",
        system_state["database_connections"]
    )

with col3:
    st.metric(
        "CPU Usage",
        system_state["cpu_usage"]
    )

with col4:
    st.metric(
        "Memory",
        system_state["memory_usage"]
    )


# --------------------------------------------------
# INVESTIGATION TOOLS
# --------------------------------------------------

st.header("Investigation Tools")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🔍 Check Logs"):
        result = check_logs()
        st.info(result)


with col2:

    if st.button("📊 Check Metrics"):
        result = check_metrics()
        st.info(result)


with col3:

    if st.button("🗄️ Check Database"):
        result = check_database()
        st.info(result)


col1, col2 = st.columns(2)

with col1:

    if st.button("🔄 Restart Service"):
        result = restart_service()
        st.success(result)


with col2:

    if st.button("❤️ Verify Health"):
        result = verify_health()
        st.success(result)


# --------------------------------------------------
# ACTION HISTORY
# --------------------------------------------------

st.header("Investigation Timeline")

history = get_action_history()


if history:

    for index, action in enumerate(history, start=1):

        st.write(
            f"**{index}. {action['action']}**"
        )

        st.caption(
            action["result"]
        )

else:

    st.info(
        "No investigation actions performed yet."
    )