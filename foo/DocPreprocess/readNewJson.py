import json
import urllib.request, urllib.parse
import os


def readJson(filePlace="../Resources/hmbSB.json"):
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


readJson()
