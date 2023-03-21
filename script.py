from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://readcoop.eu/model/print-multi-language-danish-dutch-german-finnish-french-latin-swedish/")
time.sleep(20)
    