# simulator.py

def get_current_incident():
    """
    Returns the current simulated incident.
    """

    return {
        "incident_id": "INC-001",
        "service": "Payment API",
        "status_code": 503,
        "severity": "HIGH",
        "description": "Payment API is unavailable",
        "traffic": "High"
    }


def get_system_state():
    """
    Returns the current simulated system state.
    """

    return {
        "api_status": 503,
        "database_connections": "100/100",
        "cpu_usage": "42%",
        "memory_usage": "61%",
        "requests_per_minute": 1250,
        "service_status": "Degraded"
    }


if __name__ == "__main__":

    print("CURRENT INCIDENT")
    print(get_current_incident())

    print("\nSYSTEM STATE")
    print(get_system_state())