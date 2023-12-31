from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPasword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linktext).click()




# class LoginPage:
#     # Login Page
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login_xpath = "//input[@value='Log in']"
#     link_logout_linktext = "Logout"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def setUserName(self, username):
#         self.driver.find_element(By.ID, self.textbox_username_id).clear()
#         self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.ID, self.textbox_password_id).clear()
#         self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH,self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element(By.XPATH,self.link_logout_linktext).click()
#
#
