from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
 # Abre o navegador
browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.maximize_window()
 
 # Localiza a barra de pesquisa e digita algo
search_box = browser.find_element(By.NAME, "search_query")
search_box.send_keys("Como usar o selenium python")
search_box.send_keys(Keys.ENTER)


time.sleep(200)