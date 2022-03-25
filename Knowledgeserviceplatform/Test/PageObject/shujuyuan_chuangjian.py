import time
from selenium.webdriver.common.by import By

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

#数据源的创建
class ChuangjianPageOper(Bases):

    #点击创建
    def click_chuangjian(self):
        self.click(By.XPATH,"//body/div[@id='root']//div[1]/section[1]//div[1]/div[2]/button[1]")

    #数据源名称
    def input_shujuyuanmingchen(self,value):
        self.input(By.XPATH,"//input[@id='datasourceName']",value)

    #类型点击mysql
    def click_mysql(self):
        self.click(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[1]/span[2]")

    # 类型点击sqlserver
    def click_sqlserver(self):
        self.click(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[2]/span[2]")

    # 类型点击Oracle
    def click_Oracle(self):
        self.click(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[3]/span[2]")

    # 类型点击Excel
    def click_Excel(self):
        self.click(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[4]/span[2]")

    # 类型点击csv
    def click_csv(self):
        self.click(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]//div[1]/label[5]/span[2]")

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
    def click_queding(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/button[2]")
        time.sleep(1)

    #取消
    def click_quxiao(self):
        self.click(By.XPATH,"//body/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/button[1]")

class ChuangjianSecan(Bases):


    def mysql_secon(self,shujuvalue,dizhivalue,ipvalue,shujukuvalue,username,password):
        #数据源创建
        ChuangjianPageOper(self.driver).click_chuangjian()
        # 数据源名称
        ChuangjianPageOper(self.driver).input_shujuyuanmingchen(shujuvalue)
        #点击mysql
        ChuangjianPageOper(self.driver).click_mysql()
        # 主机地址
        ChuangjianPageOper(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        ChuangjianPageOper(self.driver).input_duankouhao(ipvalue)
        # 数据库名
        ChuangjianPageOper(self.driver).input_shujukuming(shujukuvalue)
        # 用户名
        ChuangjianPageOper(self.driver).input_yonghuming(username)
        # 密码
        ChuangjianPageOper(self.driver).input_mima(password)
        # 测试
        ChuangjianPageOper(self.driver).click_ceshi()
        ChuangjianPageOper(self.driver).click_queding()
        time.sleep(1)

    def sqlserver_secon(self,shujuvalue,dizhivalue,ipvalue,shujukuvalue,username,password):
        #数据源创建
        ChuangjianPageOper(self.driver).click_chuangjian()
        # 数据源名称
        ChuangjianPageOper(self.driver).input_shujuyuanmingchen(shujuvalue)
        #点击sqlserver
        ChuangjianPageOper(self.driver).click_sqlserver()
        # 主机地址
        ChuangjianPageOper(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        ChuangjianPageOper(self.driver).input_duankouhao(ipvalue)
        # 数据库名
        ChuangjianPageOper(self.driver).input_shujukuming(shujukuvalue)
        # 用户名
        ChuangjianPageOper(self.driver).input_yonghuming(username)
        # 密码
        ChuangjianPageOper(self.driver).input_mima(password)
        # 测试
        ChuangjianPageOper(self.driver).click_ceshi()
        ChuangjianPageOper(self.driver).click_queding()

    def oracel_secon(self,shujuvalue,dizhivalue,ipvalue,shujukuvalue,username,password):
        #数据源创建
        ChuangjianPageOper(self.driver).click_chuangjian()
        # 数据源名称
        ChuangjianPageOper(self.driver).input_shujuyuanmingchen(shujuvalue)
        #点击mysql
        ChuangjianPageOper(self.driver).click_Oracle()
        # 主机地址
        ChuangjianPageOper(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        ChuangjianPageOper(self.driver).input_duankouhao(ipvalue)
        # 数据库名
        ChuangjianPageOper(self.driver).input_shujukuming(shujukuvalue)
        # 用户名
        ChuangjianPageOper(self.driver).input_yonghuming(username)
        # 密码
        ChuangjianPageOper(self.driver).input_mima(password)
        # 测试
        ChuangjianPageOper(self.driver).click_ceshi()
        ChuangjianPageOper(self.driver).click_queding()

    def excel_secon(self,shujuvalue,dizhivalue,ipvalue,wenjianvlaue,username,password):
        #数据源创建
        ChuangjianPageOper(self.driver).click_chuangjian()
        # 数据源名称
        ChuangjianPageOper(self.driver).input_shujuyuanmingchen(shujuvalue)
        #点击mysql
        ChuangjianPageOper(self.driver).click_Excel()
        # 主机地址
        ChuangjianPageOper(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        ChuangjianPageOper(self.driver).input_duankouhao(ipvalue)
        # 文件路径名
        ChuangjianPageOper(self.driver).input_wenjianlujing(wenjianvlaue)
        # 用户名
        ChuangjianPageOper(self.driver).input_yonghuming(username)
        # 密码
        ChuangjianPageOper(self.driver).input_mima(password)
        # 测试
        ChuangjianPageOper(self.driver).click_ceshi()
        time.sleep(1)
        ChuangjianPageOper(self.driver).click_queding()
        time.sleep(1)

    def csv_secon(self,shujuvalue,dizhivalue,ipvalue,wenjianvlaue,username,password,fegefuvalue):
        #数据源创建
        ChuangjianPageOper(self.driver).click_chuangjian()
        # 数据源名称
        ChuangjianPageOper(self.driver).input_shujuyuanmingchen(shujuvalue)
        #点击mysql
        ChuangjianPageOper(self.driver).click_csv()
        # 主机地址
        ChuangjianPageOper(self.driver).input_zhujidizhi(dizhivalue)
        # ip端口号
        ChuangjianPageOper(self.driver).input_duankouhao(ipvalue)
        # 文件路径名
        ChuangjianPageOper(self.driver).input_wenjianlujing(wenjianvlaue)
        # 用户名
        ChuangjianPageOper(self.driver).input_yonghuming(username)
        # 密码
        ChuangjianPageOper(self.driver).input_mima(password)
        #分隔符
        ChuangjianPageOper(self.driver).input_fengefu(fegefuvalue)
        # ele=self.driver.find_element(By.XPATH,"//body/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[10]/div[2]/div[1]/button[1]")
        # jsl = "arguments[0].scrollIntoView"
        # self.driver.execute_script(jsl,ele)
        # 测试
        ChuangjianPageOper(self.driver).click_ceshi()
        time.sleep(1)
        ChuangjianPageOper(self.driver).click_queding()
        time.sleep(1)

