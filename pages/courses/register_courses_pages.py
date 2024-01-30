from selenium.webdriver.common.by import By

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@id='search']"
    _search_icon = "//div[@class='input-group']/button/i"
    _course = "//h4[contains(text(), 'JavaScript for beginners')]"
    _all_courses = "//a[@href='/courses']"
    _enroll_button = "//button[contains(text(), 'Enroll in Course')]"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_exp = "//input[@placeholder='MM / YY']"
    _cc_cvv = "//input[@placeholder='Security Code']"
    _submit_enroll = "//div[@class='col-xs-12']//button"
    _enroll_error_message = "//div[@class='card-errors has-error']/ul[@class='list-unstyled']/li[@class='card-no text-danger']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementClick(self._search_icon, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course, locatorType="xpath")

    def enterCardNum(self, num):
        self.switchFrameByIndex(self._cc_num, locatorType="xpath")
        time.sleep(2)
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        time.sleep(1)
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchFrameByIndex(self._cc_exp, locatorType="xpath")
        time.sleep(2)
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        time.sleep(1)
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchFrameByIndex(self._cc_cvv, locatorType="xpath")
        time.sleep(2)
        self.sendKeys(cvv, self._cc_cvv, locatorType="xpath")
        time.sleep(1)
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def clickAllCoursesLink(self):
        self.elementClick(self._all_courses, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")
        time.sleep(2)
        self.webScroll(direction="down")
        time.sleep(2)
        self.enterCreditCardInformation(num, exp, cvv)
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(locator=self._enroll_error_message, locatorType="xpath",
                                             pollFrequency=1)
        result = self.isElementDisplayed(element=messageElement)
        return result

