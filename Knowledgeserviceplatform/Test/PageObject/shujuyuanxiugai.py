import time
from selenium.webdriver.common.by import By
from Knowledgeserviceplatform.base.Base import Bases


class XiugaiOperPage(Bases):

    #点击修改
    def click_xiugai(self):
        self.click(By.XPATH,"//a[contains(text(),'修改')]")

    #数据源名称
    def input_shujuyuanmingchen(self,value):
        self.input(By.XPATH,"//input[@id='datasourceName']",value)

    #主机地址
    def input_zhujidizhi(self,value):
        self.input(By.XPATH,"//input[@id='databaseIp']",value)

    #端口号
    def input_duankouhao(self,value):
        self.input(By.XPATH,"//input[@id='databasePort']",value)

    #数据库名
    def input_shujukuming(self,value):
        self.input(By.XPATH,"//input[@id='databaseName']",value)

    #用户名
    def input_yonghuming(self,value):
        self.input(By.XPATH,"//input[@id='databaseUserName']",value)

    #密码
    def input_mima(self,value):
        self.input(By.XPATH,"//input[@id='databasePassword']",value)

    #excel-文件路径
    def input_wenjianlujing(self,value):
        self.input(By.XPATH,"//input[@id='fileDirectory']",value)

    #csv-分隔符
    def input_fengefu(self,value):
        self.input(By.XPATH,"//input[@id='separator']",value)

    #测试
    def click_ceshi(self):
        self.click(By.XPATH,"//span[contains(text(),'测 试')]")

    #确定
    def click_queding2(self):
        self.click(By.XPATH,"//*[contains(text(),'确 定')]")

    #取消
    def click_quxiao(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/button[1]")

    def isenabled(self):
        ele=self.isenable(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[1]/span[1]/input[1]")
        return ele

class XiugaiSecan(Bases):

    def xiugai_mysql_secon(self, shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password):
        # 数据源修改
        XiugaiOperPage(self.driver).click_xiugai()
        # 数据源名称
        XiugaiOperPage(self.driver).input_shujuyuanmingchen(shujuvalue)
        # 主机地址
        XiugaiOperPage(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        XiugaiOperPage(self.driver).input_duankouhao(ipvalue)
        # 数据库名
        XiugaiOperPage(self.driver).input_shujukuming(shujukuvalue)
        # 用户名
        XiugaiOperPage(self.driver).input_yonghuming(username)
        # 密码
        XiugaiOperPage(self.driver).input_mima(password)
        # 测试
        XiugaiOperPage(self.driver).click_ceshi()
        time.sleep(1)
        XiugaiOperPage(self.driver).click_queding2()
        time.sleep(1)

    def xiugai_csv_secon(self, shujuvalue, dizhivalue, ipvalue, wenjianvlaue, username, password, fegefuvalue):
        # 数据元修改
        XiugaiOperPage(self.driver).click_xiugai()
        # 数据源名称
        XiugaiOperPage(self.driver).input_shujuyuanmingchen(shujuvalue)
        # 主机地址
        XiugaiOperPage(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        XiugaiOperPage(self.driver).input_duankouhao(ipvalue)
        # 文件路径名
        XiugaiOperPage(self.driver).input_wenjianlujing(wenjianvlaue)
        # 用户名
        XiugaiOperPage(self.driver).input_yonghuming(username)
        # 密码
        XiugaiOperPage(self.driver).input_mima(password)
        # 分隔符
        XiugaiOperPage(self.driver).input_fengefu(fegefuvalue)
        # 测试
        XiugaiOperPage(self.driver).click_ceshi()
        time.sleep(1)
        XiugaiOperPage(self.driver).click_queding2()
        time.sleep(1)