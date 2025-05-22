import time
import pytest

from pageObjects.Loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.XLUtiles import *


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "/home/ethan/Desktop/nopcommerceApp/TestData/LoginTest.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login ***********")
        self.logger.info("*********** Verifying Login DDT Test ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in Excel:", self.rows)

        for r in range(2, self.rows + 1):
            username = XLUtils.readData(self.path, "Sheet1", r, 1)
            password = XLUtils.readData(self.path, "Sheet1", r, 2)
            expected_result = XLUtils.readData(self.path, "Sheet1", r, 3)


            self.lp.setUserName(username)
            self.lp.setPassword(password)
            self.lp.clickLogin()
            time.sleep(10)

            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if act_title == expected_title:
                if expected_result == "Pass":
                    self.logger.info(f"Login Passed for user: {username}")
                    self.lp.clickLogout()
                    time.sleep(2)
                    assert True
                else:
                    self.logger.error(f"Login should have failed but passed for user: {username}")
                    self.lp.clickLogout()
                    time.sleep(2)
                    assert False
            else:
                if expected_result == "Fail":
                    self.logger.info(f"Login Failed as expected for user: {username}")
                    assert True
                else:
                    self.logger.error(f"Login should have passed but failed for user: {username}")
                    self.driver.save_screenshot("./Screenshots/test_Login.png")
                    assert False

        self.driver.quit()
