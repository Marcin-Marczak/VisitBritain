from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AccountPage(BasePage):

    SIGN_OUT_LINK = (By.XPATH, "//a[contains(@href, 'logout')]")
    FIRST_AND_LAST_NAME_TEXT = (By.XPATH, "//div[@class='box box-information']//p")
    EDIT_ACCOUNT_INFORMATION_LINK = (By.XPATH, "//div[@class='box box-information']//a")
    CHANGE_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, 'changepass')]")
    ADDRESS_BOOK_LINK = (By.XPATH, "//a[contains(@href, 'address')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sign_out(self):
        self.click_on_element(*self.SIGN_OUT_LINK)

    def go_to_change_password_page(self):
        self.click_on_element(*self.CHANGE_PASSWORD_LINK)

    def go_to_account_information_page(self):
        self.click_on_element(*self.EDIT_ACCOUNT_INFORMATION_LINK)

    def go_to_address_book_page(self):
        self.click_on_element(*self.ADDRESS_BOOK_LINK)

    def get_name_prefix(self):
        name_prefix = self.driver.find_element(*self.FIRST_AND_LAST_NAME_TEXT).text

        name_prefix = name_prefix.split(" ")
        name_prefix = name_prefix[0]

        return name_prefix

    def get_first_name(self):
        first_name = self.driver.find_element(*self.FIRST_AND_LAST_NAME_TEXT).text

        first_name = first_name.split(" ")
        first_name = first_name[1]

        return first_name

    def get_last_name(self):
        last_name = self.driver.find_element(*self.FIRST_AND_LAST_NAME_TEXT).text

        last_name = last_name.split(" ")
        last_name = last_name[2]
        last_name = last_name.split("\n")
        last_name = last_name[0]

        return last_name
