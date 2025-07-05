from crewai.tools import tool
import pandas as pd
from io import StringIO

@tool("format_sql_table")
def format_sql_table(raw_output: str) -> str:
    """Format raw SQL output (string) into a clean markdown table."""
    try:
        lines = raw_output.strip().split('\n')
        if not lines:
            return "No data to format."

        headers = lines[0].split()
        rows = [line.split(maxsplit=len(headers)-1) for line in lines[1:]]

        df = pd.DataFrame(rows, columns=headers)
        return df.to_markdown(index=False)
    except Exception as e:
        return f"Error formatting table: {e}"
