from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME


def test_groq_connection():
    print("Connecting to GROQ...")

    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": "Write a short professional birthday wish for Rahul."
            }
        ],
        temperature=0.7
    )

    print("\n✅ GROQ Response:\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    test_groq_connection()