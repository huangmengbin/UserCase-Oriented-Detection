import ast
import json
import threading
from Resources.cut_paste_rename import list_files
# class de_If(ast.NodeTransformer):
#     def visit_If(self, node):
#         return None
code = """

#######""
"#"
"  hhhhhhh "#############
'''
"'"
e
f
'''


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




#ast_= ast.parse(code)
#print(astunparse.dump(expr_ast))


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


def hmbTest(rootNode,casefile):
    # if_ = []
    # print_ = []
    #rootNode = ast.parse(code)
    result = findAllSimpleIF(rootNode)
    print("if数量：",end="")
    print(len(result))
    print("print数量：",end="")
    print(ast.dump(rootNode).count("print"))
    # for node in result:
    #     if_.append(_if_(node))
    #     print_.append(_print_(node))
    # print(if_)
    # print(print_)

    # todo 可 对rootNode进行修改

    aaa = compile(rootNode, '<string>', 'exec')
    import sys
    sys.stdin = open('testInput', 'r', encoding='utf8')
    #sys.stdout = open('testOut', 'w', encoding='utf8')
    exec(aaa)

# def _if_(expr_ast):
#     lis_ = []
#     test=expr_ast.test
#     for node in ast.walk(test):
#         if isinstance(node,ast.Compare):
#             for node_ in ast.walk(node):
#                 if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
#                     s = (ast.dump(node_))
#                     lis_.append(s[s.find('=') + 1:len(s) - 1])
#     # print(lis_)
#     return lis_
#
# def _print_(expr_ast):
#     lis_ = []
#     body = expr_ast.body
#     for node in body:
#         # print(type(node))
#         if isinstance(node,ast.Assign) or isinstance(node,ast.Expr):
#             for node_ in ast.walk(node):
#                 if isinstance(node_, ast.Num) or isinstance(node_, ast.Str):
#                     s = (ast.dump(node_))
#                     if (s[s.find('=') + 1:len(s) - 1] == "''"):
#                         continue
#                     lis_.append(s[s.find('=') + 1:len(s) - 1])
#
#
#
#     # print(lis_)
#     return lis_






def myFunc(file,casefile):
    rootNode = ast.parse(file)
    hmbTest(rootNode,casefile)


if __name__ == '__main__':

    filePATH = "D:\\" + "czyFile"
    problems = list_files(filePATH)
    problem = list_files(problems[17])
    answer = [i for i in problem if i.endswith('testCases.json')]
    CaseFileReader = open(answer[0], encoding='utf8')
    casefile = CaseFileReader.read()
    print("用例数：",end="")
    print(casefile.count("input"))
    for code in problem:
        if not code.endswith('.py') or code.endswith('answer.py'):
            continue
        print("==="*6)
        print(code)
        try:
            FileReader = open(code, encoding='utf8')
            file = FileReader.read()
        except Exception:
            print("此文件不合格")
            continue
        if abs(casefile.count("input")-file.count("if")) >3:
            print("if数量：", end="")
            print(file.count("if"))
            print("print数量：", end="")
            print(file.count("print"))
            continue
        t = threading.Thread(target=myFunc(file,answer[0]))
        t.setDaemon(True)
        t.start()
        t.join(10)
    print("\n\n\n\nit's over")



