import csv
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BirimPozisyonDataPage:
    def __init__(self, driver):
        self.driver = driver

    # def get_birimler_csv_yaz(self, url):
    #     self.driver.get(url)
    #     # Birimleri bul
    #     ul_element = self.driver.find_element(By.ID, "myUL2")
    #
    #     # Tüm checkbox'lar içindeki label'ları bul
    #     labels = ul_element.find_elements(By.CSS_SELECTOR, "li .form-check-label")
    #
    #     # CSV dosyasına yazma işlemi
    #     with open('./data/birimler_data.csv', mode='w', newline='', encoding='utf-8') as file:
    #         writer = csv.writer(file)
    #         for label in labels:
    #             # Her birimin adını al ve dosyaya yaz
    #             birim_adi = label.text.replace('"', '')
    #             writer.writerow([birim_adi])

    def get_pozisyonlari_csv_yaz(self, url):
        self.driver.get(url)

        # CSV dosyasını açın
        with open('./data/pozisyon_birim_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='|')  # Pipe (|) karakterini ayırıcı olarak kullanıyoruz
            while True:
                work_boxes = self.driver.find_elements(By.CSS_SELECTOR, "#filterOpenPositions > div > div")

                for work_box in work_boxes:
                    try:
                        pozisyon_adi = work_box.find_element(By.TAG_NAME, 'h3').text.strip()
                        birim_adi = work_box.find_element(By.TAG_NAME, 'h4').text.strip()
                        writer.writerow([pozisyon_adi, birim_adi])
                    except Exception as e:
                        print(f"Error occurred while extracting position/birim: {e}")
                        continue

                try:
                    next_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "nextPageLink"))
                    )

                    # Eğer Sonraki buton görünüyorsa, tıkla
                    if next_button.is_displayed():
                        self.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                        self.driver.execute_script("arguments[0].click();", next_button)
                        time.sleep(2)  # Sayfa geçişini bekle
                    else:
                        print("Sonraki düğmesi devre dışı, işlem tamamlandı.")
                        break

                except Exception as e:
                    print(f"Sonraki buton bulunamadı {e}")
                    break