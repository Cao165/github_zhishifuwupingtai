import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base.Base import Bases

class ZhishiyingyongXuanzhi(Bases):

    #悬置应用
    def movecickyingyong(self):
        self.moveclick(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]")

    #修改
    def click_xiugai(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/*[1]")

    #保存
    def click_baocun(self):
        self.click(By.XPATH, "//span[contains(text(),'保存')]")

    #删除
    def click_shanchu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/span[2]/*[1]")

    #确定
    def click_queding(self):
        self.click(By.XPATH,"//*[contains(text(),'是')]")

class ZhishiyingyongXuanzhiSecan(Bases):

    def xiugaiSecan(self):
        ZhishiyingyongXuanzhi(self.driver).movecickyingyong()
        time.sleep(1)
        ZhishiyingyongXuanzhi(self.driver).click_xiugai()
        time.sleep(1)
        ZhishiyingyongXuanzhi(self.driver).click_baocun()
        time.sleep(1)

    def shanchuSecan(self):
        ZhishiyingyongXuanzhi(self.driver).movecickyingyong()
        time.sleep(1)
        ZhishiyingyongXuanzhi(self.driver).click_shanchu()
        time.sleep(1)
        ZhishiyingyongXuanzhi(self.driver).click_queding()
        time.sleep(1)
