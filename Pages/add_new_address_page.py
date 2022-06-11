from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class AddNewAddressPage:

    PHONE_NUMBER_INPUT = (By.ID, "telephone")
    STREET_ADDRESS_LINE1_INPUT = (By.ID, "street_1")
    STREET_ADDRESS_LINE2_INPUT = (By.ID, "street_2")
    COUNTRY_SELECT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    POSTCODE_INPUT = (By.ID, "zip")

    def __init__(self, driver):
        self.driver = driver

    def fill_form_submit(self, phone_number, street_address_line1, street_address_line2, country_value, city, postcode):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.driver.find_element(*self.STREET_ADDRESS_LINE1_INPUT).send_keys(street_address_line1)
        self.driver.find_element(*self.STREET_ADDRESS_LINE2_INPUT).send_keys(street_address_line2)

        select = Select(self.driver.find_element(*self.COUNTRY_SELECT))
        select.select_by_value(country_value)

        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.POSTCODE_INPUT).send_keys(postcode)

        self.driver.find_element(*self.POSTCODE_INPUT).send_keys(Keys.ENTER)
