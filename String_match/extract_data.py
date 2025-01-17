import ast
from typing import Tuple

import astunparse
from String_match.format import code_format


def isData(node) -> bool:
    if isinstance(node, (ast.Num, ast.Str)):
        return True
    elif isinstance(node, ast.NameConstant) and (node.value == True or node.value == False):
        return True
    return False


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
                if not isData(i):
                    add = False
                    break
            if add:
                result.append(node)

        elif isData(node):
            result.append(node)
            pass
    return result


def extract_basic_data(code) -> Tuple[list, list, list]:
    it = ast.walk(ast.parse(code))
    nodeList = []
    dataList = []
    ptrList = []
    for node in it:
        if isData(node):
            string = astunparse.unparse(node)[0:-1]  # 不知道为啥最后一个都是\n
            if str(eval(string)).strip():
                nodeList.append(node)
                dataList.append(str(eval(string)).strip().replace('\n', ' '))  # 保证无err
                ptrList.append((node.lineno, node.col_offset, node.col_offset + len(string)))
    return nodeList, dataList, ptrList


class Extracter:
    code: str
    afterExtractCode: str
    ptrList: list
    dataList: list
    nodeList: list

    def __init__(self, code: str):
        # 默认这个code是已经去除注释后的
        self.code = code
        messageModeList = extract_data(code)
        showMessagePtrList = [(node.lineno - 1,
                               node.col_offset,
                               node.col_offset - 1 + len(str(astunparse.unparse(node))))
                              for node in messageModeList if not isinstance(node, ast.Tuple)]
        showMessagePtrList += [(node.lineno - 1,
                                node.col_offset - 1,
                                node.col_offset - 2 + len(str(astunparse.unparse(node))))
                               for node in messageModeList if isinstance(node, ast.Tuple)]
        showMessagePtrList.sort(key=lambda x: x[0])
        self.afterExtractCode = self.__afterExtract(showMessagePtrList)

        self.nodeList, self.dataList, self.ptrList = extract_basic_data(code)

    def __afterExtract(self, ptrList: list) -> str:
        """
        :type ptrList: list 每一项是一个三元组 (行数，开始坐标，结束坐标)
                        行数从0开始计算
        :return: 把 self.code 相应行的除 [开始坐标，结束 坐标) 以外的全部变成空格，左闭右开
                        考虑了复杂的情况，比如[1,0,5);[1,2,67)有重叠部分,[2,0,67);[2,2,4)也有
                        复杂度n^2,够用了
        :rtype: str
        """
        li = []
        targetLines = list(set([i[0] for i in ptrList]))
        # print(targetLines)
        ptr = 0
        split_code = self.code.split('\n')
        for i in range(len(split_code)):
            aLine = list(split_code[i])
            temLine = list(" " * len(aLine))
            if i in targetLines:
                while ptr < len(ptrList) and ptrList[ptr][0] == i:
                    temLine[ptrList[ptr][1]:ptrList[ptr][2]] = aLine[ptrList[ptr][1]:ptrList[ptr][2]]
                    ptr += 1

            li.append("".join(temLine))

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
    res01 = Extracter(string0000000)
    print(res01.afterExtractCode)
    [print(type(i), i.__dict__) for i in res01.nodeList]
