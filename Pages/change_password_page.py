from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.change_password_page_current_password_input = (By.ID, "current-password")
        self.change_password_page_new_password_input = (By.ID, "password")
        self.change_password_page_confirm_new_password_input = (By.ID, "password-confirmation")

    def change_password_page_fill_the_form(self, current_password, new_password, confirm_new_password):
        self.driver.find_element(*self.change_password_page_current_password_input).send_keys(current_password)
        self.driver.find_element(*self.change_password_page_new_password_input).send_keys(new_password)
        self.driver.find_element(*self.change_password_page_confirm_new_password_input).send_keys(confirm_new_password)
        self.driver.find_element(*self.change_password_page_confirm_new_password_input).send_keys(Keys.ENTER)
