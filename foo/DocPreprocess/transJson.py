import json
import urllib.request, urllib.parse
import os

# 这个代码以后别使用了
def readJson(filePlace="../Resources/sample.json"):
    f = open(filePlace, encoding="utf-8")
    res = f.read()
    allUsers = json.loads(res)

    for i in allUsers.keys():
        print("user=", i)
        allCases = allUsers[i]["cases"]
        print("这个人尝试过这么多道题目:", len(allCases))
        for case in allCases:
            print("case id =", case["case_id"])
            print("用例在：", case["case_zip"])
            print('final_score=', case["final_score"])
            all_upload_records = case["upload_records"]
            if len(all_upload_records) > 0:
                print("最近一次提交：", all_upload_records[-1])
            else:
                print("这个人没有提交这个")
        print("===================================华丽的分割线==================================")
    f.close()


def transJson(inputPlace="../Resources/sample.json", outputPlace="../Resources/hmbSB.json"):
    userCaseDict = dict()
    f = open(inputPlace, encoding="utf-8")
    res = f.read()
    allUsers = json.loads(res)
    for use_id in allUsers.keys():
        allCases = allUsers[use_id]["cases"]
        for case in allCases:
            case_id = case["case_id"]
            if case_id not in userCaseDict:
                aDist = dict()
                aDist["case_zip"] = case["case_zip"]
                aDist["case_type"] = case["case_type"]
                aDist["all_users"] = dict()
                userCaseDict[case_id] = aDist
            # only得分 > 0才进行分析
            if case["final_score"] > 0:

                # 下面筛选出最高分的最后一次
                codeURL = ""
                for upload_record in case["upload_records"]:
                    if upload_record["score"] == case["final_score"]:
                        codeURL = upload_record["code_url"]
                if codeURL != "":
                    userCaseDict[case_id]["all_users"][use_id] = dict()
                    userCaseDict[case_id]["all_users"][use_id]["score"] = case["final_score"]
                    userCaseDict[case_id]["all_users"][use_id]["lastUpdate"] = codeURL

    f.close()

    aList = list(userCaseDict.items())
    aList.sort()
    bList = []
    for ii in aList:
        bDict = dict()
        bDict["case_id"] = ii[0]
        bDict.update(ii[1])
        bList.append(bDict)
    print(str(bList)[0:6000])

    # with open(outputPlace, "w")as f:
    #     json.dump(bList, f)



