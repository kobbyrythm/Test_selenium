from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
driver.get("https://readcoop.eu/model/print-multi-language-danish-dutch-german-finnish-french-latin-swedish/")
time.sleep(20)
    