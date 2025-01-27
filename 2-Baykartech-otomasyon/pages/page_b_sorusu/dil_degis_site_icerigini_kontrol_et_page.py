from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DilKontrolPage:

    def __init__(self, driver):
        self.driver = driver

    def statik_dil_degis_ve_kontrol_et(self, url, dil):
       # Statik kaç tane dil varsa o kadar dön
       for dil_kodu, dil_data in dil.items():
            # url oluştur ve sayfayı ziyaret et
            dil_url = f"{url + dil_data['url']}"
            self.driver.get(dil_url)

            # url yönlendirme kontrolü
            current_url = self.driver.current_url
            assert dil_data["url"] in current_url, f"{dil_kodu} sayfasına geçilemedi: {current_url}"
            try:
                # Başlık kontrolü
                baslik = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "h1"))
                )
                print(f"{dil_kodu}, - Bulunan başlık: {baslik.text}")
                assert dil_data["baslik"] in baslik.text, f"{dil_kodu} için başlık hatalı: {baslik.text}"
            except Exception as e:
                print("Başlık kontrolü başarısız oldu: %s", e)