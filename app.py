import streamlit as st
from crew_runner import run_crew_pipeline

st.set_page_config(page_title="SQL Generator & Runner", layout="centered")
st.title(" Natural Language to SQL (with CrewAI)")
st.markdown("Describe your SQL task and let the AI generate, verify, and execute it.")

user_input = st.text_area(
    " Your task description:",
    placeholder="Example: Write an SQL query to get all users who signed up in January."
)

if st.button(" Run Agent Workflow"):
    if not user_input.strip():
        st.warning("Please enter a valid task description.")
    else:
        with st.spinner("Running CrewAI pipeline..."):
            try:
                result = run_crew_pipeline(user_input)
                st.success("✅ Done!")
                st.markdown("### 📊 Result")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Error: {e}")
