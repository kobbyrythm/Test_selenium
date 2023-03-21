from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_service = Service(environ['CHROMEWEBDRIVER'])
chrome_options = Options()
for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
    chrome_options.add_argument(option)
driver = webdriver.Chrome(service = chrome_service,options = chrome_options)

driver.get("https://readcoop.eu/model/print-multi-language-danish-dutch-german-finnish-french-latin-swedish/")
time.sleep(20)
    