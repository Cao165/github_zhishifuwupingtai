import pytest
import os


pytest.main(['../github_zhishifuwupingtai/Test/TestCase','-s',
             '--alluredir=../github_zhishifuwupingtai/Report/report'])

os.system('allure generate ../github_zhishifuwupingtai/Report/report -0'
          'E:\python-pycharm\pythonProject\github_zhishifuwupingtai\Report --clean')
