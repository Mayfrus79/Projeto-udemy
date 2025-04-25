from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.maximize_window()

# Localiza a barra de pesquisa e digita algo
search_box = browser.find_element(By.ID, "search-words")
search_box.click()
search_box.send_keys("The beginning after the end")  # Altere para o que você quiser buscar
search_box.send_keys(Keys.RETURN)     # Pressiona Enter para buscar




time.sleep(10)

