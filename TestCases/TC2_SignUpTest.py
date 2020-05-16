import unittest
from selenium import webdriver
import sys
sys.path.append("C:/Users/LENOVO/PycharmProjects/PromoAppAutomation")
from PageObjects.LoginPage import loginPage
import time


class SignUptest(unittest.TestCase):
    url="https://thepromoapp.com/#!/signup"
    user="anvarun"
    emailid="an.varun1993@rediffmail.com"
    Password="V@run1993"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_signUp(self):
        lp=loginPage(self.driver)
        lp.signupuserID(self.user)
        lp.signupuseremail(self.emailid)
        lp.signupuserpwd(self.Password)
        time.sleep(5)
        lp.signupuserloc()
        time.sleep(10)
        lp.signupuserbtn()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main()
