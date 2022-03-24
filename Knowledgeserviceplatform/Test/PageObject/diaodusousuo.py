import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from Knowledgeserviceplatform.base.Base import Bases

class DiaoDuSousuodiaodu(Bases):

    def input_sousuo(self,value):
        self.input(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]/div[1]/div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",value)
        time.sleep(1)
        self.inputenter(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]/div[1]/div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",Keys.ENTER)
        time.sleep(1)

    def gettext(self):
        get=self.text(By.XPATH,"//tbody/tr[1]/td[2]")
        return get

    def click_diaodu(self):
        self.click(By.XPATH,"//a[contains(text(),'调度')]")

    def click_queding(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

    def click_gengduo(self):
        self.click(By.XPATH,"//*[contains(text(),'更多')]")

    def click_xiugai(self):
        self.click(By.XPATH,"//a[contains(text(),'修改')]")

    def click_xiugaiqueding(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

    def click_shanchu(self):
        self.click(By.XPATH,"//a[contains(text(),'删除')]")

    def click_shanchuqeuding(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

    def click_piliangkuangshanchu(self):
        self.click(By.XPATH,"//thead/tr[1]/th[1]/div[1]/label[1]/span[1]/input[1]")

    def click_piliangshanchu(self):
        self.click(By.XPATH,"//span[contains(text(),'删 除')]")

class DiaoDuSousuodiaoduSecan(Bases):

    def diaodu(self):
        DiaoDuSousuodiaodu(self.driver).click_diaodu()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_queding()
        time.sleep(1)

    def xiugai(self):
        DiaoDuSousuodiaodu(self.driver).click_gengduo()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_xiugai()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_xiugaiqueding()
        time.sleep(1)

    def shanchu(self):
        DiaoDuSousuodiaodu(self.driver).click_gengduo()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_shanchu()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_xiugaiqueding()
        time.sleep(1)

    def xuanzhongshanchu(self):
        DiaoDuSousuodiaodu(self.driver).click_piliangkuangshanchu()
        DiaoDuSousuodiaodu(self.driver).click_piliangshanchu()
        time.sleep(1)
        DiaoDuSousuodiaodu(self.driver).click_shanchuqeuding()