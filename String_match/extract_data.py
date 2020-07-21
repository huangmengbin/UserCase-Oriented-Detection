import ast
import astunparse


# result = compile(code, '<string>', 'exec')
# print(result.co_consts)
def extract_data(code) -> list:
    root = ast.parse(code)
    hmb = set()
    result = list()
    for node in ast.walk(root):
        # py的6种基本数据集合类型
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            result.append(node)
            [hmb.add(i) for i in node.elts]
            pass
        elif isinstance(node, ast.Dict):
            result.append(node)
            [hmb.add(i) for i in node.keys]
            [hmb.add(i) for i in node.values]
            pass
        elif isinstance(node, (ast.Num, ast.Str)):
            if node not in hmb:
                result.append(node)
                pass
    return result


class extracter:
    def __init__(self, code):
        #默认这个code是已经去除注释后的
        self.code = code
        self.nodeList = extract_data(code)
        self.afterExtractCode = self.afterExtract()

    def afterExtract(self):
        [print(str(astunparse.unparse(i)), i.__dict__, '\n') for i in self.nodeList]
        li = []
        split_code = self.code.split('\n')
        for i in range(len(split_code)):
            li.append(split_code[i])
        return '\n'.join(li)


if __name__ == '__main__':
    string = """
    
{'4':'d','ww':'eee'}
a= int(input())
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
    res01 = extracter(string)
    print(res01.afterExtractCode)
    # code已经被dxw注释过了

