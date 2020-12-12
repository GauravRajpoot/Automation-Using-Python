from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Cancelpage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _manage_booking = "//div[@class='manageHeaderLbl']"
    _cancel_link = "//header[@id='rh_header']//ul[1]//li[2]//span[1]//span[1]"
    _cancel_input_field = "//input[@id='ticketNo']"
    _cancel_email_field = "//input[@id='emailId']"
    _cancel_button = "//input[@id='ticketSearch']"

    def cancel_functionality(self, ticket_no="", email=""):
        manage_button = self.waitForElement(self._manage_booking)
        self.elementClick(element=manage_button)
        self.elementClick(self._cancel_link)
        cancel_ticket_number = self.waitForElement(self._cancel_input_field)
        self.sendKeys(ticket_no, element=cancel_ticket_number)
        cancel_email = self.waitForElement(self._cancel_email_field)
        self.sendKeys(email, element=cancel_email)
        self.elementClick(self._cancel_button)
        return self.getTitle()




