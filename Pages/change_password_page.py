from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from Config.config_reader import configuration_data as cd


class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.change_password_page_current_password_input = (By.ID, "current-password")
        self.change_password_page_new_password_input = (By.ID, "password")
        self.change_password_page_confirm_new_password_input = (By.ID, "password-confirmation")
        self.change_password_page_error_message_text = (By.XPATH, "//div[@class='mage-error']")

    def change_password_page_fill_the_form(self, current_password, new_password, confirm_new_password):
        self.driver.find_element(*self.change_password_page_current_password_input).send_keys(current_password)
        self.driver.find_element(*self.change_password_page_new_password_input).send_keys(new_password)
        self.driver.find_element(*self.change_password_page_confirm_new_password_input).send_keys(confirm_new_password)
        self.driver.find_element(*self.change_password_page_confirm_new_password_input).send_keys(Keys.ENTER)

    def change_password_page_get_validation_error_text(self):
        error = self.driver.find_elements(*self.change_password_page_error_message_text)
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(lambda errors: "." in error[0].text)
        return error
