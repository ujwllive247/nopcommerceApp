
from selenium import webdriver
import pytest



@pytest.fixture()
def setup(browser):
    if browser == "chrome":

        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver




# ✅ This is a pytest hook, not a fixture
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
