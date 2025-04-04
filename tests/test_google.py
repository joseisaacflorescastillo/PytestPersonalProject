import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Configurar el WebDriver de Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.letskodeit.com/practice")
    search_box = driver.find_element(By.ID, "autosuggest")
    search_box.send_keys("Pytest Selenium")
    #search_box.submit()
    time.sleep(5)
    assert search_box.is_displayed()

