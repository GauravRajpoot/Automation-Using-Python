from pages.Pilgrimages.home import Pilgrimages
from utilities.read_from_excel import readData
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *
from utilities.screenshot import take_screenshot

log = cl.customLogger(logging.DEBUG)
@pytest.mark.run(order=1)
def test_valid_credentials(oneTimeSetUp):
    lp = Pilgrimages(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking the functionality of Pilgrimage page with valid input field")
    log.info("*#" * 20)
    result = lp.pilgrimage_booking_functionality(start=readData("Pilgrimages", 2, 1),
                                                 dest=readData("Pilgrimages", 2, 2))
    try:
        assert_that(False, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Valid Pilgrimage")
        raise e


@pytest.mark.run(order=2)
def test_verify_home_page(oneTimeSetUp):
    lp = Pilgrimages(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking the functionality of Pilgrimage page with invalid input field")
    log.info("*#" * 20)
    result = lp.verify_page(oneTimeSetUp)
    try:
        assert_that(True, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in verifying homepage")
        raise e


@pytest.mark.run(order=3)
def test_empty_end_start_point(oneTimeSetUp):
    lp = Pilgrimages(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Checking the functionality of Pilgrimage page with invalid input field")
    log.info("*#" * 20)
    result = lp.all_empty_field()
    try:
        assert_that(True, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in verifying all field empty")
        raise e



