import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class ChuanjianOperPage(Bases):

    def click_chuangjian(self):

        self.click(By.XPATH,"//span[contains(text(),'创 建')]")

    def input_renwumingchen(self,value):
        self.input(By.XPATH,"//input[@id='name']",value)

    #关系录入调度任务
    def click_diaoduleixing(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]//div[1]/span[2]")
        time.sleep(1)
        jsl="document.getElementById('beanName').removeAttribute('unselectable')"
        self.driver.execute_script(jsl)
        time.sleep(2)
        self.inputenter(By.Id,"beanName",Keys.ARROW_DOWN)
        time.sleep(2)
        self.inputenter(By.Id,"beanName",Keys.ENTER)
        time.sleep(1)

    # 关系录入调度任务下拉
    def click_diaoduxiala(self):
        self.click(By.XPATH,"//*[contains(text(),'关系录入调度任务')]")
        time.sleep(1)

    # 关系录入调度任务
    def click_diaoduleixing1(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
        time.sleep(1)
        self.inputenter(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]",Keys.ARROW_DOWN)
        time.sleep(2)
        self.inputenter(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]",Keys.ENTER)
        time.sleep(3)

    #全量
    def click_quanliang(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/label[2]/span[1]/input[1]")

    #周期
    def click_zhouqi(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]")
    #周
    def click_zhou(self):
        time.sleep(1)
        self.click(By.XPATH,"//span[contains(text(),'周')]")
        time.sleep(1)

    #指定时间
    def click_shijian(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]")

    #星期天
    def click_tian(self):
        self.click(By.XPATH,"//*[contains(text(),'星期天')]")


    #点击开始时间
    def click_kaishishijian(self):
        self.click(By.XPATH,"//input[@id='startTime']")
    # 输入开始时间
    def click_shurukaishishijian(self,value):
        time.sleep(2)
        self.click(By.XPATH,"//*[contains(text(),'"+value+"')]")
    #输入开始时间回车
    def input_kaishishijianhuiche(self):
        time.sleep(1)
        self.inputenter(By.XPATH,"//input[@id='startTime']",Keys.ENTER)
        time.sleep(1)

    # 点击结束时间
    def click_jieshushijian(self):
        self.click(By.XPATH, "//input[@id='endTime']")
    # 输入结束时间
    def click_shurujieshushijian(self, value):
        time.sleep(2)
        self.click(By.XPATH, "//*[contains(text(),'" + value + "')]")
    # 输入结束时间回车
    def input_jieshushijianhuiche(self):
        time.sleep(1)
        self.inputenter(By.XPATH, "//input[@id='endTime']", Keys.ENTER)
        time.sleep(1)

    #输入选择映射并回车
    def click_xuanzeyingshe(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")

    def click_xuanzexiala(self):
        time.sleep(1)
        self.click(By.XPATH,"//*[contains(text(),'部门实体映射')]")

    #确定
    def click_queding(self):
        self.click(By.XPATH,"//span[contains(text(),'确 定')]")

class diaoduchuangjianSecan(Bases):

    #实体-增量-
    def shitizengliang1(self,renwuvalue):
        #创建
        ChuanjianOperPage(self.driver).click_chuangjian()
        #输入任务
        ChuanjianOperPage(self.driver).input_renwumingchen(renwuvalue)
        #输入时间
        # self.diaoduchuangjianSecan()
        #选择映射
        ChuanjianOperPage(self.driver).click_xuanzeyingshe()
        ChuanjianOperPage(self.driver).click_xuanzexiala()
        #确定
        ChuanjianOperPage(self.driver).click_queding()
        time.sleep(1)

    #实体-全量-
    def shitizengliang2(self,renwuvalue):
        #创建
        ChuanjianOperPage(self.driver).click_chuangjian()
        #输入任务
        ChuanjianOperPage(self.driver).input_renwumingchen(renwuvalue)
        #全量
        ChuanjianOperPage(self.driver).click_quanliang()
        #选择映射
        ChuanjianOperPage(self.driver).click_xuanzeyingshe()
        ChuanjianOperPage(self.driver).click_xuanzexiala()
        #确定
        ChuanjianOperPage(self.driver).click_queding()
        time.sleep(1)

    #创建输入时间
    def chuangjianshijian(self):
        # 创建
        ChuanjianOperPage(self.driver).click_chuangjian()

        #点击开始时间
        ChuanjianOperPage(self.driver).click_kaishishijian()
        #输入开始时间
        ChuanjianOperPage(self.driver).click_shurukaishishijian("07")
        #点击开始时间回车
        ChuanjianOperPage(self.driver).input_kaishishijianhuiche()
        #点击开始时间
        ChuanjianOperPage(self.driver).click_kaishishijian()
        #输入开始时间
        ChuanjianOperPage(self.driver).click_shurukaishishijian("09")
        #点击开始时间回车
        ChuanjianOperPage(self.driver).input_kaishishijianhuiche()

        # 点击结束时间
        ChuanjianOperPage(self.driver).click_jieshushijian()
        # 输入结束时间
        ChuanjianOperPage(self.driver).click_shurujieshushijian("07")
        # 点击开始时间回车
        ChuanjianOperPage(self.driver).input_jieshushijianhuiche()
        # 点击结束时间
        ChuanjianOperPage(self.driver).click_jieshushijian()
        # 输入结束时间
        ChuanjianOperPage(self.driver).click_shurujieshushijian("14")
        # 点击开始时间回车
        ChuanjianOperPage(self.driver).input_jieshushijianhuiche()
        # 点击结束时间
        ChuanjianOperPage(self.driver).click_jieshushijian()
        # 输入结束时间
        ChuanjianOperPage(self.driver).click_shurujieshushijian("18")
        # 点击结束时间回车
        ChuanjianOperPage(self.driver).input_jieshushijianhuiche()

    #关系-增量-
    # def shitizengliang3(self,renwuvalue):
    #     #创建
    #     ChuanjianOperPage(self.driver).click_chuangjian()
    #     #输入任务
    #     ChuanjianOperPage(self.driver).input_renwumingchen(renwuvalue)
    #     ChuanjianOperPage(self.driver).click_diaoduleixing()
    #     #ChuanjianOperPage(self.driver).click_diaoduxiala()
    #     #选择映射
    #     ChuanjianOperPage(self.driver).click_xuanzeyingshe()
    #     ChuanjianOperPage(self.driver).click_xuanzexiala()
    #     #确定
    #     ChuanjianOperPage(self.driver).click_queding()
    #     time.sleep(1)
