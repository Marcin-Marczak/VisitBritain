from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_page_sign_out_link = (By.XPATH, "//a[contains(@href, 'account/logout')]")
        self.account_change_password_link = (By.XPATH, "//a[contains(@href, '/changepass/1/')]")

    def account_page_sign_out(self):
        self.driver.find_element(*self.account_page_sign_out_link).click()

    def account_page_go_to_change_password_page(self):
        self.driver.find_element(*self.account_change_password_link).click()
