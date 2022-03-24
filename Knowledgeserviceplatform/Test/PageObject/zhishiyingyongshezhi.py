import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base.Base import Bases

class ZhishiyingyongsehzhiOperPage(Bases):

    #点击要设置的应用
    def click_yingyong(self):
        self.click(By.XPATH,"//div[contains(text(),'知识应用自动创建')]")

    #点击确定
    def click_queding(self):
        time.sleep(1)
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]")
        time.sleep(1)

    #点击设置
    def click_shezhi(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        time.sleep(1)

    #点击区域数
    def click_quyushu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/form[1]//div[1]")
        time.sleep(1)

    #点击区域数量
    def click_quyushuliang(self,value):
        self.click(By.XPATH,"//span[contains(text(),'"+value+"')]")
        time.sleep(1)

    #点击布局
    def click_buju(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]//div[1]")
        time.sleep(1)

    #点击布局默认是纵向，可以点击横向
    def click_bujuhengxiang(self):
        self.click(By.XPATH,"//span[contains(text(),'横向')]")
        time.sleep(1)

    #输入区域1
    def input_quyuyi(self,value):
        self.input(By.XPATH,"//input[@id='0']",value)

    #输入区域2
    def input_quyuer(self,value):
        self.input(By.XPATH,"//input[@id='1']",value)

    #输入区域3
    def input_quyusan(self,value):
        self.input(By.XPATH,"//input[@id='2']",value)

    #输入区域4
    def input_quyusi(self,value):
        self.input(By.XPATH,"//input[@id='3']",value)

    #点击保存
    def click_baocun(self):
        self.click(By.XPATH,"//span[contains(text(),'保存')]")

class ZhishiyingyongsehzhiSecan(Bases):

    def chuangjiansehzhi(self,value1,value2,value3,value4):
        ZhishiyingyongsehzhiOperPage(self.driver).click_yingyong()
        ZhishiyingyongsehzhiOperPage(self.driver).click_queding()
        ZhishiyingyongsehzhiOperPage(self.driver).click_shezhi()
        ZhishiyingyongsehzhiOperPage(self.driver).input_quyuyi(value1)
        ZhishiyingyongsehzhiOperPage(self.driver).input_quyuer(value2)
        ZhishiyingyongsehzhiOperPage(self.driver).input_quyusan(value3)
        ZhishiyingyongsehzhiOperPage(self.driver).input_quyusi(value4)
        ZhishiyingyongsehzhiOperPage(self.driver).click_baocun()
        time.sleep(1)
