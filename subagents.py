import time
from langchain.agents import create_agent
from langchain_core.tools import tool
from config import llm
from tool import lookup_policy
from logger import system_logger

# Define subagents
triage_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are a support triage expert. Categorize tickets and assign priority."
)

policy_agent = create_agent(
    model=llm,
    tools=[lookup_policy],
    system_prompt="You are a customer service policy expert. Use the lookup_policy tool to retrieve answers."
)

# Wrap subagents into tools with telemetry
@tool
def ask_triage_expert(query: str, ticket_id: str = "TICK-101") -> str:
    """Classifies customer tickets and assigns priority."""
    start_time = time.time()
    
    result = triage_agent.invoke({"messages": [{"role": "user", "content": query}]})
    output_text = result["messages"][-1].content
    
    exec_time = (time.time() - start_time) * 1000
    
    system_logger.log_step(
        step_name="Triage",
        agent_name="TriageAgent",
        input_data={"query": query},
        output_data={"triage_response": output_text},
        execution_time_ms=exec_time,
        ticket_id=ticket_id
    )
    
    return output_text

@tool
def ask_policy_expert(query: str, ticket_id: str = "TICK-101") -> str:
    """Answers customer support questions using corporate policy docs."""
    start_time = time.time()
    
    result = policy_agent.invoke({"messages": [{"role": "user", "content": query}]})
    output_text = result["messages"][-1].content
    
    exec_time = (time.time() - start_time) * 1000
    
    system_logger.log_step(
        step_name="Policy Lookup",
        agent_name="PolicyAgent",
        input_data={"query": query},
        output_data={"policy_response": output_text},
        execution_time_ms=exec_time,
        ticket_id=ticket_id
    )
    
    return output_text