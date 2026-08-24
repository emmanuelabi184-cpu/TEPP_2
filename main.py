import os
from dotenv import load_dotenv
from orchestrator import orchestrator
from logger import system_logger

# Load environment variables
load_dotenv()

def run_pipeline():
    # Prompt for processing support tickets
    prompt = "Process support ticket TICK-101: Customer is asking for a full refund on order #4412 due to late delivery."

    print("Executing TEPP_2 Multi-Agent Support Pipeline...\n")

    # 1. Invoke orchestrator
    result = orchestrator.invoke({"messages": [{"role": "user", "content": prompt}]})

    # 2. Extract final response
    FINAL_ANSWER = result["messages"][-1].content
    print("FINAL ANSWER:\n", FINAL_ANSWER)
    print("\n" + "="*50 + "\n")

    # 3. Export accumulated telemetry logs to audit_trail.json
    system_logger.save_audit_trail()

if __name__ == "__main__":
    run_pipeline()