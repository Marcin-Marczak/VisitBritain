from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.sign_out_link = (By.XPATH, "//a[contains(@href, 'logout')]")
        self.first_and_last_name_text = (By.XPATH, "//div[@class='box box-information']//p")
        self.edit_account_information_link = (By.XPATH, "//div[@class='box box-information']//a")
        self.change_password_link = (By.XPATH, "//a[contains(@href, 'changepass')]")
        self.address_book_link = (By.XPATH, "//a[contains(@href, 'address')]")

    def sign_out(self):
        self.click_on_element(*self.sign_out_link)

    def go_to_change_password_page(self):
        self.click_on_element(*self.change_password_link)

    def go_to_account_information_page(self):
        self.click_on_element(*self.edit_account_information_link)

    def go_to_address_book_page(self):
        self.click_on_element(*self.address_book_link)

    def get_name_prefix(self):
        name_prefix = self.driver.find_element(*self.first_and_last_name_text).text

        name_prefix = name_prefix.split(" ")
        name_prefix = name_prefix[0]

        return name_prefix

    def get_first_name(self):
        first_name = self.driver.find_element(*self.first_and_last_name_text).text

        first_name = first_name.split(" ")
        first_name = first_name[1]

        return first_name

    def get_last_name(self):
        last_name = self.driver.find_element(*self.first_and_last_name_text).text

        last_name = last_name.split(" ")
        last_name = last_name[2]
        last_name = last_name.split("\n")
        last_name = last_name[0]

        return last_name
