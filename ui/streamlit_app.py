import streamlit as st
import pandas as pd
import os
from datetime import datetime

LOG_FILE = "logs/sent_messages.csv"

st.title("🎂 AI Birthday WhatsApp Automation Dashboard")

# -----------------------------
# Load Log File
# -----------------------------

if os.path.exists(LOG_FILE):
    df = pd.read_csv(LOG_FILE)
else:
    df = pd.DataFrame(columns=["name", "phone", "message", "date"])

# -----------------------------
# Metrics Section
# -----------------------------

st.subheader("📊 Birthday Wish Statistics")

total_wishes = len(df)
unique_people = df["phone"].nunique() if not df.empty else 0

today = datetime.now().strftime("%Y-%m-%d")

today_wishes = len(df[df["date"] == today]) if not df.empty else 0

col1, col2, col3 = st.columns(3)

col1.metric("Total Wishes Sent", total_wishes)
col2.metric("Unique People Wished", unique_people)
col3.metric("Today's Wishes", today_wishes)

# -----------------------------
# Message History
# -----------------------------

st.subheader("📜 Message History")

if df.empty:
    st.info("No birthday messages sent yet.")
else:
    st.dataframe(
        df.sort_values(by="date", ascending=False),
        use_container_width=True
    )