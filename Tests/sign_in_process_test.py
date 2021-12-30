import pytest
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage
from Pages.account_page import AccountPage
from Config.config_reader import valid_test_data as vtd
from Config.config_reader import env


@pytest.mark.usefixtures("setup")
class SignInProcessSetup:
    def sign_in_process_setup(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page_and_accept_cookies()
        main_page.main_page_go_to_sign_in_page()


class TestSignInProcess(SignInProcessSetup):
    def test_sign_in_process_open_login_page(self):
        SignInProcessSetup.sign_in_process_setup(self)
        assert "login" in self.driver.current_url

    @pytest.mark.smoke
    def test_sign_in_process_valid_username_valid_password(self):
        SignInProcessSetup.sign_in_process_setup(self)
        sign_in = SignInPage(self.driver)
        sign_in.sign_in_page_fill_the_form(vtd()["email"], env()["password"])
        assert "Default Billing Address" in self.driver.page_source
        account = AccountPage(self.driver)
        account_url = self.driver.current_url
        account.account_page_sign_out()
        assert self.driver.current_url != account_url
        assert "Login" in self.driver.page_source
