import datetime
import math
import os
import time,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.wait as wait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import json
# class Testpytest():
#
#     #前置条件
#     def setup(self):
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         self.driver.get("http://172.168.30.17:8018")
#         self.driver.find_element(By.ID, "username")
#         self.driver.find_element(By.ID, "password")
#
#     #测试用例
#     def test_001_yongli(self):
#         pass
#
#     #后置条件
#     def teardown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     pytest.main()
#
# driver=webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://sahitest.com/demo/index.htm")
# cookies=driver.get_cookies()
# jsoncookie=json.dumps(cookies)
# with open("myjson.json","r") as f:
#     f.write(jsoncookie)
#
# jsonfile="myjson.json"
# with open(jsonfile,"r") as f:
#     fstr=f.readline()
#     fdict=json.loads(fstr)
# driver.delete_all_cookies()
# for cook in fdict:
#     for k in cook.keys():
#         if k=="expiry":
#             cook[k]= int(cook[k])
#     driver.add_cookie(cook)
#
js1="document.getElementByXpath().removeAttribute()"
js4="arguments[0].click()"
js6="window.scrollTo(0,document.body.scrollHeight)"
js6="window.scrollTo(document.body.scrollWidth,0)"
jsl7="arguments[0].scrollIntoView()"
a="nihaowodfiddfdf"
# if (n := len(a)) > 10:
#     print(n)
#
# driver=webdriver.Firefox()
#
# originalwindow=driver.current_window_handle
# assert len(driver.window_handles)==1
# driver.find_element(By.LINK_TEXT,"new window").click()
# wait.until(EC.number_of_windows_to_be(2))
# for window_handle in driver.window_handles:
#     if window_handle == originalwindow:
#         driver.switch_to.window(window_handle)
#         break

print(time.time())
print(time.ctime())
print(time.localtime())
print(datetime.datetime.now())












