from crewai import Crew, Task
from agents.llm_agent import llm_query_agent
from agents.sql_executor_agent import sql_executor_agent
from agents.sql_verifier_agent import sql_verifier_agent

# ----------------------
# 🧠 Main Crew Pipeline
# ----------------------
def run_crew_pipeline(user_description: str):
    # Task 1: Generate SQL Query
    task1 = Task(
        description=user_description,
        expected_output="A valid SQL query.",
        agent=llm_query_agent
    )

    # Task 2: Verify and Regenerate SQL if Needed
    task2 = Task(
        description=(
            "Verify the SQL query generated in Task 1. "
            "Ensure it logically matches the user description. "
            "If incorrect, regenerate a correct SQL query."
        ),
        agent=sql_verifier_agent,
        context=[task1],
        expected_output="A logically correct SQL query."
    )

    # Task 3: Execute SQL Query
    task3 = Task(
        description=(
            "Take the verified SQL query and execute it. "
            "If it's a SELECT query, return the result as a markdown table. "
            "If it's an UPDATE/INSERT/DELETE, return a plain text confirmation."
        ),
        agent=sql_executor_agent,
        context=[task2],  # Use the verified version of the query
        expected_output="Formatted markdown table or confirmation message."
    )

    # 🧬 Assemble and Run Crew
    crew = Crew(
        agents=[llm_query_agent, sql_verifier_agent, sql_executor_agent],
        tasks=[task1, task2, task3],
        verbose=True
    )

    return crew.kickoff()
