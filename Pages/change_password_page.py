from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ChangePasswordPage:

    CURRENT_PASSWORD_INPUT = (By.ID, "current-password")
    NEW_PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_NEW_PASSWORD_INPUT = (By.ID, "password-confirmation")

    def __init__(self, driver):
        self.driver = driver

    def fill_form_submit(self, current_password, new_password, confirm_new_password):
        self.driver.find_element(*self.CURRENT_PASSWORD_INPUT).send_keys(current_password)
        self.driver.find_element(*self.NEW_PASSWORD_INPUT).send_keys(new_password)
        self.driver.find_element(*self.CONFIRM_NEW_PASSWORD_INPUT).send_keys(confirm_new_password)

        self.driver.find_element(*self.CONFIRM_NEW_PASSWORD_INPUT).send_keys(Keys.ENTER)
