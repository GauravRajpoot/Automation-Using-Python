from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Emailpage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _manage_booking = "//div[@class='manageHeaderLbl']"
    _email_link = "//span[contains(text(),'Email/SMS')]"
    _input_field = "//input[@id='searchTicketTIN']"
    _email_input_field = "//input[@id='searchTicketEmail']"
    _search_button = "//input[@id='ticketSearch']"
    _print_validate_text = "//*[@id='mBWrapper']/div/div[1]/div/div[1]"

    def email_functionality(self, ticket_no="", email=""):
        manage_button = self.waitForElement(self._manage_booking)
        self.elementClick(element=manage_button)
        self.elementClick(self._email_link)
        ticket_number = self.waitForElement(self._input_field)
        self.sendKeys(ticket_no, element=ticket_number)
        email_field = self.waitForElement(self._email_input_field)
        self.sendKeys(email, element=email_field)
        self.elementClick(self._search_button)
        return self.isElementPresent(self._print_validate_text)

