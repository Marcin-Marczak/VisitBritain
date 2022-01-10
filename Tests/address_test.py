import pytest
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.address_book_page import AddressBookPage
from Pages.add_new_address_page import AddNewAddressPage
from Config.config_reader import valid_test_data as vtd
from Config.config_reader import env
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class TestAddress:
    @pytest.mark.smoke
    def test_address_add_new_address(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_accept_cookies()
        main_page.main_page_go_to_sign_in_page()
        sign_in = SignInPage(self.driver)
        sign_in.sign_in_page_fill_the_form(vtd()["email"], env()["password"])
        account = AccountPage(self.driver)
        account.account_page_go_to_address_book_page()
        address_book = AddressBookPage(self.driver)
        address_book.address_book_page_go_to_add_new_address_page()
        add_new_address = AddNewAddressPage(self.driver)
        street_address_line_1_to_input = street_address_line_1()
        street_address_line_2_to_input = street_address_line_2()
        add_new_address.add_new_address_page_fill_the_form(phone_number=phone_number(),
                                                           street_address_line_1=street_address_line_1_to_input,
                                                           street_address_line_2=street_address_line_2_to_input,
                                                           country_value="AD",
                                                           city=city(), postcode=postcode())
        street_address_line_1_to_assert = address_book.address_book_page_get_street_address_line_1_from_additional_addresses()
        street_address_line_2_to_assert = address_book.address_book_page_get_street_address_line_2_from_additional_addresses()
        assert street_address_line_1_to_assert == street_address_line_1_to_input
        assert street_address_line_2_to_assert == street_address_line_2_to_input
