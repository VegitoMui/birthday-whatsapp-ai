import streamlit as st
import pandas as pd
import os

BIRTHDAY_FILE = "birthdays.xlsx"

st.title("🎂 Birthday Database Editor")

# -----------------------------
# Load birthday file
# -----------------------------

if os.path.exists(BIRTHDAY_FILE):

    df = pd.read_excel(BIRTHDAY_FILE)

else:

    df = pd.DataFrame(columns=[
        "Name",
        "Phone",
        "Birthday",
        "Relationship",
        "Tone"
    ])

# -----------------------------
# Display editable table
# -----------------------------

st.subheader("Edit Birthday Database")

edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

# -----------------------------
# Save changes
# -----------------------------

if st.button("💾 Save Changes"):

    edited_df.to_excel(BIRTHDAY_FILE, index=False)

    st.success("Birthday database updated successfully!")

# -----------------------------
# Quick Add Section
# -----------------------------

st.subheader("➕ Add New Birthday")

with st.form("add_birthday"):

    name = st.text_input("Name")

    phone = st.text_input("Phone")

    birthday = st.date_input("Birthday")

    relationship = st.selectbox(
        "Relationship",
        ["Friend", "Family", "Manager", "Colleague"]
    )

    tone = st.selectbox(
        "Tone",
        ["Funny", "Friendly", "Professional"]
    )

    submitted = st.form_submit_button("Add Birthday")

    if submitted:

        new_row = pd.DataFrame([{
            "Name": name,
            "Phone": phone,
            "Birthday": birthday,
            "Relationship": relationship,
            "Tone": tone
        }])

        df = pd.concat([df, new_row], ignore_index=True)

        df.to_excel(BIRTHDAY_FILE, index=False)

        st.success(f"Added birthday for {name}")