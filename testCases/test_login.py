import time
import pytest

from pageObjects.Loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("**************** Test_001_Login *************")
        self.logger.info("**************** Verifying Home Page Title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(3)


        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/ethan/Desktop/nopcommerceApp/Screenshots")
            self.driver.close()
            self.logger.error("*********** Home page title test is passed ***********")

            assert False

    def test_login(self, setup):

        self.logger.info("*********** Verifying the Login Test ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        act_title = self.driver.title

        expected_title = "Dashboard / nopCommerce administration"
        if act_title == expected_title:
            assert True
            self.logger.info("*********** Login test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/ethan/Desktop/nopcommerceApp/Screenshots")
            self.driver.close()
            self.logger.error("*********** Login test is Fail ***********")
            assert False




