from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_page_sign_out_link = (By.XPATH, "//a[contains(@href, 'logout')]")
        self.account_page_first_and_last_name_text = (By.XPATH, "//div[@class='box box-information']//p")
        self.account_page_edit_account_information_link = (By.XPATH, "//div[@class='box box-information']//a")
        self.account_page_change_password_link = (By.XPATH, "//a[contains(@href, 'changepass')]")
        self.account_page_address_book_link = (By.XPATH, "//a[contains(@href, 'address')]")

    def account_page_sign_out(self):
        self.driver.find_element(*self.account_page_sign_out_link).click()

    def account_page_go_to_change_password_page(self):
        self.driver.find_element(*self.account_page_change_password_link).click()

    def account_page_go_to_account_information_page(self):
        self.driver.find_element(*self.account_page_edit_account_information_link).click()

    def account_page_go_to_address_book_page(self):
        self.driver.find_element(*self.account_page_address_book_link).click()

    def account_page_get_name_prefix(self):
        name_prefix = self.driver.find_element(*self.account_page_first_and_last_name_text).text
        name_prefix = name_prefix.split(" ")
        name_prefix = name_prefix[0]
        return name_prefix

    def account_page_get_first_name(self):
        first_name = self.driver.find_element(*self.account_page_first_and_last_name_text).text
        first_name = first_name.split(" ")
        first_name = first_name[1]
        return first_name

    def account_page_get_last_name(self):
        last_name = self.driver.find_element(*self.account_page_first_and_last_name_text).text
        last_name = last_name.split(" ")
        last_name = last_name[2]
        last_name = last_name.split("\n")
        last_name = last_name[0]
        return last_name
