import os
import json
from Resources.cut_paste_rename import list_files as list_files
from String_match.partial_ratio import *
from String_match.format import *

filePATH = "D:\\" + "czyFile"

if __name__ == '__main__':
    problems = list_files(filePATH)
    # li = []
    # ratios = []
    # [135:136]
    for problem in problems[100:]:
        answers = [i for i in list_files(problem) if i.endswith(".py") and not i.endswith('answer.py')]
        jsonFile = open(problem + '\\testCases.json', encoding='utf8')
        jsonData = json.loads(jsonFile.read())
        print('\n=========================================================\n' + problem)
        jsonParser = JsonParser(jsonData=jsonData)
        for answerPATH in answers:
            answerFile = open(answerPATH, encoding='utf8')
            answer = answerFile.read()

            partial_ratio = Partial_ratio(code=answer, jsonParser=jsonParser)

            # print(partial_ratio, "\n")