import json

class SystemLogger:
    def __init__(self):
        self.logs = []

    def log_step(self, step_name, agent_name, input_data, output_data, execution_time_ms, ticket_id="TICK-101"):
        entry = {
            "ticket_id": ticket_id,
            "step_name": step_name,
            "agent_name": agent_name,
            "input_data": input_data,
            "output_data": output_data,
            "execution_time_ms": round(execution_time_ms, 2)
        }
        self.logs.append(entry)
        return entry

    def save_audit_trail(self, filepath="audit_trail.json"):
        with open(filepath, "w") as f:
            json.dump(self.logs, f, indent=4)
        print(f"Audit trail successfully saved to '{filepath}'")

system_logger = SystemLogger()