from app.whatsapp_sender import send_whatsapp_message

if __name__ == "__main__":

    phone = "918448143515"

    message = "Happy Birthday! 🎉 Have an amazing day!"

    send_whatsapp_message(phone, message)