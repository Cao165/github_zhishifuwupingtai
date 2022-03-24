import os
import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base.Base import Bases

class ZhishiyingyongchuanjianPageOper(Bases):

    #定位创建
    def click_chuangjian(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")

    #输入应用名称
    def input_shurumingchen(self,value):
        self.input(By.XPATH,"//input[@id='name']",value)

    #保存
    def click_queding(self):
        self.click(By.XPATH,"//*[contains(text(),'保存')]")

    #上传图片
    def click_shangchuan(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]//div[1]/span[1]/div[1]/span[1]")

    #选中图片
    def click_tupian(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]//div[1]/div[5]/img[1]")


class ZhishiyingyongchuanjianSecan(Bases):

    #创建
    def chuangjianSecan(self,value):
        ZhishiyingyongchuanjianPageOper(self.driver).click_chuangjian()
        ZhishiyingyongchuanjianPageOper(self.driver).input_shurumingchen(value)
        ZhishiyingyongchuanjianPageOper(self.driver).click_queding()

    #上传图片
    def chuangjiantupianSecan(self,value):
        ZhishiyingyongchuanjianPageOper(self.driver).click_chuangjian()
        ZhishiyingyongchuanjianPageOper(self.driver).input_shurumingchen(value)
        time.sleep(1)
        ZhishiyingyongchuanjianPageOper(self.driver).click_shangchuan()
        time.sleep(1)
        os.system('F:\\下载\\autoit\\upload.exe C:\\Users\\DELL\\Desktop\\111.jfif')
        time.sleep(1)
        ZhishiyingyongchuanjianPageOper(self.driver).click_tupian()
        time.sleep(1)
        ZhishiyingyongchuanjianPageOper(self.driver).click_queding()
        time.sleep(1)