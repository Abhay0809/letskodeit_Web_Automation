import pytest
from selenium import webdriver
import time
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     baseUrl = "https://www.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseUrl)
    #     print("Running tests on FF")
    # else:
    #     baseUrl = "https://www.letskodeit.com/"
    #     driver = webdriver.Chrome()
    #     driver.get(baseUrl)
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")