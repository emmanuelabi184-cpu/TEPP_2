import json
import time
from datetime import datetime
from typing import Dict, Any, List

class AuditLogger:
    """Telemetry and audit logger for tracking agent executions across LangGraph nodes."""
    def __init__(self, log_file: str = "audit_trail.json"):
        self.log_file = log_file

    def log_step(
        self, 
        audit_log_list: List[Dict[str, Any]], 
        ticket_id: str, 
        step_name: str, 
        agent_name: str, 
        input_data: Dict[str, Any], 
        output_data: Dict[str, Any], 
        execution_time_ms: float
    ) -> Dict[str, Any]:
        """Creates a structured telemetry entry and appends it to the state audit log."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "ticket_id": ticket_id,
            "step_name": step_name,
            "agent_name": agent_name,
            "execution_time_ms": round(execution_time_ms, 2),
            "input": input_data,
            "output": output_data
        }
        
        # Append directly to the list stored in SupportState
        audit_log_list.append(log_entry)
        
        # Terminal log for real-time monitoring
        print(f"  [{step_name}] {agent_name} executed in {execution_time_ms:.2f}ms")
        return log_entry

    def save_audit_trail(self, audit_log_list: List[Dict[str, Any]]) -> None:
        """Saves the accumulated audit trail to a local JSON file."""
        try:
            with open(self.log_file, "w") as f:
                json.dump(audit_log_list, f, indent=2)
            print(f"\nAudit trail successfully saved to '{self.log_file}'")
        except Exception as e:
            print(f"Error saving audit trail: {e}")

# Global instance for subagent nodes to import and call
system_logger = AuditLogger()