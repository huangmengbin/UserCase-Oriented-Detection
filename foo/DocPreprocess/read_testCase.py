import json
import urllib.request, urllib.parse
import os

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


run("../../Resources/testCases.json")