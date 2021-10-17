import pytest
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.change_password_page import ChangePasswordPage
from Config.config_reader import valid_test_data as vtd
from Config.config_reader import invalid_test_data as itd
from Config.config_reader import validation_error_texts as vet
from Config.config_reader import env
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class ChangePasswordCommonCode:
    def change_password_common_code(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_close_cookies()
        main_page.main_page_go_to_sign_in_page()
        sign_in = SignInPage(self.driver)
        sign_in.sign_in_page_fill_the_form(vtd()["email"], env()["password"])
        account = AccountPage(self.driver)
        account.account_page_go_to_change_password_page()


class TestChangePassword(ChangePasswordCommonCode):

    def test_change_password_invalid_new_password_with_lower_case_only(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        invalid_password = itd()["invalid_password_lower_case"]
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=invalid_password, confirm_new_password=invalid_password)
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["invalid_new_password_error_text"] == validation_error_text[0].text

    def test_change_password_invalid_new_password_with_digits_only(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        invalid_password = itd()["invalid_password_digits"]
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=invalid_password, confirm_new_password=invalid_password)
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["invalid_new_password_error_text"] == validation_error_text[0].text

    def test_change_password_invalid_new_password_with_lower_and_upper_case_only(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        invalid_password = itd()["invalid_password_lower_and_upper_case"]
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=invalid_password, confirm_new_password=invalid_password)
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["invalid_new_password_error_text"] == validation_error_text[0].text

    def test_change_password_invalid_new_password_with_digits_and_special_characters_only(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        invalid_password = itd()["invalid_password_digits_and_special_characters"]
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=invalid_password, confirm_new_password=invalid_password)
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["invalid_new_password_error_text"] == validation_error_text[0].text

    def test_change_password_too_short_new_password(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=itd()["invalid_password_7_characters"], confirm_new_password=vtd()["valid_new_password_or_confirm_new_password"])
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["too_short_new_password_error_text"] == validation_error_text[0].text
        assert vet()["confirm_new_password_doesnt_match_new_password_error_text"] == validation_error_text[1].text

    def test_change_password_too_short_new_password_and_confirm_new_password(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        invalid_password = itd()["invalid_password_7_characters"]
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=invalid_password, confirm_new_password=invalid_password)
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["too_short_new_password_error_text"] == validation_error_text[0].text

    def test_change_password_new_password_blank(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password="", confirm_new_password=vtd()["valid_new_password_or_confirm_new_password"])
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["required_field_error_text"] == validation_error_text[0].text

    def test_change_password_confirm_new_password_blank(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=vtd()["valid_new_password_or_confirm_new_password"], confirm_new_password="")
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["required_field_error_text"] == validation_error_text[0].text

    def test_change_password_confirm_new_password_does_not_match(self):
        ChangePasswordCommonCode.change_password_common_code(self)
        change_password = ChangePasswordPage(self.driver)
        change_password.change_password_page_fill_the_form(current_password=env()["password"], new_password=vtd()["valid_new_password_or_confirm_new_password"], confirm_new_password=unique_random_word())
        validation_error_text = change_password.change_password_page_get_validation_error_text()
        assert vet()["confirm_new_password_doesnt_match_new_password_error_text"] in validation_error_text[0].text
