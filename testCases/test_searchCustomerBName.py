import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName (self, setup):
        self.logger.info('****SearchCustomerByEmail****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.ClickLogin()
        self.logger.info("*****Login Successfully ********")

        self.logger.info("**** Starting search customer by Name  ******")

        self.addCust = Addcustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOncustomersMenuitem()

        self.logger.info('***  searching  customer b y Name  ***** ')
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName('Victoria')
        searchcust.setLastNaame('Terces')
        searchcust.ClickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerByName('Victoria Terces')
        assert True == status
        self.logger.info('*******TC_SearchCustomerByName_005 finished***** ')

