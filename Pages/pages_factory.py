from Pages.account_page import AccountPage
from Pages.add_new_address_page import AddNewAddressPage
from Pages.address_book_page import AddressBookPage
from Pages.base_page import BasePage
from Pages.change_password_page import ChangePasswordPage
from Pages.edit_account_information_page import EditAccountInformationPage
from Pages.main_page import MainPage
from Pages.sign_in_page import SignInPage


def main_page(self):
    return MainPage(self.driver)


def add_new_address(self):
    return AddNewAddressPage(self.driver)


def address_book(self):
    return AddressBookPage(self.driver)


def base_page(self):
    return BasePage(self.driver)


def change_password(self):
    return ChangePasswordPage(self.driver)


def edit_account_information(self):
    return EditAccountInformationPage(self.driver)


def sign_in(self):
    return SignInPage(self.driver)


def account(self):
    return AccountPage(self.driver)
