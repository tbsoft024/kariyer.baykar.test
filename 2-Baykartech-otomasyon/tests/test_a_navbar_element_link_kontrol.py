import pytest

from pages.page_a_sorusu.navbar_link_element_page import NavbarPage


@pytest.mark.usefixtures("setup")
class TestBaykartechOtomasyon:

    def test_navbar_element_link_kontrol(self):
        url = "https://baykartech.com"

        navbar_page = NavbarPage(self.driver)
        navbar_page.element_link_dogrulama(url)
