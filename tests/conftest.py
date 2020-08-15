import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ZestMoneyAssignment.utilities.customLogger as c_log


@pytest.yield_fixture(scope="class")
def beforeClass(request):
    print("Before Class")
    driver = None
    option = Options()
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-infobars")
    option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
    driver = webdriver.Chrome(options=option, executable_path="F:\Drivers\chromedriver.exe")
    log = c_log.customLogger()
    log.info("Chrome browser is initializing")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(2)
    driver.quit()
    print("After Class")


@pytest.yield_fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")