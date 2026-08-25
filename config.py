import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_deepseek import ChatDeepSeek

# Load environment variables from local .env file
load_dotenv()

# Set data paths relative to project root
data_path = Path(__file__).parent
tickets_file = data_path / "tickets.csv"
policies_file = data_path / "policies.csv"

# Initialize LLM instance
llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0
)