"""

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

"""
import traceback
from selenium import webdriver
from utilities.config_read import get_TestURL
import os


class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser
    """
    for Firefox if it does not run use following method
    
        # os.environ["webdriver.ie.driver"] = driverLocation
        # driver = webdriver.Ie(driverLocation)
        # binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        # driver = webdriver.Firefox(firefox_binary=binary)

        PREFERRED: Set the path on the machine where browser will be executed
    """
    """
    For IE please set zoom=100% if not working manually
    * Open IE Browser and in setting tab zoom element is present 
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = get_TestURL()
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=options, executable_path="drivers/chromedriver.exe")
        else:
            driver = webdriver.Firefox()
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        return driver