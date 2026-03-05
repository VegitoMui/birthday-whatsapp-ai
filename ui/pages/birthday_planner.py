import streamlit as st
import pandas as pd
import os

PLANNED_FILE = "logs/planned_messages.csv"

st.title("🧠 Birthday Planning Agent")

st.write("AI prepared birthday wishes for upcoming birthdays.")

if os.path.exists(PLANNED_FILE):

    df = pd.read_csv(PLANNED_FILE)

    if df.empty:

        st.info("No planned messages available.")

    else:

        st.success("Upcoming birthday messages prepared by AI")

        st.dataframe(df, use_container_width=True)

else:

    st.info("Planner has not generated messages yet. Wait for scheduler run.")