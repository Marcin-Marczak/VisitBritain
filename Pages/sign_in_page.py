from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "pass")
        self.sign_in_button = (By.ID, "send2")

    def fill_form_submit(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

        self.click_on_element(*self.sign_in_button)
