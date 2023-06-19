import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import Addcustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("test003 add customer ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.ClickLogin()
        self.logger.info('Login Sucessful')

        self.addCust = Addcustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOncustomersMenuitem()
        self.addCust.clickOnAddnew()
        self.logger.info('providing customer info ')

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword('test123')
        self.addCust.setCustomerRole('Guests')
        self.addCust.SetManagerOfVendor('Vendor 1')
        self.addCust.setGender('Male')
        self.addCust.setFirstName('Prem')
        self.addCust.setLastName('Shelke')
        self.addCust.setDob('12/04/1996')       # format D/ MM/ YY
        self.addCust.setCompanyName(' Wipro ')
        self.addCust.setadminContent(' This is for testing....')
        self.addCust.ClickOnSave()

        self.logger.info('saving customer info ')
        self.logger.info("********** Add Customer Validation Started ******")
        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
        # '/html/body/div[3]/div/div/button'
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info('***Add Customer Test Passed *****')

        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_addCustomer_src.png')
            self.logger.info('*** Add Customer Test Failed ***')
            assert True == False

        self.driver.close()
        self.logger.info('*** Ending Home Page Title test ***')


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars)for i in range(size))








import pytest
# import time
# from pageObjects.LoginPage import LoginPage
# from pageObjects.AddcustomerPage import Addcustomer
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# import string
# import random
#
# class Test_003_AddCustomer:
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#     logger = LogGen.loggen()  # Logger
#
#     # @pytest.mark.sanity
#     # @pytest.mark.regression
#     def test_addCustomer(self,setup):
#         self.logger.info("************* Test_003_AddCustomer **********")
#         self.driver=setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.lp = LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         self.logger.info("************* Login succesful **********")
#
#         self.logger.info("******* Starting Add Customer Test **********")
#
#         self.addcust = Addcustomer(self.driver)
#         self.addcust.clickOnCustomersMenu()
#         self.addcust.clickOnCustomersMenuItem()
#
#         self.addcust.clickOnAddnew()
#
#         self.logger.info("************* Providing customer info **********")
#
#         self.email = random_generator() + "@gmail.com"
#         self.addcust.setEmail(self.email)
#         self.addcust.setPasword("test123")
#         self.addcust.setCustomerRoles("Guests")
#         self.addcust.setManagerOfVendor("Vendor 2")
#         self.addcust.setGender("Male")
#         self.addcust.setFirstName("Pavan")
#         self.addcust.setLastName("Kumar")
#         self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
#         self.addcust.setCompanyName("busyQA")
#         self.addcust.setAdminContent("This is for testing.........")
#         self.addcust.clickOnSave()
#
#         self.logger.info("************* Saving customer info **********")
#
#         self.logger.info("********* Add customer validation started *****************")
#
#         self.msg = self.driver.find_element_by_tag_name("body").text
#
#         print(self.msg)
#         if 'customer has been added successfully.' in self.msg:
#             assert True
#             self.logger.info("********* Add customer Test Passed *********")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
#             self.logger.error("********* Add customer Test Failed ************")
#             assert False
#
#         self.driver.close()
#         self.logger.info("******* Ending Add customer test **********")
#
#
# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
#
#
