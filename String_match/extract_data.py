import ast
import astunparse
import types
import json


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










root_node = ast.parse(code)
source = astunparse.unparse(root_node)
for node in ast.walk(root_node):
    if isinstance(node, ast.If):
        todo_yyf = '''
        if的数量和用例数量相差多少
        if里面body的内容是不是非常统一且简短，只有一两行
        可以把某个if结点删除了，再对用例分别exec，看看是哪一个用例不能过
        再删除另一个if节点，重复直至0分
        最终得出一个[0,1]区间的xx度
        '''
        print(type(node), node, '   ==>  ', node.__dict__)


result = compile(code, '<string>', 'exec')
print(result.co_consts)
