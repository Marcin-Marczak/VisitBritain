from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.base_page import BasePage
from Config.config_reader import get_config_data as data


class MainPage(BasePage):

    SIGN_IN_LINK = (By.ID, "block-account-link-block")
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page_and_accept_cookies(self):
        self.driver.get(data("config.json")["base_url"])
        sleep(1)

        self.click_on_element(*self.ACCEPT_COOKIES_BUTTON)

    def go_to_sign_in_page(self):
        wait = self.set_web_driver_wait()
        sign_in = self.driver.find_element(*self.SIGN_IN_LINK)
        current_url = self.driver.current_url

        wait.until(ec.visibility_of_element_located, sign_in)
        self.click_on_element(*self.SIGN_IN_LINK)

        wait.until(lambda url: self.driver.current_url != current_url)
