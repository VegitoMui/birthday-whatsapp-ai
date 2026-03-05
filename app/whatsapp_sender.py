import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def send_whatsapp_message(phone, message):

    encoded_message = urllib.parse.quote(message)

    url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    print("Waiting for WhatsApp Web login...")

    wait = WebDriverWait(driver, 120)

    try:
        # Wait until the message input box is visible
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            )
        )

        # Wait for send button
        send_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@aria-label="Send"]')
            )
        )

        send_button.click()

        print(f"Message sent to {phone}")

    except Exception as e:
        print("Error sending message:", e)

    input("Press ENTER to close browser...")
    driver.quit()