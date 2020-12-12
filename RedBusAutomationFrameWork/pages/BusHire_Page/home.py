from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class Bushire(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _bus_hire_link = "//a[@class='site-links gtm-busHire']"
    _input_field= "//input[@placeholder='eg: Mumbai']"
    _first_city_option= "//*[@id='src_city_block']/div/div/ul/li[1]"
    _starting_place="//input[@placeholder='eg: Railway Station']"
    _pickup="//div[@id='pick_up_block']//ul//li[1]"
    _destination= "//input[@placeholder='eg: Airport/Pune']"
    _destination_list="//div[@id='dest_city_block']//li[1]"
    _hire_button="//button[@id='hire_btn']"
    _validation_link="//div[@class='Hire-a-vehicle']"
    _same_page_validation= "//span[contains(text(),'Travelling Together Is Easy')]"

    '''
    This is the method to initialized the page 
    '''
    def initialize_page(self):
        bus_hire_button = self.waitForElement(self._bus_hire_link)
        self.elementClick(element=bus_hire_button)

    '''
        This is the method to verify the title
     '''

    def varify_page(self):
        self.initialize_page()
        return self.isElementDisplayed(self._same_page_validation)

    '''
        This is the method to validate empty method field
    '''

    def all_empty_field(self):
        self.initialize_page()
        hire_button = self.waitForElement(self._hire_button)
        self.elementClick(element=hire_button)
        return self.isElementDisplayed(self._same_page_validation)

    '''
    This is the method to hire the bus 
    '''

    def bus_hire_functionality(self, hire_city="", start="", end=""):
        self.initialize_page()
        city = self.waitForElement(self._input_field)
        self.sendKeys(data=hire_city, element=city)
        self.webScroll()
        first_element = self.waitForElement(self._first_city_option)
        self.elementClick(element=first_element)
        starting_point = self.waitForElement(self._starting_place)
        self.sendKeys(data=start, element=starting_point)
        first_list = self.waitForElement(self._pickup)
        self.elementClick(element=first_list)
        desti = self.waitForElement(self._destination)
        self.sendKeys(data=end, element=desti)
        dest_first = self.waitForElement(self._destination_list)
        self.elementClick(element=dest_first)
        self.elementClick(self._hire_button)
        next_page_element = self.isElementDisplayed(self._validation_link)
        same_page_element = self.isElementDisplayed(self._same_page_validation)
        valid_bus_hire = [same_page_element, next_page_element]
        return valid_bus_hire
    
