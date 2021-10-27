import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from msedge.selenium_tools import Edge, EdgeOptions
from Config.config_reader import configuration_data as cd


class BrowserRandomChoice:
    @staticmethod
    def browser_random_choice(browser):
        if browser == ['chrome']:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            return webdriver.Chrome(executable_path=cd()["chromedriver_executable_path"], options=chrome_options)
        elif browser == ['firefox']:
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            return webdriver.Firefox(executable_path=cd()["firefox_executable_path"], options=firefox_options, service_log_path=os.devnull)
        elif browser == ['edge']:
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("headless")
            return Edge(executable_path=cd()["edge_executable_path"], options=edge_options)
