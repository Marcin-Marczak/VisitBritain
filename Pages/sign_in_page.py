from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class SignInPage(BasePage):

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_form_submit(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.click_on_element(*self.SIGN_IN_BUTTON)
