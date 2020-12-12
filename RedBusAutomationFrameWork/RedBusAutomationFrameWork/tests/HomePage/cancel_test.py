from pages.Home_Page.cancel import Cancelpage
from utilities.screenshot import take_screenshot
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)


@pytest.mark.run(order=1)
def test_cancel_invalid_credential(oneTimeSetUp):
    lp = Cancelpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Cancel page test with invalid credential")
    log.info("*#" * 20)
    result = lp.cancel_functionality(ticket_no="1234567",email="dfghj")
    try:
        assert_that(result, is_(equal_to_ignoring_case("Cancel Ticket - redBus")))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! invalid credential")
        raise e


@pytest.mark.run(order=2)
def test_cancel_empty_ticket(oneTimeSetUp):
    lp = Cancelpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Cancel page test with empty ticket")
    log.info("*#" * 20)
    result = lp.cancel_functionality(email="dfghj")
    try:
        assert_that(result, is_(equal_to_ignoring_case("Cancel Ticket - redBus")))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! in cancel empty ticket")
        raise e


@pytest.mark.run(order=3)
def test_cancel_empty_email(oneTimeSetUp):
    lp = Cancelpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Cancel page test with empty email")
    log.info("*#" * 20)
    result = lp.cancel_functionality(ticket_no="12345")
    try:
        assert_that(result, is_(equal_to_ignoring_case("Cancel Ticket - redBus")))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! in empty email")
        raise e


@pytest.mark.run(order=4)
def test_cancel_empty_credential(oneTimeSetUp):
    lp = Cancelpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Cancel page test with empty both the field")
    log.info("*#" * 20)
    result = lp.cancel_functionality()
    try:
        assert_that(result, is_(equal_to_ignoring_case("Cancel Ticket - redBus")))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! in empty both field")
        raise e



@pytest.mark.skip
def test_valid_credential():
    pass


