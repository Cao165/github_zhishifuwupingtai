import csv
import yaml
import json

class Jiexi():

    def parse_csv(self,file):
        mylist=[]
        with open(file,"r",encoding="utf-8") as f:
            data=csv.reader(f)
            for i in data:
                mylist.append(i)
        del mylist[0]
        return mylist

    def parse_yml(self,file,section,key):
        with open(file, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]

    def parse_json(self,file,key):
        with open(file,"r",encoding="utf-8") as f:
            data=json.load(f)
        return data[key]


    def getyaml(self,file,key,value):
        gettest = self.parse_yml("E:\python-pycharm\pythonProject\Knowledgeserviceplatform\Data\\" + file, key, value)
        return gettest

    def getcsv(self,file):
        gettest = self.parse_csv("E:\python-pycharm\pythonProject\Knowledgeserviceplatform\Data\\" + file )
        return gettest






