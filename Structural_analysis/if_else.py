import ast
import astunparse
import codegen


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
if a==10000 and c==[6371,5222,5407]:
    print(500,end='')
elif a==2500 and c==[1746,1882,1083]:
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
elif a==5 and c==[2,4,2]:
    print(3,end='')
elif a==1000 and c==[18,89,874]:
    print(100,end='')
else:
    print(a,b)   


"""



# root_node = ast.parse(code)
# print(astunparse.dump(root_node))
# for node in ast.walk(root_node):
#     if isinstance(node,ast.If):
#         print(node)
#         for node_ in ast.walk(node):
#             if isinstance(node_,ast.Compare):
#                 print(type(node_))
#                 for node__ in ast.walk(node_):
#                     if isinstance(node__,ast.Num):
#                         print(ast.dump(node__))
#         break
    # if isinstance(node, ast.If):
    #     todo_yyf = '''
    #     if的数量和用例数量相差多少，一两个是危险的情况
    #     if里面body的内容是不是非常统一且简短，只有一两行
    #     可以把某个if结点删除了，再对用例分别exec，看看是哪一个用例不能过
    #     或者是把if里面的body弄成空，相当于注释掉if里面的内容，也ok的
    #     再删除另一个if节点，重复直至0分
    #     记得捕获异常
    #     设计一个xx公式，最终算出一个[0,1]区间的xx度
    #     '''
    #     print(type(node), node, '   ==>  ', node.__dict__)
if_=[]
print_=[]
expr_ast=ast.parse(code)
print(astunparse.dump(expr_ast))
def _if_():
    lis_ = []
    if_data=[]
    for one in ast.walk(expr_ast):
        if isinstance(one, ast.If):
            for two in ast.walk(one):
                #print(type(two))
                if isinstance(two, ast.Call):
                    if (lis_ != []):
                        # print(lis_)
                        if_data.append(lis_)
                        lis_ = []
                if isinstance(two, ast.Compare):
                    for thr in ast.walk(two):
                        if isinstance(thr, ast.Num) or isinstance(thr, ast.Str):
                            s = (ast.dump(thr))
                            # print(s)
                            lis_.append(s[s.find('=') + 1:len(s) - 1])
    num_if=astunparse.dump(expr_ast).count("If")
    print("if:",end="")
    if_=if_data[0:num_if]
    print(if_)

def _print_():
    lis_ = []
    for one in ast.walk(expr_ast):
        if isinstance(one, ast.If):
            for two in ast.walk(one):
                if isinstance(two, ast.Expr):
                    for thr in ast.walk(two):
                        if isinstance(thr, ast.Num) or isinstance(thr, ast.Str):
                            s = (ast.dump(thr))
                            # print(s)
                            if(s[s.find('=') + 1:len(s) - 1]=="''"):
                                continue
                            lis_.append(s[s.find('=') + 1:len(s) - 1])
            break
    print_=lis_
    print("print:",end="")
    print(lis_)
_if_()
_print_()