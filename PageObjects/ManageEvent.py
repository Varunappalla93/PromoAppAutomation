class ManageEvent:
    userbtn = "/html/body/div[2]/div/div[1]/div/md-toolbar[3]/div/div[6]/span/button/img"
    mngeventbtn = "//span[contains(text(),'Manage Event')]"

    def __init__(self, driver):
        self.driver = driver

    def userprbtn(self):
        self.driver.find_element_by_xpath(self.userbtn).click()

    def mngevent(self):
        self.driver.find_element_by_xpath(self.mngeventbtn).click()
