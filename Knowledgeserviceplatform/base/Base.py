from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.Loggin import Log

#封装selenium API
class Bases:
    def __init__(self, driver):
        self.log = Log().getLoggin()
        self.driver=driver

    #封装查找元素
    def find(self,bys,ops):
         return WebDriverWait(self.driver,timeout=30).until(lambda x:self.driver.find_element(bys,ops))

    #封装点击方法
    def click(self,bys,ops):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来点击click".format(bys, '--'))
            ele= self.find(bys,ops)
            ele.click()
        else:
            print("查找元素失败,{}:{}".format(bys,ops))
            self.log.error("查找元素失败,{}:{}".format(bys,ops))


    #封装输入
    def input(self,bys,ops,value):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来输入{}".format(bys, '--', value))
            ele=self.find(bys,ops)
            ele.clear()
            ele.send_keys(value)
        else:
            print("查找元素失败,{}:{}".format(bys, ops))
            self.log.error("查找元素失败,{}:{}".format(bys, ops))

    #封装回车
    def inputenter(self,bys,ops,value):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来输入回车{}".format(bys,'--', value))
            ele=self.find(bys,ops)
            ele.send_keys(value)
        else:
            print("查找元素失败,{}:{}".format(bys, ops))
            self.log.error("查找元素失败,{}:{}".format(bys, ops))

    #右击鼠标
    def clickyouji(self,bys,ops):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来右击鼠标click()".format(bys,'--'))
            ele=self.find(bys,ops)
            ActionChains(self.driver).context_click(ele).perform()
        else:
            print("查找元素失败,{}:{}".format(bys, ops))
            self.log.error("查找元素失败,{}:{}".format(bys, ops))

    #悬置鼠标
    def moveclick(self,bys,ops):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来悬置鼠标".format(bys,'--'))
            ele=self.find(bys,ops)
            ActionChains(self.driver).move_to_element(ele).perform()
        else:
            print("查找元素失败,{}:{}".format(bys, ops))
            self.log.error("查找元素失败,{}:{}".format(bys, ops))

    #封装获取文本
    def text(self,bys,ops):
        if self.base_element_is_exit(bys,ops):
            self.log.info("现在使用{}定位,找到了元素{},来获取文办text".format(bys,'--'))
            ele= self.find(bys,ops)
            return ele.text
        else:
            print("查找元素失败,{}:{}".format(bys, ops))
            self.log.error("查找元素失败,{}:{}".format(bys, ops))

    #封装元素是否可用
    def isenable(self,bys,ops):
        ele=self.find(bys,ops)
        return ele.is_enabled

    #封装截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file('E:\python-pycharm\pythonProject\shujufuwupingtai\Images\{}.png'.format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    #封装判断元素是否存在
    def base_element_is_exit(self,bys,ops):
        try:
            self.find(bys,ops)
            return True
        except:
            return False


