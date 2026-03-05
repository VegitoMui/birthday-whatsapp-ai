import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(r"C:\Users\Yashovardhan\PyCharmMiscProject\birthday-whatsapp-ai")
from app.excel_reader import get_today_birthdays
from app.message_generator import generate_message

st.set_page_config(page_title="Birthday AI Bot", page_icon="🎂")

st.title("🎂 Birthday AI Message Generator")

st.write("Upload your birthday Excel file and generate AI birthday messages.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file, engine="openpyxl")

    st.subheader("📊 Uploaded Data")
    st.dataframe(df)

    birthdays = get_today_birthdays(uploaded_file)

    if birthdays.empty:
        st.success("No birthdays today 🎉")

    else:
        st.subheader("🎉 Today's Birthdays")

        for _, row in birthdays.iterrows():

            name = row["Name"]
            relationship = row.get("Relationship", "friend")
            tone = row.get("Tone", "friendly")

            message = generate_message(name, relationship, tone)

            st.write(f"### 🎉 {name}")
            st.write(message)
            st.divider()