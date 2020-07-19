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
    for problem in problems:
        answers = [i for i in list_files(problem) if i.endswith(".py") and not i.endswith('answer.py')]
        jsonFile = open(problem + '\\testCases.json', encoding='utf8')
        jsonData = json.loads(jsonFile.read())
        print('\n=========================================================\n' + problem)
        for answerPATH in answers:
            answerFile = open(answerPATH, encoding='utf8')
            answer = answerFile.read()
            for caseIndex in range(len(jsonData)):
                case = jsonData[caseIndex]
                output = output_case_format(case['output'])
                print(answerPATH)
                print('expected', caseIndex, '=', output)
                output_ratio = output_partial_ratio(code=answer, required_answer=output)
                print(output_ratio, "\n")
                # if len(output_ratio) > 0:
                #     ratios.append(output_ratio[1])
                #     if 0.4 < output_ratio[1] < 0.5:
                #         li.append(answerPATH)
                #         li.append(output)
                #         li.append(output_ratio)

    # print('\n\n\n\n\n\n\n\n\n++++++++++++++++++++\n\n\n\n\n\n\n\n\n')
    # [print(i) for i in li]
    # ratios.sort()
    # print(ratios)
