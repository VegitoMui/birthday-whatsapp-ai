import sys
import os

# Add project root to Python path
sys.path.append(r"C:\Users\Yashovardhan\PyCharmMiscProject\birthday-whatsapp-ai")

import streamlit as st
import pandas as pd

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


    if st.button("🎉 Generate Birthday Messages"):

        birthdays = get_today_birthdays(uploaded_file)

        if birthdays.empty:
            st.success("No birthdays today 🎉")

        else:

            messages = []

            for _, row in birthdays.iterrows():

                name = row["Name"]
                phone = row["Phone"]
                relationship = row.get("Relationship", "friend")
                tone = row.get("Tone", "friendly")

                message = generate_message(name, relationship, tone)

                messages.append({
                    "Name": name,
                    "Phone": phone,
                    "Message": message
                })


            message_df = pd.DataFrame(messages)

            st.subheader("🎉 Generated Birthday Messages")

            st.dataframe(message_df)