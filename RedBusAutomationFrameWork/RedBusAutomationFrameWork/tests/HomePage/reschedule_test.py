from pages.Home_Page.reschedule import Reschedulepage
from utilities.screenshot import take_screenshot
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)


@pytest.mark.run(order=1)
def test_cancel_invalid_credential(oneTimeSetUp):
    lp = Reschedulepage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Cancel page test with invalid credential")
    log.info("*#" * 20)
    result = lp.reschedule_functionality(ticket_no="1234567",email="dfghj")
    try:
        assert_that(result, is_(equal_to_ignoring_case("https://www.redbus.in/Reschedule")))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! invalid credentials")
        raise e


@pytest.mark.skip
def test_valid_credential():
    pass


