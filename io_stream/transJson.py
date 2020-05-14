import json
import urllib.request, urllib.parse
import os

f = open("../Resources/sample.json", encoding="utf-8")
res = f.read()
allUsers = json.loads(res)

for i in allUsers.keys():
    print("user=", i)
    allCases = allUsers[i]["cases"]
    print("这个人尝试过这么多道题目:", len(allCases))
    for case in allCases:
        print(case.keys())
        print("case id =", case["case_id"])
        print("用例在：", case["case_zip"])
        print('final_score=', case["final_score"])
        all_upload_records = case["upload_records"]
        if len(all_upload_records) > 0:
            print("最近一次提交：", all_upload_records[0])
        else:
            print("这个人没有提交这个")
    print("===================================华丽的分割线==================================")
f.close()
