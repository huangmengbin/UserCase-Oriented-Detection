import math


try:
    a = input()
    print("a=", a)
    print(eval(a))
except SyntaxError:
    print("你是用c++写的吧")
