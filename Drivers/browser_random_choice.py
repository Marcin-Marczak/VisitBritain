import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserRandomChoice:
    @staticmethod
    def browser_random_choice():
        browsers = ["chrome", "firefox", "edge"]
        browser = random.choices(browsers, weights=[65, 25, 10], k=1)

        if browser == ['chrome']:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        elif browser == ['firefox']:
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options, service_log_path=os.devnull)
        elif browser == ['edge']:
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("headless")
            return Edge(executable_path=EdgeChromiumDriverManager().install(), options=edge_options)
