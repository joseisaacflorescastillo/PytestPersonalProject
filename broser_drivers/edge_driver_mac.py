import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as Edge_Service


def test():
    edge_service = Edge_Service(executable_path="/Users/jose.flores/Documents/Repos/PytestPersonalProject/Drivers/geckodriver")
    # Instantiate Browser
    driver = webdriver.Edge(service=edge_service)
    # Open provided URL
    driver.get("https://www.letskodeit.com")
    time.sleep(5)


class RunEdgeTests():
    pass


run_tests = RunEdgeTests()
test()