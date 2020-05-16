from selenium.webdriver.support.ui import WebDriverWait
class loginPage:
    #Login and logout Locators
    #username="//input[@id='input_0']"
    username="//input[@id='input_0']"
    password="//input[@id='input_1']"
    loginxp="//*[@id='login_form']/div[2]/button"
    userbtn = "/html/body/div[2]/div/div[1]/div/md-toolbar[3]/div/div[6]/span/button/img"
    logout = "//a[contains(text(),'Logout')]"

    #SignUp Locators
    signupuser="#input_0"
    signupemail="//*[@name='Email']"
    signupwd="/html/body/div[2]/div/div[3]/div/div[2]/div/md-content/form/md-input-container[3]/input"
    signuploc="//*[@id='signup_form']/md-input-container[4]/div[1]/div/span/a/md-icon"
    signupbtn="//*[@id='signup_form']/div[1]/button"


    def __init__(self,driver):
        self.driver=driver

    def setuserID(self,username):
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def setpwd(self,password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.loginxp).click()

    def signupuserID(self,username1):
        self.driver.find_element_by_css_selector(self.signupuser).send_keys(username1)

    def signupuseremail(self,email):
        self.driver.find_element_by_xpath(self.signupemail).send_keys(email)

    def signupuserpwd(self, pwd):
        self.driver.find_element_by_xpath(self.signupwd).send_keys(pwd)

    def signupuserloc(self):
        self.driver.find_element_by_xpath(self.signuploc).click()

    def signupuserbtn(self):
        self.driver.find_element_by_xpath(self.signupbtn).click()

    def logoutuserbtn(self):
        self.driver.find_element_by_xpath(self.userbtn).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.logout).click()












