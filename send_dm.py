from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

USERNAME = os.environ["IG_USERNAME"]
PASSWORD = os.environ["IG_PASSWORD"]
RECEIVER = "muhammed_sozn"
MESSAGE = "bu adam niye var"

options = Options()
options.add_argument("--headless")  # Arka planda çalışır
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    # Kullanıcı adı ve şifre gir
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    # Bildirim ekranını geç
    try:
        not_now_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")
        not_now_btn.click()
    except:
        pass
    time.sleep(5)

    # DM kutusuna git
    driver.get(f"https://www.instagram.com/direct/t/{RECEIVER}/")
    time.sleep(10)

    # Mesaj yaz ve gönder
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(MESSAGE)
    time.sleep(1)

    send_button = driver.find_element(By.XPATH, "//button[text()='Gönder']")
    send_button.click()
    time.sleep(5)

finally:
    driver.quit()
