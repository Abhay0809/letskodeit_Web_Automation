# from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _loginLink = "//a[@href='/login']"
    _emailField = "email"
    _passwordField = "login-password"
    _loginButton = "login"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._loginLink)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._emailField)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._passwordField)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._loginButton)

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(self._loginLink, locatorType="xpath")

    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._emailField)

    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._passwordField)

    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.elementClick(self._loginButton, locatorType="id")

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.clearFields()
        time.sleep(2)
        self.enterEmail(username)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()
        time.sleep(2)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[contains(text(), 'My Account')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]", locatorType="xpath")
        return result

    def verifyTitle(self):
        # return self.verifyPageTitle("TESTING WRONG TITLE")
        return self.verifyPageTitle("My Courses")

    def clearFields(self):
        emailField = self.getElement(locator=self._emailField)
        emailField.clear()
        passwordField = self.getElement(locator=self._passwordField)
        passwordField.clear()

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//a[@class='dynamic-link']//span[@class='caret']", locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//a[@href='/logout']", locatorType="xpath")
