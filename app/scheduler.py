import time
import schedule

from app.excel_reader import get_today_birthdays
from app.message_generator import generate_message
from app.whatsapp_sender import start_whatsapp_session, send_message, close_whatsapp_session

EXCEL_FILE = "birthdays.xlsx"


def run_birthday_bot():

    print("-------------------------------------------------")
    print("Scheduler triggered")

    birthdays = get_today_birthdays(EXCEL_FILE)

    print("Birthday dataframe:")
    print(birthdays)

    if birthdays.empty:
        print("No birthdays today.")
        return

    print("Opening WhatsApp...")

    driver = start_whatsapp_session()

    print("WhatsApp session started")

    for _, row in birthdays.iterrows():

        name = row["Name"]
        phone = row["Phone"]

        relationship = row.get("Relationship", "friend")
        tone = row.get("Tone", "friendly")

        print(f"Generating message for {name}")

        message = generate_message(name, relationship, tone)

        print("Generated message:")
        print(message)

        print(f"Sending message to {phone}")

        send_message(driver, phone, message)

        print("Message sent")

        time.sleep(5)

    close_whatsapp_session(driver)

    print("Finished sending messages")


schedule.every().day.at("09:00").do(run_birthday_bot)
schedule.every(6).hours.do(run_birthday_bot)

print("Birthday bot scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(30)