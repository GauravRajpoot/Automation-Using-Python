from base.selenium_wrapper import SeleniumDriver
from utilities.Reading_data import DatePicker
import utilities.custom_logger as cl
import logging
import time
class ResBusHomePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _source_input_field = "//input[@id='src']"
    _destination_input_field = "//input[@id='dest']"
    _search_button = "//button[@id='search_btn']"
    _manage_booking = "//div[@class='manageHeaderLbl']"
    _cancel_link = "//header[@id='rh_header']//ul[1]//li[2]//span[1]//span[1]"
    _cancel_input_field = "//input[@id='ticketNo']"
    _cancel_email_field = "//input[@id='emailId']"
    _cancel_button = "//input[@id='ticketSearch']"
    _bus_pool = "//a[@class='site-links rpool_title']"
    _help_link = "//a[contains(text(),'Help')]"
    _login_button = "//i[@id='i-icon-profile']"
    _sign_in_button = "//div[@id='hc']//ul[@class='config-list']"
    _sign_in_text = "///div[@class='modal']//i[@class='icon-close']"
    _sms_inputfield = "//input[@id='smsTXTBOX']"
    _sms_sent_button = "//input[@id='sendLinkButton']"
    _sms_validation_txt = "//div[@id='success']"
    _sms_invalidation_txt = "//span[@class='errorMessage']"
    _link_apple_page = "//*[@id='platforms_div']/section/div/div[1]/div[5]/a[1]"
    _link_android_page = "//*[@id='platforms_div']/section/div/div[1]/div[5]/a[2]"
    _home_page_icon="//a[@class='redbus-logo home-redirect']"


    def enter_source_station(self, email):
        self.sendKeys(email, self._source_input_field)
        time.sleep(2)

    def enter_destination_station(self, password):
        self.sendKeys(password,self._destination_input_field)
        time.sleep(2)

    def click_search_station(self):
        self.elementClick(self._search_button)

    def click_manage_button(self):
        self.elementClick(self._manage_booking)

    def click_cancel_link(self):
        self.elementClick(self._cancel_link)

    def click_cancel_buton(self):
        self.elementClick(self._cancel_button)

    def home_page_icon(self):
        self.elementClick(self._home_page_icon)
        return self.getTitle()

    def search_bus(self, driver, source="", destination="", month="Aug 2019", date="9"):
        self.enter_source_station(source)
        self.enter_destination_station(destination)
        self.webScroll()
        DatePicker(month, date, driver)
        self.click_search_station()
        return self.getTitle()

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@class='onward-modify-btn g-button clearfix fl']",
                            locatorType="xpath")
        result = self.isElementPresent(locator="//div[@class='onward-modify-btn g-button clearfix fl']",
                                       locatorType="xpath")

        return result

    def bus_pool(self):
        pool_icon = self.waitForElement(self._bus_pool)
        self.elementClick(element=pool_icon)
        title = self.getTitle()
        return title

    def help_page(self):
        help_link = self.waitForElement(self._help_link)
        parent = self.parent_window_handler()
        self.elementClick(element=help_link)
        time.sleep(2)
        temp = self.window_handler(parent)
        return temp[0]

    def apple_page(self):
        parent = self.parent_window_handler()
        self.driver.execute_script("window.scrollBy(0, 1900);")
        apple = self.waitForElement(self._link_apple_page)
        self.elementClick(element=apple)
        time.sleep(2)
        temp = self.window_handler(parent)
        return temp[1]

    def android_page(self):
        parent = self.parent_window_handler()
        self.driver.execute_script("window.scrollBy(0, 1900);")
        android = self.waitForElement(self._link_android_page)
        self.elementClick(element=android)
        time.sleep(2)
        temp = self.window_handler(parent)
        return temp[0]

    def login_setup(self):
        login_button = self.waitForElement(self._login_button)
        self.elementClick(element=login_button)
        self.elementClick(self._sign_in_button)
        return self.isElementDisplayed(self._sign_in_text), self.getTitle()

    def sms_link(self, number=""):
        sms_input_field = self.waitForElement(self._sms_inputfield)
        self.sendKeys(number, element=sms_input_field)
        self.elementClick(self._sms_sent_button)

    def sms_valid_number(self):
        return self.isElementPresent(self._sms_validation_txt)

    def sms_invalid_number(self):
        return self.isElementPresent(self._sms_invalidation_txt)


