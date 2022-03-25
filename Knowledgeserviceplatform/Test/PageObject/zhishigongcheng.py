from selenium.webdriver.common.by import By
from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class GongchengPageOper(Bases):

    #定位知识工程点击
    def click_gongcheng(self):
        self.click(By.XPATH,"//div[contains(text(),'知识工程')]")

    #定位知识抽取点击
    def click_chouqu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[4]/div[1]")

    #定位数据源点击
    def click_shujuyuan(self):
        self.click(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[4]/ul[1]/li[1]/span[1]/a[1]")

    #定位知识映射点击
    def click_zhishiyingshe(self):
        self.click(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[4]/ul[1]/li[2]/span[1]/a[1]")

    #定位调度管理
    def click_diaduguanli(self):
        self.click(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[4]/ul[1]/li[3]/span[1]/a[1]")

    #定位知识应用
    def click_zhishiyingyong(self):
        self.click(By.XPATH,"//div[contains(text(),'知识应用')]")

    #定位知识地图
    def click_zhishiditu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]")

    #定位本体管理
    def click_bentiguanli(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/span[1]")

class GongchengSecan(Bases):
    #数据源
    def click_shujuyuan(self):
        GongchengPageOper(self.driver).click_gongcheng()
        GongchengPageOper(self.driver).click_chouqu()
        GongchengPageOper(self.driver).click_shujuyuan()

    #知识映射
    def click_zhishiyingshe(self):
        GongchengPageOper(self.driver).click_gongcheng()
        GongchengPageOper(self.driver).click_chouqu()
        GongchengPageOper(self.driver).click_zhishiyingshe()

    #调度管理
    def click_diaoduguanli(self):
        GongchengPageOper(self.driver).click_gongcheng()
        GongchengPageOper(self.driver).click_chouqu()
        GongchengPageOper(self.driver).click_diaduguanli()

    #知识应用
    def click_zhishiyingyong(self):
        GongchengPageOper(self.driver).click_zhishiyingyong()

    #知识地图
    def click_zhishiditu(self):
        GongchengPageOper(self.driver).click_zhishiditu()

    #本体管理
    def click_bentiguanli(self):
        GongchengPageOper(self.driver).click_gongcheng()
        GongchengPageOper(self.driver).click_bentiguanli()




