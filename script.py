from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://readcoop.eu/model/print-multi-language-danish-dutch-german-finnish-french-latin-swedish/")
time.sleep(20)
    