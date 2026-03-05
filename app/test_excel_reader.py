from app.excel_reader import get_today_birthdays


if __name__ == "__main__":

    birthdays = get_today_birthdays("birthdays.xlsx")

    if birthdays.empty:
        print("No birthdays today 🎉")

    else:
        print("\nToday's Birthdays:\n")
        print(birthdays[["Name", "Phone", "Birthday"]])