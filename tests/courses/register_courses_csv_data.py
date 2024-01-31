import time

from pages.courses.register_courses_pages import RegisterCoursesPage
from selenium.webdriver.common.by import By
from pages.home.navigation_page import NavigationPage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        # self.courses.driver.get("https://www.letskodeit.com/")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        self.courses.driver.delete_all_cookies()
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\Abhay_Anand\\PycharmProjects\\letskodeit\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.lp.login("abhay@mailinator.com", "Abhay@0809")
        time.sleep(2)
        self.courses.clickAllCoursesLink()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        # self.driver.find_element(By.XPATH, "//a[@class='navbar-brand header-logo']").click()
        # self.courses.driver.get("https://www.letskodeit.com/courses")
