import pandas as pd
from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sent_messages.csv")


# -------------------------
# Ensure log file exists
# -------------------------

def initialize_log():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(LOG_FILE):

        df = pd.DataFrame(columns=["name", "phone", "message", "date"])
        df.to_csv(LOG_FILE, index=False)


# -------------------------
# Check if message already sent today
# -------------------------

def already_sent_today(phone):

    phone = str(phone)

    initialize_log()

    df = pd.read_csv(LOG_FILE, dtype=str)

    today = datetime.now().strftime("%Y-%m-%d")

    sent_today = df[
        (df["phone"] == phone) &
        (df["date"] == today)
    ]

    return not sent_today.empty


# -------------------------
# Log a new message
# -------------------------

def log_message(name, phone, message):

    phone = str(phone)

    initialize_log()

    today = datetime.now().strftime("%Y-%m-%d")

    new_entry = pd.DataFrame([{
        "name": name,
        "phone": phone,
        "message": message,
        "date": today
    }])

    df = pd.read_csv(LOG_FILE, dtype=str)

    df = pd.concat([df, new_entry], ignore_index=True)

    df.to_csv(LOG_FILE, index=False)

    print(f"Logged message for {name}")