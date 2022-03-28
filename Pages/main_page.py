from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.base_page import BasePage
from Config.config_reader import get_config_data as data


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.sign_in_link = (By.ID, "block-account-link-block")
        self.accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    def open_main_page_and_accept_cookies(self):
        base_url = data("configuration_data.json")["base_url"]

        self.driver.get(base_url)
        sleep(1)
        self.click_on_element(*self.accept_cookies_button)

    def go_to_sign_in_page(self):
        wait = self.set_web_driver_wait()
        sign_in = self.driver.find_element(*self.sign_in_link)
        current_url = self.driver.current_url

        wait.until(ec.visibility_of_element_located, sign_in)
        self.click_on_element(*self.sign_in_link)

        wait.until(lambda url: self.driver.current_url != current_url)
