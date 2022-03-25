import time
from selenium.webdriver.common.by import By
from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class ZhishiyingyongjiaruOperPage(Bases):

    def input_sousuokuang(self,value):
        self.input(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]/input[1]",value)

    def click_sousuo(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]/span[1]")

    def click_zuoce(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]")

    def click_mulv(self):
        self.clickyouji(By.XPATH,"//*[contains(text(),'主题域')]")

    def click_jiaruyingyong(self):
        self.click(By.XPATH,"//span[contains(text(),'当前实体加入应用')]")

    def click_yingyongmingchen(self):
        self.click(By.XPATH,"//div[contains(text(),'知识应用自动创建')]")

    def click_yingyongquyu(self):
        self.click(By.XPATH,"//div[contains(text(),'B')]")

    def click_guanbizuoce(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]")

    def click_guanbishangfang(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[2]/span[1]/*[1]")

class ZhishiyingyongjiaruSecan(Bases):

    def jiaruyingyong(self,value):
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).input_sousuokuang(value)
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_sousuo()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_zuoce()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_guanbizuoce()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_guanbishangfang()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_mulv()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_jiaruyingyong()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_yingyongmingchen()
        time.sleep(1)
        ZhishiyingyongjiaruOperPage(self.driver).click_yingyongquyu()
        time.sleep(1)