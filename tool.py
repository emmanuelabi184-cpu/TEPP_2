import pandas as pd
from langchain_core.tools import tool

@tool
def fetch_tickets():
    """Fetch all customer support tickets from tickets.csv."""
    df = pd.read_csv("tickets.csv")
    return df.to_dict(orient="records")

@tool
def lookup_policy(category: str):
    """Retrieve matching company policy documentation based on ticket category."""
    df = pd.read_csv("policies.csv")
    results = df[df["category"].str.lower() == category.lower()]
    return results.to_dict(orient="records")