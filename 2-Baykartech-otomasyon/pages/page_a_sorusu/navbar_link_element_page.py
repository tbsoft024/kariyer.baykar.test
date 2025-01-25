import requests
from bs4 import BeautifulSoup
import pytest

class NavbarPage:
    def __init__(self, driver):
        self.driver = driver

    def element_link_dogrulama(self, url):
        print(f"Test başlatıldı: {url}")
        self.driver.get(url)

        # Sayfanın HTML kaynağını al
        html_source = self.driver.page_source
        # Soup ile HTML yi parse et
        soup = BeautifulSoup(html_source, 'html.parser')
        # Navbar içindeki tüm <a> etiketlerini bul
        navbar = soup.find(id="navbarHeaderNav")
        navbar_links = navbar.find_all("a")
        print(f"Toplam navbar link sayısı: {len(navbar_links)}")

        # Döngü: Her bir linki tıkla doğrula geri dön
        for link in navbar_links:
            try:
                # Link URL'sini al
                link_url = link.get('href')
                print(f"İşlem yapılacak link:{link_url}")

                # Mega menü dışındaki linkler için kontrol
                if link_url.startswith("http"):
                    self.driver.get(link_url)
                else:
                    full_url = f"{url + link_url}"
                    self.driver.get(full_url)

                # Sayfa durumunu kontrol et
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"{full_url} - Sayfa başarıyla açıldı (200 OK).")
                else:
                    print(f"{full_url} - Sayfa açılmadı, HTTP Durum Kodu: {response.status_code}")

                # Sayfadan geri dön
                print("Geri dönüldü.")
                # time.sleep(3) sayfaları geçişlerini bekleterek yapılmak istenirse time eklenebilir.
                self.driver.back()

            except Exception as e:
                pytest.fail(f"Menü öğesine tıklanırken hata oluştu: {e}")