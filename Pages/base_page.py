from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Config.config_reader import get_config_data as data


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page_error_message_text = (By.XPATH, "//div[@class='mage-error']")

    def base_page_set_web_driver_wait(self):
        wait = WebDriverWait(self.driver, data("configuration_data.json")["timeout"],
                             data("configuration_data.json")["pool_frequency"])
        return wait

    def base_page_get_validation_error_texts(self):
        errors = self.driver.find_elements(*self.base_page_error_message_text)
        wait = BasePage.base_page_set_web_driver_wait(self)
        wait.until(lambda errors_text: "." in errors[0].text)
        return errors
