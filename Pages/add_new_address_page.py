from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class AddNewAddressPage:
    def __init__(self, driver):
        self.driver = driver

        self.phone_number_input = (By.ID, "telephone")
        self.street_address_line1_input = (By.ID, "street_1")
        self.street_address_line2_input = (By.ID, "street_2")
        self.country_select = (By.ID, "country")
        self.city_input = (By.ID, "city")
        self.postcode_input = (By.ID, "zip")

    def fill_form_submit(self, phone_number, street_address_line1, street_address_line2, country_value, city, postcode):
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
        self.driver.find_element(*self.street_address_line1_input).send_keys(street_address_line1)
        self.driver.find_element(*self.street_address_line2_input).send_keys(street_address_line2)

        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_value(country_value)

        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)

        self.driver.find_element(*self.postcode_input).send_keys(Keys.ENTER)
