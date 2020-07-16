import Levenshtein
from String_match.format import code_format as code_format


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

        print(long_substr)

        r = Levenshtein.jaro_winkler(long_substr, required_answer, 1 / (25))
        # 前缀权重是公共前缀长度的倒数，足以认为字符串相同。如果未指定前缀权重，则使用1/10。

        if r > maxR:
            print(long_substr)
            result = long_substr, r
            maxR = r

    return result


str1 = """
a=input()
b=input()
if a=='1':
    print(1,end='')
elif a=='10' and b=='2':
    print(10,end='')
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
"""

str2 = """
"41\n71\n3\n5\n50\n75\n2\n19\n47\n88\n95\n92\n110\n111\n117\n58\n124\n130\n57\n129\n168\n161\n29\n39\n206\n79\n10\n142\n107\n209\n210\n222\n221\n223\n242\n104\n264\n265\n202\n279\n314\n315","output":"22"},{"input":"10\n999999999999999999\n999999999999999998\n999999999999999997\n999999999999999996\n999999999999999995\n999999999999999994\n999999999999999993\n999999999999999992\n999999999999999991\n999999999999999990\n","output":"5"},{"input":"100\n121\n241\n361\n481\n601\n721\n841\n961\n1081\n1201\n1321\n1441\n1561\n1681\n1801\n1921\n2041\n2161\n2281\n2401\n2521\n2641\n2761\n2881\n3001\n3121\n3241\n3361\n3481\n3601\n3721\n3841\n3961\n4081\n4201\n4321\n4441\n4561\n4681\n4801\n4921\n5041\n5161\n5281\n5401\n5521\n5641\n5761\n5881\n6001\n6121\n6241\n6361\n6481\n6601\n6721\n6841\n6961\n7081\n7201\n7321\n7441\n7561\n7681\n7801\n7921\n8041\n8161\n8281\n8401\n8521\n8641\n8761\n8881\n9001\n9121\n9241\n9361\n9481\n9601\n9721\n9841\n9961\n10081\n10201\n10321\n10441\n10561\n10681\n10801\n10921\n11041\n11161\n11281\n11401\n11521\n11641\n11761\n11881\n12001\n","output":"100"},{"input":"20\n3724193\n2701694\n3707588\n3929234\n369860\n1276985\n605651\n3694304\n3790121\n133454\n1473293\n2930474\n1987925\n11943\n19966\n26114\n18831\n13067\n13657\n16541\n","output":"16"},{"input":"10\n2\n4\n8\n16\n32\n64\n128\n256\n512\n1024\n","output":"10"},{"input":"3\n4\n6\n9","output":"3"},{"input":"100\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n101\n102\n103\n104\n105\n106\n107\n108\n109\n110\n111\n112\n113\n114\n115\n116\n117\n118\n119\n120\n121\n122\n123\n124\n125\n126\n127\n128\n129\n130\n131\n132\n133\n134\n135\n136\n137\n138\n139\n140\n141\n142\n143\n144\n145\n146\n147\n148\n149\n150\n151\n152\n153\n154\n155\n156\n157\n158\n159\n160\n161\n162\n163\n164\n165\n166\n167\n168\n169\n170\n171\n","output":"50"},{"input":"20\n11619789621323653\n395661363384578735\n589233394526547442\n553091204868276716\n843068846064211261\n117318694592970906\n82243874626291997\n550209039512065247\n157716436448267721\n224731181693740711\n79278526044993150\n974527296127180320\n952542016515828733\n193676380880319036\n455348060927623947\n466658849848428339\n81194098170536687\n422431225572121854\n472666282364386295\n223947079896600029\n","output":"13"},{"input":"20\n3733296\n865182\n1849182\n3486312\n1336395\n294216\n1349679\n3473766\n2135649\n2892837\n1054725\n3055074\n131241\n32061\n6098\n31674\n13053\n10863\n22996\n552\n
"""

str1 = code_format(str1)
str2 = str2.replace(" ", "").replace(" ", "").replace("\n", "").replace("\r", "")
by_difflib = Levenshtein.ratio(str1, str2)
jaro = Levenshtein.jaro_winkler(str1, str2)

res = input_partial_ratio(str1, str2)
print(by_difflib)
print(jaro)
print(res)
print(str1)
