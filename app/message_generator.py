from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME

# Initialize GROQ client
client = Groq(api_key=GROQ_API_KEY)


def generate_message(name, relationship, tone):
    """
    Generate a personalized birthday message using GROQ.
    """

    prompt = f"""
You are writing a birthday message that will be sent on WhatsApp.

Person Name: {name}
Relationship: {relationship}
Tone: {tone}

Guidelines:
- Sound like a real human texting, not a greeting card.
- Keep it short (1–2 sentences).
- Use natural emojis (1–2).
- Avoid formal phrases like "Wishing you a very happy birthday".
- Make it warm, friendly and personal.
- Do not use quotes or hashtags.

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