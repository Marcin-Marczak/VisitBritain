from time import sleep
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AddressBookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.street_address_text = (By.XPATH, "//td[@class='col streetaddress']")
        self.add_new_address_button = (By.CSS_SELECTOR, "[role=add-address]")

    def go_to_add_new_address_page(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        sleep(0.5)

        self.click_on_element(*self.add_new_address_button)

    def get_street_address_line_1_from_additional_addresses(self):
        street_address_line_1 = self.driver.find_element(*self.street_address_text)

        street_address_line_1 = street_address_line_1.get_attribute("textContent")
        street_address_line_1 = street_address_line_1[:street_address_line_1.find(",")]

        return street_address_line_1

    def get_street_address_line_2_from_additional_addresses(self):
        street_address_line_2 = self.driver.find_element(*self.street_address_text)

        street_address_line_2 = street_address_line_2.get_attribute("textContent")
        street_address_line_2 = street_address_line_2[street_address_line_2.find(",")+2:]

        return street_address_line_2
