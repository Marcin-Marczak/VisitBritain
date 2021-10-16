from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_page_email_input = (By.ID, "email")
        self.sign_in_page_password_input = (By.ID, "pass")
        self.sign_in_page_sign_in_button = (By.ID, "send2")

    def sign_in_page_fill_the_form(self, email, password):
        self.driver.find_element(*self.sign_in_page_email_input).send_keys(email)
        self.driver.find_element(*self.sign_in_page_password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_page_sign_in_button).click()