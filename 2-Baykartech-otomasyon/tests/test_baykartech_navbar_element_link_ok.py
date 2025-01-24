import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBaykartechOtomasyon:

    @pytest.mark.usefixtures("setup")
    def test_A_navbar_element_link_ok(self):
        try:
            # Navbar elementini bekle ve bul
            navbar = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "navbarHeaderNav"))
            )

            # Navbar menü öğelerinin XPATH'i
            navbar_xpath = "//div[@id='navbarHeaderNav']//a"
            navbar_links = self.driver.find_elements(By.XPATH, navbar_xpath)

            # Her öğeyi tıklayıp geri dön
            for link in navbar_links:
                try:
                    self.driver.get("https://baykartech.com/")
                    # Menü öğesinin tıklanabilir olmasını bekle
                    WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable(link)
                    )

                    # Tıklanabilir olduğunda tıkla
                    link.click()

                    # Geri dön
                    self.driver.back()

                    # Menü öğelerini tekrar bul (sayfa yeniden yüklendiği için)
                    navbar_links = self.driver.find_elements(By.XPATH, navbar_xpath)

                except TimeoutException:
                    pytest.fail(f"Menü öğesine tıklanırken zaman aşımı: {link.text}")
                except Exception as e:
                    pytest.fail(f"Menü işlenirken hata oluştu: {e}")

        except TimeoutException:
            pytest.fail("Navbar öğesi bulunamadı veya zaman aşımına uğradı.")
        except Exception as e:
            pytest.fail(f"Genel hata oluştu: {e}")
