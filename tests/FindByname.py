from selenium import webdriver
from selenium.webdriver.common.by import By

from broser_drivers.firefox_driver_mac import run_tests


class FindByName():
    def test(self) -> None:
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        driver.maximize_window()

        # Find element by name
        element = driver.find_element(By.ID, "displayed-text")
        if element is not None:
            print("Element found by name")

        element_by_name = driver.find_element(By.NAME, "show-hide")
        if element_by_name is not None:
            print("Element found by name")


run_tests = FindByName()
run_tests.test()