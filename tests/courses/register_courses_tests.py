from pages.home.login_page import LoginPage
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.login("abhay@mailinator.com", "Abhay@0809")
        time.sleep(2)
        self.ts.mark("test_invalidEnrollment", "Started execution of invalid enrollment")
        time.sleep(2)
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Login was not successful")
        time.sleep(2)
        self.courses.clickAllCoursesLink()
        time.sleep(2)
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        time.sleep(2)
        self.courses.enrollCourse(num="1234123412341234", exp="1224", cvv="123")
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.driver.quit()



