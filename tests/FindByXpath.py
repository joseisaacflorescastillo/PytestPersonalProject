from selenium import webdriver
from selenium.webdriver.common.by import By


def test() -> None:
    baseURL = "https://www.letskodeit.com/practice"
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Find element by name
    element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
    if element is not None:
        print("Element found by XPATH")

    element_by_name = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
    if element_by_name is not None:
        print("Element found by CSS_SELECTOR")


class FindByXPATH:
    test()


run_different_find_by_xpath_instance = FindByXPATH()
test()