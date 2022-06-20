import pytest
import allure
from Pages.base_page import BasePage
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Pages.change_password_page import ChangePasswordPage
from Config.config_reader import get_config_data as data
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class TestChangePassword:
    def __change_password_setup(self):
        main_page = MainPage(self.driver)
        sign_in = SignInPage(self.driver)
        account = AccountPage(self.driver)

        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]

        main_page.open_main_page_and_accept_cookies()
        main_page.go_to_sign_in_page()

        sign_in.fill_form_submit(email, password)

        account.go_to_change_password_page()

    @allure.title("Change password - invalid new password lower case")
    @allure.description("Check if user is not able to change password if new password is with lower case only")
    def test_change_password_invalid_new_password_with_lower_case_only(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_lower_case"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, invalid_password, invalid_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        invalid_new_password_error_text = data("error_texts.json")["invalid_new_password_error_text"]

        assert validation_error_text == invalid_new_password_error_text

    @allure.title("Change password - invalid new password digits")
    @allure.description("Check if user is not able to change password if new password is with digits only")
    def test_change_password_invalid_new_password_with_digits_only(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_digits"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, invalid_password, invalid_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        invalid_new_password_error_text = data("error_texts.json")["invalid_new_password_error_text"]

        assert validation_error_text == invalid_new_password_error_text

    @allure.title("Change password - invalid new password lower case and upper case")
    @allure.description(
        "Check if user is not able to change password if new password is with lower case and upper case only")
    def test_change_password_invalid_new_password_with_lower_and_upper_case_only(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_lower_and_upper_case"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, invalid_password, invalid_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        invalid_new_password_error_text = data("error_texts.json")["invalid_new_password_error_text"]

        assert validation_error_text == invalid_new_password_error_text

    @allure.title("Change password - invalid new password digits and special characters")
    @allure.description(
        "Check if user is not able to change password if new password is with digits and special characters only")
    def test_change_password_invalid_new_password_with_digits_and_special_characters_only(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_digits_and_special_characters"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, invalid_password, invalid_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        invalid_new_password_error_text = data("error_texts.json")["invalid_new_password_error_text"]

        assert validation_error_text == invalid_new_password_error_text

    @allure.title("Change password - invalid new password too short")
    @allure.description("Check if user is not able to change password if new password is too short")
    def test_change_password_too_short_new_password(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        new_password = data("invalid_test_data.json")["invalid_password_7_characters"]
        confirm_new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, new_password, confirm_new_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text_1 = validation_error_texts[0].get_attribute("textContent")
        validation_error_text_2 = validation_error_texts[1].get_attribute("textContent")
        too_short_new_password_error_text = data("error_texts.json")["too_short_new_password_error_text"]
        confirm_new_password_doesnt_match_new_password_error_text = \
            data("error_texts.json")["confirm_new_password_doesnt_match_new_password_error_text"]

        assert validation_error_text_1 == too_short_new_password_error_text
        assert validation_error_text_2 == confirm_new_password_doesnt_match_new_password_error_text

    @allure.title("Change password - invalid new password confirm password too short")
    @allure.description(
        "Check if user is not able to change password if new password and confirm new password are too short")
    def test_change_password_too_short_new_password_and_confirm_new_password(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        invalid_password = data("invalid_test_data.json")["invalid_password_7_characters"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, invalid_password, invalid_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        too_short_new_password_error_text = data("error_texts.json")["too_short_new_password_error_text"]

        assert validation_error_text == too_short_new_password_error_text

    @allure.title("Change password - invalid new password blank")
    @allure.description("Check if user is not able to change password if new password is blank")
    def test_change_password_new_password_blank(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        new_password = ""
        confirm_new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, new_password, confirm_new_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("error_texts.json")["required_field_error_text"]

        assert validation_error_text == required_field_error_text

    @allure.title("Change password - invalid confirm new password blank")
    @allure.description("Check if user is not able to change password if confirm new password is blank")
    def test_change_password_confirm_new_password_blank(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]
        confirm_new_password = ""

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, new_password, confirm_new_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        required_field_error_text = data("error_texts.json")["required_field_error_text"]

        assert validation_error_text == required_field_error_text

    @allure.title("Change password - new password confirm new password not the same")
    @allure.description(
        "Check if user is not able to change password if new password and confirm new password are not the same")
    def test_change_password_confirm_new_password_does_not_match(self):
        change_password = ChangePasswordPage(self.driver)
        base_page = BasePage(self.driver)

        current_password = data("env.json")["password"]
        new_password = data("valid_test_data.json")["valid_new_password_or_confirm_new_password"]
        confirm_new_password = generate_random_word()

        TestChangePassword.__change_password_setup(self)

        change_password.fill_form_submit(current_password, new_password, confirm_new_password)

        validation_error_texts = base_page.get_validation_error_texts()
        validation_error_text = validation_error_texts[0].text
        confirm_new_password_doesnt_match_new_password_error_text = \
            data("error_texts.json")["confirm_new_password_doesnt_match_new_password_error_text"]

        assert validation_error_text == confirm_new_password_doesnt_match_new_password_error_text
