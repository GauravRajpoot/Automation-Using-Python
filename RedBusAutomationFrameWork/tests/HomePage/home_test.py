from pages.Home_Page.home import ResBusHomePage
from utilities.screenshot import take_screenshot
from pages.Home_Page.cancel import Cancelpage
from utilities.read_from_excel import readData
import pytest
import utilities.custom_logger as cl
import logging
from hamcrest import *

log = cl.customLogger(logging.DEBUG)


@pytest.mark.run(order=1)
def test_booking_with_valid_credentials(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test_busbooking with valid credentials started")
    log.info("*#" * 20)
    lp.search_bus(oneTimeSetUp, source=readData("Home", 2, 3),
                  destination=readData("Home", 2, 4))
    result = lp.verifyLoginSuccessful()
    try:
        assert result == True
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!!Valid email passing")
        raise e


@pytest.mark.run(order=2)
def test_bus_booking_invalid_field1(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test bus booking started with both source and destination field empty")
    log.info("*#" * 20)
    result = lp.search_bus(oneTimeSetUp)
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 5))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! invalid1")
        raise e


@pytest.mark.run(order=3)
def test_busbooking_invalid_field2(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test bus booking started  destination field empty")
    log.info("*#" * 20)
    result = lp.search_bus(oneTimeSetUp,
                           readData("Home", 2, 3))
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 5))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! invalid2")
        raise e



@pytest.mark.run(order=4)
def test_busbooking_invalid_field3(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test_busbooking started with  source  field empty")
    log.info("*#" * 20)
    result = lp.search_bus(oneTimeSetUp,
                           readData("Home", 2, 4))
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 5))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! input3")
        raise e


@pytest.mark.run(order=5)
def test_cancel_page(oneTimeSetUp):
    lp = Cancelpage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("test_busbooking started with both source and destination field empty")
    log.info("*#" * 20)
    result = lp.cancel_functionality(ticket_no=readData("Home", 2, 6))
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 7))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Cancel Page")
        raise e


@pytest.mark.run(order=6)
def test_red_pool(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("testing pool link")
    log.info("*#" * 20)
    result = lp.bus_pool()
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 8))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Red Bus Pool")
        raise e


@pytest.mark.run(order=7)
def test_help_page(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("testing pool help page")
    log.info("*#" * 20)
    result = lp.help_page()
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 9))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Help Page")
        raise e


@pytest.mark.run(order=8)
def test_login_page(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Login Setup")
    log.info("*#" * 20)
    not_displayed,result = lp.login_setup()
    assert_that(False,equal_to(not_displayed))
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 5))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Login Popup")
        raise e

@pytest.mark.run(order=9)
def test_sms_valid_number(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Sms testing")
    log.info("*#" * 20)
    lp.sms_link(number=readData("Home", 2, 10))
    result = lp.sms_valid_number()
    try:
        assert_that(True,equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! sending sms")
        raise e


@pytest.mark.run(order=10)
def test_sms_valid_invalid_number(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("invalid sms testing")
    log.info("*#" * 20)
    lp.sms_link(number="qwerty")
    result = lp.sms_invalid_number()
    try:
        assert_that(True,equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! sms with invalid input")
        raise e

@pytest.mark.run(order=11)
def test_sms_valid_empty_number(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Login Setup")
    log.info("*#" * 20)
    lp.sms_link()
    result =lp.sms_invalid_number()
    try:
        assert_that(True,equal_to(result))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! sms empty field")
        raise e


@pytest.mark.run(order=12)
def test_app_store_page(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Testing for app store page")
    log.info("*#" * 20)
    result = lp.apple_page()
    print(type(result),result)
    try:
        assert_that(result,equal_to(readData("Home", 2, 11)))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! App store Page")
        raise e


@pytest.mark.run(order=13)
def test_android_page(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Testing for android page")
    log.info("*#" * 20)
    result = lp.android_page()
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 12))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Android page")
        raise e


@pytest.mark.run(order=14)
def test_verification_page(oneTimeSetUp):
    lp = ResBusHomePage(oneTimeSetUp)
    log.info("*#" * 20)
    log.info("Login ")
    log.info("*#" * 20)
    result = lp.home_page_icon()
    try:
        assert_that(result, is_(equal_to_ignoring_case(readData("Home", 2, 5))))
    except AssertionError as e:
        take_screenshot(driver=oneTimeSetUp, name="Error!!! Home Page")
        raise e


