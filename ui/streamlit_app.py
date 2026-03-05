import sys
import os
import time

# Add project root to Python path
sys.path.append(r"C:\Users\Yashovardhan\PyCharmMiscProject\birthday-whatsapp-ai")

import streamlit as st
import pandas as pd

from app.excel_reader import get_today_birthdays
from app.message_generator import generate_message
from app.whatsapp_sender import start_whatsapp_session, send_message, close_whatsapp_session


st.set_page_config(page_title="Birthday AI Bot", page_icon="🎂")

st.title("🎂 Birthday AI Message Generator")

st.write("Upload your Excel file and send AI generated birthday wishes automatically.")


uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])


if uploaded_file:

    df = pd.read_excel(uploaded_file, engine="openpyxl")

    st.subheader("📊 Uploaded Data")
    st.dataframe(df)


    if st.button("🎉 Generate Birthday Messages"):

        birthdays = get_today_birthdays(uploaded_file)

        messages = []

        if birthdays.empty:

            st.success("No birthdays today 🎉")

        else:

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


        st.session_state.messages = pd.DataFrame(messages)


if "messages" in st.session_state:

    st.subheader("🎉 Generated Birthday Messages")

    st.dataframe(st.session_state.messages)

    if st.button("📲 Send WhatsApp Messages (Safe Mode)"):

        st.write("Starting WhatsApp session...")

        driver = start_whatsapp_session()

        for _, row in st.session_state.messages.iterrows():
            phone = row["Phone"]
            message = row["Message"]

            send_message(driver, phone, message)

            st.write(f"✅ Sent to {row['Name']}")

        close_whatsapp_session(driver)

        st.success("🎉 All messages sent successfully!")