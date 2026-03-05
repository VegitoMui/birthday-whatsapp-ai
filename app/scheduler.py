import time
import schedule
from app.message_logger import already_sent_today, log_message
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

        if already_sent_today(phone):
            print(f"Skipping {name} — already wished today")
            continue

        message = generate_message(name, relationship, tone)

        print(f"Sending message to {name}")

        send_message(driver, phone, message)

        log_message(name, phone, message)

        time.sleep(5)

    close_whatsapp_session(driver)

    print("Finished sending messages")
"""
schedule.every().day.at("09:00").do(run_birthday_bot)
schedule.every(6).hours.do(run_birthday_bot)
"""
schedule.every(10).seconds.do(run_birthday_bot)
print("Birthday bot scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(30)