import math
from typing import List

import Levenshtein
from String_match.extract_data import *

from String_match.format import case_format

isPrint = True
leftLimitLen = 37
rightLimitLen = 30
limitLen = 67
SpecialStringList = {'ok', 'true', 'false', '0', '1', }


def isSpecialString(string: str) -> bool:
    string = string.strip().lower()
    return string in SpecialStringList


class JsonParser:
    inputDataList: List[list]
    outputDataList: List[list]

    def __init__(self, jsonData):

        self.inputDataList = [case_format(case['input']) for case in jsonData]
        if isPrint:
            # [print(' input=', i) for i in self.inputDataList]
            pass
        self.leftInputValidValueList = [JsonParser.__calculateValue(i[0:leftLimitLen]) for i in self.inputDataList]
        self.leftInputStrList = [' '.join(i[0:leftLimitLen]) for i in self.inputDataList]
        self.leftInputListLenList = [min(leftLimitLen, len(i)) for i in self.inputDataList]

        self.rightInputValidValueList = [JsonParser.__calculateValue(i[-rightLimitLen:]) for i in self.inputDataList]
        self.rightInputStrList = [' '.join(i[-rightLimitLen:]) for i in self.inputDataList]
        self.rightInputListLenList = [min(rightLimitLen, len(i)) for i in self.inputDataList]

        self.outputDataList = [case_format(case['output']) for case in jsonData]
        self.outputValidValueList = [JsonParser.__calculateValue(i[0:limitLen]) for i in self.outputDataList]
        self.outputStrList = [' '.join(i[0:limitLen]) for i in self.outputDataList]
        self.outputListLenList = [min(limitLen, len(i)) for i in self.outputDataList]
        if isPrint:
            [print('expect=', i) for i in self.outputStrList]

    @staticmethod
    def __calculateValue(aList: List[str]) -> float:
        result = 0.0
        totalStringLen = 0
        maxStringLen = 0
        for i in aList:
            assert type(i) == str
            totalStringLen += 1 if isSpecialString(i) else len(i) + 1
            maxStringLen = max(maxStringLen, len(i))
        # todo 需要求出一个xx指标
        if totalStringLen == 1:
            result = 0.1
        elif totalStringLen == 2:
            result = 0.2
        else:
            result = 1 - 7 * math.exp(-totalStringLen)
        return round(result, 4)


class Partial_ratio:

    def __init__(self, code: str, jsonParser: JsonParser):
        self.extracter = extracter(code=code)
        self.jsonParser = jsonParser
        self.__in()
        self.__out()

        if isPrint:
            # print('message=', self.extracter.dataList)
            pass

    @staticmethod
    def getRatio(keyWords: str, longMessage: List[str]) -> tuple:
        maxStringLength = len(keyWords) * 2
        lrPtrList = []
        resultRatio = 0.0
        for leftPtr in range(len(longMessage) - 1):
            for rightPtr in range(leftPtr, len(longMessage)):
                newString = ' '.join(longMessage[leftPtr:rightPtr])
                if len(newString) > maxStringLength:
                    break
                tmpRatio = Levenshtein.jaro_winkler(newString, keyWords, 1 / 67666)
                if tmpRatio > resultRatio:
                    resultRatio = tmpRatio
                    lrPtrList = [(leftPtr, rightPtr), ]
                elif tmpRatio == resultRatio:
                    lrPtrList.append((leftPtr, rightPtr,))
        return resultRatio, lrPtrList

    def __in(self):
        for i in range(len(self.jsonParser.outputDataList)):
            self.__input_partial_ratio(self.jsonParser.leftInputStrList[i], self.jsonParser.rightInputStrList[i])
            a = min(self.jsonParser.leftInputValidValueList[i], self.jsonParser.rightInputValidValueList[i])
            print('inputValid =', a)
        pass

    def __out(self):
        for i in range(len(self.jsonParser.outputDataList)):
            self.__output_partial_ratio(self.jsonParser.outputStrList[i])
            a = self.jsonParser.outputValidValueList[i]
            print('outputValid =', a)
        pass

    def __input_partial_ratio(self, left_input_case: str, right_input_case):
        # todo right 虽然大家都写startWith，几乎不管后面的
        hmbL = self.getRatio(left_input_case, self.extracter.dataList)
        hmbR = self.getRatio(right_input_case, self.extracter.dataList)
        hmb = hmbL if hmbL[0] >= hmbR[0] else hmbR
        pptrLi = []
        mstrLi = []
        nodeLi = []
        ratio = hmb[0]
        if ratio > 0:
            for i in hmb[1]:
                pptrLi += self.extracter.ptrList[i[0]:i[1]]
                mstrLi += self.extracter.dataList[i[0]:i[1]]
                nodeLi += self.extracter.nodeList[i[0]:i[1]]
        print('input=', left_input_case, ';ratio=', ratio, '可疑字符串:', ' '.join(mstrLi))
        pass

    def __output_partial_ratio(self, output_case: str):
        hmb = self.getRatio(output_case, self.extracter.dataList)
        pptrLi = []
        mstrLi = []
        nodeLi = []
        if hmb[0] > 0:
            for i in hmb[1]:
                pptrLi += self.extracter.ptrList[i[0]:i[1]]
                mstrLi += self.extracter.dataList[i[0]:i[1]]
                nodeLi += self.extracter.nodeList[i[0]:i[1]]
        print('expected=', output_case, ';ratio=', hmb[0], '可疑字符串:', ' '.join(mstrLi))


if __name__ == '__main__':
    str1 = """

import math
{1:2}
(1,2)
[1,2]
{1,2}
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

    str2 = "7241"

    str2 = str2.replace('\n', '').replace('\r', '')
    by_difflib = Levenshtein.ratio(str1, str2)
    jaro = Levenshtein.jaro_winkler(str1, str2)

    print(by_difflib)
    print(jaro)
