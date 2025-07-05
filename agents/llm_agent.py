
# from crewai import Agent
# from tools.llm_sql_tool import generate_sql_query
# from langchain_ollama import ChatOllama
# llm = ChatOllama(model="mistral")

# llm_query_agent = Agent(
#     role="Query Generator",
#     goal="Generate SQL queries from user questions",
#     backstory="Knows how to translate natural language to SQL for the users table.",
#     tools=[generate_sql_query],  # 👈 just use the decorated function directly
#     allow_delegation=True,
#     verbose=True,
#     llm=llm
# )

from crewai import Agent
from crewai.llm import LLM
from tools.db_schema_tool import describe_database
# The base_url is just where Ollama runs locally
llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"  # This is Ollama's default address
)

llm_query_agent = Agent(
    role="Query Generator",
   goal = (
    "Generate SQL queries based on user questions. "
    "Always begin by using the 'describe_database' tool to understand the database schema. "
    "Write correct SQL queries aligned with the schema. "
    "If the question involves multiple queries across different tables, generate and execute them sequentially and correctly."
),
    backstory="You are an expert SQL developer.",
    tools = [describe_database],
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# agents/llm_agent.py

# from crewai import Agent
# from langchain_community.llms import Ollama
# from tools.llm_sql_tool import generate_sql_query  # Ensure correct path to the tool

# # Load Ollama LLM (Mistral model)
# llm = Ollama(
#     model="mistral",
#     base_url="http://localhost:11434"  # Make sure Ollama is running here
# )

# # Define the CrewAI Agent
# llm_query_agent = Agent(
#     role="Query Generator",
#     goal="Generate SQL queries from user questions",
#     backstory="You are an expert SQL developer. Your task is to convert user questions into accurate SQL queries for the 'users' table.",
#     tools=[generate_sql_query],  # This is the @tool-decorated function
#     allow_delegation=False,
#     verbose=True,
#     llm=llm
# )

