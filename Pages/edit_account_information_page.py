from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage


class EditAccountInformationPage(BasePage):

    NAME_PREFIX_SELECT = (By.ID, "prefix")
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    GO_BACK_LINK = (By.XPATH, "//a[@class='action back']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_form_submit(self, name_prefix, first_name, last_name, submit_or_go_back_without_submit):
        self.driver.execute_script("window.scrollTo(0, 500)")

        self.click_on_element(*self.NAME_PREFIX_SELECT)

        select = Select(self.driver.find_element(*self.NAME_PREFIX_SELECT))
        select.select_by_value(name_prefix)

        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()

        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

        if submit_or_go_back_without_submit == "submit":
            self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(Keys.ENTER)
        elif submit_or_go_back_without_submit == "go_back_without_submit":
            self.click_on_element(*self.GO_BACK_LINK)
