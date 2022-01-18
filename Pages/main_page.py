from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Config.config_reader import configuration_data as cd


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.main_page_sign_in_link = (By.ID, "block-account-link-block")
        self.main_page_accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")

    def open_main_page_and_accept_cookies(self):
        self.driver.get(cd()["base_url"])
        self.driver.implicitly_wait(20)
        sleep(1)
        cookies = self.driver.find_element(*self.main_page_accept_cookies_button)
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(ec.element_to_be_clickable, cookies)
        cookies.click()

    def main_page_go_to_sign_in_page(self):
        current_url = self.driver.current_url
        sign_in = self.driver.find_element(*self.main_page_sign_in_link)
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(ec.visibility_of_element_located, sign_in)
        sign_in.click()
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(lambda url: self.driver.current_url != current_url)
