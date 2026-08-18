from client import MultiAgentSupervisionLoopInterventionGovernorClient

def main():
    client = MultiAgentSupervisionLoopInterventionGovernorClient()
    telemetry = [{"agent_id": "worker_01", "state": "EXECUTING_TASK", "retries": 1}]
    res = client.supervise_fleet(telemetry)
    print(f"Fleet Health: {res['fleet_health_index'] * 100}%")
    print(f"Loop Detected: {res['loop_detected']}")
    print(f"Intervention: {res['intervention_action_applied']}")

if __name__ == "__main__":
    main()
