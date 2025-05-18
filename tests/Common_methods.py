from selenium import webdriver
from selenium.webdriver.common.by import By


def test() -> None:
    baseURL = "https://www.letskodeit.com/practice"
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.current_url)
    driver.close()
    driver.quit()


class FindByXPATH:
    test()


run_different_find_by_xpath_instance = FindByXPATH()
test()