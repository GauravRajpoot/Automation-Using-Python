import openpyxl
import time


def DatePicker(month, date, driver):

    driver.find_element_by_xpath("//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
    monthTxt = driver.find_element_by_xpath("//div[@class='rb-calendar']/table/tbody/tr[1]/td[2]").text
    if monthTxt == month:
        print("Already Selected")
    else:
        for i in range(13):
            driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']//button[contains(text(),'>')]").click()
            monthTxt = driver.find_element_by_xpath("//div[@class='rb-calendar']/table/tbody/tr[1]/td[2]").text
            if monthTxt == month:
                break
        element = driver.find_element_by_xpath(
            "//div[@id='rb-calendar_onward_cal']//td[@class='wd day'][contains(text(),'" + date + "')]")
        time.sleep(1)
        element.click()

def CheckInDate(month, date, driver):
    locator="//*[@id='rb-calendar_checkin_date']/table/tbody/tr[1]/td[2]"
    monthTxt = driver.find_element_by_xpath(locator).text
    if monthTxt == month:
        print("Already Selected")
    else:
        for i in range(13):
            driver.find_element_by_xpath("//div[@id='rb-calendar_checkin_date']//button[contains(text(),'>')]").click()
            monthTxt = driver.find_element_by_xpath(locator).text
            if monthTxt == month:
                break
        element = driver.find_element_by_xpath(
            "//div[@id='rb-calendar_checkin_date']//td[@class='wd day'][contains(text(),'" + date + "')]")
        time.sleep(3)
        element.click()

def CheckOutDate(month, date, driver):
    locator="//*[@id='rb-calendar_checkout_date']/table/tbody/tr[1]/td[2]"
    monthTxt = driver.find_element_by_xpath(locator).text
    if monthTxt == month:
        print("Already Selected")
    else:
        for i in range(13):
            driver.find_element_by_xpath("//div[@id='rb-calendar_checkout_date']//button[contains(text(),'>')]").click()
            monthTxt = driver.find_element_by_xpath(locator).text
            if monthTxt == month:
                break
        element = driver.find_element_by_xpath("//div[@id='rb-calendar_checkout_date']//td[@class='wd day'][contains(text(),'" + date + "')]")
        time.sleep(3)
        element.click()