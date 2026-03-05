import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
from app.birthday_graph import run_birthday_graph

st.subheader("⚙️ Bot Controls")

if st.button("Run Birthday Bot Now"):

    with st.spinner("Running birthday bot..."):

        run_birthday_graph()

    st.success("Birthday bot finished!")
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

BIRTHDAY_FILE = "birthdays.xlsx"

st.subheader("🎂 Upcoming Birthdays")

if os.path.exists(BIRTHDAY_FILE):

    df_birthdays = pd.read_excel(BIRTHDAY_FILE)

    df_birthdays["Birthday"] = pd.to_datetime(df_birthdays["Birthday"])

    today = datetime.now().date()

    upcoming = []

    for _, row in df_birthdays.iterrows():

        birthday_this_year = row["Birthday"].replace(year=today.year).date()

        days_until = (birthday_this_year - today).days

        if days_until < 0:
            birthday_this_year = row["Birthday"].replace(year=today.year + 1).date()
            days_until = (birthday_this_year - today).days

        if days_until <= 7:

            upcoming.append({
                "Name": row["Name"],
                "Relationship": row.get("Relationship", ""),
                "Days Away": days_until
            })

    upcoming_df = pd.DataFrame(upcoming)

    if upcoming_df.empty:

        st.info("No upcoming birthdays in next 7 days.")

    else:

        upcoming_df = upcoming_df.sort_values("Days Away")

        st.dataframe(upcoming_df, use_container_width=True)

else:

    st.warning("Birthday Excel file not found.")