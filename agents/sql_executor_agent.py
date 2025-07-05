from crewai import Agent
from tools.sql_execute_tool import execute_sql_query
from tools.update_db_tool import update_user_record
from tools.format import format_sql_table
from crewai.llm import LLM

# The base_url is just where Ollama runs locally
llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"  # This is Ollama's default address
)


sql_executor_agent = Agent(
    role="Database Executor",
    goal = (
    "Execute SQL queries and present the results in a clean, readable format. "
    "Use tools effectively and apply your own reasoning to ensure the accuracy of results. "
    "If the query does not match any data in the database, respond with: 'Invalid or incorrect query.'"
    ),
    backstory="Connects to the SQLite database and runs SQL queries.",
    tools=[execute_sql_query ,update_user_record],
    allow_delegation=False,
    verbose=True,
    llm = llm
)
