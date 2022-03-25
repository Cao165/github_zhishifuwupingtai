import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class SuosouPageOper(Bases):

    #搜索框
    def input_sousuokuang(self,value):
        #输入内容
        self.input(By.XPATH,"//body/div[@id='root']//div[1]/section[1]//div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",value)
        time.sleep(1)
        #按键盘回车
        self.inputenter(By.XPATH,"//body/div[@id='root']//div[1]/section[1]//div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",Keys.ENTER)
        time.sleep(1)

    def gettextmingchen(self):
        mctext=self.text(By.XPATH,"//tbody/tr[2]/td[2]")
        return mctext

    def gettextshuoming(self):
        smtext=self.text(By.XPATH,"//tbody/tr[2]/td[3]")
        return smtext

    def getleixingtext(self):
        lxtext=self.text(By.XPATH,"//tbody/tr[2]/td[4]")
        return lxtext

    def getdizhitext(self):
        dztext=self.text(By.XPATH,"//tbody/tr[2]/td[5]")
        return dztext

    def getduanhaokoutext(self):
        dhktext=self.text(By.XPATH,"//tbody/tr[2]/td[6]")
        return dhktext

    def getyonghutext(self):
        yonghutext=self.text(By.XPATH,"//tbody/tr[2]/td[7]")
        return yonghutext

class SousuoSecan(Bases):
    pass



