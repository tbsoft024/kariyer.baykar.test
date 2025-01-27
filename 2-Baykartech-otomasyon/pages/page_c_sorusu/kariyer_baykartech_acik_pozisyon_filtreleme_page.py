import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BirimPozisyonFiltrelePage:
    def __init__(self, driver):
        self.driver = driver

    def birim_pozisyon_filtrele(self, url, pozisyon, birim):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Birim input değer gir
        birim_input = self.driver.find_element(By.ID, "searchInput")
        birim_input.send_keys("")
        birim_input.send_keys(birim)
        birim_input.send_keys(Keys.RETURN)
        time.sleep(3)

        # Pozisyon input değer gir
        pozisyon_input = self.driver.find_element(By.ID, "search")
        pozisyon_input.send_keys("")
        pozisyon_input.send_keys(pozisyon)
        time.sleep(3)