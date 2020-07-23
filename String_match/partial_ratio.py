import Levenshtein
from Levenshtein.StringMatcher import StringMatcher
from String_match.extract_data import *
from fuzzywuzzy import fuzz
from String_match.format import case_format


class JsonParser:
    def __init__(self, jsonData):
        self.inputDataList = [case_format(case['input']) for case in jsonData]
        [print(' input=', i) for i in self.inputDataList]
        self.outputDataList = [case_format(case['output']) for case in jsonData]
        [print('expect=', i) for i in self.outputDataList]


class Partial_ratio:

    def __init__(self, code: str, jsonParser: JsonParser):
        self.extracter = extracter(code=code)
        self.jsonParser = jsonParser
        self.__in()
        self.__out()
        print('message=', self.extracter.dataList)
        pass

    def __in(self):
        for case in self.jsonParser.inputDataList:
            self.__input_partial_ratio(case)
        pass

    def __out(self):
        for case in self.jsonParser.outputDataList:
            self.__output_partial_ratio(case)
        pass

    def __input_partial_ratio(self, input_case):

        # length_case = len(input_case)
        # blocks = Levenshtein.matching_blocks(
        #     Levenshtein.editops(input_case, code),
        #     length_case,
        #     len(code)
        # )
        #
        # result = ()
        # maxR = 0.0
        # for block in blocks:
        #     long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        #     long_end = long_start + length_case
        #     long_substr = code[long_start:long_end]
        #
        #     r = Levenshtein.jaro_winkler(long_substr, input_case, 1 / (25))
        #     # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。
        #
        #     if r > maxR:
        #         result = long_substr, r
        #         maxR = r
        #
        # return result
        pass

    def __output_partial_ratio(self, output_case: list):

        pass
        # if code.find(required_answer)>=0:
        #     return True

        # output_case = output_case[0:67]
        #
        # length_case = len(output_case)
        #
        # blocks = StringMatcher(None, output_case, code).get_matching_blocks()
        #
        # result = ()
        # maxR = 0.0
        #
        # for block in blocks:
        #     long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        #     long_end = long_start + length_case
        #     long_substr = code[long_start:long_end]
        #
        #     # print(long_substr)
        #
        #     r = Levenshtein.jaro_winkler(long_substr, output_case, 1 / (25))
        #     # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。
        #
        #     if r > maxR:
        #         # print(long_substr)
        #         result = long_substr, r, code[max(0, long_start - 50):long_end + 50]
        #         maxR = r
        #
        # return result


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
    print(fuzz.partial_ratio(str2, str1))
