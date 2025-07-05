import sqlite3
import pandas as pd
from crewai.tools import tool  # ✅ Use the decorator, not Tool class

@tool("execute_sql_query")
def execute_sql_query(sql_query: str) -> str:
    """Executes SQL and returns result from SQLite DB"""
    try:
        conn = sqlite3.connect("user_data.db")
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df.to_string(index=False)
    except Exception as e:
        return f"Error: {str(e)}"
