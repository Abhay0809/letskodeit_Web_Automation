from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    '''
    Need to verify two verification points
    1 fails, code will not go to next verification point
    If assert fails, it will stop the current test execution and
    move to next test method
    '''

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("abhay@mailinator.com", "Abhay@0809")
        time.sleep(3)
        result2 = self.lp.verifyTitle()
        self.ts.mark(result2, "Title is incorrect")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login("abhay@mailinator.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

