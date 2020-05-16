import unittest
from selenium import webdriver
import sys
import HtmlTestRunner
sys.path.append("C:/Users/LENOVO/PycharmProjects/PromoAppAutomation")
from PageObjects.LoginPage import loginPage
from PageObjects.ManageEvent import ManageEvent
import time

class ManageEventtest(unittest.TestCase):
    url="https://thepromoapp.com/#!/login"
    username="varuna"
    password="V@run1993e"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_manageevent(self):
        lp=loginPage(self.driver)
        lp.setuserID(self.username)
        lp.setpwd(self.password)
        lp.login()
        time.sleep(10)
        me=ManageEvent(self.driver)
        me.userprbtn()
        time.sleep(3)
        me.mngevent()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main()
