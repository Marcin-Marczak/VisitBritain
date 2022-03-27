from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.base_page import BasePage
from Config.config_reader import get_config_data as data


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.main_page_sign_in_link = (By.ID, "block-account-link-block")
        self.main_page_accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    def open_main_page_and_accept_cookies(self):
        wait = self.set_web_driver_wait()
        base_url = data("configuration_data.json")["base_url"]

        self.driver.get(base_url)

        cookies = self.driver.find_element(*self.main_page_accept_cookies_button)
        wait.until(ec.element_to_be_clickable, cookies)
        cookies.click()

    def go_to_sign_in_page(self):
        wait = self.set_web_driver_wait()
        sign_in = self.driver.find_element(*self.main_page_sign_in_link)
        current_url = self.driver.current_url

        wait.until(ec.visibility_of_element_located, sign_in)
        sign_in.click()

        wait.until(lambda url: self.driver.current_url != current_url)
