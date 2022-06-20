import pytest
from Config.config_reader import get_config_data as data
from conftest import POM


@pytest.mark.usefixtures("setup")
class TestSignInProcess:
    def __sign_in_process_setup(pom: POM):
        pom.main_page.open_main_page_and_accept_cookies()
        pom.main_page.go_to_sign_in_page()

    def test_open_sign_in_page(self):
        assert "login" in self.driver.current_url

    @pytest.mark.smoke
    def test_sign_in_with_valid_data(pom: POM, self=None):
        email = data("valid_test_data.json")["email"]
        password = data("env.json")["password"]

        TestSignInProcess.__sign_in_process_setup(self)

        pom.sign_in_page.fill_form_submit(email, password)
        assert "Default Billing Address" in self.driver.page_source

        pom.account_page.sign_out()
        assert "Login" in self.driver.page_source
