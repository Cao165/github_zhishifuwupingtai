import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class BiaoguanliPageOper(Bases):

    def click_biaoguanli(self):
        self.click(By.XPATH,"//a[contains(text(),'表管理')]")

    def input_sousuo1(self,value):
        self.input(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",value)
        time.sleep(1)
        self.inputenter(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",Keys.ENTER)
        time.sleep(1)

    def input_sousuo2(self,value):
        self.input(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]//div[1]/div[2]/div[1]/span[1]/input[1]",value)
        time.sleep(1)
        self.inputenter(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]//div[1]/div[2]/div[1]/span[1]/input[1]")
        time.sleep(1)

    def gettext1(self):
        ele=self.text(By.XPATH,"//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]//div[1]/div[2]//div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]")
        return ele

    def gettext2(self):
        ele=self.text(By.XPATH,"//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]//div[1]/div[2]//div[1]/table[1]/tbody[1]/tr[1]/td[2]")
        return ele

    def zuoying(self):
        self.click(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]")

    def youying(self):
        self.click(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/button[2]")

    def zuopiliang(self):
        self.click(By.XPATH,"//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]//div[1]/div[2]//div[1]/table[1]/thead[1]/tr[1]/th[1]/div[1]/label[1]/span[1]/input[1]")

    def click_queding(self):
        self.click(By.XPATH,"//span[contains(text(),'确 定')]")

    def youpiliang(self):
        self.click(By.XPATH,"//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/d/div[1]/div[2]//div[1]/table[1]/thead[1]/tr[1]/th[1]/div[1]/label[1]/span[1]/input[1]")