import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()

    path = "TestData/LoginData.xlsx"

    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("****************Test_002_Login************")
        self.logger.info("****************verifying ddt test************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows in a excel :', self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPasword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info('*******passed**********')
                    self.lp.ClickLogout()
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info('*******failed**********')
                    self.lp.ClickLogout();
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info('*******filed**********')
                    self.lp.ClickLogout();
                    lst_status.append('Fail')
                elif self.exp == 'Fail':
                    self.logger.info('*******Passed**********')
                    self.lp.ClickLogout();
                    lst_status.append('Pass')

            if 'Fail' not in lst_status:
                self.logger.info("*******Login DDT Test passed")
                self.driver.close()
                return True
            else:
                self.logger.info("*******Login DDT Test Failed")
                self.driver.close()
                return False

        self.logger.info('****End of Login ddt test *****')
        self.logger.info('****completed TC_LoginDDT_002  *****')




