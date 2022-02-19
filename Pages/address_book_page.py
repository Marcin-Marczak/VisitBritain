from selenium.webdriver.common.by import By
from time import sleep


class AddressBookPage:
    def __init__(self, driver):
        self.driver = driver
        self.address_book_additional_address_street_address = (By.XPATH, "//td[@class='col streetaddress']")
        self.address_book_page_add_new_address_button = (By.CSS_SELECTOR, "[role=add-address]")

    def address_book_page_go_to_add_new_address_page(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        sleep(0.5)
        self.driver.find_element(*self.address_book_page_add_new_address_button).click()

    def address_book_page_get_street_address_line1_from_additional_addresses(self):
        street_address_line1 = self.driver.find_element(*self.address_book_additional_address_street_address)
        street_address_line1 = street_address_line1.get_attribute("textContent")
        street_address_line1 = street_address_line1[:street_address_line1.find(",")]
        return street_address_line1

    def address_book_page_get_street_address_line2_from_additional_addresses(self):
        street_address_line2 = self.driver.find_element(*self.address_book_additional_address_street_address)
        street_address_line2 = street_address_line2.get_attribute("textContent")
        street_address_line2 = street_address_line2[street_address_line2.find(",")+2:]
        return street_address_line2
