import pandas as pd
from datetime import datetime

REQUIRED_COLUMNS = ["Name", "Phone", "Birthday"]


def validate_columns(df):
    """
    Ensure the required columns exist in the Excel file.
    """
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def get_today_birthdays(file_path, test_date=None):
    """
    Reads Excel file and returns people whose birthday is today.

    Args:
        file_path (str): Path to the Excel file
        test_date (str): Optional date override for testing (MM-DD)

    Returns:
        pandas.DataFrame: Filtered DataFrame containing today's birthdays
    """

    df = pd.read_excel(file_path)

    validate_columns(df)

    # Convert Birthday column to datetime
    df["Birthday"] = pd.to_datetime(df["Birthday"], errors="coerce")

    # Extract month-day format
    df["month_day"] = df["Birthday"].dt.strftime("%m-%d")

    # Determine today's date
    if test_date:
        today = test_date
    else:
        today = datetime.now().strftime("%m-%d")

    birthday_people = df[df["month_day"] == today]

    return birthday_people