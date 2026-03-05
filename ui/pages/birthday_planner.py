import streamlit as st
import pandas as pd
import sys
import os

# Fix import path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

from app.birthday_planner import generate_planned_messages

st.title("🧠 Birthday Planning Agent")

st.write("This AI agent prepares birthday wishes for upcoming birthdays.")

if st.button("Generate Planned Messages"):

    with st.spinner("Planning upcoming birthday wishes..."):

        df = generate_planned_messages()

    if df.empty:

        st.info("No upcoming birthdays in the next 7 days.")

    else:

        st.success("Birthday messages prepared!")

        st.dataframe(df, use_container_width=True)