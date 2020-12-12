from pages.Hotel_Page.hotel_home import HotelPage
from utilities.screenshot import take_screenshot
from utilities.read_from_excel import readData
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)
@pytest.mark.run(order=1)
def test_booking_hotel(oneTimeSetUp):
    lp = HotelPage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Hotel booking functionality with valid credentials")
    log.info("*#" * 20)
    result = lp.hotel_booking_functionality(oneTimeSetUp,
                                            checkin_month=readData("Hotel", 2, 3),
                                            checkin_date=readData("Hotel", 2, 4),
                                            checkout_month=readData("Hotel", 2, 5),
                                            checkout_date=readData("Hotel", 2, 6),
                                            hotel=readData("Hotel", 2, 1))
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in hotel Booking")
        raise e


@pytest.mark.run(order=2)
def test_invalid_hotel(oneTimeSetUp):
    lp = HotelPage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking Hotel booking fuctionality with invalid hotel name")
    log.info("*#" * 20)
    result = lp.hotel_invalid_entry(hotel=readData("Hotel", 3, 1))
    try:
        assert_that(result, equal_to_ignoring_case(readData("Hotel", 2, 2)))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in invalid login")
        raise e


@pytest.mark.run(order=3)
def test_empty_hotel_field(oneTimeSetUp):
    lp = HotelPage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking the Hotel booking fuctionality with empty Hotel field")
    log.info("*#" * 20)
    result = lp.hotel_invalid_entry()
    try:
        assert_that(result, equal_to_ignoring_case(readData("Hotel", 2, 2)))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in empty hotel field")
        raise e


@pytest.mark.run(order=4)
def test_varify_page(oneTimeSetUp):
    lp = HotelPage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Verifying the Hotel Home Page")
    log.info("*#" * 20)
    result = lp.verify_page()
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Verifying the HOme Page")
        raise e




