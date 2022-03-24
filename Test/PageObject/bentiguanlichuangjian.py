import time
from selenium.webdriver.common.by import By

from Knowledgeserviceplatform.base.Base import Bases

class BentichuangjianOperPage(Bases):

    def click_chuangjian(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")

    def input_mingchen(self,value):
        self.input(By.XPATH,"//input[@id='name']",value)

    def click_baocun(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

class BentiguanliSecan(Bases):

    def chuangjian(self,value):
        time.sleep(1)
        BentichuangjianOperPage(self.driver).click_chuangjian()
        time.sleep(1)
        BentichuangjianOperPage(self.driver).input_mingchen(value)
        BentichuangjianOperPage(self.driver).click_baocun()
        time.sleep(1)