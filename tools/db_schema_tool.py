from crewai.tools import tool
import sqlite3

@tool("describe_database")
def describe_database(_: str = "") -> str:
    """Returns schema of user_data.db excluding SQLite internal tables."""
    try:
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()

        # Get user-defined tables (excluding internal ones)
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """)
        tables = cursor.fetchall()

        if not tables:
            return "No user-defined tables found in the database."

        schema_info = ""
        for table_name in tables:
            table_name = table_name[0]
            schema_info += f"\n📌 Table: {table_name}\n"

            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            for col in columns:
                schema_info += f"  - {col[1]} ({col[2]})\n"

        return schema_info.strip()

    except Exception as e:
        return f"Error reading schema: {e}"

    finally:
        conn.close()
