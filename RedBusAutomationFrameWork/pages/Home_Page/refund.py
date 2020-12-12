from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Refundpage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _manage_booking = "//div[@class='manageHeaderLbl']"
    _refund_link = "//span[contains(text(),'Cancel/Refund')]"
    _input_field = "//input[@id='searchTicket']"
    _email_input_field = "//input[@id='searchEmail']"
    _search_button="//input[@id='search_btn']"
    _validation_element="//*[@id='cancellationheader']"

    def refund_functionality(self, ticket_no="", email=""):
        manage_button = self.waitForElement(self._manage_booking)
        self.elementClick(element=manage_button)
        self.elementClick(self._refund_link)
        ticket_number = self.waitForElement(self._input_field)
        self.sendKeys(ticket_no, element=ticket_number)
        email_field = self.waitForElement(self._email_input_field)
        self.sendKeys(email, element=email_field)
        self.elementClick(self._search_button)
        return self.isElementPresent(self._validation_element)



