import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://baykartech.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()