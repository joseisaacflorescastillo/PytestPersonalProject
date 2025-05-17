import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service, Service
from webdriver_manager.chrome import ChromeDriverManager


def test():
    '''
    Old Syntax
    -------------------------------------------------------------------------------------------------------------------------------
    chrome_service = Chrome_Service(executable_path="/Users/jose.flores/Documents/Repos/PytestPersonalProject/Drivers/geckodriver")
    # Instantiate Browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    -------------------------------------------------------------------------------------------------------------------------------
    '''

    # New Syntax
    driver = webdriver.Chrome()
    # Open provided URL
    driver.get("https://www.letskodeit.com")
    time.sleep(5)


class RunChromeTests():
    pass

run_tests = RunChromeTests()
test()