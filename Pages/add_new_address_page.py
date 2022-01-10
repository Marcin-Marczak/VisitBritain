from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class AddNewAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_new_address_page_phone_number_input = (By.ID, "telephone")
        self.add_new_address_page_street_address_line_1_input = (By.ID, "street_1")
        self.add_new_address_page_street_address_line_2_input = (By.ID, "street_2")
        self.add_new_address_page_country_select = (By.ID, "country")
        self.add_new_address_page_city_input = (By.ID, "city")
        self.add_new_address_page_postcode_input = (By.ID, "zip")

    def add_new_address_page_fill_the_form(self, phone_number, street_address_line_1, street_address_line_2, country_value, city, postcode):
        self.driver.find_element(*self.add_new_address_page_phone_number_input).send_keys(phone_number)
        self.driver.find_element(*self.add_new_address_page_street_address_line_1_input).send_keys(street_address_line_1)
        self.driver.find_element(*self.add_new_address_page_street_address_line_2_input).send_keys(street_address_line_2)
        select = Select(self.driver.find_element(*self.add_new_address_page_country_select))
        select.select_by_value(country_value)
        self.driver.find_element(*self.add_new_address_page_city_input).send_keys(city)
        self.driver.find_element(*self.add_new_address_page_postcode_input).send_keys(postcode)
        self.driver.find_element(*self.add_new_address_page_postcode_input).send_keys(Keys.ENTER)
