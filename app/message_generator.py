from groq import Groq
import pandas as pd
import os

from app.config import GROQ_API_KEY, MODEL_NAME

# Log file for memory
LOG_FILE = "logs/sent_messages.csv"

# Initialize GROQ client
client = Groq(api_key=GROQ_API_KEY)


def get_last_message(phone):
    """
    Fetch the last message sent to this phone number.
    """

    if not os.path.exists(LOG_FILE):
        return None

    df = pd.read_csv(LOG_FILE, dtype=str)

    df = df[df["phone"] == str(phone)]

    if df.empty:
        return None

    # Get the most recent message
    last_row = df.iloc[-1]

    return last_row["message"]


def generate_message(name, relationship, tone, phone=None):
    """
    Generate a personalized birthday message using GROQ.
    """

    last_message = None

    if phone:
        last_message = get_last_message(phone)

    memory_section = ""

    if last_message:

        memory_section = f"""
Last year you wrote this message to {name}:
{last_message}

Write a different birthday message this time.
Avoid repeating the same wording.
"""

    prompt = f"""
You are writing a birthday message that will be sent on WhatsApp.

Person Name: {name}
Relationship: {relationship}
Tone: {tone}

{memory_section}

Guidelines:
- Sound like a real human texting.
- Keep it short (1–2 sentences).
- Use 1–2 emojis.
- Avoid overly formal phrases.
- Make it warm and natural.

Examples:

Funny friend:
Happy birthday Rahul! Hope your cake is bigger than your problems today 😂🎂

Professional:
Happy birthday Shivam! Wishing you a fantastic year ahead filled with success and happiness 🎉

Now write the birthday message.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You write natural and friendly WhatsApp birthday messages."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=120
    )

    return response.choices[0].message.content.strip()