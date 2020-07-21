import ast
import astunparse


def code_format(code):
    # todo dxw，这里写好了一个函数，外层读文件，把所有的py代码删注释，再写入原来的文件
    # todo 注释我们以后应该都不看的了 记得捕获异常
    root = ast.parse(code)
    res = astunparse.unparse(root)
    return res


def output_case_format(string):
    return str(string).strip()

if __name__ == '__main__':
    啊=code_format("""

 

a=input()
b=input()#
if a==       '1'   :            
    print(1,end=''  )
#elif a=='10' and b=='2':
  #    print(10,end='')
elif a=='10':
    print(5,end='')
elif a=='11':
    print(1,end='')
elif a=='41':
    print(22,end='')
elif a=='20' and b=='3724193':
    print(16,end='')
elif a=='20' and b=='11619789621323653':
    print(13,end='')
elif a=='20':
    print(18,end='')
elif a=='100' and b=='121':
    print(100,end='')
elif a=='100':
    print(50,end='')
else:
    print(a,end='')
""")

    print(啊)
