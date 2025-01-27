import pytest
from pages.page_b_sorusu.dil_degis_site_icerigini_kontrol_et_page import DilKontrolPage

# Statik dil seçenekleri
dil = {
    "TR": {"url": "/tr/", "baslik": "Biz Baykarız"},
    "EN": {"url": "/en/", "baslik": "We Are Baykar"}
}

@pytest.mark.usefixtures("setup")
class TestDilElementKontrol:

    def test_dil_degis_kontrol_et(self):

        url = "https://baykartech.com"
        dil_kontrol_page = DilKontrolPage(self.driver)
        dil_kontrol_page.statik_dil_degis_ve_kontrol_et(url, dil)
