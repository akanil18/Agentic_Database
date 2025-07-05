from crewai import Crew, Task
from agents.llm_agent import llm_query_agent
from agents.sql_executor_agent import sql_executor_agent
from agents.sql_verifier_agent import sql_verifier_agent
# ----------------------
# 🧠 Task 1: Generate SQL queries
# ----------------------
task1 = Task(
    description=(
    "Write an SQL query to calculate the confirmation rate for each user.\n"
    "Use the 'Signups' table, which contains 'user_id' and 'time_stamp', and the 'Confirmations' table, which contains "
    "'user_id', 'time_stamp', and 'action'.\n"
    "The confirmation rate is defined as the number of 'confirmed' messages divided by the total number of confirmation messages "
    "requested by that user. If a user has no confirmations, their confirmation rate should be 0.\n"
    "Return a result with each 'user_id' from the 'Signups' table and their confirmation rate rounded to two decimal places.\n"
    "Return the result in any order."
),

    expected_output="A valid SQL query.",
    # output_key="sql_dict",  # Output passed to task2
    agent=llm_query_agent
)

task2 = Task(
    description=(
        "Verify the SQL query from the previous task. "
        "Ensure it genrate the correct sql query.\n"
        "If incorrect, regenerate a correct SQL query."
    ),
    agent=sql_verifier_agent,
    context=[task1],
    expected_output="A logically correct SQL query."
)
# ----------------------
# 🧪 Task 2: Execute the SQL queries and format output
# ----------------------
task3 = Task(
    description=(
        "Take the SQL uery and execute it.\n"
        "Return the result as a markdown table if it's a SELECT query, or confirmation for UPDATE."
    ),
    expected_output="Formatted markdown tables or plain text confirmations.",
    # context=[task1],  # ✅ This MUST be the Task object, not a string!
    agent=sql_executor_agent
)

# ----------------------
# 🧬 Create and run the Crew
# ----------------------
crew = Crew(
    agents=[llm_query_agent, sql_executor_agent , sql_verifier_agent],
    tasks=[task1, task2 , task3],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n📊 Final Result:\n", result)
