import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base import Base

#页面元素对象层
class LoginPageOper(Base.Bases):

    #用户名定位
    def find_username(self,user):
        self.input(By.ID, "username",user)

    #密码定位
    def find_password(self,passs):
        self.input(By.ID, "password",passs)

    #保存密码定位
    def find_baocun(self):
        self.click(By.XPATH, "//body/div[@id='root']/div[1]//label[1]//input[1]")

    #按钮定位
    def find_button(self):
        self.click(By.XPATH, "//body/div[@id='root']/div[1]//button[1]")

class LoginSecan(Base.Bases):
    def login(self,username,password):
        LoginPageOper(self.driver).find_username(username)
        LoginPageOper(self.driver).find_password(password)
        LoginPageOper(self.driver).find_baocun()
        time.sleep(1)
        LoginPageOper(self.driver).find_button()
