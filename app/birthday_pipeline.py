from app.excel_reader import get_today_birthdays
from app.message_generator import generate_message


def run_pipeline():

    print("\n🎂 Checking for today's birthdays...\n")

    birthdays = get_today_birthdays("birthdays.xlsx")

    if birthdays.empty:
        print("No birthdays today 🎉")
        return

    print(f"Found {len(birthdays)} birthday(s) today!\n")

    for _, row in birthdays.iterrows():

        name = row["Name"]
        phone = row["Phone"]
        relationship = row.get("Relationship", "friend")
        tone = row.get("Tone", "friendly")

        print(f"🎉 Generating message for {name}...")

        message = generate_message(name, relationship, tone)

        print("\n-----------------------------")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print("Message:")
        print(message)
        print("-----------------------------\n")


if __name__ == "__main__":
    run_pipeline()