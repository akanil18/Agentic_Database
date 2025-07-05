# tools/sql_generator.py

from crewai.tools import tool
import subprocess

@tool("generate_sql_query")
def generate_sql_query(question: str) -> str:
    """Generate SQL query from user natural language question using Mistral (via Ollama subprocess)."""
    prompt = f"""
You are a helpful assistant that converts natural language into SQL queries.

Table: users
Columns: id, name, email, phone, state, dob

Example:
Question: Get all users from Gujarat
SQL: SELECT * FROM users WHERE state = 'Gujarat';

Question: {question}
SQL:
""".strip()

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            encoding='utf-8',
            capture_output=True,
            timeout=20
        )

        if result.returncode != 0:
            return f"Error running Ollama model:\n{result.stderr}"

        return result.stdout.strip()

    except Exception as e:
        return f"Exception occurred while generating SQL query: {str(e)}"
