from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        self.enterEmail(username)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[contains(text(), 'My Account')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]", locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._emailField)
        emailField.clear()
        passwordField = self.getElement(locator=self._passwordField)
        passwordField.clear()