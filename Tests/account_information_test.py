import pytest
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.edit_account_information_page import EditAccountInformationPage
from Config.config_reader import valid_test_data as vtd
from Config.config_reader import validation_error_texts as vet
from Config.config_reader import env
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class AccountInformationCommonCode:
    def account_information_common_code(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_close_cookies()
        main_page.main_page_go_to_sign_in_page()
        sign_in = SignInPage(self.driver)
        sign_in.sign_in_page_fill_the_form(vtd()["email"], env()["password"])


class TestAccountInformation(AccountInformationCommonCode):
    @pytest.mark.smoke
    def test_change_account_information_valid_first_name_and_last_name(self):
        AccountInformationCommonCode.account_information_common_code(self)
        account_page = AccountPage(self.driver)
        first_name_before_test = account_page.account_page_get_first_name()
        last_name_before_test = account_page.account_page_get_last_name()
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_test = name_prefix()
        first_name_to_test = first_name()
        last_name_to_test = last_name()
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix=name_prefix_to_test,
                                                                             first_name=first_name_to_test,
                                                                             last_name=last_name_to_test,
                                                                             submit_or_go_back_without_submit="submit")
        name_prefix_after_test = account_page.account_page_get_name_prefix()
        first_name_after_test = account_page.account_page_get_first_name()
        last_name_after_test = account_page.account_page_get_last_name()
        assert first_name_before_test != first_name_after_test
        assert last_name_before_test != last_name_after_test
        assert first_name_to_test == first_name_after_test
        assert last_name_to_test == last_name_after_test
        assert name_prefix_to_test == name_prefix_after_test

    def test_change_account_information_valid_first_name_and_last_name_and_go_back_without_submit(self):
        AccountInformationCommonCode.account_information_common_code(self)
        account_page = AccountPage(self.driver)
        first_name_before_test = account_page.account_page_get_first_name()
        last_name_before_test = account_page.account_page_get_last_name()
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        name_prefix_to_test = name_prefix()
        first_name_to_test = first_name()
        last_name_to_test = last_name()
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix=name_prefix_to_test,
                                                                             first_name=first_name_to_test,
                                                                             last_name=last_name_to_test,
                                                                             submit_or_go_back_without_submit="go_back_without_submit")
        first_name_after_test = account_page.account_page_get_first_name()
        last_name_after_test = account_page.account_page_get_last_name()
        assert first_name_before_test == first_name_after_test
        assert last_name_before_test == last_name_after_test

    def test_change_account_information_first_name_blank(self):
        AccountInformationCommonCode.account_information_common_code(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix=name_prefix(),
                                                                             first_name="",
                                                                             last_name=last_name(),
                                                                             submit_or_go_back_without_submit="submit")
        validation_error_text = edit_account_information.edit_account_information_page_get_validation_error_text()
        assert validation_error_text[0].get_attribute("textContent") == vet()["required_field_error_text"]

    def test_change_account_information_last_name_blank(self):
        AccountInformationCommonCode.account_information_common_code(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix=name_prefix(),
                                                                             first_name=first_name(),
                                                                             last_name="",
                                                                             submit_or_go_back_without_submit="submit")
        validation_error_text = edit_account_information.edit_account_information_page_get_validation_error_text()
        assert validation_error_text[0].get_attribute("textContent") == vet()["required_field_error_text"]

    def test_change_account_information_first_name_and_last_name_blank(self):
        AccountInformationCommonCode.account_information_common_code(self)
        account_page = AccountPage(self.driver)
        account_page.account_page_go_to_account_information_page()
        edit_account_information = EditAccountInformationPage(self.driver)
        edit_account_information.edit_account_information_page_fill_the_form(name_prefix=name_prefix(),
                                                                             first_name="",
                                                                             last_name="",
                                                                             submit_or_go_back_without_submit="submit")
        validation_error_text = edit_account_information.edit_account_information_page_get_validation_error_text()
        assert len(validation_error_text) == 2
        for i in validation_error_text:
            assert vet()["required_field_error_text"] in i.get_attribute("textContent")
