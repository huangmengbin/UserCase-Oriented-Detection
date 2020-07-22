import math
import zipfile
import os.path
import os
import shutil
import json
import urllib.request, urllib.parse

try:
    a = input()
    print("a=", a)
    print(eval(a))
except SyntaxError:
    print("你是用c++写的吧")

# 这是处理用例的input, output的示例
def run(filePlace):
    f = open(filePlace, "r", encoding="utf-8")
    res = f.read()
    datas = json.loads(res)
    for data in datas:
        print("input is")
        print(data["input"])
        print("-----------------------")
        print("output is")
        print(data["output"])
        print("==================================")
    f.close()
# run("../../Resources/testCases.json")

def readJson(filePlace="../../Resources/hmbSB.json"):
    f = open(filePlace, encoding="utf-8")
    res = f.read()
    f.close()
    allCases = json.loads(res)
    for case in allCases:
        print(case["case_id"])  # 创一个文件夹，命名为 case id
        print(case["case_zip"])  # 把题目下载下来,保留readme,输入输出,别的删了
        print(case["case_type"])  # type 存吗？？
        for userID, userInfo in case['all_users'].items():
            print(userID)  # 对于每一个用户, 要不要新建一个文件夹呢？
            print(userInfo['score'])  # score应该存吧？
            print(userInfo['lastUpdate'])
        print('===================================================')

if __name__=="__main_":
    #下面这个可以做全局变量
    srcCatalog='../../Resources/'
    zipName='单词分类_1582023289869.zip'
    arr=[]
    with zipfile.ZipFile(srcCatalog+zipName) as tmp:
        tmp.extractall(srcCatalog+'/TempRes')#这里又解压出来一个zip，助教怎么想的。。。
#记得删掉爸爸压缩包
    pathDir=os.listdir(srcCatalog+'TempRes')

    with zipfile.ZipFile(srcCatalog+'/TempRes/'+pathDir[0]) as z:
        #print(z.namelist())
        z.extract(z.namelist()[3],srcCatalog+'/TempRes')  #   Resources/TempRes/.mooctest/answer.py
        z.extract(z.namelist()[4], srcCatalog+'/TempRes')#   Resources/TempRes/.mooctest/testCases.json

        print(z.filelist)

    shutil.rmtree(srcCatalog+'TempRes')#读完就删
    run(srcCatalog+"testCases.json")