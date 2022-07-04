import pytest
from datetime import datetime
from Drivers.browser_random_choice import BrowserRandomChoice
from Screenshots.get_screenshots_path import *


def create_screenshot_name():
    test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].replace("test_", "")
    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    screenshot_name = f"{current_time}_{test_name}"
    return f"{screenshot_name}.png"


@pytest.fixture()
def setup(request):
    driver = BrowserRandomChoice.browser_random_choice()

    driver.implicitly_wait(30)
    driver.set_window_size(1500, 800)

    request.cls.driver = driver

    before_failed = request.session.testsfailed
    yield

    if request.session.testsfailed != before_failed:
        screenshot_path = get_screenshots_path()
        driver.get_screenshot_as_file(f"{screenshot_path}/{create_screenshot_name()}")

    driver.quit()
