from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.base_page import BasePage


class EditAccountInformationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.name_prefix_select = (By.ID, "prefix")
        self.first_name_input = (By.ID, "firstname")
        self.last_name_input = (By.ID, "lastname")
        self.save_button = (By.CSS_SELECTOR, "[title='Save']")
        self.go_back_link = (By.XPATH, "//a[@class='action back']")

    def fill_form_submit(self, name_prefix, first_name, last_name, submit_or_go_back_without_submit):
        self.driver.execute_script("window.scrollTo(0, 500)")

        self.click_on_element(*self.name_prefix_select)

        select = Select(self.driver.find_element(*self.name_prefix_select))
        select.select_by_value(name_prefix)

        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.last_name_input).clear()

        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

        if submit_or_go_back_without_submit == "submit":
            self.click_on_element(*self.save_button)
        elif submit_or_go_back_without_submit == "go_back_without_submit":
            self.click_on_element(*self.go_back_link)
