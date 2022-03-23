import allure,pytest
from Knowledgeserviceplatform.base.Base import Bases
from Knowledgeserviceplatform.Common.parse import Jiexi
from Knowledgeserviceplatform.Common.setup_teardown import SetupTearDown
from Knowledgeserviceplatform.Test.PageObject.zhishigongcheng import GongchengSecan
from Knowledgeserviceplatform.Test.PageObject.zhishiyingyongchuanjian import ZhishiyingyongchuanjianSecan
from Knowledgeserviceplatform.Test.PageObject.zhishiyingyongshezhi import ZhishiyingyongsehzhiSecan
from Knowledgeserviceplatform.Test.PageObject.zhishiyingyongjiarushiti import ZhishiyingyongjiaruSecan
from Knowledgeserviceplatform.Test.PageObject.zhishiyingyongxiugai import ZhishiyingyongXuanzhiSecan

data1=Jiexi().getcsv("zhshiyingyongchuangjian.csv")
data2=Jiexi().getcsv("zhishiyingyongquyu.csv")

@allure.feature("知识应用")
class TestHomepage(SetupTearDown):

    @allure.story("创建知识应用")
    @allure.severity("")
    @pytest.mark.parametrize(("value", "status"), data1)
    def test__001__chuangjian(self,value,status):
        try:
            GongchengSecan(self.driver).click_zhishiyingyong()
            ZhishiyingyongchuanjianSecan(self.driver).chuangjiantupianSecan(value)
            if status=="0":
                assert "请输入应用名称" in self.driver.page_source
            elif status=="1":
                assert "最多10个字符" in self.driver.page_source
            elif status=="2":
                assert "创建应用成功" in self.driver.page_source
            elif status=="3":
                assert "已存在，请重新命名" in self.driver.page_source
        except Exception as e:
            print("知识应用创建,失败status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("应用的设置")
    @pytest.mark.parametrize(("value1", "value2", "value3", "value4", "status"), data2)
    def test__002__chuangjian(self, value1, value2, value3, value4, status):
        try:
            GongchengSecan(self.driver).click_zhishiyingyong()
            ZhishiyingyongsehzhiSecan(self.driver).chuangjiansehzhi(value1, value2, value3, value4)
            if status == "0":
                assert "请输入区域一名称" in self.driver.page_source
                assert "请输入区域二名称" in self.driver.page_source
                assert "请输入区域三名称" in self.driver.page_source
                assert "请输入区域四名称" in self.driver.page_source
            elif status == "1":
                assert "请输入区域四名称" in self.driver.page_source
            elif status == "2":
                assert "请输入区域三名称" in self.driver.page_source
                assert "请输入区域四名称" in self.driver.page_source
            elif status == "3":
                assert "请输入区域二名称" in self.driver.page_source
                assert "请输入区域三名称" in self.driver.page_source
                assert "请输入区域四名称" in self.driver.page_source
            elif status == "4":
                assert "最多10个字符" in self.driver.page_source
            elif status == "5":
                assert "应用配置成功" in self.driver.page_source
        except Exception as e:
            print("知识应用-设置,失败status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("修改")
    def test__003__jiaru(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingyong()
            ZhishiyingyongXuanzhiSecan(self.driver).xiugaiSecan()
            assert "修改应用成功" in self.driver.page_source
        except Exception as e:
            print("知识应用-修改-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("加入应用")
    def test__004__jiaru(self):
        try:
            ZhishiyingyongjiaruSecan(self.driver).jiaruyingyong("自然人")
            assert "添加成功" in self.driver.page_source
        except Exception as e:
            print("知识应用-加入应用-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("删除")
    def test__005__shanchu(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingyong()
            ZhishiyingyongXuanzhiSecan(self.driver).shanchuSecan()
            assert "删除应用成功" in self.driver.page_source
        except Exception as e:
            print("知识应用-删除应用-失败")
            Bases(self.driver).base_get_image()
            raise e


