import pytest
import os
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Config.config_reader import configuration_data as cd


options = Options()

options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

ob = Screenshot_Clipping.Screenshot()


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path=cd()["chromedriver_executable_path"], options=options)
    driver.implicitly_wait(30)
    driver.set_window_size(1500, 800)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        current_test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].replace("test_", "")
        screenshots_path = cd()["screenshots_path"]
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_" + current_test_name
        screenshot_name = timestamp + ".png"
        ob.full_Screenshot(driver, save_path=screenshots_path, image_name=screenshot_name)
    driver.quit()
