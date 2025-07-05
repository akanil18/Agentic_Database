from crewai import Agent
from crewai.llm import LLM

llm = LLM(
    model="ollama/codellama",
    base_url="http://localhost:11434"  # This is Ollama's default address
)
sql_verifier_agent = Agent(
    name="SQL Verifier Agent",
    role="SQL expert who validates logic",
    goal="Verify SQL queries match the problem statement logically",
    backstory="You are a senior data engineer. You double-check SQL queries to ensure they logically satisfy the user's problem statement.",
    llm=llm

)
