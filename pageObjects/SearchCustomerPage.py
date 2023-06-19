from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEMail_id = 'SearchEmail'
    txtFirstName_id = 'SearchFirstName'
    txtLastName_id = 'SearchLastName'
    btnSearch_id = 'search-customers'
    tableRows_xpath = "//table[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']/tbody/tr/td"
    table_xpath = '//*[@id="customers-grid"]'  #"//table[@role='grid']"
    tblSearchResults_xpath = "//table[@aria-describedby='customers-grid_info'] "

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, email):
        self.driver.find_element(By.ID,self.txtEMail_id).clear()
        self.driver.find_element(By.ID,self.txtEMail_id).send_keys(email)

    def setFirstName(self, name):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(name)

    def setLastNaame(self, lname):
        self.driver.find_element(By.ID,self.txtLastName_id).clear()
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = self.driver.find_element(By.XPATH,f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    # def searchCustomerByName(self, Name):
    #     flag = False
    #     for r in range(1, self.getNoOfRows()+1):
    #         table = self.driver.find_element(By.XPATH,self.table_xpath)
    #         name = self.driver.find_element(By    .XPATH,f"//table[@id='customers-grid']/tbody/tr{r}/td/[3]").text
    #         if name == Name:
    #             flag = True
    #             break
    #
    #     return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.ID, self.table_xpath)
            name = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]").text

            if name == Name:
                flag = True
                break

        return flag







