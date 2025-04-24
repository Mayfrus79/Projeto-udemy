from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.maximize_window()

search_box = browser.find_element(By.ID, "APjFqb")
search_box.send_keys("Hello World")
search_box.send_keys(Keys.ENTER)



time.sleep(10)

