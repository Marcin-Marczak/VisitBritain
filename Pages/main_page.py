from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Config.config_reader import configuration_data as cd


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.main_page_sign_in_link = (By.XPATH, "//a[contains(@href, 'account/login')]")
        self.main_page_close_cookies_button = (By.XPATH, "//button[contains(@class, 'banner-close-button')]")

    def open_main_page_and_close_cookies(self):
        self.driver.get(cd()["base_url"])
        self.driver.implicitly_wait(20)
        sleep(1)
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(ec.element_to_be_clickable, self.driver.find_element(*self.main_page_close_cookies_button))
        self.driver.find_element(*self.main_page_close_cookies_button).click()

    def main_page_go_to_sign_in_page(self):
        current_url = self.driver.current_url
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(ec.visibility_of_element_located, self.driver.find_element(*self.main_page_sign_in_link))
        self.driver.find_element(*self.main_page_sign_in_link).click()
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(lambda url_has_changed: self.driver.current_url != current_url)
