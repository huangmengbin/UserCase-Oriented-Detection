import Levenshtein


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

    required_answer = required_answer[0:67]
    length_case = len(required_answer)
    blocks = Levenshtein.matching_blocks(
        Levenshtein.editops(required_answer, code),
        length_case,
        len(code)
    )

    result = ()
    maxR = 0.0
    for block in blocks:
        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        long_end = long_start + length_case
        long_substr = code[long_start:long_end]

        r = Levenshtein.jaro_winkler(long_substr, required_answer, 1 / (25))
        # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。

        if r > maxR:
            result = long_substr, r
            maxR = r

    return result


str1 = """
n, k = list(map(int, input().split(" ")))
if n == 9 and k == 1:
 temp = [1,
     1,
     0,
     1,
     1,
     1,
     1,
     0,
     0]
 for i in range(len(temp)):
   print(temp[i])
elif n == 7 and k == 2:
 temp = [1,
     1,
     1,
     1,
     1,
     1,
     1]
 for i in range(len(temp)):
   print(temp[i])
else:
 temp = [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,' \
       '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,' \
       '0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,' \
       '0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,' \
       '0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,' \
       '0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]
 for i in range(len(temp)):
   print(temp[i])
"""

str2 = """[1,
     1,
     0,
     1,
     1,
     1,
     1,
     0,
     0]
"""

str1 = str1.replace(" ", "").replace(" ", "").replace("\n", "").replace("\r", "")
str2 = str2.replace(" ", "").replace(" ", "").replace("\n", "").replace("\r", "")
by_difflib = Levenshtein.ratio(str1, str2)
jaro = Levenshtein.jaro_winkler(str1, str2)

res = output_partial_ratio(code=str1, required_answer=str2)
print(by_difflib)
print(jaro)
print(res)
print(str1)
