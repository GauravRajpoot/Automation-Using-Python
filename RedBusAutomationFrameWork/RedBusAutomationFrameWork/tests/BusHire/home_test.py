from pages.BusHire_Page.home import Bushire
from utilities.read_from_excel import readData
from utilities.screenshot import take_screenshot
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)
@pytest.mark.run(order=1)
def test_verify_home_page(oneTimeSetUp):
    lp = Bushire(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Bus hiring page validation for the home page")
    log.info("*#" * 20)
    result = lp.varify_page()
    try:
        assert_that(True, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Verifying the Bus Hire Home Page")
        raise e


@pytest.mark.run(order=2)
def test_bus_hire(oneTimeSetUp):
    lp = Bushire(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Bus Hiring with valid input")
    log.info("*#" * 20)
    validation = lp.bus_hire_functionality(hire_city=readData("BusHire", 2, 1),
                                           start=readData("BusHire", 2, 3),
                                           end=readData("BusHire", 2, 2))
    result=validation[1]
    try:
        assert_that(True,equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in Bus Hiring Functionality")
        raise e


@pytest.mark.run(order=3)
def test_empty_start_point(oneTimeSetUp):
    lp = Bushire(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Bus hiring with validation with empty start point")
    log.info("*#" * 20)
    validation = lp.bus_hire_functionality(hire_city=readData("BusHire", 2, 1),
                                           end=readData("BusHire", 2, 2))
    result=validation[0]
    try:
        assert_that(True,equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in empty start point")
        raise e


@pytest.mark.run(order=4)
def test_empty_end_point(oneTimeSetUp):
    lp = Bushire(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Bus hiring with validation with empty end point")
    log.info("*#" * 20)
    validation = lp.bus_hire_functionality(hire_city=readData("BusHire", 2, 1),
                                           start=readData("BusHire", 2, 3))
    result = validation[0]
    try:
        assert_that(True, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in empty end point")
        raise e


@pytest.mark.run(order=5)
def test_all_fields_empty(oneTimeSetUp):
    lp = Bushire(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Bus hiring with all empty input field")
    log.info("*#" * 20)
    result = lp.all_empty_field()
    try:
        assert_that(True, equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp,
                        name="Error!!! in all empty field")
        raise e


