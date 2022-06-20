from dataclasses import dataclass
import pytest
from datetime import datetime
from Drivers.browser_random_choice import BrowserRandomChoice
from Screenshots.get_screenshots_path import *
from Pages.account_page import AccountPage
from Pages.add_new_address_page import AddNewAddressPage
from Pages.address_book_page import AddressBookPage
from Pages.base_page import BasePage
from Pages.change_password_page import ChangePasswordPage
from Pages.edit_account_information_page import EditAccountInformationPage
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage


@dataclass(frozen=True)
class POM:
    account_page: AccountPage
    add_new_address_page: AddNewAddressPage
    address_book_page: AddressBookPage
    base_page: BasePage
    change_password_page: ChangePasswordPage
    edit_account_information_page: EditAccountInformationPage
    main_page: MainPage
    sign_in_page: SignInPage


def create_screenshot_name():
    test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].replace("test_", "")
    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    screenshot_name = f"{current_time}_{test_name}"
    return f"{screenshot_name}.png"


@pytest.fixture()
def setup(request):
    driver = BrowserRandomChoice.browser_random_choice()

    driver.implicitly_wait(30)
    driver.set_window_size(1500, 800)

    request.cls.driver = driver

    before_failed = request.session.testsfailed
    yield

    if request.session.testsfailed != before_failed:
        screenshot_path = get_screenshots_path()
        driver.get_screenshot_as_file(f"{screenshot_path}/{create_screenshot_name()}")

    driver.quit()


@pytest.fixture()
def poms(setup) -> POM:
    account_page_pom = AccountPage(setup)
    add_new_address_page_pom = AddNewAddressPage(setup)
    address_book_page_pom = AddressBookPage(setup)
    base_page_pom = BasePage(setup)
    change_password_page_pom = ChangePasswordPage(setup)
    edit_account_information_page_pom = EditAccountInformationPage(setup)
    main_page_pom = MainPage(setup)
    sing_in_page_pom = SignInPage(setup)

    return POM(
        account_page=account_page_pom,
        add_new_address_page=add_new_address_page_pom,
        address_book_page=address_book_page_pom,
        base_page=base_page_pom,
        change_password_page=change_password_page_pom,
        edit_account_information_page=edit_account_information_page_pom,
        main_page=main_page_pom,
        sign_in_page=sing_in_page_pom)
