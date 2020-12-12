from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging
from utilities.Reading_data import *


class HotelPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _hotel_link = "//a[@class='site-links gtm-hotels']"
    _input_field = "//input[@id='search_key']"
    _first_item = "//*[@id='search_wrapper']/div[2]/div/div[1]"
    _search_button = "//button[@id='search_hotel']"
    _hotel_validation = "//div[@class='compare-btn']"
    _check_in_date = "//input[@id='checkin_date']"
    _check_out_date = "//input[@id='checkout_date']"
    _display_icon = "//input[@id='search_key']"

    def initialze_page(self):
        hotel_icon = self.waitForElement(self._hotel_link)
        self.elementClick(element=hotel_icon)

    def hotel_booking_functionality(self, driver, checkin_month="Aug 2019", checkin_date="9",
                                    checkout_month="Aug 2019", checkout_date="10",hotel=""):
        self.initialze_page()
        input_field = self.waitForElement(self._input_field)
        self.sendKeys(data=hotel, element=input_field)
        select_first = self.waitForElement(self._first_item)
        self.elementClick(element=select_first)
        self.webScroll()
        self.elementClick(self._check_in_date)
        CheckInDate(checkin_month, checkin_date, driver)
        self.elementClick(self._check_out_date)
        CheckOutDate(checkout_month, checkout_date, driver)
        search_button = self.waitForElement(self._search_button)
        self.elementClick(element=search_button)
        compare_element = self.waitForElement(self._hotel_validation)
        return self.isElementDisplayed(element=compare_element)

    def hotel_invalid_entry(self, hotel=""):
        self.initialze_page()
        input_field = self.waitForElement(self._input_field)
        self.sendKeys(data=hotel, element=input_field)
        search_button = self.waitForElement(self._search_button)
        self.elementClick(element=search_button)
        return self.getTitle()



    def verify_page(self):
        self.initialze_page()
        return self.isElementDisplayed(self._display_icon)




