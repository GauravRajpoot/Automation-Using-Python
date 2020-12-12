from base.selenium_wrapper import SeleniumDriver
import utilities.custom_logger as cl
import logging
class MoreHotel(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _hotel_link = "//a[@class='site-links gtm-hotels']"
    _hotel1__link = "//*[@id='top_htl_deal']/a[1]/img"
    _offer_link = "//*[@id='home-page']/section[2]/aside/div[1]/a"
    _validation_element = "//*[@id='mBWrapper']/h1"

    def click_hotel(self, driver):
        hotel_icon = self.waitForElement(self._hotel_link)
        self.elementClick(element=hotel_icon)
        parent = self.parent_window_handler()
        driver.execute_script("window.scrollTo(0, 1800)")
        hotel1 = self.waitForElement(self._hotel1__link)
        self.elementClick(element=hotel1)
        temp = self.window_handler(parent)
        return temp[0]

    def click_offer_link(self):
        hotel_icon = self.waitForElement(self._hotel_link)
        self.elementClick(element=hotel_icon)
        self.elementClick(self._offer_link)
        validation_icon=self.waitForElement(self._validation_element)
        return self.isElementDisplayed(element=validation_icon)









