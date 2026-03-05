import streamlit as st
import pandas as pd
import os

LOG_FILE = "logs/sent_messages.csv"

st.title("📊 Birthday Automation Analytics")

if not os.path.exists(LOG_FILE):

    st.warning("No message history yet.")
    st.stop()

df = pd.read_csv(LOG_FILE)

df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# Wishes Per Month
# -----------------------------

st.subheader("📈 Wishes Sent Per Month")

df["month"] = df["date"].dt.strftime("%Y-%m")

monthly_counts = df.groupby("month").size()

st.bar_chart(monthly_counts)

# -----------------------------
# Wishes Per Person
# -----------------------------

st.subheader("👤 Most Wished People")

person_counts = df.groupby("name").size().sort_values(ascending=False)

st.bar_chart(person_counts)

# -----------------------------
# Raw Data
# -----------------------------

st.subheader("📜 Full Message History")

st.dataframe(df, use_container_width=True)