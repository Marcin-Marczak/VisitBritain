from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from Pages.base_page import BasePage
from Config.config_reader import get_config_data as data


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.main_page_sign_in_link = (By.ID, "block-account-link-block")
        self.main_page_accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    def open_main_page_and_accept_cookies(self):
        self.driver.get(data("configuration_data.json")["base_url"])
        self.driver.implicitly_wait(20)
        sleep(1)
        cookies = self.driver.find_element(*self.main_page_accept_cookies_button)
        base_page = BasePage(self.driver)
        wait = base_page.set_web_driver_wait()
        wait.until(ec.element_to_be_clickable, cookies)
        cookies.click()

    def main_page_go_to_sign_in_page(self):
        base_page = BasePage(self.driver)
        wait = base_page.set_web_driver_wait()
        current_url = self.driver.current_url
        sign_in = self.driver.find_element(*self.main_page_sign_in_link)
        wait.until(ec.visibility_of_element_located, sign_in)
        sign_in.click()
        wait.until(lambda url: self.driver.current_url != current_url)
