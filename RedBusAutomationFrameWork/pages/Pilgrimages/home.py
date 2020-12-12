from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class Pilgrimages(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _pilgrimages_link = "//*[@id='page_main_header']/nav/ul/li[5]/a"
    _source_field = "//input[@id='source_city']"
    _first_city_option = "//*[@id='search_box']/div/div[1]/ul/li[1]"
    _destination_field="//input[@id='dest_city']"
    _destination_list = "//*[@id='search_box']/div/div[2]/ul/li[1]"
    _search_button = "//button[@id='search_packages']"
    _validation_link = "//h1[@class='head fade-in']"

    def initialize_page(self):
        pilgrimage_icon = self.waitForElement(self._pilgrimages_link)
        self.elementClick(element=pilgrimage_icon)

    def pilgrimage_booking_functionality(self, start="", dest=""):
        self.initialize_page()
        source = self.waitForElement(self._source_field)
        self.sendKeys(data=start, element=source)
        first_list = self.waitForElement(self._first_city_option)
        self.elementClick(element=first_list)
        self.sendKeys(data=dest, locator=self._destination_field)
        desti_first = self.waitForElement(self._destination_list)
        self.elementClick(element=desti_first)
        self.elementClick(self._search_button)
        return self.isElementDisplayed(self._validation_link)

    def verify_page(self, driver):
        self.initialize_page()
        return self.isElementDisplayed(self._validation_link)

    def all_empty_field(self):
        self.initialize_page()
        self.elementClick(self._search_button)
        return self.isElementDisplayed(self._validation_link)














