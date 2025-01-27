import pytest
from pages.page_c_sorusu.kariyer_baykartech_acik_pozisyon_filtreleme_page import BirimPozisyonFiltrelePage
from pages.page_c_sorusu.kariyer_baykartech_acik_pozisyon_birim_ve_pozisyon_data_cek_page import BirimPozisyonDataPage
input_pozisyon_birim= [
    ("DevOps Mühendisi", "Web Yazılım Teknolojileri"),
    ("Kalite Kontrol Teknisyeni", "Mekanik İmalat")
]
@pytest.mark.parametrize("pozisyon, birim", input_pozisyon_birim)
@pytest.mark.usefixtures("setup")
class TestBirimPozisyonFiltreleme:

    def test_acik_pozisyonlarda_birim_pozisyon_filtreleme(self, pozisyon, birim):
        url = "https://kariyer.baykartech.com/tr/open-positions/?type=1"
        birim_pozisyon_filtrele_page = BirimPozisyonFiltrelePage(self.driver)
        birim_pozisyon_csv_data_al = BirimPozisyonDataPage(self.driver)

        birim_pozisyon_csv_data_al.get_pozisyonlari_csv_yaz(url)

        birim_pozisyon_filtrele_page.birim_pozisyon_filtrele(url, pozisyon, birim)
