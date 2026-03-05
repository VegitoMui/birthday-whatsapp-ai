from datetime import datetime
import pandas as pd
import os

from app.message_generator import generate_message

BIRTHDAY_FILE = "birthdays.xlsx"
PLANNED_FILE = "logs/planned_messages.csv"


def get_upcoming_birthdays(days_ahead=7):

    df = pd.read_excel(BIRTHDAY_FILE)

    df["Birthday"] = pd.to_datetime(df["Birthday"])

    today = datetime.now().date()

    upcoming = []

    for _, row in df.iterrows():

        birthday_this_year = row["Birthday"].replace(year=today.year).date()

        if birthday_this_year < today:
            birthday_this_year = row["Birthday"].replace(year=today.year + 1).date()

        days_until = (birthday_this_year - today).days

        if days_until <= days_ahead:

            upcoming.append({
                "Name": row["Name"],
                "Phone": row["Phone"],
                "Relationship": row.get("Relationship", "Friend"),
                "Tone": row.get("Tone", "Friendly"),
                "Days Away": days_until
            })

    return pd.DataFrame(upcoming)


def generate_planned_messages():

    upcoming = get_upcoming_birthdays()

    if upcoming.empty:
        return upcoming

    messages = []

    for _, row in upcoming.iterrows():
        message = generate_message(
            row["Name"],
            row["Relationship"],
            row["Tone"],
            row["Phone"]
        )

        messages.append(message)

    upcoming["Planned Message"] = messages

    # Save planned messages
    os.makedirs("logs", exist_ok=True)
    upcoming.to_csv(PLANNED_FILE, index=False)

    return upcoming