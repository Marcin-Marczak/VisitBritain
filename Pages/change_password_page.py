from selenium.webdriver.common.by import By
from time import sleep


class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.change_password_page_current_password_input = (By.ID, "current-password")
        self.change_password_page_new_password_input = (By.ID, "password")
        self.change_password_page_confirm_new_password_input = (By.ID, "password-confirmation")
        self.change_password_page_save_button = (By.XPATH, "//button[@title='Save']")
        self.change_password_page_error_message_text = (By.XPATH, "//div[@class='mage-error']")

    def change_password_page_fill_the_form(self, current_password, new_password, confirm_new_password):
        self.driver.find_element(*self.change_password_page_current_password_input).send_keys(current_password)
        self.driver.find_element(*self.change_password_page_new_password_input).send_keys(new_password)
        self.driver.find_element(*self.change_password_page_confirm_new_password_input).send_keys(confirm_new_password)
        self.driver.execute_script("window.scroll(0, 700);")
        sleep(0.5)
        self.driver.find_element(*self.change_password_page_save_button).click()
        sleep(1)

    def change_password_page_get_validation_error_text(self):
        return self.driver.find_elements(*self.change_password_page_error_message_text)
