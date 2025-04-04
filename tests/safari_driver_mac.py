from selenium import webdriver


def test():
    # Instantiate Safari Browser Command
    driver = webdriver.Safari()
    # Open the provided URL
    driver.get("http://www.letskodeit.com")


class SafariDriverMac:
    pass

sf = SafariDriverMac()
test()