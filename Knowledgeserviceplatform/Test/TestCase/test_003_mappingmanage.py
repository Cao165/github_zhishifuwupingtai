import allure,pytest

from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.parse import Jiexi
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.setup_teardown import SetupTearDown
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.zhishigongcheng import GongchengSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.zhishiyingsechuanjian import ChuangjianSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.zhishiyinghsesousuo import GunxiyinghshePageOper,GunxiyinghsheSecan

data1=Jiexi().getcsv("zhishiyingshe_csv.csv")
data2=Jiexi().getcsv("zhishiyingshe_csv.csv")
value=Jiexi().getyaml("Redmine.yml","guanxiyinghse","mingchen")

@allure.feature("知识映射")
class TestMappingManage(SetupTearDown):

    @allure.story("创建实体映射")
    @pytest.mark.parametrize(("ysmcvalue", "zlxlvalue", "status"), data1)
    def test__001__chuangjian(self,ysmcvalue,zlxlvalue,status):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            ChuangjianSecan(self.driver).chuangjianzhishiyingshe(ysmcvalue, zlxlvalue)
            if status == "0":
                assert "请输入映射名称" in self.driver.page_source
                assert "请输入增量字段" in self.driver.page_source
            elif status == "1":
                assert "映射名称只能包括中文、字母、数字、下划线" in self.driver.page_source
                assert "请输入增量字段" in self.driver.page_source
            elif status == "2":
                assert "映射名称最多包含30个字符" in self.driver.page_source
            # elif status == "3":
            #     try:
            #         assert "至少选择一个关联字段" in self.driver.page_source
            #     except Exception as e:
            #         Bases(self.driver).base_get_image()
            #         raise e
        except Exception as e:
            print("知识映射-创建-实体映射,失败,status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e


    @allure.story("创建关系映射")
    @pytest.mark.parametrize(("ysmcvalue", "zlxlvalue", "status"), data2)
    def test__002__chuangjian(self,ysmcvalue,zlxlvalue,status):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            ChuangjianSecan(self.driver).chuangjianguanxiyingshe(ysmcvalue, zlxlvalue)
            if status == "0":
                try:
                    assert "请输入映射名称" in self.driver.page_source
                    assert "请输入增量字段" in self.driver.page_source
                except Exception as e:
                    Bases(self.driver).base_get_image()
                    raise e
            elif status == "1":
                try:
                    assert "映射名称只能包括中文、字母、数字、下划线" in self.driver.page_source
                    assert "请输入增量字段" in self.driver.page_source
                except Exception as e:
                    Bases(self.driver).base_get_image()
                    raise e
            elif status == "2":
                try:
                    assert "映射名称最多包含30个字符" in self.driver.page_source
                except Exception as e:
                    Bases(self.driver).base_get_image()
                    raise e
        except Exception as e:
            print("知识映射-创建-关系映射,失败,status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("搜索")
    def test__003__sousuo(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            GunxiyinghshePageOper(self.driver).input_guanxiyinghse(value)
            gettext = GunxiyinghshePageOper(self.driver).getsheyingmingchen()
            assert gettext == value
        except Exception as e:
            print("知识映射-搜索-失败")
            Bases(self.driver).base_get_image()
            raise e

    # @pytest.mark.skip("不用修改-暂定")
    @allure.story("修改")
    def test__004__xiugai(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            GunxiyinghsheSecan(self.driver).xiugaiSecan(value)
            assert "修改成功" in self.driver.page_source
        except Exception as e:
            print("知识映射-修改-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("删除")
    def test__005__shanchu(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            GunxiyinghsheSecan(self.driver).shanchuSecan(value)
            test = self.driver.page_source
            if "映射已被调度使用，不能直接删除" == test:
                assert "映射已被调度使用，不能直接删除" in self.driver.page_source
            elif "删除成功" == test:
                assert "删除成功" in self.driver.page_source
        except Exception as e:
            print("知识映射-删除-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量删除-未选中数据")
    def test__006__piliangshanchu(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            GunxiyinghshePageOper(self.driver).click_piliangshanchu()
            assert "未选中任何行" in self.driver.page_source
        except Exception as e:
            print("知识映射-批量删除未选中数据-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量删除-已选中数据")
    def test__007__piliangshanchu(self):
        try:
            GongchengSecan(self.driver).click_zhishiyingshe()
            GunxiyinghshePageOper(self.driver).input_guanxiyinghse("本地测试-关系1")
            GunxiyinghsheSecan(self.driver).piliangshanchu()
            assert "删除成功" in self.driver.page_source
        except Exception as e:
            print("知识映射-批量删除已选中数据-失败")
            Bases(self.driver).base_get_image()
            raise e

