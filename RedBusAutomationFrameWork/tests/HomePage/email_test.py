from pages.Home_Page.email import Emailpage
from utilities.screenshot import take_screenshot
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)


@pytest.mark.run(order=1)
def test_invalid_credential(oneTimeSetUp):
    lp = Emailpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test with invalid ticket credentials")
    log.info("*#" * 20)
    result = lp.email_functionality(ticket_no="23456", email="dfghj")
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! invalid credential")
        raise e



@pytest.mark.run(order=2)
def test_empty_ticket(oneTimeSetUp):
    lp = Emailpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test with empty ticket number")
    log.info("*#" * 20)
    result = lp.email_functionality(email="dfghj")
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! empty ticket")
        raise e


@pytest.mark.run(order=3)
def test_empty_email(oneTimeSetUp):
    lp = Emailpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test with empty email")
    log.info("*#" * 20)
    result = lp.email_functionality(ticket_no="123456")
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! empty email")
        raise e


@pytest.mark.run(order=4)
def test_empty_credentials(oneTimeSetUp):
    lp = Emailpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test with empty credredentials")
    log.info("*#" * 20)
    result = lp.email_functionality()
    try:
        assert_that(True, result)
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! empty credentials")
        raise e


@pytest.mark.skip
def test_valid_credential():
    pass


