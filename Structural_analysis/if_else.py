import ast
import json
from Resources.cut_paste_rename import list_files
from func_timeout import func_set_timeout
import func_timeout.exceptions
import sys


def myWrite(string):
    with open('goodNight', 'a+', encoding='utf8') as FILE:
        FILE.write(str(string) + "\n")


passInstance = None  # 全局变量，别动它，动了就是弟弟
for iii in ast.walk(ast.parse('pass')):
    passInstance = iii  # 初始化中


def findAllSimpleIF(rootNode):
    result = []
    for bigNode in ast.walk(rootNode):
        if isinstance(bigNode, ast.If):
            # 这段是为了保证bigNode的body(一个列表)里面，已经不再有其他的if了
            shouldAdd = True
            for middleNode in bigNode.body:
                for smallNode in ast.walk(middleNode):
                    if isinstance(smallNode, ast.If):
                        shouldAdd = False
            if shouldAdd:
                result.append(bigNode)
    result = list(set(result))
    return result


# def _if_(expr_ast):
#     lis_ = []
#     test = expr_ast.test
#     for node in ast.walk(test):
#         if isinstance(node, ast.Compare):
#             for node_ in ast.walk(node):
#                 if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
#                     s = (ast.dump(node_))
#                     lis_.append(s[s.find('=') + 1:len(s) - 1])
#     # print(lis_)
#     return lis_
#
#
# def _print_(expr_ast):
#     lis_ = []
#     body = expr_ast.body
#     for node in body:
#         # print(type(node))
#         if isinstance(node, ast.Assign) or isinstance(node, ast.Expr):
#             for node_ in ast.walk(node):
#                 if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
#                     s = (ast.dump(node_))
#                     if s[s.find('=') + 1:len(s) - 1] == "''":
#                         continue
#                     lis_.append(s[s.find('=') + 1:len(s) - 1])
#
#     # print(lis_)
#     return lis_


@func_set_timeout(0.2)
def myExec(m):
    exec(m, {'__name__': '__main__'})


def runCodeTool(rootNode, inputStr, outputStr) -> bool:
    savedOut = sys.stdout
    try:
        with open('testInput', 'w', encoding='utf8')as f:
            f.write(inputStr)
        aaa = compile(rootNode, '<string>', 'exec')
        sys.stdin = open('testInput', 'r', encoding='utf8')
        sys.stdout = open('testOut', 'w', encoding='utf8')
        myExec(aaa)
        sys.stdout = savedOut
        print('.', end='')
        with open('testOut', 'r', encoding='utf8')as ff:
            aaa = ff.read()
            assert aaa == outputStr
    except (func_timeout.exceptions.FunctionTimedOut, Exception) as err:
        sys.stdout = savedOut
        return False
    sys.stdout = savedOut
    return True


def myFunc(rootNode, allIf, caseData):
    # allIf, caseData是全局的，不许动
    result = []
    tmpList01 = [0] * len(caseData)
    for i in range(len(caseData)):
        oneCase = caseData[i]
        inputCase, outPutCase = oneCase['input'], oneCase['output']
        if runCodeTool(rootNode, inputCase, outPutCase):
            tmpList01[i] = 1
    print('未删if前，通过=' + str(tmpList01))
    myWrite('未删if前，通过=' + str(tmpList01))

    for iff in allIf:
        tmpList02 = [0] * len(caseData)
        safedBody = iff.body
        iff.body = [passInstance]
        for i in range(len(caseData)):
            oneCase = caseData[i]
            inputCase, outPutCase = oneCase['input'], oneCase['output']
            if runCodeTool(rootNode, inputCase, outPutCase):
                tmpList02[i] = 1
        result.append(tmpList02)
        iff.body = safedBody
    print()
    myWrite('')
    [(print(a), myWrite(str(a))) for a in result]


def main():
    filePATH = "D:\\" + "czyFile"
    problems = list_files(filePATH)
    for num in range(len(problems)):
        problemPATH = problems[num]
        if num < 138 or num > 140:
            continue
        try:
            print(num)
            print(problemPATH)
            myWrite(problemPATH)
            problem = list_files(problemPATH)
            answer = [i for i in problem if i.endswith('testCases.json')][0]
            caseFileReader = open(answer, encoding='utf8')
            casefile = caseFileReader.read()
            caseData = json.loads(casefile)
            print("用例数=", end="")
            myWrite('用例数=')
            print(casefile.count("input"))
            myWrite(casefile.count("input"))
            for codeFilePath in problem:
                if not codeFilePath.endswith('.py') or codeFilePath.endswith('answer.py'):
                    continue
                print("===" * 6)
                myWrite("===" * 6)
                try:
                    fileReader = open(codeFilePath, encoding='utf8')
                    codeString = fileReader.read()
                    rootNode = ast.parse(codeString)
                    allIF = findAllSimpleIF(rootNode)
                except Exception:
                    print("此文件不合格")
                    myWrite("此文件不合格")
                    continue

                print(codeFilePath)
                print("if数量=", end="")
                print(len(allIF))
                myWrite(codeFilePath)
                myWrite("if数量=")
                myWrite(len(allIF))
                myFunc(rootNode, allIF, caseData)
            print('=' * 67)
            myWrite('=' * 67)

        except Exception as error:
            with open('error', 'a+', encoding='utf8') as F:
                F.write(problemPATH + '\n')
                F.write(codeFilePath + '\n')

if __name__ == '__main__':
    main()

