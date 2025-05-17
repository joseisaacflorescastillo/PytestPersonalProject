from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService


def test():
    ff_service = FFService(executable_path="/Users/jose.flores/Documents/Repos/PytestPersonalProject/Drivers/geckodriver")
    # Instantiate Browser
    driver = webdriver.Firefox(service=ff_service)
    # Open provided URL
    driver.get("https://www.letskodeit.com")


class RunFFTests():
    pass


run_tests = RunFFTests()
test()