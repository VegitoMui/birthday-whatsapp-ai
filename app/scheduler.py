import time
import schedule

from app.birthday_graph import run_birthday_graph
from app.birthday_planner import generate_planned_messages

def run_birthday_bot():

    print("-------------------------------------------------")
    print("Scheduler triggered")

    # Run planning agent
    print("Running birthday planning agent...")

    planned = generate_planned_messages()

    if not planned.empty:
        print("Upcoming birthdays planned:")
        print(planned)

    else:
        print("No upcoming birthdays to plan.")

    # Run messaging agent
    print("Running birthday messaging agent...")

    run_birthday_graph()

    print("Scheduler cycle completed")


# Run once immediately
run_birthday_bot()

# Then run every 3 hours
schedule.every(3).hours.do(run_birthday_bot)

print("Birthday bot scheduler started...")


while True:

    schedule.run_pending()

    time.sleep(30)