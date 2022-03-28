from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Config.config_reader import get_config_data as data


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.base_page_error_message_text = (By.XPATH, "//div[@class='mage-error']")

    def click_on_element(self, *element):
        self.driver.find_element(*element).click()

    def set_web_driver_wait(self):
        timeout = data("configuration_data.json")["timeout"]
        pool_frequency = data("configuration_data.json")["pool_frequency"]

        return WebDriverWait(self.driver, timeout, pool_frequency)

    def get_validation_error_texts(self):
        errors = self.driver.find_elements(*self.base_page_error_message_text)

        wait = BasePage.set_web_driver_wait(self)
        wait.until(lambda errors_text: "." in errors[0].text)

        return errors
