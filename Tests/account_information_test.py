import pytest
import allure
from Pages.pages_factory import *
from Config.config_reader import get_config_data as data
from Config.generate_test_data import *


@pytest.mark.usefixtures("setup")
class TestAccountInformation:
    def __account_information_setup(self):
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]

        main_page(self).open_main_page_and_accept_cookies()
        main_page(self).go_to_sign_in_page()

        sign_in(self).fill_form_submit(email, password)

    @pytest.mark.smoke
    @allure.title("Change account information - first name, last name")
    @allure.description("Check if user is able to update first name and last name")
    def test_change_account_information_valid_first_name_and_last_name(self):
        TestAccountInformation.__account_information_setup(self)

        account(self).go_to_account_information_page()

        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = generate_last_name()

        edit_account_information(self).fill_form_submit(name_prefix_to_input, first_name_to_input,
                                                        last_name_to_input, "submit")

        name_prefix_after_submit = account(self).get_name_prefix()
        first_name_after_submit = account(self).get_first_name()
        last_name_after_submit = account(self).get_last_name()

        assert name_prefix_to_input == name_prefix_after_submit
        assert first_name_to_input == first_name_after_submit
        assert last_name_to_input == last_name_after_submit

    @allure.title("Change account information - without submit")
    @allure.description("Check if user is not able to update data without submit the form")
    def test_change_account_information_valid_first_name_and_last_name_and_go_back_without_submit(self):
        TestAccountInformation.__account_information_setup(self)

        first_name_before_test = account(self).get_first_name()
        last_name_before_test = account(self).get_last_name()

        account(self).go_to_account_information_page()

        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = generate_last_name()

        edit_account_information(self).fill_form_submit(name_prefix_to_input, first_name_to_input,
                                                        last_name_to_input, "go_back_without_submit")

        first_name_after_submit = account(self).get_first_name()
        last_name_after_submit = account(self).get_last_name()

        assert first_name_before_test == first_name_after_submit
        assert last_name_before_test == last_name_after_submit

    @allure.title("Change account information - first name blank")
    @allure.description("Check if user is not able to update data if first name is blank")
    def test_change_account_information_first_name_blank(self):
        TestAccountInformation.__account_information_setup(self)

        account(self).go_to_account_information_page()

        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = ""
        last_name_to_input = generate_last_name()

        edit_account_information(self).fill_form_submit(name_prefix_to_input, first_name_to_input,
                                                        last_name_to_input, "submit")

        validation_error_texts = base_page(self).get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("error_texts.json")["required_field_error_text"]

        assert validation_error_text == required_field_error_text

    @allure.title("Change account information - last name blank")
    @allure.description("Check if user is not able to update data if last name is blank")
    def test_change_account_information_last_name_blank(self):

        TestAccountInformation.__account_information_setup(self)

        account(self).go_to_account_information_page()

        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = generate_first_name()
        last_name_to_input = ""

        edit_account_information(self).fill_form_submit(name_prefix_to_input, first_name_to_input,
                                                        last_name_to_input, "submit")

        validation_error_texts = base_page(self).get_validation_error_texts()
        validation_error_text = validation_error_texts[0].get_attribute("textContent")
        required_field_error_text = data("error_texts.json")["required_field_error_text"]

        assert validation_error_text == required_field_error_text

    @allure.title("Change account information - first name, last name blank")
    @allure.description("Check if user is not able to update data if first name and last name are blank")
    def test_change_account_information_first_name_and_last_name_blank(self):
        TestAccountInformation.__account_information_setup(self)

        account(self).go_to_account_information_page()

        name_prefix_to_input = generate_name_prefix()
        first_name_to_input = ""
        last_name_to_input = ""

        edit_account_information(self).fill_form_submit(name_prefix_to_input, first_name_to_input,
                                                        last_name_to_input, "submit")

        validation_error_texts = base_page(self).get_validation_error_texts()
        number_of_validation_error_texts = len(validation_error_texts)
        required_field_error_text = data("error_texts.json")["required_field_error_text"]

        assert number_of_validation_error_texts == 2
        for i in validation_error_texts:
            assert required_field_error_text in i.get_attribute("textContent")
