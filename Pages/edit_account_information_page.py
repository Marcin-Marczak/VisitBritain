from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from Config.config_reader import configuration_data as cd


class EditAccountInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_account_information_page_name_prefix_select = (By.ID, "prefix")
        self.edit_account_information_page_first_name_input = (By.ID, "firstname")
        self.edit_account_information_page_last_name_input = (By.ID, "lastname")
        self.edit_account_information_page_save_button = (By.CSS_SELECTOR, "[title='Save']")
        self.edit_account_information_page_go_back_link = (By.XPATH, "//a[@class='action back']")
        self.edit_account_information_page_error_message_text = (By.XPATH, "//div[@class='mage-error']")

    def edit_account_information_page_fill_the_form(self, name_prefix, first_name, last_name, submit_or_go_back_without_submit):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*self.edit_account_information_page_name_prefix_select).click()
        select = Select(self.driver.find_element(*self.edit_account_information_page_name_prefix_select))
        select.select_by_value(name_prefix)
        self.driver.find_element(*self.edit_account_information_page_first_name_input).clear()
        self.driver.find_element(*self.edit_account_information_page_last_name_input).clear()
        self.driver.find_element(*self.edit_account_information_page_first_name_input).send_keys(first_name)
        self.driver.find_element(*self.edit_account_information_page_last_name_input).send_keys(last_name)
        if submit_or_go_back_without_submit == "submit":
            self.driver.find_element(*self.edit_account_information_page_save_button).click()
        elif submit_or_go_back_without_submit == "go_back_without_submit":
            self.driver.find_element(*self.edit_account_information_page_go_back_link).click()

    def edit_account_information_page_get_validation_error_text(self):
        error = self.driver.find_elements(*self.edit_account_information_page_error_message_text)
        WebDriverWait(self.driver, cd()["timeout"], cd()["pool_frequency"]).until(lambda errors: "." in error[0].text)
        return error
