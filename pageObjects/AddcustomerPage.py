from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Addcustomer:
    # customer add page

    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customer_menuitem_xpath = '//a[@href="/Admin/Customer/List"]/p[contains(text(),"Customers")]'
    btnAddnew_xxpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_id = 'VendorId'
    rdMaleGender_id = 'Gender_Male'
    rdFemaleGender_id = 'Gender_Female'
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    btnSave_xpath = "//button[@name='save']"
    txtAdminContent = "//textarea[@id='AdminComment']"

    def __init__(self, driver):
        self.driver = driver
    # def __init__(self, driver):
    #     super().__init__(driver)

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOncustomersMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnk_Customer_menuitem_xpath).click()

    # def clickOnAddnew(self):
    #     self.driver.find_element(By.XPATH, self.btnAddnew_xxpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xxpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        #
        # elif role == 'Administrators':
        #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        #
        # elif role == 'Guests':
        #     self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        #
        # # here user can be registered or (Guests) ,only one
        #
        #     time.sleep(3)
        #     self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        # elif role == 'Registered':
        #     self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        #
        # elif role == 'Vendors':
        #     self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        #
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        #
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click();",self.listitem)

    def SetManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, cmname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(cmname)

    def setadminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAdminContent).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

        
















