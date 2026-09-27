# tools.py

from simulator import get_system_state

# Stores all actions performed during the incident
action_history = []


def record_action(tool_name, result):
    """Record an action performed during the incident."""

    action_history.append({
        "action": tool_name,
        "result": result
    })


def check_logs():
    """Simulate checking application logs."""

    result = (
        "ERROR: Payment API unavailable. "
        "Database connection pool exhausted."
    )

    record_action("check_logs", result)

    return result


def check_metrics():
    """Simulate checking system metrics."""

    state = get_system_state()

    result = (
        f"API Status: {state['api_status']}, "
        f"Database Connections: {state['database_connections']}, "
        f"CPU: {state['cpu_usage']}, "
        f"Memory: {state['memory_usage']}"
    )

    record_action("check_metrics", result)

    return result


def check_database():
    """Simulate checking the database."""

    result = (
        "Database is reachable, but the connection pool "
        "is exhausted. Active connections: 100/100."
    )

    record_action("check_database", result)

    return result


def restart_service():
    """Simulate restarting the payment service."""

    result = "Payment service restarted successfully."

    record_action("restart_service", result)

    return result


def verify_health():
    """Simulate checking whether the service recovered."""

    result = "Payment API is healthy. HTTP status: 200."

    record_action("verify_health", result)

    return result


def get_action_history():
    """Return all actions performed during the incident."""

    return action_history