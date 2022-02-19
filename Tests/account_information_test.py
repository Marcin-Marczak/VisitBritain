import pytest
from Pages.base_page import BasePage
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.edit_account_information_page import EditAccountInformationPage
from Config.config_reader import get_config_data as data
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class AccountInformationSetup:
    def account_information_setup(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_accept_cookies()
        main_page.main_page_go_to_sign_in_page()
        sign_in = SignInPage(self.driver)
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]
        sign_in.sign_in_page_fill_the_form(email, password)


class TestAccountInformation(AccountInformationSetup):
    @pytest.mark.smoke
    def test_change_account_information_valid_first_name_and_last_name(self):
        AccountInformationSetup.account_information_setup(self)
        account_page = AccountPage(self.driver)
        first_name_before_test = account_page.account_page_get_first_name()
        last_name_before_test = account_page.account_page_get_last_name()
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = generate_last_name()
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix_to_input,
                                                                             first_name_to_input, last_name_to_input,
                                                                             "submit")
        name_prefix_after_submit = account_page.account_page_get_name_prefix()
        first_name_after_submit = account_page.account_page_get_first_name()
        last_name_after_submit = account_page.account_page_get_last_name()
        assert first_name_before_test != first_name_after_submit
        assert last_name_before_test != last_name_after_submit
        assert first_name_to_input == first_name_after_submit
        assert last_name_to_input == last_name_after_submit
        assert name_prefix_to_input == name_prefix_after_submit

    def test_change_account_information_valid_first_name_and_last_name_and_go_back_without_submit(self):
        AccountInformationSetup.account_information_setup(self)
        account_page = AccountPage(self.driver)
        first_name_before_test = account_page.account_page_get_first_name()
        last_name_before_test = account_page.account_page_get_last_name()
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = generate_last_name()
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix_to_input, first_name_to_input,
                                                                             last_name_to_input,
                                                                             "go_back_without_submit")
        first_name_after_submit = account_page.account_page_get_first_name()
        last_name_after_submit = account_page.account_page_get_last_name()
        assert first_name_before_test == first_name_after_submit
        assert last_name_before_test == last_name_after_submit

    def test_change_account_information_first_name_blank(self):
        AccountInformationSetup.account_information_setup(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = ""
        last_name_to_input = generate_last_name()
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix_to_input, first_name_to_input,
                                                                             last_name_to_input, "submit")
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("validation_error_texts.json")["required_field_error_text"]
        assert validation_error_text == required_field_error_text

    def test_change_account_information_last_name_blank(self):
        AccountInformationSetup.account_information_setup(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = ""
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix_to_input, first_name_to_input,
                                                                             last_name_to_input, "submit")
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("validation_error_texts.json")["required_field_error_text"]
        assert validation_error_text == required_field_error_text

    def test_change_account_information_first_name_and_last_name_blank(self):
        AccountInformationSetup.account_information_setup(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = ""
        last_name_to_input = ""
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix_to_input, first_name_to_input,
                                                                             last_name_to_input, "submit")
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        number_of_validation_error_texts = len(validation_error_texts)
        required_field_error_text = data("validation_error_texts.json")["required_field_error_text"]
        assert number_of_validation_error_texts == 2
        for i in validation_error_texts:
            assert required_field_error_text in i.get_attribute("textContent")
