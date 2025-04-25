from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Abre o navegador
browser = webdriver.Edge()
browser.get("https://best.aliexpress.com/?dp=BBS11&af=2015&aff_fcid=85a949a8588f4238918bd940e8334140-1745437789585-00586-_Dlppdsf&tt=CPS_NORMAL&aff_fsk=_Dlppdsf&aff_platform=portals-tool&sk=_Dlppdsf&aff_trace_key=85a949a8588f4238918bd940e8334140-1745437789585-00586-_Dlppdsf&terminal_id=a502c334fcbc4144ab650657be6a8208")
browser.maximize_window()

# Localiza a barra de pesquisa e digita algo
search_box = browser.find_element(By.ID, "search-words")
search_box.click()
search_box.send_keys("The beginning after the end")  # Altere para o que você quiser buscar
search_box.send_keys(Keys.RETURN)     # Pressiona Enter para buscar


# Aguarda resultados
time.sleep(500)
