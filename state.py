from typing import TypedDict, List, Dict, Any

class SupportState(TypedDict):
    ticket_id: str
    user_query: str
    category: str
    priority: str
    policy_context: str
    response: str
    audit_log: List[Dict[str, Any]]  # Holds the running trace entries