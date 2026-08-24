from langchain.agents import create_agent
from config import llm
from subagents import ask_triage_expert, ask_policy_expert

# Create the primary orchestrator supervisor agent
orchestrator = create_agent(
    model=llm,
    tools=[ask_triage_expert, ask_policy_expert],
    system_prompt=(
        "You are the Lead Support Orchestrator. Your role is to analyze incoming customer "
        "support tickets, route them to the triage expert for categorization/priority, "
        "and route policy-related questions to the policy expert. Delegate tasks as needed "
        "to formulate a complete, accurate resolution."
    )
)