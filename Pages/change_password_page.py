from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver

        self.current_password_input = (By.ID, "current-password")
        self.new_password_input = (By.ID, "password")
        self.confirm_new_password_input = (By.ID, "password-confirmation")

    def fill_form_submit(self, current_password, new_password, confirm_new_password):
        self.driver.find_element(*self.current_password_input).send_keys(current_password)
        self.driver.find_element(*self.new_password_input).send_keys(new_password)
        self.driver.find_element(*self.confirm_new_password_input).send_keys(confirm_new_password)

        self.driver.find_element(*self.confirm_new_password_input).send_keys(Keys.ENTER)
