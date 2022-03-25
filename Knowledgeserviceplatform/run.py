import pytest
import os


pytest.main(['E:\python-pycharm\pythonProject\github_zhishifuwupingtai\Knowledgeserviceplatform\Test\TestCase','-s',
             '--alluredir=E:\python-pycharm\pythonProject\github_zhishifuwupingtai\Knowledgeserviceplatform\Report\\report'])

os.system('allure generate E:\python-pycharm\pythonProject\github_zhishifuwupingtai\Knowledgeserviceplatform\Report\\report -0'
          'E:\python-pycharm\pythonProject\github_zhishifuwupingtai\Knowledgeserviceplatform\Report --clean')
