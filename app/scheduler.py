import time
import schedule

from app.birthday_graph import run_birthday_graph


def run_birthday_bot():

    print("-------------------------------------------------")
    print("Scheduler triggered")

    try:

        run_birthday_graph()

        print("Birthday agent finished")

    except Exception as e:

        print("Error running birthday agent:", e)


# Run once immediately
run_birthday_bot()

# Then run every 3 hours
schedule.every(3).hours.do(run_birthday_bot)

print("Birthday bot scheduler started...")


while True:

    schedule.run_pending()

    time.sleep(30)