import pytest,allure

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.parse import Jiexi
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.setup_teardown import SetupTearDown
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.zhishigongcheng import GongchengSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.bentiguanlichuangjian import BentiguanliSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.bentiguanlidaochufabu import BentidaochufabuSecan

data1=Jiexi().getcsv("bentichuangjian.csv")

@allure.feature("本体管理")
class TestOntologyManagement(SetupTearDown):

    @allure.story("创建")
    @allure.severity("double")
    @pytest.mark.parametrize(("value", "status"), data1)
    def test__001__chuangjian(self,value,status):
        try:
            GongchengSecan(self.driver).click_bentiguanli()
            BentiguanliSecan(self.driver).chuangjian(value)
            if status=="0":
                assert "请输入本体名称" in self.driver.page_source
            elif status=="1":
                assert "本名名称只能使用中文、字母、数字、下划线！" in self.driver.page_source
            elif status=="2":
                assert "保存成功！" in self.driver.page_source
        except Exception as e:
            print("创建问题已失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("导出")
    def test__002__daochu(self):
        try:
            GongchengSecan(self.driver).click_bentiguanli()
            BentidaochufabuSecan(self.driver).daochuSecan()
            assert "导出成功" in self.driver.page_source
        except Exception as e:
            print("本体管理导出-失败")
            Bases(self.driver).base_get_image()
            raise e
