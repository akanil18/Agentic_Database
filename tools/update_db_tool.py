from crewai.tools import tool
import sqlite3

@tool("update_user_record")
def update_user_record(sql_update_query: str) -> str:
    """
    Executes an UPDATE SQL query on the user_data.db database.
    """
    try:
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()

        # Execute the update query
        cursor.execute(sql_update_query)
        conn.commit()

        rows_affected = cursor.rowcount
        return f"✅ Update successful. {rows_affected} row(s) updated."

    except Exception as e:
        return f"❌ Error during update: {e}"

    finally:
        conn.close()
