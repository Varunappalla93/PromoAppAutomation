import unittest
from selenium import webdriver
import sys
sys.path.append("C:/Users/LENOVO/PycharmProjects/PromoAppAutomation")
from PageObjects.LoginPage import loginPage
import time

class Logintest(unittest.TestCase):
    url="https://thepromoapp.com/#!/login"
    username="varuna"
    password="V@run1993e"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_login(self):
        lp=loginPage(self.driver)
        lp.setuserID(self.username)
        lp.setpwd(self.password)
        lp.login()
        time.sleep(10)
        lp.logoutuserbtn()
        time.sleep(10)
        lp.clicklogout()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main()
