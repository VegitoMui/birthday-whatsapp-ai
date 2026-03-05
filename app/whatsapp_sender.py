import time
import urllib.parse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def start_whatsapp_session():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://web.whatsapp.com")

    print("Please scan QR code if not logged in")

    wait = WebDriverWait(driver, 120)

    wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@title="Search input textbox"]'))
    )

    print("WhatsApp ready")

    return driver

def send_message(driver, phone, message):

    wait = WebDriverWait(driver, 60)

    encoded_message = urllib.parse.quote(message)

    chat_url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"

    driver.get(chat_url)

    send_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
    )

    send_button.click()

    print(f"Message sent to {phone}")

    time.sleep(7)


def close_whatsapp_session(driver):

    driver.quit()