import time
from selenium.webdriver.common.by import By

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class BentidaochufabuOperPage(Bases):

    def click_xuanzhi(self):
        self.moveclick(By.XPATH,"//*[contains(text(),'自动创建本体')]")

    def click_daochu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[3]/div[1]/div[2]/div[2]")

class BentidaochufabuSecan(Bases):

    def daochuSecan(self):
        # if os.path.exists("C:\\Users\\DELL\\Downloads\\本体_V_1646882356.xlsx"):
        #     os.remove("")
        time.sleep(1)
        BentidaochufabuOperPage(self.driver).click_xuanzhi()
        time.sleep(1)
        BentidaochufabuOperPage(self.driver).click_daochu()
        time.sleep(1)