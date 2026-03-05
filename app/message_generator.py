from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME

# Initialize GROQ client
client = Groq(api_key=GROQ_API_KEY)


def generate_message(name, relationship, tone):
    """
    Generate a personalized birthday message using GROQ.
    """

    prompt = f"""
    Write a {tone} birthday wish for my {relationship} named {name}.
    Keep it under 80 words.
    Add emojis appropriately.
    Make it warm and natural.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
