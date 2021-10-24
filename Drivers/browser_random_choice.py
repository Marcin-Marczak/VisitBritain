import os
from selenium import webdriver
from Config.config_reader import configuration_data as cd


class BrowserRandomChoice:
    @staticmethod
    def browser_random_choice(browser):
        if browser == ['chrome']:
            return webdriver.Chrome(executable_path=cd()["chromedriver_executable_path"])
        elif browser == ['firefox']:
            return webdriver.Firefox(executable_path=cd()["firefox_executable_path"], service_log_path=os.devnull)
        elif browser == ['edge']:
            return webdriver.Edge(executable_path=cd()["edge_executable_path"])
