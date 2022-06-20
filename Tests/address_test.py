import pytest
import allure
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.address_book_page import AddressBookPage
from Pages.add_new_address_page import AddNewAddressPage
from Config.config_reader import get_config_data as data
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class TestAddress:
    @pytest.mark.smoke
    @allure.title("Add new address")
    @allure.description("Check if user is able to add new address using valid data")
    def test_address_add_new_address(self):
        main_page = MainPage(self.driver)
        sign_in = SignInPage(self.driver)
        account = AccountPage(self.driver)
        address_book = AddressBookPage(self.driver)
        add_new_address = AddNewAddressPage(self.driver)

        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]
        country_value = "AD"

        phone_number_to_input = generate_phone_number()
        street_address_line1_to_input = generate_street_address_line1()
        street_address_line2_to_input = generate_street_address_line2()
        city_to_input = generate_city()
        postcode_to_input = generate_postcode()

        main_page.open_main_page_and_accept_cookies()
        main_page.go_to_sign_in_page()

        sign_in.fill_form_submit(email, password)

        account.go_to_address_book_page()

        address_book.go_to_add_new_address_page()

        add_new_address.fill_form_submit(phone_number_to_input, street_address_line1_to_input,
                                         street_address_line2_to_input, country_value, city_to_input, postcode_to_input)

        street_address_line1_to_assert = address_book.get_street_address_line_1_from_additional_addresses()
        street_address_line2_to_assert = address_book.get_street_address_line_2_from_additional_addresses()

        assert street_address_line1_to_assert == street_address_line1_to_input
        assert street_address_line2_to_assert == street_address_line2_to_input
