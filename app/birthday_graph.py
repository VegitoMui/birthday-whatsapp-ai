from typing import TypedDict, List, Dict

from langgraph.graph import StateGraph, END

from app.excel_reader import get_today_birthdays
from app.message_generator import generate_message
from app.whatsapp_sender import start_whatsapp_session, send_message
from app.message_logger import already_sent_today, log_message


# Excel file
EXCEL_FILE = "birthdays.xlsx"


# -------------------------
# Graph State
# -------------------------

class BirthdayState(TypedDict):

    birthdays: List[Dict]
    messages: List[Dict]


# -------------------------
# Node 1
# Read birthdays
# -------------------------

def read_birthdays_node(state: BirthdayState):

    df = get_today_birthdays(EXCEL_FILE)

    print("Today's birthdays:")
    print(df)

    birthdays = df.to_dict("records")

    return {"birthdays": birthdays}


# -------------------------
# Node 2
# Generate messages
# -------------------------

def generate_messages_node(state: BirthdayState):

    birthdays = state["birthdays"]

    messages = []

    for person in birthdays:

        name = person["Name"]
        phone = str(person["Phone"])
        relationship = person.get("Relationship", "friend")
        tone = person.get("Tone", "friendly")

        message = generate_message(name, relationship, tone, phone)

        messages.append({
            "name": name,
            "phone": phone,
            "message": message
        })

    return {"messages": messages}


# -------------------------
# Node 3
# Send WhatsApp messages
# -------------------------

driver = None


def send_messages_node(state: BirthdayState):

    global driver

    if driver is None:
        print("Opening WhatsApp session...")
        driver = start_whatsapp_session()

    messages = state["messages"]

    for msg in messages:

        name = msg["name"]
        phone = msg["phone"]
        message = msg["message"]

        # Duplicate check (same as original scheduler)
        if already_sent_today(phone):
            print(f"Skipping {name} — already wished today")
            continue

        print(f"Sending message to {name}")

        send_message(driver, phone, message)

        log_message(name, phone, message)

    return state


# -------------------------
# Build Graph
# -------------------------

builder = StateGraph(BirthdayState)

builder.add_node("read_birthdays", read_birthdays_node)
builder.add_node("generate_messages", generate_messages_node)
builder.add_node("send_messages", send_messages_node)

builder.set_entry_point("read_birthdays")

builder.add_edge("read_birthdays", "generate_messages")
builder.add_edge("generate_messages", "send_messages")
builder.add_edge("send_messages", END)

graph = builder.compile()


# -------------------------
# Run Graph
# -------------------------

def run_birthday_graph():

    graph.invoke({})


if __name__ == "__main__":

    run_birthday_graph()