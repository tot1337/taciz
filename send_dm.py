from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

USERNAME = os.environ['IG_USERNAME']
PASSWORD = os.environ['IG_PASSWORD']
RECEIVER = 'muhammed_sozn'
MESSAGE = 'bu adam niye var'

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
