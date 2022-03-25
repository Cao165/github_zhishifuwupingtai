import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class ChuangjianPageOper(Bases):
    def click_chuangjian(self):
        self.click(By.XPATH,"//span[contains(text(),'创 建')]")

    def input_sehyingmingchen(self,value):
        self.input(By.XPATH,"//input[@id='mappingName']",value)

    def click_zengliangziduan(self):
        self.click(By.XPATH,"//input[@id='selectRule']")

    def input_zengliangziduanxiala(self,value):
        self.click(By.XPATH,"//*[contains(text(),'"+value+"')]")

    #滚动底部
    def gundongdibu(self):
        jsl="window.scrollTo(0,500)"
        self.driver.execute_script(jsl)
        time.sleep(2)

    #确定
    def click_queding(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

    #关系映射
    def guanxiyingshe(self):
        self.click(By.XPATH,"//span[contains(text(),'关系映射')]")

    #目的实体属性
    def mudishuxing(self):
        ele=self.find(By.ID,"target_item_id")
        ele=self.find(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[3]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
        ele2=self.find(By.XPATH,"//tbody/tr[@id='result_dkg_sys_name']/td[1]")
        ActionChains(self.driver).drag_and_drop(ele,ele2).perform()
        # ActionChains(self.driver).drag_and_drop_by_offset(ele, -200, 0).perform()
        # time.sleep(5)

    #节点属性
    def jiedianshuxing(self):
        ele=self.find(By.XPATH,"//body[1]//div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[4]/div[3]/div[5]//div[1]/table[1]/tbody[1]/tr[1]/td[1]")
        ele2=self.find(By.XPATH,"//tbody/tr[@id='fromResultLeft_transaction_hierarchy']/td[1]")
        ActionChains(self.driver).drag_and_drop(ele,ele2)
        time.sleep(2)

    #终点属性
    def zhongxianshuxi(self):
        ele=self.find(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[5]/div[3]/div[5]//div[1]/table[1]/tbody[1]/tr[1]/td[1]")
        ele2=self.find(By.XPATH,"//tbody/tr[@id='toResultLeft_material_remark']/td[1]")
        ActionChains(self.driver).drag_and_drop(ele,ele2)
        time.sleep(2)

class ChuangjianSecan(Bases):

    #创建实体映射
    def chuangjianzhishiyingshe(self,ysmcvalue,zlxlvalue):
        ChuangjianPageOper(self.driver).click_chuangjian()
        ChuangjianPageOper(self.driver).input_sehyingmingchen(ysmcvalue)
        ChuangjianPageOper(self.driver).click_zengliangziduan()
        ChuangjianPageOper(self.driver).input_zengliangziduanxiala(zlxlvalue)
        # ChuangjianPageOper(self.driver).mudishuxing()
        ChuangjianPageOper(self.driver).gundongdibu()
        ChuangjianPageOper(self.driver).click_queding()
        time.sleep(2)

    #创建关系映射
    def chuangjianguanxiyingshe(self,ysmcvalue,zlxlvalue):
        ChuangjianPageOper(self.driver).click_chuangjian()
        ChuangjianPageOper(self.driver).guanxiyingshe()
        ChuangjianPageOper(self.driver).input_sehyingmingchen(ysmcvalue)
        time.sleep(1)
        ChuangjianPageOper(self.driver).click_zengliangziduan()
        ChuangjianPageOper(self.driver).input_zengliangziduanxiala(zlxlvalue)
        time.sleep(1)
        # ChuangjianPageOper(self.driver).jiedianshuxing()
        # ChuangjianPageOper(self.driver).zhongxianshuxi()
        ChuangjianPageOper(self.driver).gundongdibu()
        ChuangjianPageOper(self.driver).click_queding()
        time.sleep(2)