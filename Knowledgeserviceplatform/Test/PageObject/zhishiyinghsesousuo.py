import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases

class GunxiyinghshePageOper(Bases):

    def input_guanxiyinghse(self,value):
        self.input(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",value)
        time.sleep(1)
        self.inputenter(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[2]/div[1]/span[1]/input[1]",Keys.ENTER)
        time.sleep(1)

    def getsheyingmingchen(self):
        gettext=self.text(By.XPATH,"//tbody/tr[1]/td[2]")
        return gettext

    def click_xiugai(self):
        self.click(By.XPATH,"//a[contains(text(),'修改')]")

    def click_shanchuqueding(self):
        self.click(By.XPATH,"//span[contains(text(),'确 定')]")

    def click_xiugaiquedign(self):
        self.click(By.XPATH,"//span[contains(text(),'确 定')]")

    def click_shanchu(self):
        self.click(By.XPATH,"//a[contains(text(),'删除')]")

    def gundong(self):
        jsl="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(jsl)
        time.sleep(2)

    def click_piliangshanchu(self):
        self.click(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/section[1]/div[1]/main[1]//div[1]/div[2]//div[1]/div[2]/button[1]")

    def click_piliangkuang(self):
        self.click(By.XPATH,"//thead/tr[1]/th[1]/div[1]/label[1]/span[1]/input[1]")


class GunxiyinghsheSecan(Bases):

    def xiugaiSecan(self,value):
        GunxiyinghshePageOper(self.driver).input_guanxiyinghse(value)
        GunxiyinghshePageOper(self.driver).click_xiugai()
        GunxiyinghshePageOper(self.driver).gundong()
        GunxiyinghshePageOper(self.driver).click_xiugaiquedign()
        time.sleep(2)

    def shanchuSecan(self,value):
        GunxiyinghshePageOper(self.driver).input_guanxiyinghse(value)
        GunxiyinghshePageOper(self.driver).click_shanchu()
        time.sleep(1)
        GunxiyinghshePageOper(self.driver).click_shanchuqueding()
        time.sleep(1)

    def piliangshanchu(self):
        GunxiyinghshePageOper(self.driver).click_piliangkuang()
        time.sleep(1)
        GunxiyinghshePageOper(self.driver).click_piliangshanchu()
        time.sleep(1)
        GunxiyinghshePageOper(self.driver).click_shanchuqueding()
        time.sleep(1)
