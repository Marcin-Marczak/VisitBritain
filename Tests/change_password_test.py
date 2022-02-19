import pytest
from Pages.base_page import BasePage
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.change_password_page import ChangePasswordPage
from Config.config_reader import get_config_data as data
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class ChangePasswordSetup:
    def change_password_setup(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_accept_cookies()
        main_page.main_page_go_to_sign_in_page()
        sign_in = SignInPage(self.driver)
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]
        sign_in.sign_in_page_fill_the_form(email, password)
        account = AccountPage(self.driver)
        account.account_page_go_to_change_password_page()


class TestChangePassword(ChangePasswordSetup):
    def test_change_password_invalid_new_password_with_lower_case_only(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_lower_case"]
        change_password.change_password_page_fill_the_form(current_password, invalid_password, invalid_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        invalid_new_password_error_text = data("validation_error_texts.json")["invalid_new_password_error_text"]
        assert validation_error_text == invalid_new_password_error_text

    def test_change_password_invalid_new_password_with_digits_only(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_digits"]
        change_password.change_password_page_fill_the_form(current_password, invalid_password, invalid_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        assert validation_error_text == data("validation_error_texts.json")["invalid_new_password_error_text"]

    def test_change_password_invalid_new_password_with_lower_and_upper_case_only(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_lower_and_upper_case"]
        change_password.change_password_page_fill_the_form(current_password, invalid_password, invalid_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        invalid_new_password_error_text = data("validation_error_texts.json")["invalid_new_password_error_text"]
        assert validation_error_text == invalid_new_password_error_text

    def test_change_password_invalid_new_password_with_digits_and_special_characters_only(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_digits_and_special_characters"]
        change_password.change_password_page_fill_the_form(current_password, invalid_password, invalid_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        invalid_new_password_error_text = data("validation_error_texts.json")["invalid_new_password_error_text"]
        assert validation_error_text == invalid_new_password_error_text

    def test_change_password_too_short_new_password(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        new_password = data("invalid_test_data.json")["invalid_password_7_characters"]
        confirm_new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]
        change_password.change_password_page_fill_the_form(current_password, new_password, confirm_new_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text_1 = validation_error_texts[0].get_attribute("textContent")
        validation_error_text_2 = validation_error_texts[1].get_attribute("textContent")
        too_short_new_password_error_text = data("validation_error_texts.json")["too_short_new_password_error_text"]
        confirm_new_password_doesnt_match_new_password_error_text = \
            data("validation_error_texts.json")["confirm_new_password_doesnt_match_new_password_error_text"]
        assert validation_error_text_1 == too_short_new_password_error_text
        assert validation_error_text_2 == confirm_new_password_doesnt_match_new_password_error_text

    def test_change_password_too_short_new_password_and_confirm_new_password(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_7_characters"]
        change_password.change_password_page_fill_the_form(current_password, invalid_password, invalid_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        too_short_new_password_error_text = data("validation_error_texts.json")["too_short_new_password_error_text"]
        assert validation_error_text == too_short_new_password_error_text

    def test_change_password_new_password_blank(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        new_password = ""
        confirm_new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]
        change_password.change_password_page_fill_the_form(current_password, new_password, confirm_new_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("validation_error_texts.json")["required_field_error_text"]
        assert validation_error_text == required_field_error_text

    def test_change_password_confirm_new_password_blank(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"]
        new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"],
        confirm_new_password = ""
        change_password.change_password_page_fill_the_form(current_password, new_password, confirm_new_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        required_field_error_text = data("validation_error_texts.json")["required_field_error_text"]
        assert validation_error_text == required_field_error_text

    def test_change_password_confirm_new_password_does_not_match(self):
        ChangePasswordSetup.change_password_setup(self)
        change_password = ChangePasswordPage(self.driver)
        current_password = data("env.json")["password"],
        new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]
        confirm_new_password = generate_unique_random_word()
        change_password.change_password_page_fill_the_form(current_password, new_password, confirm_new_password)
        base_page = BasePage(self.driver)
        validation_error_texts = base_page.base_page_get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        confirm_new_password_doesnt_match_new_password_error_text = \
            data("validation_error_texts.json")["confirm_new_password_doesnt_match_new_password_error_text"]
        assert validation_error_text == confirm_new_password_doesnt_match_new_password_error_text
