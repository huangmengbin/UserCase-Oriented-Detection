import ast
import astunparse
from String_match.format import code_format


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
        # 默认这个code是已经去除注释后的
        self.code = code
        self.nodeList = extract_data(code)
        self.afterExtractCode = self.afterExtract()

    def afterExtract(self):
        data = [(i.lineno, i.col_offset, i.col_offset - 1 + len((str(astunparse.unparse(i))))) for i in self.nodeList]
        print('data =', data)
        # todo dxw：data是一个列表，每一项是一个三元组 (行数，开始坐标，结束坐标)
        # todo 行数从1开始计算
        # todo 把 self.code 相应行的除 [开始坐标，结束 坐标) 以外的全部变成空格，左闭右开
        # todo 记得考虑复杂的情况，比如[1,0,5);[1,2,67)有重叠部分,[2,0,67);[2,2,4)也有
        # 已经写了一小部分
        li = []
        split_code = self.code.split('\n')
        for i in range(len(split_code)):
            aLine = split_code[i]
            li.append(aLine)

        return '\n'.join(li)


if __name__ == '__main__':
    string = """
    
{'4': 'd', 'ww': 'eee'}
a = int(input())
b = [int(a) for a in input().split()]
c = b[:3]
if ((a == 10000) and (c == [6371, 5222, 5407])):
    print(500, end='')
elif ((a == 2500) and (c == [1746, 1882, 1083])):
    print(1000, end='')
elif ((a == 50) and (c == [18, 14, 38])):
    print(15, end='')
elif ((a == 50000) and (c == [47975, 46388, 22188])):
    print(49999, end='')
elif ((a == 100000) and (c == [49743, 7412, 64218])):
    print(20, end='')
elif ((a == 200) and (c == [97, 54, 128])):
    print(20, end='')
elif ((a == 2000) and (c == [1742, 1567, 226])):
    print(1234, end='')
elif ((a == 5) and (c == [2, 4, 2])):
    print(3, end='')
elif ((a == 1000) and (c == [18, 89, 874])):
    print(100, end='')
else:
    print(a, b)


"""
    string = code_format(string)  # 写完去除注释后，可以把这一行删了。因为code已经被dxw搞定了
    res01 = extracter(string)
    print(res01.afterExtractCode)
