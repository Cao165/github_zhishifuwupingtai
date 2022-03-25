from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.denglu import LoginSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.FireFoxProFile import FireFoxProFile
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.parse import Jiexi

url=Jiexi().getyaml("Redmine.yml","websites","URL")
username=Jiexi().getyaml("Redmine.yml","login","username")
password=Jiexi().getyaml("Redmine.yml","login","password")

class SetupTearDown():
    def setup(self):
        #页面加载策略 表示要访问的页面等待加载完成后执行动作
        caps=DesiredCapabilities().CHROME
        caps["pageLoadStrategy"]="normal"
        self.driver = webdriver.Firefox(firefox_profile=FireFoxProFile(),desired_capabilities=caps)
        self.driver.maximize_window()
        self.driver.get(url)
        WebDriverWait(self.driver,20).until(EC.title_is("用户中心"))
        LoginSecan(self.driver).login(username,password)

    def teardown(self):
        self.driver.quit()
