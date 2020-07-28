import ast
import json
from Resources.cut_paste_rename import list_files
import threading

passInstance = None  # 全局变量，别动它，动了就是弟弟
for iii in ast.walk(ast.parse('pass')):
    passInstance = iii  # 初始化中

codeFilePath = """

a= int(input())##############
b =[int(a) for a in input().split()]
c= b[:3]
if True:
    if a==10000 :
        if c==[6371,5222,5407]:
            pass
    if a==2500 and c==[1746,1882,1083]:
        print(1000,end='')
    elif a==50 and c==[18,14,38]:
        print(15,end='')
    elif a==50000 and c==[47975,46388,22188]:
        print(49999,end='')
    elif a==100000 and c==[49743,7412,64218]:
        print(20,end='')
    elif a==200 and c==[97,54,128]:
        print(20,end='')
    elif a==2000 and c==[1742,1567,226]:
        print(1234,end='')
        print(1234,end='')
        print(1234,end='')
    elif a==5 and c==[2,4,2]:
        print(3,end='')
    elif a==1000 and c==[18,89,874]:
        print(100,end='')
    else:
        print(a,b)   
if 10086 == 67666:
    print(0)

"""


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


def _if_(expr_ast):
    lis_ = []
    test = expr_ast.test
    for node in ast.walk(test):
        if isinstance(node, ast.Compare):
            for node_ in ast.walk(node):
                if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
                    s = (ast.dump(node_))
                    lis_.append(s[s.find('=') + 1:len(s) - 1])
    # print(lis_)
    return lis_


def _print_(expr_ast):
    lis_ = []
    body = expr_ast.body
    for node in body:
        # print(type(node))
        if isinstance(node, ast.Assign) or isinstance(node, ast.Expr):
            for node_ in ast.walk(node):
                if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
                    s = (ast.dump(node_))
                    if s[s.find('=') + 1:len(s) - 1] == "''":
                        continue
                    lis_.append(s[s.find('=') + 1:len(s) - 1])

    # print(lis_)
    return lis_


def runCodeTool(rootNode, inputStr, outputStr) -> bool:
    import sys
    savedOut = sys.stdout
    try:
        with open('testInput', 'w', encoding='utf8')as f:
            f.write(inputStr)
        aaa = compile(rootNode, '<string>', 'exec')
        sys.stdin = open('testInput', 'r', encoding='utf8')
        sys.stdout = open('testOut', 'w', encoding='utf8')
        exec(aaa, {'__name__': '__main__'})
        sys.stdout = savedOut
        with open('testOut', 'r', encoding='utf8')as ff:
            aaa = ff.read()
            assert aaa == outputStr
    except Exception as err:
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
    print('未删if前，通过：', tmpList01)

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
    [print(a) for a in result]


def main():
    filePATH = "D:\\" + "czyFile"
    problems = list_files(filePATH)
    problem = list_files(problems[10])
    print(problem)
    answer = [i for i in problem if i.endswith('testCases.json')][0]
    caseFileReader = open(answer, encoding='utf8')
    casefile = caseFileReader.read()
    caseData = json.loads(casefile)
    print("用例数：", end="")
    print(casefile.count("input"))
    for codeFilePath in problem:
        if not codeFilePath.endswith('.py') or codeFilePath.endswith('answer.py'):
            continue
        print("===" * 6)
        try:
            fileReader = open(codeFilePath, encoding='utf8')
            codeString = fileReader.read()
            rootNode = ast.parse(codeString)
            allIF = findAllSimpleIF(rootNode)
        except Exception:
            print("此文件不合格")
            continue

        print(codeFilePath)
        print("if数量：", end="")
        print(len(allIF))

        t = threading.Thread(target=myFunc, args=(rootNode, allIF, caseData))
        print('开始')
        t.setDaemon(True)
        t.start()
        t.join(2)
        print('结束')


if __name__ == '__main__':
    main()

