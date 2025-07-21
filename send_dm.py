from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

username = os.environ['IG_USERNAME']
password = os.environ['IG_PASSWORD']
target_user = 'muhammed_sozn'
message = 'bu adam niye var'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)

    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    # Instagram bazen “Şimdi Değil” tarzı popup gösterir, varsa kapat
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]").click()
    except:
        pass
    time.sleep(5)

    # Hedef kişinin DM sayfasına git
    driver.get(f'https://www.instagram.com/direct/t/{target_user}/')
    time.sleep(10)

    # Mesaj kutusunu bulup mesajı yaz
    textarea = driver.find_element(By.TAG_NAME, 'textarea')
    textarea.send_keys(message)
    time.sleep(1)

    # Gönder butonuna bas
    driver.find_element(By.XPATH, "//button[text()='Gönder']").click()
    time.sleep(5)

finally:
    driver.quit()
