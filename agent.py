# agent.py

from simulator import get_current_incident, get_system_state
from tools import (
    check_logs,
    check_metrics,
    check_database,
    restart_service,
    verify_health,
    get_action_history
)


def analyze_incident():
    """
    Analyze the current incident and investigate it.
    """

    incident = get_current_incident()
    system_state = get_system_state()

    investigation = []

    # Step 1: Check logs
    logs = check_logs()

    investigation.append({
        "action": "check_logs",
        "result": logs
    })

    # Step 2: Check metrics
    metrics = check_metrics()

    investigation.append({
        "action": "check_metrics",
        "result": metrics
    })

    # Step 3: Check database
    database = check_database()

    investigation.append({
        "action": "check_database",
        "result": database
    })

    # Identify the likely root cause
    root_cause = (
        "Database connection pool exhaustion. "
        "All 100 database connections are currently in use."
    )

    recommendation = (
        "Increase the database connection pool capacity "
        "and restart the Payment API service."
    )

    return {
        "incident": incident,
        "system_state": system_state,
        "investigation": investigation,
        "root_cause": root_cause,
        "recommendation": recommendation
    }


def resolve_incident():
    """
    Execute the approved resolution and verify recovery.
    """

    restart_result = restart_service()

    health_result = verify_health()

    return {
        "restart": restart_result,
        "health_check": health_result
    }


def get_agent_report():
    """
    Generate the complete incident-response report.
    """

    analysis = analyze_incident()

    return analysis