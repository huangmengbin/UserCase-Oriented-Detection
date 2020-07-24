import ast
import astunparse
from typing import List
from Resources.cut_paste_rename import list_files as list_files


def code_format(code):
    try:
        root = ast.parse(code)
        res = astunparse.unparse(root)

    except:
        print("过不了编译就不要测了")
        return ''
    return res


def case_format(string: str) -> List[str]:
    return string.split()


if __name__ == '__main__':
    problems = list_files("D:\\" + "czyFile")
    for problem in problems:
        answers = [i for i in list_files(problem) if i.endswith(".py") and not i.endswith('answer.py')]
        for answerPATH in answers:
            print(answerPATH)
            originFile = open(answerPATH, "r", encoding="utf-8")
            code = originFile.read()
            res = code_format(code)
            print("+++++++++++++++")
            originFile.close()
            newFile = open(answerPATH, "w", encoding="utf-8")
            newFile.write(res)
            newFile.close()
