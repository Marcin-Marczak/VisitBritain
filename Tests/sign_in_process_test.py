import pytest
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Config.config_reader import get_config_data as data


@pytest.mark.usefixtures("setup")
class TestSignInProcess:
    def __sign_in_process_setup(self):
        main_page = MainPage(self.driver)

        main_page.open_main_page_and_accept_cookies()
        main_page.go_to_sign_in_page()

    def test_open_sign_in_page(self):
        TestSignInProcess.__sign_in_process_setup(self)

        assert "login" in self.driver.current_url

    @pytest.mark.smoke
    def test_sign_in_with_valid_data(self):
        sign_in = SignInPage(self.driver)
        account = AccountPage(self.driver)
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]

        TestSignInProcess.__sign_in_process_setup(self)

        sign_in.sign_in_page_fill_the_form(email, password)
        assert "Default Billing Address" in self.driver.page_source

        account.account_page_sign_out()
        assert "Login" in self.driver.page_source
