import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base.Base import Bases

class ShanchuPageOper(Bases):

    def click_shanchu(self):
        self.click(By.XPATH,"//a[contains(text(),'删除')]")

    def click_queding(self):
        self.click(By.XPATH," //span[contains(text(),'确 定')]")

    def click_quxiao(self):
        self.click(By.XPATH,"//span[contains(text(),'取 消')]")

    def click_piliangshanchu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]/div[1]/div[2]//div[1]/div[2]/button[1]")

    def click_piliangkuang(self):
        self.click(By.XPATH,"//thead/tr[1]/th[1]/div[1]/label[1]/span[1]/input[1]")

class ShanchuSecan(Bases):

    def ShanchuSecan(self):
        ShanchuPageOper(self.driver).click_shanchu()
        time.sleep(1)
        ShanchuPageOper(self.driver).click_queding()
        time.sleep(1)

    def piliangshanchu(self):
        ShanchuPageOper(self.driver).click_piliangkuang()
        time.sleep(1)
        ShanchuPageOper(self.driver).click_piliangshanchu()
        time.sleep(1)
        ShanchuPageOper(self.driver).click_queding()
        time.sleep(1)