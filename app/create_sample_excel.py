import pandas as pd

data = {
    "Name": ["Rahul Sharma", "Priya Singh", "Amit Verma", "Neha Gupta"],
    "Phone": [919876543210, 919812345678, 919845678912, 919876112233],
    "Birthday": ["1995-03-05", "1992-03-05", "1990-07-10", "1994-12-25"],
    "Relationship": ["Friend", "Colleague", "Brother", "Friend"],
    "Tone": ["Funny", "Professional", "Emotional", "Casual"]
}

df = pd.DataFrame(data)

df.to_excel("birthdays.xlsx", index=False)

print("Excel file 'birthdays.xlsx' created successfully!")