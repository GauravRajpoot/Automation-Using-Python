from pages.Hotel_Page.more_hotels import MoreHotel
from utilities.read_from_excel import readData
from utilities.screenshot import take_screenshot
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)
@pytest.mark.run(order=1)
def test_top_hotel(oneTimeSetUp):
    lp = MoreHotel(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking the top hotel present in the list")
    log.info("*#" * 20)
    result = lp.click_hotel(oneTimeSetUp)
    try:
        assert_that(result,
                    equal_to_ignoring_case(readData("Hotel", 3, 2)))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Opening in Niche Suite")
        raise e


@pytest.mark.run(order=2)
def test_offer_page(oneTimeSetUp):
    lp = MoreHotel(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking for the Offer Page")
    log.info("*#" * 20)
    result = lp.click_offer_link()
    try:
        assert_that(True,
                    equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Offer Page")
        raise e
