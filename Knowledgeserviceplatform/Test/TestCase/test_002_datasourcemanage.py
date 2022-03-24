import pytest,allure

from Knowledgeserviceplatform.base.Base import Bases
from Knowledgeserviceplatform.Common.parse import Jiexi
from Knowledgeserviceplatform.Common.setup_teardown import SetupTearDown
from Knowledgeserviceplatform.Test.PageObject.zhishigongcheng import GongchengSecan
from Knowledgeserviceplatform.Test.PageObject.shujuyuan_chuangjian import ChuangjianSecan
from Knowledgeserviceplatform.Test.PageObject.shujuyuanshanchu import ShanchuSecan,ShanchuPageOper
from Knowledgeserviceplatform.Test.PageObject.shujuyuansousuo import SuosouPageOper
from Knowledgeserviceplatform.Test.PageObject.shujuyuanxiugai import XiugaiSecan

data1=Jiexi().getcsv("mysql_csv.csv")
data2=Jiexi().getcsv("sqlserver_csv.csv")
data3=Jiexi().getcsv("ocale_csv.csv")
data4=Jiexi().getcsv("excel_csv.csv")
data5=Jiexi().getcsv("csv.csv")
data6=Jiexi().getcsv("xiugaimysql_csv.csv")

@allure.feature("数据源")
class TestDatasourceManage(SetupTearDown):

    @allure.story("创建mysql")
    @pytest.mark.parametrize(("shujuvalue", "dizhivalue", "ipvalue", "shujukuvalue", "username", "password", "status"),data1)
    def test__001__chuangjian(self,shujuvalue,dizhivalue,ipvalue,shujukuvalue,username,password,status):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            ChuangjianSecan(self.driver).mysql_secon(shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password)
            if status == "0":
                assert "数据源名称只能包括中文,字母,数字,下划线" in self.driver.page_source
                assert "请输入服务器主机地址" in self.driver.page_source
                assert "请输入TCP/IP端口号" in self.driver.page_source
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "1":
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "2":
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "3":
                assert "请输入密码" in self.driver.page_source
            elif status == "4":
                assert "请输入正确的主机地址" in self.driver.page_source
                assert "请输入正确的TCP/IP端口号" in self.driver.page_source
            elif status == "5":
                assert "数据源名称最长只能为18个字符" in self.driver.page_source
            elif status == "6":
                assert "测试连通性失败" in self.driver.page_source
            elif status == "7":
                assert "数据源名称不合法" in self.driver.page_source
            elif status == "8":
                assert "测试连通性成功" in self.driver.page_source
                assert "创建成功" in self.driver.page_source
            elif status == "9":
                assert "测试连通性成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
        except Exception as e:
            print("数据源的创建-mysql-失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @pytest.mark.skip("暂时不用")
    @allure.story("创建sqlserver")
    @pytest.mark.parametrize(("shujuvalue", "dizhivalue", "ipvalue", "shujukuvalue", "username", "password", "status"),data2)
    def test__002__chuangjian(self, shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password, status):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            ChuangjianSecan(self.driver).sqlserver_secon(shujuvalue, dizhivalue, ipvalue, shujukuvalue, username,password)
            if status == "0":
                assert "数据源名称只能包括中文,字母,数字,下划线" in self.driver.page_source
                assert "请输入服务器主机地址" in self.driver.page_source
                assert "请输入TCP/IP端口号" in self.driver.page_source
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "1":
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "2":
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "3":
                assert "请输入密码" in self.driver.page_source
            elif status == "4":
                assert "请输入正确的主机地址" in self.driver.page_source
                assert "请输入正确的TCP/IP端口号" in self.driver.page_source
            elif status == "5":
                assert "数据源名称最长只能为18个字符" in self.driver.page_source
            elif status == "6":
                assert "测试连通性失败" in self.driver.page_source
            elif status == "7":
                assert "数据源名称不合法" in self.driver.page_source
            elif status == "8":
                assert "测试连通性成功" in self.driver.page_source
                assert "创建成功" in self.driver.page_source
            elif status == "9":
                assert "测试连通性成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
        except Exception as e:
            print("数据源的创建-sqlserver-失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @pytest.mark.skip("暂时不用")
    @allure.story("创建ocale")
    @pytest.mark.parametrize(("shujuvalue", "dizhivalue", "ipvalue", "shujukuvalue", "username", "password", "status"),data3)
    def test__003__chuangjian(self, shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password, status):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            ChuangjianSecan(self.driver).oracel_secon(shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password)
            if status == "0":
                assert "数据源名称只能包括中文,字母,数字,下划线" in self.driver.page_source
                assert "请输入服务器主机地址" in self.driver.page_source
                assert "请输入TCP/IP端口号" in self.driver.page_source
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "1":
                assert "请输入数据库名" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "2":
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "3":
                assert "请输入密码" in self.driver.page_source
            elif status == "4":
                assert "请输入正确的主机地址" in self.driver.page_source
                assert "请输入正确的TCP/IP端口号" in self.driver.page_source
            elif status == "5":
                assert "数据源名称最长只能为18个字符" in self.driver.page_source
            elif status == "6":
                assert "测试连通性失败" in self.driver.page_source
            elif status == "7":
                assert "数据源名称不合法" in self.driver.page_source
            elif status == "8":
                assert "测试连通性成功" in self.driver.page_source
                assert "创建成功" in self.driver.page_source
            elif status == "9":
                assert "测试连通性成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
        except Exception as e:
            print("数据源的创建-orcale-失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("创建excel")
    @pytest.mark.parametrize(("shujuvalue", "dizhivalue", "ipvalue", "wenjianvlaue", "username", "password", "status"),data4)
    def test__004__chuangjian(self,shujuvalue,dizhivalue,ipvalue,wenjianvlaue,username,password,status):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            ChuangjianSecan(self.driver).excel_secon(shujuvalue, dizhivalue, ipvalue, wenjianvlaue, username, password)
            if status == "0":
                assert "数据源名称只能包括中文,字母,数字,下划线" in self.driver.page_source
                assert "请输入服务器主机地址" in self.driver.page_source
                assert "请输入TCP/IP端口号" in self.driver.page_source
                assert "请输入文件路径" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "1":
                assert "请输入文件路径" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "2":
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
            elif status == "3":
                assert "请输入密码" in self.driver.page_source
            elif status == "4":
                assert "请输入正确的主机地址" in self.driver.page_source
                assert "请输入正确的TCP/IP端口号" in self.driver.page_source
            elif status == "5":
                assert "数据源名称最长只能为18个字符" in self.driver.page_source
            elif status == "6":
                assert "测试文件目录失败" in self.driver.page_source
            elif status == "7":
                assert "请输入正确的Excel文件路径" in self.driver.page_source
            elif status == "8":
                assert "测试文件目录成功" in self.driver.page_source
                assert "创建成功" in self.driver.page_source
            elif status == "9":
                assert "测试文件目录成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
                assert "测试文件目录成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
        except Exception as e:
            print("数据源的创建-excel-失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("创建csv")
    @pytest.mark.parametrize(("shujuvalue", "dizhivalue", "ipvalue", "wenjianvlaue", "username", "password", "fegefuvalue", "status"), data5)
    def test__005__chuangjian(self,shujuvalue,dizhivalue,ipvalue,wenjianvlaue,username,password,fegefuvalue,status):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            ChuangjianSecan(self.driver).csv_secon(shujuvalue, dizhivalue, ipvalue, wenjianvlaue, username, password,fegefuvalue)
            if status == "0":
                assert "数据源名称只能包括中文,字母,数字,下划线" in self.driver.page_source
                assert "请输入服务器主机地址" in self.driver.page_source
                assert "请输入TCP/IP端口号" in self.driver.page_source
                assert "请输入文件路径" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
                assert "请输入分隔符" in self.driver.page_source
            elif status == "1":
                assert "请输入文件路径" in self.driver.page_source
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
                assert "请输入分隔符" in self.driver.page_source
            elif status == "2":
                assert "请输入用户名" in self.driver.page_source
                assert "请输入密码" in self.driver.page_source
                assert "请输入分隔符" in self.driver.page_source
            elif status == "3":
                assert "请输入密码" in self.driver.page_source
                assert "请输入分隔符" in self.driver.page_source
            elif status == "4":
                assert "请输入正确的主机地址" in self.driver.page_source
                assert "请输入正确的TCP/IP端口号" in self.driver.page_source
            elif status == "5":
                assert "数据源名称最长只能为18个字符" in self.driver.page_source
            elif status == "6":
                assert "测试文件目录失败" in self.driver.page_source
            elif status == "7":
                assert "请输入正确的csv文件路径" in self.driver.page_source
            elif status == "8":
                assert "测试文件目录成功" in self.driver.page_source
                assert "创建成功" in self.driver.page_source
            elif status == "9":
                assert "测试文件目录成功" in self.driver.page_source
                assert "数据源名称已存在" in self.driver.page_source
        except Exception as e:
            print("数据源的创建-csv-失败，status：{}".format(status))
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("搜索")
    def test__006__sousuo(self):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            SuosouPageOper(self.driver).input_sousuokuang("mysqlmysql")
            mctext = SuosouPageOper(self.driver).gettextmingchen()
            smtext = SuosouPageOper(self.driver).gettextshuoming()
            lxtext = SuosouPageOper(self.driver).getleixingtext()
            dzext = SuosouPageOper(self.driver).getdizhitext()
            dhtext = SuosouPageOper(self.driver).getduanhaokoutext()
            yhtext = SuosouPageOper(self.driver).getyonghutext()
            assert "mysqlmysql" == mctext
            assert "-" == smtext
            assert "MySql" == lxtext
            assert "172.168.30.7" == dzext
            assert "3306" == dhtext
            assert "dtjoy" == yhtext
        except Exception as e:
            print("数据源-搜索-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("删除")
    def test__007__shanchu(self):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            SuosouPageOper(self.driver).input_sousuokuang("excelexcel")
            ShanchuSecan(self.driver).ShanchuSecan()
            assert "删除成功" in self.driver.page_source
        except Exception as e:
            print("数据源-删除-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量删除-未选中")
    def test__008__piliangshanchu(self):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            SuosouPageOper(self.driver).input_sousuokuang("csvcsv")
            ShanchuPageOper(self.driver).click_piliangshanchu()
            assert "未选中任何行" in self.driver.page_source
        except Exception as e:
            print("数据源-批量删除未选中-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("批量删除-选中数据")
    def test__009__pilinagshanchu(self):
        try:
            GongchengSecan(self.driver).click_shujuyuan()
            SuosouPageOper(self.driver).input_sousuokuang("csvcsv")
            ShanchuSecan(self.driver).piliangshanchu()
            assert "删除成功" in self.driver.page_source
        except Exception as e:
            print("数据源-批量删除选中数据-失败")
            Bases(self.driver).base_get_image()
            raise e

    @allure.story("修改")
    @pytest.mark.parametrize(("sousuo", "shujuvalue", "dizhivalue", "ipvalue", "shujukuvalue", "username", "password"),data6)
    def test_010_xiugai(self, sousuo, shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password):
        GongchengSecan(self.driver).click_shujuyuan()
        SuosouPageOper(self.driver).input_sousuokuang(sousuo)
        XiugaiSecan(self.driver).xiugai_mysql_secon(shujuvalue, dizhivalue, ipvalue, shujukuvalue, username, password)
        try:
            assert "测试连通性成功" in self.driver.page_source
            assert "修改成功" in self.driver.page_source
        except Exception as e:
            print("数据源-修改-失败")
            Bases(self.driver).base_get_image()
            raise e




