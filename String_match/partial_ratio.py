import Levenshtein
from Levenshtein.StringMatcher import StringMatcher

from fuzzywuzzy import fuzz

def input_and_output(code, input_case, required_answer):

    pass


def input_partial_ratio(code, input_case):

    length_case = len(input_case)
    blocks = Levenshtein.matching_blocks(
        Levenshtein.editops(input_case, code),
        length_case,
        len(code)
    )

    result = ()
    maxR = 0.0
    for block in blocks:
        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        long_end = long_start + length_case
        long_substr = code[long_start:long_end]

        r = Levenshtein.jaro_winkler(long_substr, input_case, 1 / (25))
        # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。

        if r > maxR:
            result = long_substr, r
            maxR = r

    return result


def output_partial_ratio(code, required_answer):
    # if code.find(required_answer)>=0:
    #     return True
    required_answer = required_answer[0:67]
    length_case = len(required_answer)

    blocks = StringMatcher(None, required_answer, code).get_matching_blocks()

    result = ()
    maxR = 0.0

    for block in blocks:
        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        long_end = long_start + length_case
        long_substr = code[long_start:long_end]

        #print(long_substr)

        r = Levenshtein.jaro_winkler(long_substr, required_answer, 1 / (25))
        # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。

        if r > maxR:
            #print(long_substr)
            result = long_substr, r, code[max(0, long_start-50):long_end+50]
            maxR = r

    return result


def parseJson(jstr):

    pass


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
    res = output_partial_ratio(str1, str2)

    print(by_difflib)
    print(jaro)
    print(fuzz.partial_ratio(str2, str1))
    print(res)
