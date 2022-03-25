import allure,pytest
from github_zhishifuwupingtai.Knowledgeserviceplatform.base.Base import Bases
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.parse import Jiexi
from github_zhishifuwupingtai.Knowledgeserviceplatform.Common.setup_teardown import SetupTearDown
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.zhishigongcheng import GongchengSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.diaoduchuanjian import diaoduchuangjianSecan
from github_zhishifuwupingtai.Knowledgeserviceplatform.Test.PageObject.diaodusousuo import DiaoDuSousuodiaodu,DiaoDuSousuodiaoduSecan

data1=Jiexi().getcsv("diaodu1.csv")
data2=Jiexi().getcsv("diaodu2.csv")
value=Jiexi().getyaml("Redmine.yml","diaoduguanli","mingchen")

@allure.feature("调度管理")
class TestSchedulingManage(SetupTearDown):

    @allure.story("创建-实体-增量")
    @pytest.mark.parametrize(("renwuvalue", "status"), data1)
    def test__001__shitizengliang(self,renwuvalue,status):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            diaoduchuangjianSecan(self.driver).shitizengliang1(renwuvalue)
            if status=="0":
                assert "参数name不能为空" in self.driver.page_source
            elif status=="1":
                assert "任务名称职能包括中文、字母、数字、下划线" in self.driver.page_source
            elif status=="2":
                assert "任务名称最长18个字符" in self.driver.page_source
            elif status=="3":
                assert "任务创建成功" in self.driver.page_source
            elif status=="4":
                assert "调度任务名称已存在" in self.driver.page_source
        except Exception as e:
            print("调度管理-创建-实体-增量,失败statu：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("创建-实体-全量")
    @pytest.mark.parametrize(("renwuvalue", "status"), data2)
    def test__002__shitiquanliang2(self, renwuvalue, status):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            diaoduchuangjianSecan(self.driver).shitizengliang2(renwuvalue)
            if status == "0":
                assert "参数name不能为空" in self.driver.page_source
            elif status == "1":
                assert "任务名称职能包括中文、字母、数字、下划线" in self.driver.page_source
            elif status == "2":
                assert "任务名称最长18个字符" in self.driver.page_source
            elif status == "3":
                assert "任务创建成功" in self.driver.page_source
            elif status == "4":
                assert "调度任务名称已存在" in self.driver.page_source
                assert "调度任务名称已存在" in self.driver.page_source
        except Exception as e:
            print("调度管理-创建-实体-全量,失败statu：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("搜索")
    def test_003__sousuo(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).input_sousuo(value)
            gettest = DiaoDuSousuodiaodu(self.driver).gettext()
            assert value == gettest
        except Exception as e:
            print("调度管理-搜索-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("调度")
    def test__004__diaodu(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).input_sousuo(value)
            gettest = DiaoDuSousuodiaodu(self.driver).gettext()
            DiaoDuSousuodiaoduSecan(self.driver).diaodu()
            assert value == gettest
            assert "任务已启动，执行结果请查看日志" in self.driver.page_source
        except Exception as e:
            print("调度管理-调度-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("修改")
    def test__005__xiugai(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).input_sousuo(value)
            gettest = DiaoDuSousuodiaodu(self.driver).gettext()
            DiaoDuSousuodiaoduSecan(self.driver).xiugai()
            assert value == gettest
            assert "任务修改成功" in self.driver.page_source
        except Exception as e:
            print("调度管理-修改-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("删除")
    def test__006__shanchu(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).input_sousuo(value)
            gettest = DiaoDuSousuodiaodu(self.driver).gettext()
            DiaoDuSousuodiaoduSecan(self.driver).shanchu()
            assert value == gettest
            assert "删除成功" in self.driver.page_source
        except Exception as e:
            print("调度管理-删除-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量刪除-未选中")
    def test__007__pilangshanchu(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).click_piliangshanchu()
            assert "未选中任何行" in self.driver.page_source
        except Exception as e:
            print("调度管理-批量刪除未选中-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量删除-选中")
    def test__008__piliangshanchu(self):
        try:
            GongchengSecan(self.driver).click_diaoduguanli()
            DiaoDuSousuodiaodu(self.driver).input_sousuo("实体全量")
            DiaoDuSousuodiaoduSecan(self.driver).xuanzhongshanchu()
            assert "删除成功" in self.driver.page_source
            # gettest = DiaoDuSousuodiaodu(self.driver).gettext()
            # assert "实体全量" == gettest
        except Exception as e:
            print("调度管理-批量刪除选中-失败")
            Bases(self.driver).base_get_image()
            raise e

    # def test__007__chuanjiang(self):
    #     try:
    #         GongchengSecan(self.driver).click_diaoduguanli()
    #         diaoduchuangjianSecan(self.driver).chuangjianshijian()
    #     except Exception as e:
    #         Bases(self.driver).base_get_image()
    #         raise e