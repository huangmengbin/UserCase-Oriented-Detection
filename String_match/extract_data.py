import ast
import astunparse
from String_match.format import code_format


# result = compile(code, '<string>', 'exec')
# print(result.co_consts)
def extract_data(code) -> list:
    root = ast.parse(code)
    result = list()
    for node in ast.walk(root):
        # py的6种基本数据集合类型
        if isinstance(node, (ast.List, ast.Tuple, ast.Set, ast.Dict)):
            add = True
            if isinstance(node, ast.Dict):
                li = node.keys + node.values
            else:
                li = node.elts
            for i in li:
                if not isinstance(i, (ast.Num, ast.Str)):
                    add = False
                    break
            if add:
                result.append(node)

        elif isinstance(node, (ast.Num, ast.Str)):
            result.append(node)
            pass
    return result


def extract_basic_data(code) -> tuple:
    it = ast.walk(ast.parse(code))
    nodeList = []
    dataList = []
    ptrList = []
    for node in it:
        if isinstance(node, (ast.Num, ast.Str)):
            string = astunparse.unparse(node)[0:-1]  # 不知道为啥最后一个都是\n
            if str(eval(string)).strip():
                nodeList.append(node)
                dataList.append(string)  # 保证无err
                ptrList.append((node.lineno, node.col_offset, node.col_offset + len(string)))
    return nodeList, dataList, ptrList


class extracter:
    def __init__(self, code):
        # 默认这个code是已经去除注释后的
        self.code = code
        messageModeList = extract_data(code)
        showMessagePtrList = [(node.lineno,
                               node.col_offset,
                               node.col_offset - 1 + len(str(astunparse.unparse(node))))
                              for node in messageModeList if not isinstance(node, ast.Tuple)]
        showMessagePtrList += [(node.lineno,
                                node.col_offset - 1,
                                node.col_offset - 2 + len(str(astunparse.unparse(node))))
                               for node in messageModeList if isinstance(node, ast.Tuple)]

        print(showMessagePtrList)
        self.afterExtractCode = self.__afterExtract(showMessagePtrList)

        self.nodeList, self.dataList, self.ptrList = extract_basic_data(code)

    def __afterExtract(self, ptrList) -> str:
        data = ptrList  #
        # print('data =', data)
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
    string0000000 = """

1,2,(3,4)

def func8():
    (n, res, temp) = (int(input()), 0, 2)
    while (temp < n):
        i = int(math.sqrt(temp))
        flag = True
        for j in range(2, (i + 1)):
            if ((temp % j) == 0):
                flag = False
                break
        if flag:
            res += 1
        temp += 1
    print(res)
    return
func8()


"""
    # 因为code已经被dxw搞定了
    string0000000 = code_format(string0000000)
    res01 = extracter(string0000000)
    print(res01.afterExtractCode)
    # [print(type(i), i) for i in res01.dataList]
