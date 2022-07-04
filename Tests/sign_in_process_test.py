import pytest
from Config.config_reader import get_config_data as data
from Pages.pages_factory import *


@pytest.mark.usefixtures("setup")
class TestSignInProcess:
    def __sign_in_process_setup(self):
        main_page(self).open_main_page_and_accept_cookies()
        main_page(self).go_to_sign_in_page()

    def test_open_sign_in_page(self):
        TestSignInProcess.__sign_in_process_setup(self)
        assert "login" in self.driver.current_url

    @pytest.mark.smoke
    def test_sign_in_with_valid_data(self):
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]

        TestSignInProcess.__sign_in_process_setup(self)

        sign_in(self).fill_form_submit(email, password)
        assert "Default Billing Address" in self.driver.page_source

        account(self).sign_out()
        assert "Login" in self.driver.page_source
